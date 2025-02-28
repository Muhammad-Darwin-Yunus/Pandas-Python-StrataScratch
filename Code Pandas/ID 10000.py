>.<

Title: Find the year that Uber acquired more than 2000 customers through celebrities
Link: https://platform.stratascratch.com/coding/10000-find-the-year-that-uber-acquired-more-than-2000-customers-through-celebrities?code_type=2
Level: Easy

Find the year that Uber acquired more than 2000 customers through advertising using celebrities.

Data uber_advertising:
advertising_channel: text
customers_acquired: bigint
money_spent: bigint
year: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

uber = pd.DataFrame(uber_advertising)

uber_celebrities = uber[(uber['customers_acquired']>2000) & (uber['advertising_channel']=='celebrities')]

uber_celebrities['year']
    
Output:

year
2018
