>.<

Title: Find the advertising channel where Uber spent more than 100k USD in 2019
Link: https://platform.stratascratch.com/coding/10002-find-the-advertising-channel-where-uber-spent-more-than-100k-usd-in-2019?code_type=2
Level: Easy

Find the advertising channel(s) where Uber spent more than 100k USD in 2019.

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

advertising_channel = pd.DataFrame(uber_advertising)

advertising_channel_spent = advertising_channel[(advertising_channel['money_spent']>100000) & (advertising_channel['year']==2019)]

advertising_channel_spent['advertising_channel']
    
Output:

advertising_channel
celebrities
billboards
tv
