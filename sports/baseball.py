import os
import requests
from datetime import datetime, timedelta, UTC
import json
from dotenv import load_dotenv


load_dotenv()



def get_baseball_games(date):
    """
    gets all of the baseball games from API from specified date
    takes input of date which is a date in "YYYY-MM-DD" format
    outputs a dictionary representing JSON response
    """
    url = f"https://v1.baseball.api-sports.io/games?date={date}"
    headers = {
        "x-rapidapi-key": os.getenv("API_BASEBALL_KEY"),
        "x-rapidapi-host": "v1.baseball.api-sports.io"
    }
    response = requests.get(url, headers=headers)
    return response.json()
    

def filter_baseball_games(data, team_name):
    """
    filters matches to show only ones with specific teams
    takes input data which is a dictionary outputted by get_baseball_games
    and team name which is a string
    outputs a list of tuples with format (home_team, home_score, away_score, away_team)
    """
    
    matches = data.get("response", [])
    filtered = []
    for match in matches:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]
        if team_name in home.lower() or team_name in away.lower():
            home_score = match["scores"]["home"]["total"]
            away_score = match["scores"]["away"]["total"]
            filtered.append((home, home_score, away_score, away))
    return filtered

    

