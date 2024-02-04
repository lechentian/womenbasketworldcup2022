
import pandas as pd
import pygal
from pygal.style import Style



df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
USDf = df.loc[df['Team'] == 'USA']
USDf = USDf[["Team", "OfficialName","Efficiency","PointsTotal","AssistsTotal","FreeThrowsMadeTotal",
                             "ReboundsTotal","StealsTotal"]]
ChinaDf = df.loc[df['Team'] == 'CHN']
ChinaDf = ChinaDf[["Team", "OfficialName","Efficiency","PointsTotal","AssistsTotal","FreeThrowsMadeTotal",
                             "ReboundsTotal","StealsTotal"]]
#print(efficiencyDf)

custom_style = Style(colors=('#4554B3', '#D5262B', '#4554B3', '#D5262B','#4554B3', '#D5262B'))

box_plot = pygal.Box(style=custom_style)
box_plot.title = 'Team USA vs China (Offense)'
box_plot.add('USA Points', USDf["PointsTotal"].tolist())
box_plot.add('China Points', ChinaDf["PointsTotal"].tolist())
box_plot.add('USA Assists', USDf["AssistsTotal"].tolist())
box_plot.add('China Assists', ChinaDf["AssistsTotal"].tolist())
box_plot.add('USA FreeThrowsMade', USDf["FreeThrowsMadeTotal"].tolist())
box_plot.add('China FreeThrowsMade', ChinaDf["FreeThrowsMadeTotal"].tolist())
box_plot.render_to_file("chart/teamAustraliaToChinaBenchmarkOffense.svg")


