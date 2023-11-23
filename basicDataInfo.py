

import pandas as pd

df = pd.read_csv('women_basket_world_cup_2022_all_players.csv')
pd.set_option('display.max_columns', None)

print("-------- print this dataframe basic info --------")
print(df.describe())

print("-------- print this dataframe first row --------")
print(df.loc[0])

print("-------- print this dataframe 'PointsTotal' column--------")
print(df['PointsTotal'])