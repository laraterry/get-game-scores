import os
from dotenv import load_dotenv
from utils.date import get_yesterdays_date
from sports.football import get_football_matches, filter_football_matches



load_dotenv()


def main():
    sport = input("Enter your sport here: ").strip().lower()
    date = get_yesterdays_date()

    if sport == 
    data = get_football_matches(date)
    matches = filter_football_matches(data, team)

    if not matches:
        print(f"No matches found for '{team}' on {date}.")
    else:
        print(f"\nMatches for {team.title()} on {date}:\n")
        for home, hs, as_, away in matches:
            print(f"⚽ {home} {hs} - {as_} {away}")



if __name__ == "__main__":
    main()
