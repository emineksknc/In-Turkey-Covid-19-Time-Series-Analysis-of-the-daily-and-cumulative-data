# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:34:30 2020

@author: Emine
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





df = pd.read_csv('covid_19_data_tr.csv')



#new attribute daily_confirmed
Daily_Confirmed = []
Daily_Confirmed.append(df['Confirmed'][0])
print(Daily_Confirmed)
j = 0
for i in df['Confirmed']:
    if len(Daily_Confirmed) != len(df['Confirmed']):
        Daily_Confirmed.append(df['Confirmed'][j+1]-df['Confirmed'][j])
        j = j+1
    else:
        break
df['Daily_Confirmed'] = Daily_Confirmed

#new attribute daily_deaths
Daily_Deaths = []
Daily_Deaths.append(df['Deaths'][0])
j = 0
for i in df['Deaths']:
    if len(Daily_Deaths) != len(df['Deaths']):
        Daily_Deaths.append(df['Deaths'][j+1]-df['Deaths'][j])
        j = j+1
    else:
        break
    
df['Daily_Deaths'] = Daily_Deaths

#new attribute daily_recovered
Daily_Recovered = []
Daily_Recovered.append(df['Recovered'][0])
j = 0
for i in df['Recovered']:
    if len(Daily_Recovered) != len(df['Recovered']):
        Daily_Recovered.append(df['Recovered'][j+1]-df['Recovered'][j])
        j = j+1
    else:
        break
    
df['Daily_Recovered'] = Daily_Recovered

#for time series analysis time attribute convert from object to datetime
df['Last_Update'] = pd.to_datetime(df['Last_Update'] , format = '%m/%d/%Y')
data = df.drop(['Last_Update'], axis=1)
data.index = df.Last_Update
print(data)



del_cols = ['Province/State','Country/Region']
data.drop(del_cols, axis=1, inplace=True) 


data =[ df['Confirmed'],df['Deaths'],df['Recovered']]
langs = df['Last_Update']
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
X = np.arange(len(df['Last_Update']))
plt.plot(df['Last_Update'], data[0], color = 'b', linewidth = 2.0, label = 'Tanı')
plt.xticks(rotation='vertical')
plt.plot(df['Last_Update'], data[1], color = 'g', linewidth = 2.0,label = 'Ölüm')
plt.plot(df['Last_Update'], data[2], color = 'r', linewidth = 2.0,label = 'İyileşme')
plt.legend()




