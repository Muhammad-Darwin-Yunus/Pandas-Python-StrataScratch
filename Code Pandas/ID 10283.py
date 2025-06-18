>.<

Title: Find the top-ranked songs for the past 20 years
Link: https://platform.stratascratch.com/coding/10283-find-the-top-ranked-songs-for-the-past-30-years?code_type=2
Level: Easy

Find all the songs that were top-ranked (at first position) at least once since the year 2005.

Data billboard_top_100_year_end:
artist: text
group_name: text
id: bigint
song_name: text
year: bigint
year_rank: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

billboard = pd.DataFrame(billboard_top_100_year_end)

billboard_filter = billboard[(billboard['year']>=2005) & (billboard['year_rank']==1)]

billboard_duplicate = billboard_filter.drop_duplicates('song_name')

billboard_duplicate['song_name']
    
Output:

song_name
We Belong Together
Bad Day
Irreplaceable
Low
Boom Boom Pow
TiK ToK
Rolling In The Deep
Somebody That I Used To Know
Thrift Shop
