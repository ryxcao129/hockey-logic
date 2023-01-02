import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
## os is used at end to save the data

def create_soup(url):
    webpage = urllib.request.urlopen(url)
    soup = BeautifulSoup(webpage,'html.parser')
    return soup
## read the table rows and table columns and then pull them out and save to csv file

soup = create_soup('https://www.hockey-reference.com/leagues/NHL_2023_skaters.html')
## put desired url in parentheses

all_data = ""
for records in soup.select('tr[class != "colhead"]'):
    player_data = ""
    for data in records.findAll('td'):
        player_data = player_data + "," + data.text
    all_data = all_data + '\n' + player_data[1:]

stat_headers = "Player, Age, Team, Pos, GP, G, A, PTS, +/-, PIM, PS, EV, PP, SH, GW, EV, PP, SH, S, S%, TOI, ATOI, BLK, HIT, FOW, FOL, FO%"
file = open(os.path.expanduser('nhl_player_stat_database.csv'), 'wb')
file.write(bytes(stat_headers, encoding='ascii',errors='ignore'))
file.write(bytes(all_data, encoding='ascii', errors='ignore'))

print(all_data)

## Filters: If TOT in player_data -> delete future mentions of player_name in player_data