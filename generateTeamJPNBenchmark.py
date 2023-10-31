import pandas as pd
import pygal



df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
efficiencyDf = df.loc[df['Team'] == 'JPN']
efficiencyDf = efficiencyDf[["Team", "OfficialName","Efficiency","PointsTotal","AssistsTotal","FreeThrowsMadeTotal",
                             "OffensiveReboundsTotal","DefensiveReboundsTotal","StealsTotal"]]
#print(efficiencyDf)

box_plot = pygal.Box()
box_plot.title = 'Team JPN'
box_plot.add('Efficiency', efficiencyDf["Efficiency"].tolist())
box_plot.add('Points', efficiencyDf["PointsTotal"].tolist())
box_plot.add('Assists', efficiencyDf["AssistsTotal"].tolist())
box_plot.add('FreeThrows', efficiencyDf["FreeThrowsMadeTotal"].tolist())
box_plot.add('Offensive Rebounds', efficiencyDf["OffensiveReboundsTotal"].tolist())
box_plot.add('Defensive Rebounds', efficiencyDf["DefensiveReboundsTotal"].tolist())
box_plot.add('Steals', efficiencyDf["StealsTotal"].tolist())
box_plot.render_to_file("chart/teamJPNBenchmark.svg")



