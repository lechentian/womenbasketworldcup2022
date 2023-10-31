

# import pandas as pd
#
# with open('women_basket_world_cup_2022_all_players.json', encoding='utf-8') as inputfile:
#     df = pd.read_json(inputfile)
#
# df.to_csv('women_basket_world_cup_2022_all_players_origin.csv', encoding='utf-8', index=False)


import json
import csv

with open('women_basket_world_cup_2022_all_players.json') as json_file:
    data = json.load(json_file)
json_data = json.dumps(data, indent=4)

data_file = open('women_basket_world_cup_2022_all_players.csv', 'w')
csv_writer = csv.writer(data_file)

header = ["PlayerId","Position","OfficialName","Team","GamesPlayedTotal","MinutesTotal",
          "SecondsTotal","PointsTotal","FieldGoals2PointsMadeTotal","FieldGoals2PointsAttemptedTotal",
          "FieldGoals3PointsMadeTotal","FieldGoals3PointsAttemptedTotal","FreeThrowsMadeTotal",
          "FreeThrowsAttemptedTotal","OffensiveReboundsTotal","DefensiveReboundsTotal","BlocksTotal",
          "AssistsTotal","TurnOversTotal","StealsTotal","PersonalFoulsTotal","Efficiency","PlusMinus",
          "DoubleDoubles","TripleDoubles"]
csv_writer.writerow(header)

for dat in data:
    dat.pop('PlayerLink', None)
    dat.pop('ShirtNumber', None)
    OfficialName = dat['OfficialName']
    Name = OfficialName.split("(")[0].strip()
    Team = OfficialName.split("(")[1]
    dat['OfficialName'] = Name
    dat['LastName'] =Team[:-1]
    csv_writer.writerow(dat.values())
data_file.close()
