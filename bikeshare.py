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
    Asks user to specify a city and a choice for month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('='*60)
    print("\nHello! Let\'s explore some US bikeshare data!")
    print("Available cities are:- \n \
        chicago\n \
        new york city\n \
        washington")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in ['chicago', 'new york city', 'washington']:
        if city != '':
            print('Wrong input, please enter a city name again from above.')
        city = input('Enter city name to analyze: ').lower()

    more_filter = input(
        'Would you like to explore the bikshare data for particular month and day? \
    Enter yes or no.\n').lower()

    if more_filter == 'yes':
        # get user input for month (all, january, february, ... , june)
        print('\nThe months range from January to June.')
        month = input(
            "Enter name of the month to filter by, or 'all' to apply no month filter:\n")

        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input(
            "Enter name of the day of week to filter by, or 'all' to apply no day filter:\n")
    else:
        month = 'all'
        day = 'all'

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

    print('\nPreparing the data...\n')
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour  # hour column
    df['routes'] = df['Start Station'] + ' to ' + \
        df['End Station']  # station combination

    try:
        # filtering by month if applicable
        if month != 'all':
            # use the index of the MONTHS list to get the corresponding int
            month = MONTHS.index(month.title()) + 1
            df = df[df['month'] == month]

        # filtering by day of week if applicable
        if day != 'all':
            df = df[df['day_of_week'] == day.title()]

        return df
    except:
        raise Exception


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    common_month = MONTHS[common_month-1].title()
    print("\nThe most popular month is: ", common_month)

    # Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nThe most popular day of the week is: ", common_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("\nThe most popular starting hour is: ", common_hour)

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]
    print("\nThe most popular start station is: ", popular_start_st)

    # Display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]
    print("\nThe most popular end station is: ", popular_end_st)

    # Display most frequent combination of start station and end station trip
    pop = df['routes'].value_counts()
    # fetched the id of the max value occured from "routes" column
    popular_route = pop.idxmax()
    print('\nMost popular route from Start Station to End Station is from\n', popular_route)

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_time = df['Trip Duration'].sum()
    print("\nTotal travel time of all the trips is %d hours and %d minutes" %
          (total_time/3600, (total_time/60) % 60))

    # Display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("\nMean travel time of all the trips is %d minutes and %d seconds" %
          (mean_time/60, mean_time % 60))

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if('User Type' in df):
        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print("The types of users and their counts:-\n")
        for i in range(len(user_types)):
            print("%s: %s" %
                  (user_types.index[i], user_types[user_types.index[i]]))

    if('Gender' in df):
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("\nGender counts of user:-\n")
        for i in range(len(gender_counts)):
            print("%s: %s" %
                  (gender_counts.index[i], gender_counts[gender_counts.index[i]]))

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

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:

        city, month, day = get_filters()

        try:
            df = load_data(city, month, day)
                        
            stat_choice = input(
                'For what do you want the insights for?\n \
                1. Regarding the users\n \
                2. Regarding popular stations\n \
                3. Regarding the most frequent times of travel\n \
                4. Regarding trip durations\n \
                5. For all of the above\n \
                Enter a number of your choice. \n'
            )
            if int(stat_choice) == 1:
                user_stats(df)
            elif int(stat_choice) == 2:
                station_stats(df)
            elif int(stat_choice) == 3:
                time_stats(df)
            elif int(stat_choice) == 4:
                trip_duration_stats(df)
            elif int(stat_choice) == 5:
                user_stats(df)
                station_stats(df)
                time_stats(df)
                trip_duration_stats(df)

            restart = input(
                '\nWould you like to explore some more? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except:
            print(
                '\nSomething went wrong! You might have entered something incorrectly.\n' +
                'Things you might have entered incorrect:\n' +
                '>> Enter a "Number" as your choice.\n' +
                '>> Enter a full name of the "Month" or "Day".\n' +
                'Please try again...'
            )


if __name__ == "__main__":
    main()
