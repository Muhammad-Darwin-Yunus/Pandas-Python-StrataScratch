>.<

Title: Top 10 Ranked Songs
Link: https://platform.stratascratch.com/coding/9995-top-10-ranked-songs?code_type=2
Level: Easy

Find the top 10 ranked songs by position.
Output the track name along with the corresponding position and sort records by the position in descending order and track name alphabetically, as there are many tracks that are tied for the same position.


Data spotify_worldwide_daily_song_ranking:
artist: text
date: datetime
id bigint
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

ranked_spotify = spotify[(spotify['position']>=1) & (spotify['position']<=10)]

ranked_spotify_sort = ranked_spotify.sort_values(by='position',ascending=False)

ranked_spotify_sort[['trackname','position']]
    
Output:

kname                          |  position
Ahora Dice                          10
Bling Bling                          10
El Party                            10
Vacaciones                          10
You Don't Know Me - Radio Edit      10
Castle on the Hill                    9
Chocolat (feat. Awa)                  9
Mobali                                9
Scared to Be Lonely                   9
Una Lady Como Tu                      9
Alone                                  8
Attention                              8
Make Me (Cry)                          8
Perfect Duet (Ed Sheeran & Beyonce)    8
Una Lady Como Tu                       8
Versace On The Floor                    4
DNA.                                    2
DNA.                                    2
Perfect Duet (Ed Sheeran & Beyonce)     2
Bad and Boujee (feat. Lil Uzi Vert)      1
HUMBLE.                                  1
HUMBLE.                                  1
HUMBLE.                                  1
HUMBLE.                                  1
HUMBLE.                                  1
HUMBLE.                                  1
HUMBLE.                                  1
Look What You Made Me Do                  1
