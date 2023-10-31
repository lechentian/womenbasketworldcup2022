
import pandas as pd
import pygal

df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
efficiencyDf = df.sort_values(by=['Efficiency'], ascending=False)
efficiencyDf = efficiencyDf[["Team", "OfficialName","Efficiency","PointsTotal","AssistsTotal","DefensiveReboundsTotal",
                             "StealsTotal", "TurnOversTotal", "PersonalFoulsTotal"]]
#print(efficiencyDf.head(10)["OfficialName"].tolist())
#print(efficiencyDf.head(10)["Efficiency"].tolist())

bar_chart = pygal.Bar()
bar_chart.title = 'Top 10 Player by Efficiency'
bar_chart.x_labels = efficiencyDf.head(10)["OfficialName"].tolist()
bar_chart.add('Efficiency', efficiencyDf.head(10)["Efficiency"].tolist())
bar_chart.add('Points', efficiencyDf.head(10)["PointsTotal"].tolist())
bar_chart.add('Assist',      efficiencyDf.head(10)["AssistsTotal"].tolist())
bar_chart.add('Steal',  efficiencyDf.head(10)["StealsTotal"].tolist())
bar_chart.add('Turn Overs',  efficiencyDf.head(10)["TurnOversTotal"].tolist())
bar_chart.add('Fouls',  efficiencyDf.head(10)["PersonalFoulsTotal"].tolist())
bar_chart.render_to_file("chart/top10playerByEfficiency.svg")
