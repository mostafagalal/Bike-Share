import time
import pandas as pd
import numpy as np


CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}

Months_Data = ["All", "January", "February", "March", "April", "May", "June"]

Days_Data = ["All", "Friday", "Saturday", "Sunday",
             "Monday", "Tuesday", "Wednesday", "Thursday"]


def filter():
    '''-This function filters the inputs from the user if it City, month or Day 
       - Matchs the user inputs with the related data above
    '''
    # A loop asks the user and give him 3 options for the city
    cityByUser = ''
    while cityByUser.title() not in CITY_DATA:
        cityByUser = input(
            "Hello! Let\'s explore some US bikeshare data! \n Which city you want to see data from \"chicago, new york city, washington\" \n")
        if cityByUser.title() in CITY_DATA:
            city = CITY_DATA[cityByUser.title()]
        else:
            print("Sorry you\'ve entered a wrong city,Please try again\n")
    # a loop asks the user for a month
    monthByUser = ''
    while monthByUser.title() not in Months_Data:
        monthByUser = input(
            "Please provide the Month that you want to analyze\n")

        if monthByUser.title() in Months_Data:
            month = monthByUser.title()
        else:
            print("Sorry you\'ve entered a wrong month,Please try again\n")
    # a loop asks the user for a day
    dayByUser = ''
    while dayByUser.title() not in Days_Data:
        dayByUser = input("Please provide the Day that you want to analyze\n")
        if dayByUser.title() in Days_Data:
            day = dayByUser.title()
        else:
            print("**Sorry you\'ve entered a wrong day,Please try again\n")
    # return the city, month , day that we have got from the user
    return city, month, day


def get_data(city, month, day):
    ''' gets the data as a DataFrame from the csv files and transfer the Start time to "datetime" 
    it also adds column after extracting them from start time  such as montsh, days, hours'''
    # this code access the data and saved it as a DataFrame
    df = pd.read_csv(f"{city}")
    # Converting time to month,day and hour
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Months"] = df["Start Time"].dt.month
    df['Days'] = df["Start Time"].dt.day_name()
    df["Hours"] = df["Start Time"].dt.hour
    #  2 If statments to filter the month and day
    if month != "All":
        month = Months_Data.index(month)
        df = df[df["Months"] == month]

    if day != "All":
        df = df[df["Days"] == day]

    # Return the all df if the user didn't specify a day or a month
    return df
    print("^" * 50)


def time_stats(df):
    '''This Function : gets the most frequent month, day and hour   '''

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # gets the most frequent month, day and hour and using the [0]
    # so we get the first one cause if we have more than mod
    month = df["Months"].mode()[0]
    day = df["Days"].mode()[0]
    hour = df["Hours"].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("^" * 50)


def station_stats(df):
    ''' This function gets the most frequent start_station, end_station, and both  using the mode()[0] 
    and puting the zero to get the first frequented number because maybe the column has more than 2 frequented numbers '''

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # Getting the most frequent Start station
    start_station = df["Start Station"].mode()[0]
    print(f"This is the most common Start Station: {start_station}")
    # Getting the most frequent End station
    end_station = df["End Station"].mode()[0]
    print(f"This is the most common End Station: {end_station}")
    # Getting the most frequent start station and end station both of them
    both = [start_station, end_station]
    print(f"This is the most common End & Start Station: {both}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("^" * 50)


def trip_duration_stats(df):
    '''This function calculates the total trip time sum and the mean of the total trip time '''

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # It calculate's all the trip's duration in the data
    trip_time = df["Trip Duration"].sum()
    print(f"This is the Total Trip Time: {trip_time}")
    # calculate the mean for the total time trip
    trip_mean = df["Trip Duration"].mean()
    print(f"This is the Mean for the Trip Time: {trip_mean}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("^" * 50)


def user_stats(df):
    ''' this function calculating the user type even if he a customer or a subscriber 
    and counts the gender in "chicago , new_york_city" cause the last city doesn't have the Gender column 
    also it get the attribute such as (max,min and mode ) of the year '''

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # counts the values in the user type's column
    User_Types = df['User Type'].value_counts()
    print(f"This is the counts of user type: {User_Types}")
    # Cause washington doesn't have the gender column,
    # so this if statement handls it and counts the values in gender column
    if 'Chicago' == "chicago.csv" or "New York City" == "new_york_city.csv":
        gender = df['Gender'].value_counts()
        print(f"This is the counts of user type: {gender}")

    if 'Chicago' == "chicago.csv" or "New York City" == "new_york_city.csv":
        # the smalles no. of the Birth Year
        min_year = df['Birth Year'].min()
        # the Biggest no. of the Birth Year
        max_year = df['Birth Year'].max()
        # the most frequent no. of the Birth Year
        mode_year = df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("^" * 50)


def raw_data(df):
    ''' this function asks the user if he want's to see more 5 rows in the data
    1-First it represent the first 5 rows in the data
    2-asks the user if he wanted to check more 5 rows or not 
    3- if yes, we represent them, if no, we break he loop and end the function '''

    print(df.head())
    # counter and it starts with 5 as the function above represent the first 5 as default
    count = 5
    # a loop to keep asking the user for displaying more 5 rows until he type's no
    # if he typed a wrnog answer it will ask him to repeat the question
    while True:
        user = input("do you want to get more 5 rows \"Yes or No\" ")
        if user.title() == "Yes":
            count += 5
            print(df.head(count))
        elif user.title() == "No":
            break
        # break statement to break the loop if the user typed no
        else:
            print("Sorry you have typed a wrong answer")


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
