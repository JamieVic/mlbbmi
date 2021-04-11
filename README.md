# MLB BMI
## About this Project
The mean and median BMIs (Body Mass Index) of MLB (Major League Baseball) players is calculated and categorised by team and position.
## How it Works
Every MLB player's height and weight has been taken and stored in a CSV file. A Python list appends the data from the CSV file and a NumPy function takes the list and turns it into an array. A simple calculation is used to find the BMI of each player. Two NumPy functions are used to find the average and median BMIs per team and position.
## Results
In no particular order, here are the results:
### BMI by Teams
| Team | Mean | Median |
| --- | --- | --- |
| BAL | 25.58 | 25.04 |
| CWS | 26.56 | 26.35 |
| ANA | 26.26 | 26.25 |
| BOS | 26.13 | 26.25 |
| CLE | 25.79 | 25.42 |
| OAK | 26.05 | 25.83 |
| NYY | 26.46 | 26.47 |
| DET | 26.41 | 26.32 |
| SEA | 25.79 | 25.76 |
| TB | 25.58 | 26.32 |
| KC | 25.44 | 25.09 |
| TEX | 25.96 | 25.68 |
| TOR | 26.18 | 26.11 |
| MIN | 26.43 | 26.78 |
| ATL | 25.73 | 25.68 |
| CHC | 26.11 | 25.97 |
| ARZ | 26.95 | 26.90 |
| FLA | 26.00 | 25.49 |
| CIN | 26.33 | 26.17 |
| COL | 25.50 | 26.12 |
| NYM | 26.07 | 26.24 |
| HOU | 26.12 | 25.96 |
| LA | 26.65 | 26.17 |
| PHI | 25.32 | 25.44 |
| MLW | 26.66 | 26.45 |
| SD | 26.55 | 26.39 |
| WAS | 25.48 | 25.07 |
| PIT | 26.49 | 26.58 |
| SF | 26.35 | 26.21 |
| STL | 26.15 | 25.71 |
### BMI by Positions
| Position | Mean | Median |
| --- | --- | --- |
| Catcher | 27.17 | 27.06 |
| First Baseman | 27.35 | 27.71 |
| Second Baseman | 25.47 | 25.10 |
| Shortstop | 24.88 | 24.41 |
| Third Baseman | 26.44 | 26.39 |
| Outfielder | 26.25 | 26.11 |
| Designated Hitter | 28.16 | 28.00 |
| Starting Pitcher | 25.82 | 25.81 |
| Relief Pitcher | 25.85 | 25.68 |
## Conclusion
From observation, it is determined that ARZ (Arizona Diamondbacks) players have the highest average BMI with 26.95, and PHI (Philadelphia Phillies) players have the lowest average BMI with 25.32. For positions, the First Basemen have the highest average BMI with 27.35, and Shortstop players have the lowest average BMI with 24.88.

Data Source: http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights
