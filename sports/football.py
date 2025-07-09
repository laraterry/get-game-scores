import os
import requests



def get_football_matches(date):
    """
    gets all of the football games from API from specified date
    takes input of date which is a date in "YYYY-MM-DD" format
    outputs a dictionary representing JSON response
    """
    url = f"https://v3.football.api-sports.io/fixtures?date={date}"
    headers = {
        "x-apisports-key": os.getenv("API_FOOTBALL_KEY")
    }
    response = requests.get(url, headers=headers)
    return response.json()

def filter_football_matches(data, team_name):
    """
    filters matches to show only ones with specific teams
    takes input data which is a dictionary outputted by get_football_matches
    and team name which is a string
    outputs a list of tuples with format (home_team, home_score, away_score, away_team)
    """
    
    matches = data.get("response", [])
    filtered = []
    for match in matches:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]
        if team_name in home.lower() or team_name in away.lower():
            home_score = match["goals"]["home"]
            away_score = match["goals"]["away"]
            filtered.append((home, home_score, away_score, away))
    return filtered