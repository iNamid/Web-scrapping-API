import pandas as pd
import requests
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List

class AdvancedMetrics:
    def calculate_xg(self, shots_data: List[Dict]) -> float:
        """Calculate expected goals based on shot location and type"""
        xg = 0
        for shot in shots_data:
            distance = shot.get('distance', 0)
            angle = shot.get('angle', 0)
            # Basic xG model
            xg += 1 / (1 + np.exp(-(-3 + 0.1 * distance + 0.1 * angle)))
        return xg

    def create_heatmap(self, positions_data: List[Dict], title: str):
        """Generate position heatmap"""
        pitch = np.zeros((100, 100))
        for pos in positions_data:
            x, y = pos.get('x', 0), pos.get('y', 0)
            pitch[int(x)][int(y)] += 1
            
        plt.figure(figsize=(10, 7))
        sns.heatmap(pitch, cmap='YlOrRd')
        plt.title(title)
        plt.savefig(f'{title}_heatmap.png')
        plt.close()

class Scores(AdvancedMetrics):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.games = self.data.get("events", [])
        self.scores = []
        self.teams = {}
        self.game_status_list = []

    def get_advanced_stats(self, game_id: str) -> Dict:
        """Fetch advanced stats for a game"""
        stats_url = f"{self.url}/stats/{game_id}"
        try:
            response = requests.get(stats_url)
            stats_data = response.json()
            return {
                'shots': self._parse_shots(stats_data),
                'possession': self._parse_possession(stats_data),
                'passes': self._parse_passes(stats_data)
            }
        except Exception as e:
            print(f"Error fetching advanced stats: {e}")
            return {}

    def _parse_shots(self, stats_data: Dict) -> List[Dict]:
        """Parse shots data from stats"""
        # Implementation would depend on ESPN API structure
        return []

    def _parse_possession(self, stats_data: Dict) -> Dict:
        """Parse possession data"""
        return {}

    def _parse_passes(self, stats_data: Dict) -> List[Dict]:
        """Parse passing data"""
        return []

    def get_scores(self):
        for game in self.games:
            game_id = game.get('id', '')
            advanced_stats = self.get_advanced_stats(game_id)
            
            home_team = game["competitions"][0]["competitors"][0]["team"]["displayName"]
            away_team = game["competitions"][0]["competitors"][1]["team"]["displayName"]
            home_score = game["competitions"][0]["competitors"][0]["score"]
            away_score = game["competitions"][0]["competitors"][1]["score"]
            
            # Calculate xG if shots data available
            home_xg = self.calculate_xg(advanced_stats.get('shots', {}).get('home', []))
            away_xg = self.calculate_xg(advanced_stats.get('shots', {}).get('away', []))
            
            # Create heatmaps if position data available
            if advanced_stats.get('possession'):
                self.create_heatmap(
                    advanced_stats['possession'].get('home', []),
                    f"{home_team}_possession_heatmap"
                )
            
            self.scores.append({
                "Home Team": home_team,
                "Home Score": home_score,
                "Home xG": round(home_xg, 2),
                "Away Score": away_score,
                "Away xG": round(away_xg, 2),
                "Away Team": away_team,
                "Game Status": self._get_game_status(game),
                "Date": game["date"],
                "Possession": advanced_stats.get('possession', {}),
                "Passes Completed": advanced_stats.get('passes', {})
            })
            
        return self.scores

    def _get_game_status(self, game: Dict) -> str:
        status_name = game["status"]["type"]["name"]
        if status_name == "STATUS_FULL_TIME":
            return "Full time"
        elif status_name == "STATUS_SCHEDULED":
            return "Scheduled"
        return game["status"]["displayClock"]

    def generate_match_report(self, game_data: Dict):
        """Generate detailed match report with visualizations"""
        home_team = game_data["Home Team"]
        away_team = game_data["Away Team"]
        
        # Create match report plots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
        
        # xG comparison
        xg_data = {
            'Teams': [home_team, away_team],
            'Actual Goals': [game_data["Home Score"], game_data["Away Score"]],
            'Expected Goals': [game_data["Home xG"], game_data["Away xG"]]
        }
        
        ax1.bar(xg_data['Teams'], xg_data['Actual Goals'], label='Actual Goals')
        ax1.bar(xg_data['Teams'], xg_data['Expected Goals'], alpha=0.5, label='Expected Goals')
        ax1.set_title('Goals vs Expected Goals')
        ax1.legend()
        
        # Possession pie chart
        if game_data["Possession"]:
            possession_data = [
                game_data["Possession"].get('home', 0),
                game_data["Possession"].get('away', 0)
            ]
            ax2.pie(possession_data, labels=[f'{home_team}\n{possession_data[0]}%', 
                                           f'{away_team}\n{possession_data[1]}%'])
            ax2.set_title('Possession %')
        
        plt.savefig(f'match_report_{home_team}_vs_{away_team}.png')
        plt.close()