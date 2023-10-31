import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pygal

df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
# print(df.describe())
pd.set_option('display.max_columns', None)
#topEfficiencyPlayerDf = df.sort_values(by=['Efficiency'], ascending=False)
topEfficiencyPlayerDf = df[["PlayerId","Team", "OfficialName", "PointsTotal", "AssistsTotal", "FreeThrowsMadeTotal",
     "OffensiveReboundsTotal", "DefensiveReboundsTotal", "StealsTotal"]]
#topEfficiencyPlayerDf = topEfficiencyPlayerDf.head(10)
#print(topEfficiencyPlayerDf)

topEfficiencyPlayerDf[["PointsTotal", "AssistsTotal", "FreeThrowsMadeTotal",
                       "OffensiveReboundsTotal", "DefensiveReboundsTotal","StealsTotal"]] \
= MinMaxScaler().fit_transform(topEfficiencyPlayerDf[["PointsTotal", "AssistsTotal", "FreeThrowsMadeTotal",
                           "OffensiveReboundsTotal", "DefensiveReboundsTotal", "StealsTotal"]])
#print(topEfficiencyPlayerDf)



#print(topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] == 224131)].tolist())

#abc = topEfficiencyPlayerDf[topEfficiencyPlayerDf['PlayerId'] == 224131]
firstPlayerList = topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] == 224131)].iloc[0].tolist()
secondPlayerList = topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] == 239832)].iloc[0].tolist()
print(firstPlayerList)
print(secondPlayerList)

#print(topEfficiencyPlayerDf.iloc[3].tolist()[2:])

radar_chart = pygal.Radar()
radar_chart.title = 'Player benchmark results'
radar_chart.x_labels = ['Points', 'Assists', 'FreeThrows', 'OffensiveRebounds', 'DefensiveRebounds', 'Steals']
radar_chart.add(firstPlayerList[2], firstPlayerList[3:])
radar_chart.add(secondPlayerList[2], secondPlayerList[3:])
radar_chart.render_to_file("chart/playerBenchmark.svg")
