
import requests
import json

print('fetching and saving player data from FIBA')
r = requests.get('https://www.fiba.basketball/en/Module/970915d0-6793-4baf-9c9f-88bd718911a1/00000000-0000-0000-0000-000000000000')
json_data = r.json()

with open('women_basket_world_cup_2022_all_players.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print('save all player data to women_basket_world_cup_2022_all_players.json')
