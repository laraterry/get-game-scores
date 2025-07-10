import os
from dotenv import load_dotenv
from utils.date import get_yesterdays_date, get_todays_date
from sports.football import get_football_matches, filter_football_matches
from sports.baseball import get_baseball_games, filter_baseball_games



load_dotenv()


def main():
    sport = input("Enter your sport here: ").strip().lower()
    date = get_yesterdays_date()
    team = input("Enter your team here: ").strip().lower()

    if sport == "football":
        data = get_football_matches(date)
        matches = filter_football_matches(data, team)

        if not matches:
            print(f"No matches found for '{team}' on {date}.")
        else:
            print(f"\nMatches for {team.title()} on {date}:\n")
            for home, hs, as_, away in matches:
                print(f"⚽ {home} {hs} - {as_} {away}")
    
    elif sport == "baseball": 
        date = get_todays_date()
        data = get_baseball_games(date)
        matches = filter_baseball_games(data, team)

        if not matches:
            print(f"No matches found for '{team}' on {date}.")
        else:
            print(f"Games for {team.title()} on {date}:\n")
            for home, hs, as_, away in matches:
                print(f"⚾ {home} {hs} - {as_} {away}")



if __name__ == "__main__":
    main()
