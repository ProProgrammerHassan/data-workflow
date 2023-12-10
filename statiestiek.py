import os
import csv
import logging
from collections import defaultdict
from datetime import datetime

logging.basicConfig(
    filename="analyse.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def read_csv(filename):
    try:
        with open(filename, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
            return data
    except Exception as e:
        logging.error(f"Fout bij het lezen van het bestand '{filename}': {e}")
        return None

def calculate_statistics(data):
    team_stats = defaultdict(lambda: {"goals_for": 0, "goals_against": 0, "matches_won": 0, "matches_played": 0})

    for match in data:
        home_team = match["home_team"]
        away_team = match["away_team"]
        score_home = match["home_score"]
        score_away = match["away_score"]

        # Voeg controle toe om te vermijden dat "None" als score wordt gebruikt
        if is_numeric(score_home) and is_numeric(score_away):
            score_home = int(score_home)
            score_away = int(score_away)

            team_stats[home_team]["goals_for"] += score_home
            team_stats[home_team]["goals_against"] += score_away
            team_stats[home_team]["matches_played"] += 1

            team_stats[away_team]["goals_for"] += score_away
            team_stats[away_team]["goals_against"] += score_home
            team_stats[away_team]["matches_played"] += 1

            if score_home > score_away:
                team_stats[home_team]["matches_won"] += 1
            elif score_home < score_away:
                team_stats[away_team]["matches_won"] += 1

    return team_stats

def calculate_percentage(part, whole):
    if whole == 0:
        return 0
    return round((part / whole) * 100, 2)

def generate_markdown(stats, output_filename):
    with open(output_filename, "w") as markdown_file:
        markdown_file.write("# Team Statistics\n\n")
        markdown_file.write("| Team | Goals For | Goals Against | Goal Difference | Matches Played | Matches Won | Win Percentage |\n")
        markdown_file.write("|------|-----------|--------------|------------------|-----------------|-------------|-----------------|\n")

        # Sorteer de ploegen volgens win percentage
        sorted_teams = sorted(stats.items(), key=lambda x: calculate_percentage(x[1]["matches_won"], x[1]["matches_played"]), reverse=True)

        for team, stat in sorted_teams:
            goal_difference = stat["goals_for"] - stat["goals_against"]
            win_percentage = calculate_percentage(stat["matches_won"], stat["matches_played"])

            markdown_file.write(f"| {team} | {stat['goals_for']} | {stat['goals_against']} | {goal_difference} | {stat['matches_played']} | {stat['matches_won']} | {win_percentage}% |\n")

        timestamp = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
        markdown_file.write(f"\n*Laatst bijgewerkt op {timestamp}*")
        
        logging.info(f"Statistieken berekend en opgeslagen in {output_filename}")

if __name__ == "__main__":
    input_filename = "uitvoer/verwerkt.csv"
    output_filename = "statistieken.md"

    data = read_csv(input_filename)

    if data:
        team_statistics = calculate_statistics(data)
        generate_markdown(team_statistics, output_filename)
    else:
        logging.warning("Geen gegevens beschikbaar voor statistieken.")
