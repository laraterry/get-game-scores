import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import requests

load_dotenv()
API_KEY = os.getenv("API_FOOTBALL_KEY")

if not API_KEY:
    print("API key not found. Check your .env file!")
else:
    print("API key loaded successfully.")


def get_yesterdays_date():
    today = datetime.now(timezone.utc)  # use UTC for consistency with most APIs
    yesterday = today - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')  # format as YYYY-MM-DD


def get_fixtures(date):
    url = f"https://v3.football.api-sports.io/fixtures?date={date}"
    headers = {
        "x-apisports-key": API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    date = get_yesterdays_date()
    print("Yesterday's date was:" + date)

    data = get_fixtures(date)

    matches = data.get("response", [])
    if not matches:
        print("⚠️ No matches found for that date.")
    else:
        for match in matches[:5]:  # Show first 5 matches
            home = match["teams"]["home"]["name"]
            away = match["teams"]["away"]["name"]
            home_score = match["goals"]["home"]
            away_score = match["goals"]["away"]
            print(f"⚽ {home} {home_score} - {away_score} {away}")


