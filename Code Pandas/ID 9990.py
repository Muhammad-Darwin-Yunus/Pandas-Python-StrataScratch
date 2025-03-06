>.<

Title: Find songs that have more than 3 million streams
Link: https://platform.stratascratch.com/coding/9990-find-songs-that-have-more-than-3-million-streams?code_type=2
Level: Easy

Find songs that have more than 3 million streams.
Output the track name, artist, and the corresponding streams.
Sort records based on streams in descending order.

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

spotify_ranked = spotify.groupby(['trackname','artist'])['streams'].sum().reset_index()

spotify_rename = spotify_ranked.rename(columns={'streams':'total_streams'})

spotify_sort = spotify_rename.sort_values(by='total_streams',ascending=False)

spotify_filter = spotify_sort[spotify_sort['total_streams']>3000000]
    
Output:

trackname                  |  artist      |  total_streams
HUMBLE.                      Kendrick Lamar      23898196
DNA.                        Kendrick Lamar      6656727
Look What You Made Me Do    Taylor Swift        3828478
