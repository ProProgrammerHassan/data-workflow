import requests
import json
from datetime import datetime

def fetch_bundesliga_results():
    url = "https://api.football-data.org/v2/competitions/BL1/matches"
    headers = {"X-Auth-Token": "bef7045b5333493ead87607554cedaf4"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Er kon geen data opgehaald worden: {e}")
        return None

def save_json(data):
    if data:
        currenttime = datetime.now().strftime("%Y%m%d%H%M")
        filename = f"data/BundesligaResults_{currenttime}.json"

        try:
            with open(filename, "w") as json_file:
                json.dump(data, json_file, indent=2)

            print(f"Data saved to {filename}")
            return filename
        except Exception as e:
            print(f"Er kon geen JSON Gemaakt worden: {e}")
    else:
        print("Leeg")
        return None

if __name__ == "__main__":
    football_data = fetch_bundesliga_results()
    json_filename = save_json(football_data)


    with open('/home/linuxmint/script_log.log', 'a') as log_file:
        log_file.write('Ran on: {}\n'.format(datetime.now()))
