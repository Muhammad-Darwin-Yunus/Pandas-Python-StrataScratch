>.<

Title: Find the average number of streams across all songs
Link: https://platform.stratascratch.com/coding/9996-find-the-average-number-of-streams-across-all-songs?code_type=2
Level: Easy

Find the average number of streams across all songs.

Data spotify_worldwide_daily_song_ranking:
artist: text
date: datetime
id: bigint
position: bigint
region: text
streams bigint
trackname: text
url: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

spotify = pd.DataFrame(spotify_worldwide_daily_song_ranking)

average_spotify = spotify['streams'].mean()

average_spotify_fix = pd.DataFrame({'average_streams_songs':[average_spotify]})
    
Output:

average_streams_songs
421291.47
