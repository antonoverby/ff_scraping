# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:19:33 2022

@author: Anton
"""

import pandas as pd
from scraping import dksb_nfl
import numpy as np

import datetime

t = datetime.datetime.now()
now = t.strftime("%Y%m%d%H%M")

def get_vegas_lines():

    games = dksb_nfl.NFLScraper().nfl_games_dk()
    spreads = []
    gm_ttls = []

    for i in games:
        teams = list(games.keys())
        i = games[i]
        for v in i:
            spread = i['spread'][0]
            gm_ttl = i['over'][0]
        spreads.append(spread)
        gm_ttls.append(gm_ttl)

    vegas = list(zip(teams,spreads,gm_ttls))

    vegas_df = pd.DataFrame(vegas, columns=['Team', 'Spread', 'OU'])

    vegas_df['TIT'] = np.where(vegas_df['Spread'] > 0, vegas_df['OU']/2 -                       vegas_df['Spread']*0.5, vegas_df['OU']/2 + abs(vegas_df['Spread']*0.5))
    
    return vegas_df 

vegas_lines = get_vegas_lines()



    
    
