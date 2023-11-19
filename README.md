# Women Basket World Cup 2022 - All Players Data Analysis

## 1 get and save all players data to local
    https://www.fiba.basketball/womensbasketballworldcup/2022/playerstats
  python script : getPlayersData.py save output as 'women_basket_world_cup_2022_all_players.json'  
  


## 2 preprocessing data
   download file is json file, to use pandas library, we need convert json file to csv.\
   we need the following change for convert data.\
   1 add new column as Team.\
   2 add new column 'ReboundsTotal',get value from DefensiveReboundsTotal and OffensiveReboundsTotal

## 3 Player data analysis
### 3.1 top 10 player by efficiency 
![top 10 player by Efficiency](chart/top10playerByEfficiency.svg)

### 3.2 Player Compare 
Top 5 China Player Compare
![player top5 China player](chart/playerBenchmarkCHNTop5.svg)

Han vs Li
![player Han vs LI](chart/playerBenchmarkHanVsLi.svg)

Han vs Wilson
![player Han vs Wilson](chart/playerBenchmarkHanVsWilson.svg)

## 4 Team data analysis
Team China box data
![Team China](chart/teamCHNBenchmark.svg)

Team USA box data
![Team USA](chart/teamUSABenchmark.svg)

Team JPN box data
![Team JPN](chart/teamJPNBenchmark.svg)

## 5 conclusion

