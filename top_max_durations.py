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
df['Birth Year'].fillna(0, inplace=True)

print('-'*80)
df.sort_values('Trip Duration', axis=0, ascending=True, inplace=True)
print(df.head(2))

hf = df.tail(10)
# hf = df.iloc[np.r_[0:10, -10:0]]

x = hf['routes']
y = hf['Trip Duration']/3600

plt.plot(y ,x)

plt.legend()
plt.show()
