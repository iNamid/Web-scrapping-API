import pytest
from final import *

def test_nba_scores():
    nba_url = "http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"
    nba_scores = NBA(nba_url)
    scores_data = nba_scores.get_scores()
    assert len(scores_data) > 0
    assert isinstance(scores_data[0], dict)
    assert "Home Team" in scores_data[0]
    assert "Away Team" in scores_data[0]
    assert "Home Score" in scores_data[0]
    assert "Away Score" in scores_data[0]
    assert "Game Status" in scores_data[0]
    assert "Date" in scores_data[0]

def test_premier_league_scores():
    premier_league_url = "http://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard"
    premier_league_scores = PremierLeague(premier_league_url)
    scores_data = premier_league_scores.get_scores()
    assert len(scores_data) > 0
    assert isinstance(scores_data[0], dict)
    assert "Home Team" in scores_data[0]
    assert "Away Team" in scores_data[0]
    assert "Home Score" in scores_data[0]
    assert "Away Score" in scores_data[0]
    assert "Game Status" in scores_data[0]
    assert "Date" in scores_data[0]

def test_champions_league_scores():
    champions_league_url = "http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard"
    champions_league_scores = ChampionsLeague(champions_league_url)
    scores_data = champions_league_scores.get_scores()
    assert len(scores_data) > 0
    assert isinstance(scores_data[0], dict)
    assert "Home Team" in scores_data[0]
    assert "Away Team" in scores_data[0]
    assert "Home Score" in scores_data[0]
    assert "Away Score" in scores_data[0]
    assert "Game Status" in scores_data[0]
    assert "Date" in scores_data[0]

def test_laliga_scores():
    laliga_url = "http://site.api.espn.com/apis/site/v2/sports/soccer/esp.1/scoreboard"
    laliga_scores = LaLiga(laliga_url)
    scores_data = laliga_scores.get_scores()
    assert len(scores_data) > 0
    assert isinstance(scores_data[0], dict)
    assert "Home Team" in scores_data[0]
    assert "Away Team" in scores_data[0]
    assert "Home Score" in scores_data[0]
    assert "Away Score" in scores_data[0]
    assert "Game Status" in scores_data[0]
    assert "Date" in scores_data[0]

def test_seriea_scores():
    seriea_url = "http://site.api.espn.com/apis/site/v2/sports/soccer/ita.1/scoreboard"
    seriea_scores = SerieA(seriea_url)
    scores_data = seriea_scores.get_scores()
    assert len(scores_data) > 0
    assert isinstance(scores_data[0], dict)
    assert "Home Team" in scores_data[0]
    assert "Away Team" in scores_data[0]
    assert "Home Score" in scores_data[0]
    assert "Away"

def test_nfl_scores():
    nfl_url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
    nfl_scores = NFL(nfl_url)
    scores_data = nfl_scores.get_scores()
    assert len(scores_data) > 0
    assert isinstance(scores_data[0], dict)
    assert "Home Team" in scores_data[0]
    assert "Away Team" in scores_data[0]
    assert "Home Score" in scores_data[0]
    assert "Away Score" in scores_data[0]
    assert "Game Status" in scores_data[0]
    assert "Date" in scores_data[0]

def test_bundesliga_scores():
    bundesliga_url = "http://site.api.espn.com/apis/site/v2/sports/soccer/ger.1/scoreboard"
    bundesliga_scores = Bundesliga(bundesliga_url)
    scores_data = bundesliga_scores.get_scores()
    assert len(scores_data) > 0
    assert isinstance(scores_data[0], dict)
    assert "Home Team" in scores_data[0]
    assert "Away Team" in scores_data[0]
    assert "Home Score" in scores_data[0]
    assert "Away Score" in scores_data[0]
    assert "Game Status" in scores_data[0]
    assert "Date" in scores_data[0]
    
def test_ligue1_scores():
    ligue1_url = "http://site.api.espn.com/apis/site/v2/sports/soccer/fra.1/scoreboard"
    ligue1_scores = Ligue1(ligue1_url)
    scores_data = ligue1_scores.get_scores()
    assert len(scores_data) > 0
    assert isinstance(scores_data[0], dict)
    assert "Home Team" in scores_data[0]
    assert "Away Team" in scores_data[0]
    assert "Home Score" in scores_data[0]
    assert "Away Score" in scores_data[0]
    assert "Game Status" in scores_data[0]
    assert "Date" in scores_data[0]


def test_invalid_url():
    invalid_url = "http://example.com/invalid"
    with pytest.raises(Exception):
        scores = Scores(invalid_url)


if __name__ == "__main__":
    pytest.main()
