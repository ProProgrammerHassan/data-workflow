# Lees de inhoud van het statistieken.md bestand en parse de tabel
with open("statistieken.md", "r", encoding="utf-8") as statistieken_file:
    statistieken_inhoud = statistieken_file.read()

# Zoek de tabel en split de rijen
tabel_start = statistieken_inhoud.find("| Team |")
tabel_einde = statistieken_inhoud.find("*Laatst bijgewerkt op")
tabel_inhoud = statistieken_inhoud[tabel_start:tabel_einde].strip()

rijen = tabel_inhoud.split('\n')
header = rijen[0].strip('|').split('|')
teams_data = [dict(zip(header, map(str.strip, rij.strip('|').split('|')))) for rij in rijen[2:]]

# Bereken de gevraagde waarden
aantal_matchen = len(teams_data)
totaal_goals_voor = sum(int(team[' Goals For']) for team in teams_data)
totaal_goals_tegen = sum(int(team[' Goals Against']) for team in teams_data)
totaal_goal_diff = sum(int(team[' Goal Difference']) for team in teams_data)

# Lees het sjabloonbestand
with open("sjabloon.txt", "r", encoding="utf-8") as sjabloon_file:
    sjabloon_inhoud = sjabloon_file.read()

# Vervang de variabelen in het sjabloon
sjabloon_inhoud = sjabloon_inhoud.replace("[matchen]", str(aantal_matchen))
sjabloon_inhoud = sjabloon_inhoud.replace("[goals_for]", str(totaal_goals_voor))
sjabloon_inhoud = sjabloon_inhoud.replace("[goals_against]", str(totaal_goals_tegen))
sjabloon_inhoud = sjabloon_inhoud.replace("[goal_diff]", str(totaal_goal_diff))

# Schrijf het resultaat naar het tussenresultaten.txt bestand
with open("tussenresultaten.txt", "w", encoding="utf-8") as resultaten_file:
    resultaten_file.write(sjabloon_inhoud)

print("Tussenresultaten zijn berekend en opgeslagen in tussenresultaten.txt.")
