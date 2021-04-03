import numpy as np
import csv

# Creating Python list
mlbdata = []
f = "1035 Records of Heights (in) and Weights (lbs) of Major League Baseball Players.csv"
with open(f, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    for row in csvreader:
        mlbdata.append(list(row))

# Creating initial Numpy array
arrdata = np.array(mlbdata)

# Creating variables by indexing arrdata, converting height and weight data to integers and multiplying the integers to reflect metric measurements
team = arrdata[:, 1]
teams = ["BAL", "CWS", "ANA", "BOS", "CLE", "OAK", "NYY", "DET", "SEA", "TB", "KC", "TEX", "TOR", "MIN", "ATL", "CHC", "ARZ", "FLA", "CIN", "COL", "NYM", "HOU", "LA", "PHI", "MLW", "SD", "WAS", "PIT", "SF", "STL"]
position = arrdata[:, 2]
positions = ["Catcher", "First Baseman", "Second Baseman", "Shortstop", "Third Baseman", "Outfielder", "Designated Hitter", "Starting Pitcher", "Relief Pitcher"]
height = arrdata[:, 3].astype(int) * 0.0254
weight = arrdata[:, 4].astype(int) * 0.453592

# Calculating BMI
bmi = weight / (height ** 2)

# Finding the mean and median values of BMI by team and position
print("== Average BMI by Team ==")
for team_bmi_avg in teams:
    print(team_bmi_avg + ": " + str("{:.2f}".format(np.mean(bmi[team == team_bmi_avg]))))
print("== Average BMI by Position ==")
for position_bmi_avg in positions:
    print(position_bmi_avg + ": " + str("{:.2f}".format(np.mean(bmi[position == position_bmi_avg]))))
print("== Median BMI by Team ==")
for team_bmi_med in teams:
    print(team_bmi_med + ": " + str("{:.2f}".format(np.median(bmi[team == team_bmi_med]))))
print("== Median BMI by Position ==")
for position_bmi_med in positions:
    print(position_bmi_med + ": " + str("{:.2f}".format(np.median(bmi[position == position_bmi_med]))))
