import re

def parse_markdown_table(markdown):
    # Extract data from markdown table
    lines = markdown.strip().split('\n')

    # Check if there are at least three lines (header, separator, data)
    if len(lines) < 3:
        print("Invalid markdown table. Expected at least three lines.")
        return None, None

    header = [item.strip() for item in lines[0].split('|')[1:-1]]

    # Check if the header has the expected number of elements
    if len(header) != 7:
        print("Invalid number of columns in the header. Expected 7 columns.")
        return None, None

    # Identify the separator line by finding the position of '|'
    separator_line = lines[1]
    separator_positions = [pos for pos, char in enumerate(separator_line) if char == '|']

    # Check if there are at least two '|' characters in the separator line
    if len(separator_positions) < 2:
        print("Invalid separator line in the markdown table.")
        return None, None

    # Check if the separator line has the expected number of elements
    if len(separator_positions) != len(header) + 1:
        print("Invalid number of columns in the separator line.")
        return None, None

    try:
        data = [list(map(str.strip, line.split('|')[1:-1])) for line in lines[2:]]
    except Exception as e:
        print(f"Error while parsing data: {e}")
        return None, None

    return header, data

def calculate_totals(data):
    total_matchen = 0
    total_goals = 0
    total_saldo = 0

    for row in data:
        try:
            total_matchen += int(row[4])
        except ValueError:
            print(f"Invalid value for 'Matches Played': {row[4]}")
        total_goals += int(row[1])
        total_saldo += int(row[3])

    return total_matchen, total_goals, total_saldo

def calculate_total_goals_for_all_teams(data):
    return sum([int(team[1]) for team in data])

def calculate_total_goal_difference_for_all_teams(data):
    return sum([int(team[3]) for team in data])

def main():
    with open('statistieken.md', 'r') as file:
        markdown_content = file.read()

    header, data = parse_markdown_table(markdown_content)

    if header is None or data is None:
        print("Error parsing markdown table. Exiting.")
        return

    total_matchen, total_goals, total_saldo = calculate_totals(data)
    total_goals_for_all_teams = calculate_total_goals_for_all_teams(data)
    total_goal_difference_for_all_teams = calculate_total_goal_difference_for_all_teams(data)

    # Open het sjabloonbestand en lees de inhoud
    with open('Sjabloon.txt', 'r') as template_file:
        template_content = template_file.read()

    # Vervang de placeholders in het sjabloon met de berekende waarden
    template_content = template_content.replace('[matchen]', str(total_matchen))
    template_content = template_content.replace('[goals_for]', str(total_goals_for_all_teams))
    template_content = template_content.replace('[goal_diff]', str(total_goal_difference_for_all_teams))

    # Schrijf het resultaat naar een nieuw Markdown-bestand
    with open('resultaten.md', 'w') as result_file:
        result_file.write(template_content)

if __name__ == "__main__":
    main()

