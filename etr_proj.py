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

s = session.get('https://establishtherun.com/draftkings-projections/')

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
    

    
