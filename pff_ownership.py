import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.pff.com/dfs/ownership'
page = requests.get(url)

#Test for <Response [200]> reply
# print(page)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table', class_='g-table')
table = table[1]

headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)

#Check for correct table headers
#print(headers)

pffown_df = pd.DataFrame(columns = headers)

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(pffown_df)
    pffown_df.loc[length] = row
    
pffown_df.to_csv('pffown.csv', index=False)
