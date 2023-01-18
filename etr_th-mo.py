import requests
import pandas as pd
from bs4 import BeautifulSoup
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

ETR_username = os.getenv("ETR_USERNAME")
ETR_pass = os.getenv("ETR_PASSWORD")

t = datetime.datetime.now()
now = t.strftime("%Y%m%d%H%M")

session = requests.Session()
payload = {
    'log' : ETR_username,
    'pwd' : ETR_pass }

s = session.post('https://establishtherun.com/wp-login.php', data=payload)

s = session.get('https://establishtherun.com/fantasy-point-projections/')

soup = BeautifulSoup(s.text, 'html.parser')

table = soup.find_all('table')
table = table[1]

headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)
    
etr_df = pd.DataFrame(columns=headers)
    
for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(etr_df)
    etr_df.loc[length] = row
    
etr_df['Player'] = etr_df.Player.apply(lambda x: x.strip())

team_changes = {
    'ARI DST':'Cardinals',
'ATL DST':'Falcons',
'BAL DST':'Ravens',
'BUF DST':'Bills',
'CAR DST':'Panthers',
'CHI DST':'Bears',
'CIN DST':'Bengals',
'CLE DST':'Browns',
'DAL DST':'Cowboys',
'DEN DST':'Broncos',
'DET DST':'Lions',
'GB DST':'Packers',
'HOU DST':'Texans',
'IND DST':'Colts',
'JAX DST':'Jaguars',
'KC DST':'Chiefs',
'LA DST':'Rams',
'LAC DST':'Chargers',
'LV DST':'Raiders',
'MIA DST':'Dolphins',
'MIN DST':'Vikings',
'NE DST':'Patriots',
'NO DST':'Saints',
'NYG DST':'Giants',
'NYJ DST':'Jets',
'PHI DST':'Eagles',
'PIT DST':'Steelers',
'SEA DST':'Seahawks',
'SF DST':'49ers',
'TB DST':'Buccaneers',
'TEN DST':'Titans',
'WAS DST':'Commanders'

    }

player_changes = {
    'Kenneth Walker': 'Kenneth Walker III',
    'Travis Etienne': 'Travis Etienne Jr.',
    'A.J. Dillon': 'AJ Dillon',
    'Brian Robinson': 'Brian Robinson Jr.',
    'Jeffery Wilson': 'Jeff Wilson Jr.',
    'Chigoziem Okonkwo': 'Chig Okonkwo',
    'Donald Parham': 'Donald Parham Jr.',
    'Michael Pittman', 'Michael Pittman Jr.',
    'D.J. Moore': 'DJ Moore',
    'Josh Palmer': 'Joshua Palmer',
    'D.J. Chark': 'DJ Chark Jr.',
    'Richie James': 'Richie James Jr.',
    'Terrace Marshall': 'Terrace Marshall Jr.',
    'Marvin Jones': 'Marvin Jones Jr.', 
    'Laviska Shenault': 'Laviska Shenault Jr.', 
    'Phillip Dorsett': 'Phillip Dorsett II', 
    'Gardner Minshew': 'Gardner Minshew II'
    }

etr_df.replace({"Player": team_changes}, inplace=True)
etr_df.replace({"Player": player_changes}, inplace=True)


    
    
    