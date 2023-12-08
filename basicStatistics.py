
import json
with open('women_basket_world_cup_2022_all_players.json') as json_file:
    data = json.load(json_file)
for dat in data:
    print(type(dat))
    print(dat)


# basic statistics https://fanlv.fun/2018/06/19/statistics/