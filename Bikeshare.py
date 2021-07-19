import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}

Months_Data = ["all", "January", "February", "March", "April", "May", "June"]

Days_Data = ["all", "Friday", "Saturday", "Sunday",
             "Monday", "Tuesday", "Wednesday", "Thursday"]


def filter():
    '''This Function
     takes inputs from the user then it defines which 
     country, month or day it will manipulate or analyze   '''

    cityByUser = ''
    # These 3 while loops ask the user to input his data and repeat if he typed a wrong data
    while cityByUser.title() not in CITY_DATA:
        cityByUser = input(
            "Hello! Let\'s explore some US bikeshare data! \n Which city you want to see data from \"chicago, new york city, washington\" ?\n")
        if cityByUser.title() in CITY_DATA:
            city = CITY_DATA[cityByUser.title()]
        else:
            print("Sorry you\'ve entered a wrong city,Please try again\n")

    monthByUser = ''
    while monthByUser.title() not in Months_Data:
        monthByUser = input(
            "Please provide the Month that you want to analyze\n")
        if monthByUser.title() in Months_Data:
            month = monthByUser.title()
        else:
            print("Sorry you\'ve entered a wrong month,Please try again\n")

    dayByUser = ''
    while dayByUser.title() not in Days_Data:
        dayByUser = input("Please provide the Day that you want to analyze\n")
        if dayByUser.title() in Days_Data:
            day = dayByUser.title()
        else:
            print("**Sorry you\'ve entered a wrong day,Please try again\n")

    return city, month, day


def get_data(city, month, day):
    ''' gets the data as a DataFrame from the csv files and transfer the Start time to "datetime" 
    it also adds column after extracting them from start time  such as montsh, days, hours'''

    df = pd.read_csv(f"E:\\Data_Analysis_Pro\Bikeshare\{city}")

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Months"] = df["Start Time"].dt.month
    df['Days'] = df["Start Time"].dt.day_name()
    df["Hours"] = df["Start Time"].dt.hour

    #  2 If statments to filter the month and day
    if month != "all":
        month = Months_Data.index(month)
        df = df[df["Months"] == month]

    if day != "all":
        df = df[df["Days"] == day]

    return df


def time_stats(df):
    ''' This function gets the most frequent months, days, hours using the mode()[0] 
    and puting the zero to get the first frequented number because maybe the column has more than 2 frequented numbers '''

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    month = df["Months"].mode()[0]
    day = df["Days"].mode()[0]
    hour = df["Hours"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))


def station_stats(df):
    ''' This function gets the most frequent start_station, end_station, and both  using the mode()[0] 
    and puting the zero to get the first frequented number because maybe the column has more than 2 frequented numbers '''

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_station = df["Start Station"].mode()[0]
    print(f"This is the most common Start Station: {start_station}")

    end_station = df["End Station"].mode()[0]
    print(f"This is the most common End Station: {end_station}")

    both = [start_station, end_station]
    print(f"This is the most common Start & End Station: {both}")

    print("\nThis took %s seconds." % (time.time() - start_time))


def trip_duration_stats(df):
    '''This function calculates the total trip time sum and the mean of the total trip time '''

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    trip_time = df["Trip Duration"].sum()
    print(f"This is the Total Trip Time: {trip_time}")

    trip_mean = df["Trip Duration"].mean()
    print(f"This is the Mean for the Trip Time: {trip_mean}")

    print("\nThis took %s seconds." % (time.time() - start_time))


def user_stats(df):
    ''' this function calculating the user type even if he a customer or a subscriber 
    and counts the gender in "chicago , new_york_city" cause the last city doesn't have the Gender column 
    also it get the attribute such as (max,min and mode ) of the year '''

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    User_Types = df['User Type'].value_counts()
    print(f"This is the counts of user type: {User_Types}")

    if 'Chicago' == "chicago.csv" or "New York City" == "new_york_city.csv":
        gender = df['Gender'].value_counts()
        print(f"This is the counts of user type: {gender}")
    # it get the minimum value of year
    min_year = df['Birth Year'].min()
    # it get the maximum value of year
    max_year = df['Birth Year'].max()
    # it get the most frequented value of year
    mode_year = df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))


def raw_data(df):

    print(df.head())
    count = 5
    while True:
        user = input("do you want to get more 5 rows ")
        if user.title() == "Yes":
            count += 5
            print(df.head(count))

        else:
            break


def main():
    while True:
        city, month, day = filter()
        df = get_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
