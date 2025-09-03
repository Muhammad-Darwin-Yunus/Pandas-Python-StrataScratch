>.<

Title: Drafted Into NFL
Link: https://platform.stratascratch.com/coding/9648-drafted-into-nfl?code_type=2
Level: Easy

How many athletes were drafted into NFL from 2013 NFL Combine?
The pickround column specifies if the athlete was drafted into the NFL.
A value of 0 means that the athlete was not drafted into the NFL.

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

nfl_combine_filter = nfl_combine[(nfl_combine['year']==2013) & (nfl_combine['pickround'] !=0)]

nfl_combine_name = nfl_combine_filter['name'].count()

nfl_combine_fix = pd.DataFrame({'drafted_NFL_2013':[nfl_combine_name]})
    
Output:

drafted_NFL_2013
26
