import pandas as pd

df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
#print(df.describe())
pd.set_option('display.max_columns', None)
# pointTotalDf = df.sort_values(by=['PointsTotal'], ascending=False)
# pointTotalDf = pointTotalDf[["Team", "OfficialName","PointsTotal"]]
# print(pointTotalDf.head(10))

co = df["PointsTotal"].corr(df["MinutesTotal"])
print(co)

co2 = df["AssistsTotal"].corr(df["TurnOversTotal"])
print(co2)



#print(df.corr())