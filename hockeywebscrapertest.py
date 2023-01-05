import pandas as pd
import numpy as np
import requests
import os
from bs4 import BeautifulSoup

all_data = ""
for page in range(2019, 2023):
    season = page + 1
    url = "https://www.hockey-reference.com/leagues/NHL_{page}_skaters.html".format(page =page+1)

    print(url)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    
    for records in soup.select('tr[class != "colhead"]'):
        player_data = ""
        for data in records.findAll('td'):
            player_data = player_data + "," + data.text
            
        all_data = all_data + '\n' + player_data[1:]
    all_data = all_data + '\n' + "SEASON: " + str(season - 1) + "-" + str(season)
stat_headers = "Player,Age,Team,Pos,GP,G,A,PTS,+/-,PIM,PS,EVG,PPG,SHG,GW,EVA,PPA,SHA,S,S%,TOI,ATOI,BLK,HIT,FOW,FOL,FO%"
file = open(os.path.expanduser('nhl_player_stat_databasetest.csv'), 'wb')
all_data = stat_headers + '\n' + all_data
## file.write(bytes(stat_headers, encoding='ascii',errors='ignore'))
file.write(bytes(all_data, encoding='ascii', errors='ignore'))

df = pd.read_csv('nhl_player_stat_databasetest.csv')    
columns = stat_headers

all_players_teams = df[['Player','Team']]
print(all_players_teams)

all_tot = df[df['Team'] == 'TOT']
subset_tot = all_tot[['Player','Team']]

tot_players = []
to_remove = []
for num in (subset_tot).index.values:
  player_name = subset_tot._get_value(num,'Player')
  tot_players.append(player_name)

for num in (subset_tot).index.values:
  for player in tot_players:
    i = num + 1
    next_name = all_players_teams._get_value(i,'Player')
    if next_name != player:
      (to_remove).append(player)
    i += 1

print(to_remove)

for elem in to_remove:
  pass
  # remove from data


# print(df.to_string())
## print(all_data)
print(df.index)
print(df.columns)
# print(df.axes)
print(df.dtypes)
print(df.size)
print(df.shape)
print(df.ndim)
print(df.empty)
print(df.T)
print(df.values)

