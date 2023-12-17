

#{'PlayerId': 240137, 'PlayerLink': '/womensbasketballworldcup/2022/player/Aika-Hirashita',
# 'ShirtNumber': 'N/A', 'Position': 'Shooting Guard', 'OfficialName': 'Aika Hirashita (JPN)',
# 'LastName': 'Hirashita', 'GamesPlayedTotal': 5, 'MinutesTotal': 96, 'SecondsTotal': 5777,
# 'PointsTotal': 43, 'FieldGoals2PointsMadeTotal': 4, 'FieldGoals2PointsAttemptedTotal': 12,
# 'FieldGoals3PointsMadeTotal': 11, 'FieldGoals3PointsAttemptedTotal': 28, 'FreeThrowsMadeTotal': 2,
# 'FreeThrowsAttemptedTotal': 2, 'OffensiveReboundsTotal': 2, 'DefensiveReboundsTotal': 6, 'BlocksTotal': 0, 'AssistsTotal': 3, 'TurnOversTotal': 1, 'StealsTotal': 3, 'PersonalFoulsTotal': 5, 'Efficiency': 31.0, 'PlusMinus': 28, 'DoubleDoubles': 0, 'TripleDoubles': 0}

# basic statistics https://fanlv.fun/2018/06/19/statistics/
import json
with open('women_basket_world_cup_2022_all_players.json') as json_file:
    data = json.load(json_file)
#playercount = 0
#timecount = 0
low_est = 1000000

for dat in data:
    print('-------')
    #print(type(dat))
    #print(dat['MinutesTotal'])
    # playercount = playercount + 1
    # timecount = timecount + dat['MinutesTotal']
    if dat['MinutesTotal'] < low_est:
        low_est = dat['MinutesTotal']
print(low_est)

# print(timecount / playercount)
#print(playercount)


