import time
import pandas as pd
import numpy as np

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

user_types = df['User Type'].value_counts()
print("The types of users and their counts:-\n", user_types['Subscriber'])

