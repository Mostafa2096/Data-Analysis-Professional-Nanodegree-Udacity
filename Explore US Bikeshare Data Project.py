import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('name of the city to analyze').lower()
    while city not in CITY_DATA.keys():
        print('Not a valid City')
        city = input('Enter one of these cities names : chicago,new york city, washington').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)

    month = input('name of the month to filter by, or "all" to apply no month filter').lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:   
        print("that\'s not a valid month name!")    
        month = input('Enter a valid month name').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('name of the day of week to filter by, or "all" to apply no day filter').lower()
    while day not in ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        print("that\'s not a valid day name!")
        day = input('Enter a valid day name').lower()
            

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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    #if month != 'all':
     #   months = ['January', 'February', 'March', 'April', 'May', 'June']
      #  month = months.index(month)+1
    df=df[df['month'] == month]

    if day != 'all' :
        df=df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('the most common month :' , popular_month)
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day :' , popular_day_of_week)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('the most common hour :' , popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print('the most commonly used start station :', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print('the most commonly used end station :', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    all_stations = df['Start Station'] + df['End Station']
    print('the most frequent combination of start station and end station trip :',all_stations.mode())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('the total travel time :',total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time :',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if city != 'washington' :
        user_type_count = df['User Type'].value_counts()
        print('the counts of user types : ',user_type_count)

    # TO DO: Display counts of gender
    if city != 'washington' :
        gender_counts = df['Gender'].value_counts()
        print('the counts of gender : ',gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    print('the earliest year of birth : ', df['Birth Year'].min())
    print('the most recent year of birth : ', df['Birth Year'].max())
    print('the most common year of birth : ', df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    view_data = input('\nWould you like to view the first 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data=='yes' :
        print(df.iloc[start_loc : start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to view next 5 rows?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
