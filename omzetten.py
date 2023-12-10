import os
import json
import logging

logging.basicConfig(
    filename="omgezet.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def read_json(filename):
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        logging.error(f"Fout bij het lezen van het bestand '{filename}': {e}")
        return None

def process_and_write_to_file(data, output_filename):
    if data:
        with open(output_filename, "w") as output_file:
            output_file.write("date,home_team,away_team,home_score,away_score\n")

            for match in data.get("matches", []):
                date = match.get("utcDate", "Onbekend")
                home_team = match.get("homeTeam", {}).get("name", "Onbekend thuis")
                away_team = match.get("awayTeam", {}).get("name", "Onbekend uit")
                score_home = match.get("score", {}).get("fullTime", {}).get("homeTeam", "Onbekend thuis")
                score_away = match.get("score", {}).get("fullTime", {}).get("awayTeam", "Onbekend uit")

                output_file.write(f"{date},{home_team},{away_team},{score_home},{score_away}\n")

            logging.info(f"Gegevens verwerkt en opgeslagen in {output_filename}")
    else:
        logging.warning("Geen gegevens beschikbaar.")

def process_data_folder_and_write():
    data_folder = "data"
    output_folder = "uitvoer"
    output_filename = "verwerkt.csv"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(data_folder):
        if filename.endswith(".json"):
            full_path = os.path.join(data_folder, filename)
            data = read_json(full_path)
            output_path = os.path.join(output_folder, output_filename)
            process_and_write_to_file(data, output_path)

if __name__ == "__main__":
    process_data_folder_and_write()
