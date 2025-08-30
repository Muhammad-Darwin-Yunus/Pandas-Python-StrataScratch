>.<

Title: Find the average height of a quarterback
Link: https://platform.stratascratch.com/coding/9656-find-the-average-height-of-a-quarterback?code_type=2
Level: Easy

What is the average height of quarterbacks?

Data nfl_combine:
year: bigint
name: text
firstname: text
lastname: text
position: text
heightfeet: bigint
heightinches: double
heightinchestotal: double
weight: bigint
arms: double
hands: double
fortyyd: double
twentyyd: double
tenyd: double
twentyss: double
threecone: double
vertical: double
broad: bigint
bench: bigint
round: bigint
college: text
pick: text
pickround: bigint
picktotal: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

nfl_combine = pd.DataFrame(nfl_combine)

nfl_combine_filter = nfl_combine[nfl_combine['position']=='QB']['weight'].mean()

nfl_combine_fix = pd.DataFrame({'average_height_of_quarterbacks':[nfl_combine_filter]})
    
Output:

average_height_of_quarterbacks
221
