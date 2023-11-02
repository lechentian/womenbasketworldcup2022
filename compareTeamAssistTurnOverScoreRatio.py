import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pygal

df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')

usaDf = df.loc[df['Team'] == 'USA']
usaDf = usaDf[["Team", "OfficialName","PointsTotal","GamesPlayedTotal", "AssistsTotal", "TurnOversTotal" ]]

usaPointsLists = usaDf["PointsTotal"].tolist()
useGamePlayeds = usaDf["GamesPlayedTotal"].tolist()
useAssists = usaDf["AssistsTotal"].tolist()
useTurnOvers = usaDf["TurnOversTotal"].tolist()
usaList = []
for i in range(len(usaPointsLists)):
    usaList.append(( usaPointsLists[i]/useGamePlayeds[i], useAssists[i]/useTurnOvers[i]))

chnDf = df.loc[df['Team'] == 'CHN']
chnDf = chnDf[["Team", "OfficialName","PointsTotal","GamesPlayedTotal", "AssistsTotal", "TurnOversTotal" ]]

chnPointsLists = chnDf["PointsTotal"].tolist()
chnGamePlayeds = chnDf["GamesPlayedTotal"].tolist()
chnAssists = chnDf["AssistsTotal"].tolist()
chnTurnOvers = chnDf["TurnOversTotal"].tolist()
chnList = []
for i in range(len(chnPointsLists)):
    chnList.append(( chnPointsLists[i]/chnGamePlayeds[i], chnAssists[i]/chnTurnOvers[i]))

jpnDf = df.loc[df['Team'] == 'JPN']
jpnDf = jpnDf[["Team", "OfficialName","PointsTotal","GamesPlayedTotal", "AssistsTotal", "TurnOversTotal" ]]
jpnPointsLists = jpnDf["PointsTotal"].tolist()
jpnGamePlayeds = jpnDf["GamesPlayedTotal"].tolist()
jpnAssists = jpnDf["AssistsTotal"].tolist()
jpnTurnOvers = jpnDf["TurnOversTotal"].tolist()
jpnList = []
for i in range(len(jpnPointsLists)):
    jpnList.append(( jpnPointsLists[i]/jpnGamePlayeds[i], jpnAssists[i]/jpnTurnOvers[i]))


bihDf = df.loc[df['Team'] == 'BIH']
bihDf = bihDf[["Team", "OfficialName","PointsTotal","GamesPlayedTotal", "AssistsTotal", "TurnOversTotal" ]]
bihPointsLists = bihDf["PointsTotal"].tolist()
bihGamePlayeds = bihDf["GamesPlayedTotal"].tolist()
bihAssists = bihDf["AssistsTotal"].tolist()
bihTurnOvers = bihDf["TurnOversTotal"].tolist()
bihList = []
for i in range(len(bihPointsLists)):
    bihList.append(( bihPointsLists[i]/bihGamePlayeds[i], bihAssists[i]/bihTurnOvers[i]))

print(usaList)
print(usaDf["OfficialName"].tolist())
print(chnList)
print(chnDf["OfficialName"].tolist())
print(jpnList)
print(jpnDf["OfficialName"].tolist())
print(bihList)
print(bihDf["OfficialName"].tolist())

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Assist Turnover Ratio vs Points Per Game'
xy_chart.add('USA', usaList)
xy_chart.add('China', chnList)
xy_chart.add('JPN', jpnList)
xy_chart.add('BIH', bihList)
xy_chart.render_to_file("chart/teamAssistTurnOverScoreRatio.svg")
