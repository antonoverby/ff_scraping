#Spits out a dataframe with current PPR fantasy point projections from FantasyPros

import pandas as pd

import datetime

t = datetime.datetime.now()
now = t.strftime("%Y%m%d%H%M")
  
positions = ['qb', 'flex', 'dst']
projections = []
for position in positions:
    df = pd.read_html(f'https://www.fantasypros.com/nfl/projections/{position}.php?scoring=PPR')[0]
    projections.append(df)
    
for df in projections[:2]:
    df = df.droplevel(0, axis=1)
    projections.append(df)
        
for _ in range(2):
    projections.pop(0)
    
for df in projections [1:]:
    df['Team'] = df.Player.apply(lambda x: x[-3:].strip())
    df['Player'] = df.Player.apply(lambda x: x[:-3].strip())
        
    dst = projections[0]
    dst['Player'] = dst['Player'].str.extract(r'\b(\w+)$', expand=False)

team = {
        'Cardinals': 'ARI',
        'Falcons': 'ATL',
        'Ravens': 'BAL',
        'Bills': 'BUF',
        'Panthers': 'CAR',
        'Bears': 'CHI',
        'Bengals': 'CIN',
        'Browns': 'CLE',
        'Cowboys': 'DAL',
        'Broncos': 'DEN',
        'Lions': 'DET',
        'Packers': 'GB',
        'Texans': 'HOU',
        'Colts': 'IND',
        'Jaguars': 'JAX',
        'Chiefs': 'KC',
        'Dolphins': 'MIA',
        'Vikings': 'MIN',
        'Patriots': 'NE',
        'Saints': 'NO',
        'Giants': 'NYG',
        'Jets': 'NYJ',
        'Raiders': 'LV',
        'Eagles': 'PHI',
        'Steelers': 'PIT',
        'Chargers': 'LAC',
        '49ers': 'SF',
        'Seahawks': 'SEA',
        'Rams': 'LAR',
        'Buccaneers': 'TB',
        'Titans': 'TEN',
        'Commanders': 'WAS'
        }

dst['Team'] = dst['Player'].map(team)
dst = dst[['Player', 'Team', 'FPTS']]

qb = projections[1]
qb = qb[['Player', 'Team','FPTS']]

flx = projections[2]
flx['Opps'] = flx['ATT'] + flx['REC']
flx = flx[['Player', 'Team', 'Opps', 'FPTS']]

proj_df = pd.DataFrame(columns=['Player', 'Team', 'Opps', 'FPTS'])
proj_df = pd.concat([qb, flx, dst], axis=0).reset_index(drop=True)

player_name_changes = {
    'Patrick Mahomes II': 'Patrick Mahomes', 
    'D.J. Chark Jr.': 'DJ Chark Jr.', 
    'Demetric Felton Jr.': 'Demetric Felton',
    'Chigoziem Okonkwo': 'Chig Okonkwo',
    'PJ Walker': 'P.J. Walker',
    'Keelan Cole Sr.': 'Keelan Cole'
    }

proj_df.replace({"Player": player_name_changes}, inplace=True)


# proj_df.to_csv('projections.csv')

