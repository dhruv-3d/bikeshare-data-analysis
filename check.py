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

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
user_ct, cust_ct, subs_ct = {}, {}, {}
x, y = [], []

for day in days:
    user_ct[day] = df[df['day_of_week'] == day].count()

    # cust_ct[day] = dayframe[dayframe['User Type'] == 'Customer'].count()
    # subs_ct[day] = dayframe[dayframe['User Type'] == 'Subscriber'].count()
    
for day, count in user_ct.items():
    x.append(day)
    y.append(count)


plt.plot(x ,y)

plt.legend()
plt.show()
