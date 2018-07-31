import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

df = pd.read_csv('chicago.csv')

df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])
df['month'] = df['Start Time'].dt.month # month column
df['day_of_week'] = df['Start Time'].dt.weekday_name # day column
df['hour'] = df['Start Time'].dt.hour # hour column
df['routes'] = df['Start Station'] + ' to ' + df['End Station'] # station combination

hf = df.tail(10)
print(hf[['routes', 'Trip Duration']].values)
plt.plot(hf['Trip Duration']/60 , hf['routes'])

plt.show()