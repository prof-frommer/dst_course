# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 15:01:02 2026

@author: IFrommer
"""
state = 'Connecticut'
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data/state-trim.csv", parse_dates=["Date"])
plt.plot(df['Date'],df['Deaths'])
plt.title(f'Covid Statistics in {state}')
plt.ylabel('Deaths')
plt.xlabel('Date')
plt.savefig('plot.png')
