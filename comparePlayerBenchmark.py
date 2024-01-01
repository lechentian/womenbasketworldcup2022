import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pygal

df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
# print(df.describe())
pd.set_option('display.max_columns', None)
#topEfficiencyPlayerDf = df.sort_values(by=['Efficiency'], ascending=False)
topEfficiencyPlayerDf = df[["PlayerId","Team", "OfficialName", "PointsTotal", "AssistsTotal", "FreeThrowsMadeTotal", "ReboundsTotal", "TurnOversTotal", "StealsTotal"]]
#topEfficiencyPlayerDf = topEfficiencyPlayerDf.head(10)
#print(topEfficiencyPlayerDf)

topEfficiencyPlayerDf[["PointsTotal", "AssistsTotal", "FreeThrowsMadeTotal","ReboundsTotal", "TurnOversTotal","StealsTotal"]] \
= MinMaxScaler().fit_transform(topEfficiencyPlayerDf[["PointsTotal", "AssistsTotal", "FreeThrowsMadeTotal",
                           "ReboundsTotal", "TurnOversTotal", "StealsTotal"]])
#print(topEfficiencyPlayerDf)



#print(topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] == 224131)].tolist())

#abc = topEfficiencyPlayerDf[topEfficiencyPlayerDf['PlayerId'] == 224131]
firstPlayerList = topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] == 224131)].iloc[0].tolist()
secondPlayerList = topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] ==218464 )].iloc[0].tolist()
thirdPlayerList = topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] == 203409)].iloc[0].tolist()
fourPlayerList = topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] == 258186)].iloc[0].tolist()
fivePlayerList = topEfficiencyPlayerDf[(topEfficiencyPlayerDf['PlayerId'] == 181482)].iloc[0].tolist()
print(firstPlayerList)
print(secondPlayerList)

#print(topEfficiencyPlayerDf.iloc[3].tolist()[2:])

radar_chart = pygal.Radar()
radar_chart.title = 'Player benchmark results'
radar_chart.x_labels = ['Points', 'Assists', 'FreeThrows', 'Rebounds', 'TurnOvers', 'Steals']
radar_chart.add(firstPlayerList[2], firstPlayerList[3:])
radar_chart.add(secondPlayerList[2], secondPlayerList[3:])
radar_chart.add(thirdPlayerList[2], thirdPlayerList[3:])
radar_chart.add(fourPlayerList[2], fourPlayerList[3:])
radar_chart.add(fivePlayerList[2], fivePlayerList[3:])
radar_chart.render_to_file("chart/chinaPlayerBenchmarkTop5.svg")
