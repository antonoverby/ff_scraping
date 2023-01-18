import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.footballguys.com/dfs-roster-percentages'
page = requests.get(url)

#print(page)

soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table', class_='table')
print(tables[0])