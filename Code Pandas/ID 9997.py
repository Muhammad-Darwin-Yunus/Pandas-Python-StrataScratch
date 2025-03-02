>.<

Title: Top 100 Ranked Songs
Link: https://platform.stratascratch.com/coding/9997-top-100-ranked-songs?code_type=2
Level: Easy

Find the total number of streams for the top 100 ranked songs.

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

song = pd.DataFrame(spotify_worldwide_daily_song_ranking)

ranked_song = song.groupby('trackname').agg(position=('position','first'),total_streams=('streams','sum')).reset_index()

ranked_song_filter = ranked_song[(ranked_song['position']>=1) & (ranked_song['position']<=100)]

ranked_song_sort = ranked_song_filter.sort_values(by='position',ascending=True)
    
Output:

trackname                                                        |  position  |  total_streams
Bad and Boujee (feat. Lil Uzi Vert)                                    1            1840019
Look What You Made Me Do                                                1            3828478
HUMBLE.                                                                1              23898196
DNA.                                                                    2              6656727
Perfect Duet (Ed Sheeran & Beyonce)]                                    2              94302
Versace On The Floor                                                    4              144230
Una Lady Como Tu                                                        8              29430
Attention                                                                8            113556
Alone                                                                    8            92447
Make Me (Cry)                                                            8              81932
Mobali                                                                    9            81790
Castle on the Hill                                                        9            15127
Scared to Be Lonely                                                      9            71259
Chocolat (feat. Awa)                                                      9            93144
You Don't Know Me - Radio Edit                                            10            255434
El Party                                                                  10            100715
Vacaciones                                                                10            86922
Ahora Dice                                                                10              4543
Bling Bling                                                                10            97760
Party On The West Coast (feat. Snoop Dogg)                                14              73059
Perfect Strangers                                                          16            109998
Touch                                                                      17              96248
Too Good At Goodbyes - Edit                                                19              37747
‰Ω†,Â•Ω‰∏çÂ•Ω? - Ending Theme Song of TVBS Series "Life List"              19              10600
Unforgettable                                                              25              46603
Location                                                                    34              1119
Santa Baby                                                                  37              1450
Olsun                                                                      37                15010
Scars To Your Beautiful                                                    39                7661
All We Know                                                                42                65113
366.G√ºn                                                                    42                14090
First Time                                                                  44                1224
Bad Liar                                                                    44                1857
Young Dumb & Broke                                                          45                524715
I'm the One                                                                46                  5278
Django                                                                      46                77111
Imitadora                                                                  48                  52478
Galway Girl                                                                 49                44892
Jocelyn Flores                                                              49                1137
Solo Dance                                                                  51                14617
Heart Won't Forget                                                          52                28047
Him & I (with Halsey)                                                      54                  52233
Let Me Love You                                                            56                  1526
Sorry Not Sorry                                                            63                  3552
Lush Life                                                                  70                  8068
Tutto il mondo √® periferia                                                73                  18919
I Like Me Better                                                            77                  5246
Sunset Lover                                                                90                  27642
All Night                                                                  100                  3808
