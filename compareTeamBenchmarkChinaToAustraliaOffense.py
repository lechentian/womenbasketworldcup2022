
import pandas as pd
import pygal
from pygal.style import Style



df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
AustraliaDf = df.loc[df['Team'] == 'AUS']
AustraliaDf = AustraliaDf[["Team", "OfficialName","Efficiency","PointsTotal","AssistsTotal","FreeThrowsMadeTotal",
                             "ReboundsTotal","StealsTotal"]]
ChinaDf = df.loc[df['Team'] == 'CHN']
ChinaDf = ChinaDf[["Team", "OfficialName","Efficiency","PointsTotal","AssistsTotal","FreeThrowsMadeTotal",
                             "ReboundsTotal","StealsTotal"]]
#print(efficiencyDf)

custom_style = Style(colors=('#1B990F', '#D5262B', '#1B990F', '#D5262B','#1B990F', '#D5262B'))

box_plot = pygal.Box(style=custom_style)
box_plot.title = 'Team Australia vs China (Offense)'
box_plot.add('Australia Points', AustraliaDf["PointsTotal"].tolist())
box_plot.add('China Points', ChinaDf["PointsTotal"].tolist())
box_plot.add('Australia Assists', AustraliaDf["AssistsTotal"].tolist())
box_plot.add('China Assists', ChinaDf["AssistsTotal"].tolist())
box_plot.add('Australia FreeThrowsMade', AustraliaDf["FreeThrowsMadeTotal"].tolist())
box_plot.add('China FreeThrowsMade', ChinaDf["FreeThrowsMadeTotal"].tolist())
box_plot.render_to_file("chart/teamAustraliaToChinaBenchmarkOffense.svg")


