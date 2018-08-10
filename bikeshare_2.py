import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

DAYS = ['Sunday', 'Monday', 'Tuesday',
        'Wednesday', 'Thursday', 'Friday', 'Saturday']

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let\'s explore some US bikeshare data!")
    print("Please select from these 3 cities:- \n \
        chicago\n \
        new york city\n \
        washington")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Enter city name to analyze: ').lower()

    # get user input for month (all, january, february, ... , june)
    print('\nThe months range from January to June.')
    month = input(
        "Enter name of the month to filter by, or 'all' to apply no month filter:\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        "Enter name of the day of week to filter by, or 'all' to apply no day filter:\n")

    print('-'*40)
    return city, month, day


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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    common_month = MONTHS[common_month-1].title()
    print("\nThe most popular month is: ", common_month)
    time_stat['common_month'] = common_month

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nThe most popular day of the week is: ", common_day)
    time_stat['common_day'] = common_day

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("\nThe most popular starting hour is: ", common_hour)
    time_stat['common_hour'] = common_hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return time_stat


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    station_stat = {}

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]
    print("\nThe most popular start station is: ", popular_start_st)
    station_stat['popular_start_st'] = popular_start_st

    # display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]
    print("\nThe most popular end station is: ", popular_end_st)
    station_stat['popular_end_st'] = popular_end_st

    # display most frequent combination of start station and end station trip
    pop = df['routes'].value_counts()
    popular_st = pop.idxmax()
    print("\nMost popular route from Start Station to End Station: \n", popular_st)
    station_stat['popular_st'] = popular_st

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return station_stat


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    trip_stat = {}

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("\nTotal travel time of all the trips: ", total_time)
    trip_stat['total_time'] = total_time

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("\nMean travel time of all the trips: ", mean_time)
    trip_stat['mean_time'] = mean_time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return trip_stat


def user_stats(df):
    """Displays statistics on bikeshare users."""

    user_stat = {}

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if('User Type' in df):
        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print("The types of users and their counts:-\n", user_types)
        user_stat['user_types'] = user_types

    if('Gender' in df):
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("\nGender counts of user:-\n", gender_counts)
        user_stat['gender_counts'] = gender_counts

    if('Birth Year' in df):
        # Display earliest, most recent, and most common year of birth
        most_recent_yob = int(df['Birth Year'].max())
        earliest_yob = int(df['Birth Year'].min())
        most_common_yob = int(df['Birth Year'].mode()[0])
        print(
            "\n Earliest year of birth: {} \
                \n Most recent year of birth: {} \
                \n Most common year of birth: {} "
            .format(earliest_yob, most_recent_yob, most_common_yob)
        )
        user_stat['earliest_yob'] = earliest_yob
        user_stat['most_recent_yob'] = most_recent_yob
        user_stat['most_common_yob'] = most_common_yob

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return user_stat


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
