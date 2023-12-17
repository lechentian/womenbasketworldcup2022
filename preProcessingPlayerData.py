

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
          "DoubleDoubles","TripleDoubles","ReboundsTotal"]
csv_writer.writerow(header)


for dat in data:
    #print('-----------------')
    #print(dat)
    dat.pop('PlayerLink', None)
    dat.pop('ShirtNumber', None)
    OfficialName = dat['OfficialName']
    #print(OfficialName)
    Name = OfficialName.split("(")[0].strip()
    Team = OfficialName.split("(")[1]
    dat['OfficialName'] = Name
    dat['LastName'] =Team[:-1]
    dat['ReboundsTotal'] = dat['DefensiveReboundsTotal'] + dat['OffensiveReboundsTotal']
    dat['PointsTotal'] = abs(dat['PointsTotal'])
    #print(dat.values())
    csv_writer.writerow(dat.values())
data_file.close()


{'PlayerId': 224132, 'PlayerLink': '/womensbasketballworldcup/2022/player/Yuan-Li',
 'ShirtNumber': 'N/A', 'Position': 'Guard', 'OfficialName': 'Yuan Li (CHN)',
 'LastName': 'Li', 'GamesPlayedTotal': 8, 'MinutesTotal': 124,
 'SecondsTotal': 7474, 'PointsTotal': 38, 'FieldGoals2PointsMadeTotal': 7,
 'FieldGoals2PointsAttemptedTotal': 20, 'FieldGoals3PointsMadeTotal': 7,
 'FieldGoals3PointsAttemptedTotal': 16, 'FreeThrowsMadeTotal': 3, 'FreeThrowsAttemptedTotal': 6, 'OffensiveReboundsTotal': 7, 'DefensiveReboundsTotal': 7, 'BlocksTotal': 0, 'AssistsTotal': 28, 'TurnOversTotal': 11, 'StealsTotal': 4, 'PersonalFoulsTotal': 12, 'Efficiency': 48.0, 'PlusMinus': 83, 'DoubleDoubles': 0, 'TripleDoubles': 0}

