>.<

Title: Find how many times each artist appeared on the Spotify ranking list
Link: https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=2
Level: Easy

Find how many times each artist appeared on the Spotify ranking list
Output the artist name along with the corresponding number of occurrences.
Order records by the number of occurrences in descending order.

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

spotify_count = spotify.groupby('artist')['position'].count().reset_index(name='number_of_occurrences')

spotify_sort = spotify_count.sort_values(by='number_of_occurrences',ascending=False)
    
Output:

artist              |  number_of_occurrences
Kendrick Lamar                9
Ed Sheeran                    5
Matoma                        2
Petit Biscuit                  2
Manuel Turizo                  2
Khalid                        2
Zara Larsson                  2
Wisin                          2
The Chainsmokers              2
Migos                          2
Sia                            2
Diva Faune                     1
Sagopa Kajmer                  1
Kygo                            1
Skrillex                        1
Girls' Generation               1
Enzo Ortiz                      1
Lil Peep                        1
Calvin Harris                    1
Post Malone                      1
Ofenbach                         1
Extreme                          1
Eric Chou                        1
Jesse McCartney                  1
Lauv                            1
Little Mix                      1
Dadju                            1
DNCE                            1
Ermal Meta                      1
J-AX                            1
Kaaris                          1
Chris Jeday                      1
Alan Walker                      1
Martin Garrix                    1
Noah Cyrus                        1
Siboy                            1
Jax Jones                        1
Lartiste                          1
Charlie Puth                      1
Jake La Furia                      1
Taylor Swift                      1
Ariana Grande                      1
Emma Stone                        1
French Montana                    1
Jonas Blue                        1
DJ Khaled                          1
Martin Jensen                      1
Christina Perri                    1
Nicky Jam                          1
Sam Smith                          1
Murat Boz                          1
Selena Gomez                       1
DJ Snake                            1
Sertab Erener                      1
G-Eazy                              1
MYMP                                1
Demi Lovato                          1
Eartha Kitt                          1
Passenger                            1
Maroon 5                            1
Katharine McPhee                    1
Ellinoora                            1
XXXTENTACION                        1
Romeo Santos                        1
Alessia Cara                        1
Piolo Pascual                      1
C. Tangana                          1
Desiigner                          1
Bruno Mars                         1
Still Fresh                        1
Adele                              1
Haloo Helsinki!                    1
Fifth Harmony                      1
