>.<

Title: Movie Duration Match
Link: https://platform.stratascratch.com/coding/10367-aggregate-listening-data?code_type=2
Level: Easy

As a data scientist at Amazon Prime Video, you are tasked with enhancing the in-flight entertainment experience for Amazon’s airline partners. Your challenge is to develop a feature that suggests individual movies from Amazon's content database that fit within a given flight's duration.
For flight 101, find movies whose runtime is less than or equal to the flight's duration.
The output should list suggested movies for the flight, including 'flight_id', 'movie_id', and 'movie_duration'."

Data entertainment_catalog:
movie_id: int64
title: object
duration: int64

Data flight_schedule:
flight_id: int64
flight_duration: int64
flight_date: datetime64[ns]

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

flight_101_duration = flight_schedule.loc[flight_schedule['flight_id']==101,'flight_duration'].iloc[0]

filter_movies = entertainment_catalog[entertainment_catalog['duration']<= flight_101_duration]

filter_movies['flight_id']=101

filter_movies[['flight_id','movie_id','duration']]

Output:

flight_id | movie_id | movie_duration
101            1            120
101            2            90
101            3            60
101            4            150
101            5            110
101            6            95
101            7            100
101            8            85
101            9            75
101            10            105
