import pandas as pd
import requests
import re

class Scores:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.data = self.response.json()
        self.games = self.data.get("events", [])
        self.scores = []
        self.teams = {}
        self.game_status_list = []
        
    def get_scores(self):
        for game in self.games:
            home_team = game["competitions"][0]["competitors"][0]["team"]["displayName"]
            away_team = game["competitions"][0]["competitors"][1]["team"]["displayName"]
            home_score = game["competitions"][0]["competitors"][0]["score"]
            away_score = game["competitions"][0]["competitors"][1]["score"]
            if game["status"]["type"]["name"] == "STATUS_FULL_TIME":
                game_status = "Full time"

            elif game["status"]["type"]["name"] == "STATUS_SCHEDULED":
                game_status = "Scheduled"
            else:
                game_status = game["status"]["displayClock"]
            date = game["date"]

            self.scores.append({"Home Team": home_team, "Home Score": home_score, "Away Score": away_score, "Away Team": away_team,"Game Status": game_status, "Date": date })
        return self.scores
    
   

    
    
class ChampionsLeague(Scores):
    def __init__(self, url):
        super().__init__(url)

  
class NBA(Scores):
    def __init__(self, url):
        super().__init__(url)
        
       
class PremierLeague(Scores):
    def __init__(self, url):
        super().__init__(url)

       

class LaLiga(Scores):
    def __init__(self, url):
        super().__init__(url)


class Ligue1(Scores):
    def __init__(self, url):
        super().__init__(url)
        

class Bundesliga(Scores):
    def __init__(self, url):
        super().__init__(url)
        

class NFL(Scores):
    def __init__(self, url):
        super().__init__(url)
        

class SerieA(Scores):
    def __init__(self, url):
        super().__init__(url)

def main():
    with open('league_urls.txt', 'r', encoding='ISO-8859-1') as file:
        urls = file.readlines()

    pattern = re.compile(r'^http://site\.api\.espn\.com/apis/site/v2/.*$')
    leagues = []
    for url in urls:
        if pattern.match(url):
            url = url.strip()  
            if 'basketball/nba' in url:
                leagues.append(NBA(url))
            elif 'soccer/eng.1' in url:
                leagues.append(PremierLeague(url))
            elif 'soccer/esp.1' in url:
                leagues.append(LaLiga(url))
            elif 'soccer/fra.1' in url:
                leagues.append(Ligue1(url))
            elif 'soccer/ger.1' in url:
                leagues.append(Bundesliga(url))
            elif 'football/nfl' in url:
                leagues.append(NFL(url))
            elif 'soccer/ita.1' in url:
                leagues.append(SerieA(url))
            elif 'soccer/uefa.champions' in url:
                leagues.append(ChampionsLeague(url))
        else:
            print(f"Invalid URL: {url}")

    for league in leagues:
        scores_data = league.get_scores()
        df_scores = pd.DataFrame(scores_data)
        print(f"\n{league.__class__.__name__} Scores")
        league_class_name = league.__class__.__name__
        filename = f"{league_class_name.lower()}_scores.csv"
        df_scores.to_csv(filename, index=False)
        print(df_scores)

        

if __name__ == '__main__':
    main()








