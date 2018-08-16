import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

DAYS = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour  # hour column
    df['routes'] = df['Start Station'] + ' to ' + \
        df['End Station']  # station combination

    # filtering by month if applicable
    if month != 'all':
        # filtering over range of months if applicable
        if type(month) == list:
            df = df[
                (df['month'] >= month[0]) &
                (df['month'] <= month[1])
            ]
        else:
            # use the index of the MONTHS list to get the corresponding int
            month = MONTHS.index(month.title()) + 1
            df = df[df['month'] == month]

    # filtering by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    time_stat = {}

    # display the most common month
    common_month = df['month'].mode()[0]
    common_month = MONTHS[common_month-1].title()
    time_stat['popular_month'] = common_month

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    time_stat['popular_day'] = common_day

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    time_stat['popular_hour'] = common_hour

    return time_stat


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    station_stat = {}

    # display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]
    station_stat['popular_start_st'] = popular_start_st

    # display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]
    station_stat['popular_end_st'] = popular_end_st

    # display most frequent combination of start station and end station trip
    pop = df['routes'].value_counts()[0:5]
    # fetched the id of the max value occured from "routes" column
    popular_st = pop.idxmax()
    station_stat['popular_st'] = popular_st

    return station_stat


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    trip_stat = {}

    # display total travel time
    total_time = df['Trip Duration'].sum()
    trip_stat['total_trip_time'] = "%d hours and %d minutes" %(total_time/3600, (total_time/60) % 60)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    trip_stat['mean_trip_time'] = "%d minutes and %d seconds"%(mean_time/60, mean_time % 60)

    return trip_stat


def user_stats(df):
    """Displays statistics on bikeshare users."""

    user_stat = {}

    if('User Type' in df):
        # Display counts of user types
        user_types = df['User Type'].value_counts()
        user_stat['user_counts'] = user_types

    if('Gender' in df):
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        user_stat['gender_counts'] = gender_counts

    if('Birth Year' in df):
        # Display earliest, most recent, and most common year of birth
        most_recent_yob = int(df['Birth Year'].max())
        earliest_yob = int(df['Birth Year'].min())
        most_common_yob = int(df['Birth Year'].mode()[0])

        user_stat['most_recent_yob'] = most_recent_yob
        user_stat['earliest_yob'] = earliest_yob
        user_stat['most_common_yob'] = most_common_yob

    return user_stat
