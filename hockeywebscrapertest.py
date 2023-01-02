import requests
import os
from bs4 import BeautifulSoup
all_data = ""
for page in range(2019, 2023):
    url = "https://www.hockey-reference.com/leagues/NHL_{page}_skaters.html".format(page =page+1)

    print(url)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    
    for records in soup.select('tr[class != "colhead"]'):
        player_data = ""
        for data in records.findAll('td'):
            player_data = player_data + "," + data.text
            
        all_data = all_data + '\n' + player_data[1:]
stat_headers = "Player, Age, Team, Pos, GP, G, A, PTS, +/-, PIM, PS, EV, PP, SH, GW, EV, PP, SH, S, S%, TOI, ATOI, BLK, HIT, FOW, FOL, FO%"
file = open(os.path.expanduser('nhl_player_stat_databasetest.csv'), 'wb')
file.write(bytes(stat_headers, encoding='ascii',errors='ignore'))
file.write(bytes(all_data, encoding='ascii', errors='ignore'))

    
print(all_data)



##for page in range(1,65):
  ##  url = "https://www.expansion.com/empresas-de/ganaderia/granjas-en-general/{page}.html".format(page =page)
    ###print(url)
    ##page = requests.get(url)
    ##soup = BeautifulSoup(page.content, "html.parser")
    ##lists = soup.select("div#simulacion_tabla ul")

    ##for lis in lists:
      ##  title = lis.find('li', class_="col1").text
        ##location = lis.find('li', class_="col2").text
        ##province = lis.find('li', class_="col3").text
        ##info = [title, location, province]
        ##print(info)

##