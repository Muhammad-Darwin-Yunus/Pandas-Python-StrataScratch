>.<

Title: Aggregate Listening Data
Link: https://platform.stratascratch.com/coding/10367-aggregate-listening-data?code_type=2
Level: Easy

You're tasked with analyzing a Spotify-like dataset that captures user listening habits.
For each user, calculate the total listening time and the count of unique songs they've listened to.
In the database duration values are displayed in seconds.
Round the total listening duration to the nearest whole minute.
The output should contain three columns: 'user_id', 'total_listen_duration', and 'unique_song_count'.

Data listening_habits:
user_id: int64
song_id: int64
listen_duration: float64

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

aggregate_listening_data = pd.DataFrame(listening_habits)

listening_data = aggregate_listening_data.groupby('user_id').agg(total_listen_duration=('listen_duration',lambda x: round(x.sum()/60)),unique_song_count=('song_id','nunique')).reset_index()

listening_data

Output:

user_id	| total_listen_duration	| unique_song_count
  101	            8	                      2
  102	            5	                      2
  103	            6	                      1
  104	            6	                      2
  105	            4	                      1
  106	            3	                      1
  107	            4	                      1
  108	            8	                      2
  109	            0	                      1
