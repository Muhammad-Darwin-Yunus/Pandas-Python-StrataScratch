>.<

Title: Top Ranked Songs
Link: https://platform.stratascratch.com/coding/9991-top-ranked-songs?code_type=2
Level: Easy

Find songs that have ranked in the top position.
Output the track name and the number of times it ranked at the top.
Sort your records by the number of times the song was in the top position in descending order.

Data spotify_worldwide_daily_song_ranking:
artist: text
id: bigint
position: bigint
region: text
stream_date: date
streams: bigint
trackname: text
url: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

spotify = pd.DataFrame(spotify_worldwide_daily_song_ranking)

spotify_1 = spotify[spotify['position']==1]

spotify_top_song = spotify_1.groupby('trackname')['position'].count().reset_index(name='times_top1')

spotify_sprt = spotify_top_song.sort_values(by='times_top1',ascending=False)
    
Output:

trackname                          |  times_top1
HUMBLE.                                  7
Bad and Boujee (feat. Lil Uzi Vert)      1
Look What You Made Me Do                  1
