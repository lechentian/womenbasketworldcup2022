
import pandas as pd
import pygal



df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
efficiencyDf = df.loc[df['Team'] == 'USA']
efficiencyDf = efficiencyDf[["Team", "OfficialName","Efficiency","PointsTotal","AssistsTotal","FreeThrowsMadeTotal",
                             "ReboundsTotal","StealsTotal"]]
print(efficiencyDf)

box_plot = pygal.Box()
box_plot.title = 'Team USA'
box_plot.add('Efficiency', efficiencyDf["Efficiency"].tolist())
box_plot.add('Points', efficiencyDf["PointsTotal"].tolist())
box_plot.add('Assists', efficiencyDf["AssistsTotal"].tolist())
box_plot.add('FreeThrowsMade', efficiencyDf["FreeThrowsMadeTotal"].tolist())
box_plot.add('Rebounds', efficiencyDf["ReboundsTotal"].tolist())
box_plot.add('Steals', efficiencyDf["StealsTotal"].tolist())
box_plot.render_to_file("chart/teamUSABenchmark.svg")

