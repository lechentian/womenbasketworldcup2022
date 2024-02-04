
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

custom_style = Style(colors=('#1B990F', '#D5262B', '#1B990F', '#D5262B'))

box_plot = pygal.Box(style=custom_style)
box_plot.title = 'Team Australia vs China (Dffense)'
box_plot.add('Australia Rebounds', AustraliaDf["ReboundsTotal"].tolist())
box_plot.add('China Rebounds', ChinaDf["ReboundsTotal"].tolist())
box_plot.add('Australia Steals', AustraliaDf["StealsTotal"].tolist())
box_plot.add('China Steals', ChinaDf["StealsTotal"].tolist())
box_plot.render_to_file("chart/teamAustraliaToChinaBenchmarkDefense.svg")


