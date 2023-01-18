# Table made with BeautifulSoup returns empty list. May need to get through JavaScript

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

session = requests.Session()
payload = {
    'log': os.getenv("FFB_USERNAME"), 
    'pwd': os.getenv("FFB_PASSWORD")
    }

s = session.post('https://www.thefantasyfootballers.com/login/', data=payload)

positions = ('QB', 'RB', 'WR', 'TE', 'D')
ownerships = []

page = session.get('https://www.thefantasyfootballers.com/2022-ultimate-dfs-pass/dfs-pass-roster-percentage/?position=QB')

soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find_all('table')
# df = pd.read_html(get_request, flavor='lxml')

# s = session.get('https://www.thefantasyfootballers.com/2022-ultimate-dfs-pass/dfs-pass-roster-percentage/?position=QB')
# soup = BeautifulSoup(s.text, 'html.parser')
# table = soup.find('table')

# headers = []
# for i in table.find_all('th'):
#     title = i.text
#     headers.append(title)
    
# for j in table.find_all('tr')[1:]:
#     row_data = j.find_all('td')
#     row = [i.text for i in row_data]
#     length = len(pffown_df)
#     pffown_df.loc[length] = row