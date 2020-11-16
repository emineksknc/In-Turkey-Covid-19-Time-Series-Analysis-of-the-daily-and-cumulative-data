# -*- coding: utf-8 -*-
"""
Created on Tue May 19 01:28:10 2020

@author: Emine
"""

from fbprophet import Prophet
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('covid_19_data_tr.csv')
#new attribute daily_confirmed
Daily_Confirmed = []
Daily_Confirmed.append(data['Confirmed'][0])
print(Daily_Confirmed)
j = 0
for i in data['Confirmed']:
    if len(Daily_Confirmed) != len(data['Confirmed']):
        Daily_Confirmed.append(data['Confirmed'][j+1]-data['Confirmed'][j])
        j = j+1
    else:
        break
data['Daily_Confirmed'] = Daily_Confirmed

#new attribute daily_deaths
Daily_Deaths = []
Daily_Deaths.append(data['Deaths'][0])
j = 0
for i in data['Deaths']:
    if len(Daily_Deaths) != len(data['Deaths']):
        Daily_Deaths.append(data['Deaths'][j+1]-data['Deaths'][j])
        j = j+1
    else:
        break
    
data['Daily_Deaths'] = Daily_Deaths

#new attribute daily_recovered
Daily_Recovered = []
Daily_Recovered.append(data['Recovered'][0])
j = 0
for i in data['Recovered']:
    if len(Daily_Recovered) != len(data['Recovered']):
        Daily_Recovered.append(data['Recovered'][j+1]-data['Recovered'][j])
        j = j+1
    else:
        break
    
data['Daily_Recovered'] = Daily_Recovered

df = data.loc[:, ["Last_Update","Daily_Recovered"]]
df['Last_Update'] = pd.DatetimeIndex(df['Last_Update'])
print(df.dtypes)
#df['Last_Update'] = pd.to_numeric(df['Last_Update'], errors='coerce')
df = df.rename(columns={'Last_Update': 'ds',
                        'Daily_Recovered': 'y'})

my_model = Prophet(yearly_seasonality=True)
my_model.fit(df)


future_dates = my_model.make_future_dataframe(periods=30)

forecast =my_model.predict(future_dates)

fig2 = my_model.plot_components(forecast)




