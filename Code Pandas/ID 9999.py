>.<

Title: Find songs that are ranked between 8-10
Link: https://platform.stratascratch.com/coding/9999-find-songs-that-are-ranked-between-8-10?code_type=2
Level: Easy

Find songs that are ranked between 8-10.
Output the track name along with the corresponding position, ordered ascendingly.

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

rank_spotify = spotify[(spotify['position']>= 8) & (spotify['position']<=10)].reset_index()

rank_spotify_sort = rank_spotify.sort_values(by='position',ascending=True)

rank_spotify_sort[['trackname','position']]
    
Output:

trackname                          |  position
Una Lady Como Tu                          8
Alone                                    8
Perfect Duet (Ed Sheeran & Beyonce)      8
Make Me (Cry)                            8
Attention                                8
Castle on the Hill                        9
Una Lady Como Tu                          9
Scared to Be Lonely                        9
Mobali                                     9
Chocolat (feat. Awa)                      9
Bling Bling                                10
Ahora Dice                                10
Vacaciones                                10
You Don't Know Me - Radio Edit            10
El Party                                  10
