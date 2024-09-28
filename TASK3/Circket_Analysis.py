import csv
# Input_Data
fielding_data = [
    [1, 1, "RCB", "Virat Kohli", 1.1, "Cover", "Clean pick and good throw", "Clean pick", "Run out", 3, 1,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Faf du Plessis", 2.3, "Mid-off", "Catch taken", "Catch", "No throw", 2, 2, "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Glenn Maxwell", 3.4, "Deep Midwicket", "Clean pick and fumble", "Fumble", "Missed run out", -2, 3,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Mahipal Lomror", 4.1, "Long-on", "Clean pick, direct hit", "Clean pick", "Run out", 4, 4,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Dinesh Karthik", 5.2, "Wicketkeeper", "Stumping", "Clean pick", "Stumping", 5, 5,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Harshal Patel", 6.5, "Long-off", "Catch dropped", "Drop catch", "Missed run out", -4, 6,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Wanindu Hasaranga", 7.3, "Midwicket", "Clean pick", "Clean pick", "No throw", 2, 7,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Shahbaz Ahmed", 8.2, "Point", "Direct hit run-out", "Clean pick", "Run out", 6, 8,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Mohammed Siraj", 9.5, "Mid-off", "Clean pick", "Clean pick", "No throw", 1, 9,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Josh Hazlewood", 10.4, "Long-off", "Good throw, no run out", "Good throw", "No throw", 0, 10,
     "Chinnaswamy Stadium"],
    [1, 1, "RCB", "Karn Sharma", 11.6, "Third man", "Clean pick and fumble", "Fumble", "Missed run out", -1, 11,
     "Chinnaswamy Stadium"]
]
# performance score formula
weights = {
    "Clean pick": 1.5,
    "Good throw": 2.0,
    "Catch": 3.0,
    "Drop catch": -2.0,
    "Stumping": 4.0,
    "Run out": 5.0,
    "Missed run out": -1.0,
    "Direct hit": 3.5,
    "Fumble": -1.5
}
player_performance = {}
def calculate_performance_score(events):
    total_score = 0
    runs_saved = 0
    for event in events:
        pick, throw, runs = event["Pick"], event["Throw"], event["Runs"]

        # Add score for the pick-up
        if pick in weights:
            total_score += weights[pick]

        # Add score for the throw
        if throw in weights:
            total_score += weights[throw]
        runs_saved += runs

    return total_score + runs_saved

for entry in fielding_data:
    match_no, innings, team, player_name, ballcount, position, description, pick, throw, runs, overcount, venue = entry


    if player_name not in player_performance:
        player_performance[player_name] = []


    player_performance[player_name].append({
        "Pick": pick,
        "Throw": throw,
        "Runs": runs
    })
for player, events in player_performance.items():
    performance_score = calculate_performance_score(events)
    print(f"Player: {player}")
    print(f"Performance Score: {performance_score}")
    print("-" * 30)

output_file = 'Fielding_analysis_2024.csv'
with open(output_file, mode='w', newline='') as file:
    fieldnames = ['Player Name', 'Performance Score']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # player performance data
    for player, events in player_performance.items():
        performance_score = calculate_performance_score(events)
        csv_writer.writerow({'Player Name': player, 'Performance Score': performance_score})

print(f"Performance analysis data saved to {output_file}.")
