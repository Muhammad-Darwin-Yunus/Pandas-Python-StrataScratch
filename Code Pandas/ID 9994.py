>.<

Title: Find songs with less than 2000 streams
Link: https://platform.stratascratch.com/coding/9994-find-songs-with-less-than-2000-streams?code_type=2
Level: Easy

Find songs with less than 2000 streams.
Output the track name along with the corresponding streams.
Sort records by streams in descending order.
There is no need to group rows with same track name.

Data spotify_worldwide_daily_song_ranking:
artist: text
date: datetime
id: bigint
position: bigint
region: text
streams: bigint
trackname: text
url: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

spotify = pd.DataFrame(spotify_worldwide_daily_song_ranking)

spotify_filter = spotify[spotify['streams']<2000]

spotify_sort = spotify_filter.sort_values(by='streams',ascending=False)

spotify_sort[['trackname','streams']]
    
Output:

trackname                  |  streams
Hasta el Amanecer              1907
Bad Liar                        1857
Sugar                           1830
Don't Let Me Down              1818
This Is What You Came For      1670
Hello                          1537
Let Me Love You                1526
Santa Baby                      1450
First Time                      1224
Jocelyn Flores                  1137
Location                        1119
