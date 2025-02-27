>.<

Title: Find the cost per customer for advertising via public transport
Link: https://platform.stratascratch.com/coding/10001-find-the-cost-per-customer-for-advertising-via-public-transport?code_type=2
Level: Easy

Find the cost per customer for each advertising channel and year combination.
Include only channels that are advertised via public transport (advertising channel includes "bus" substring).
The cost per customer is equal to the total spent money divided by the total number of acquired customers through that advertising channel.
Output advertising channel, year and its cost per customer.

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

advertising = pd.DataFrame(uber_advertising)

advertising_public_transport = advertising[advertising['advertising_channel'].str.contains('bus',case=False)]

advertising_public_transport['cost_per_customer'] = advertising_public_transport['money_spent']/advertising_public_transport['customers_acquired']

advertising_public_transport[['advertising_channel','year','cost_per_customer']]
    
Output:

advertising_channel  |  year  |  cost_per_customer
busstops                2019          3.75
buses                    2019          28
busstops                2018          58.33
buses                    2018        239.13
busstops                2017          100
buses                    2017        1329.26
