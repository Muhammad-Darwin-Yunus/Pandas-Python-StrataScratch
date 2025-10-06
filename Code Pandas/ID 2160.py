>.<

Title: Oregon's Prior Month's Sales
Link: https://platform.stratascratch.com/coding/2160-oregons-prior-months-sales?code_type=2
Level: Easy

The sales division is investigating their sales for the past month in Oregon.
Calculate the total revenue generated from Oregon-based customers for April 2022.

Data online_orders:
product_id: bigint
promotion_id: bigint
cost_in_dollars: bigint
customer_id: bigint
date_sold: date
units_sold: bigint

Data online_customers:
id: bigint
first_name: text
last_name: text
age: bigint
email: text
state: text
address: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

online_orders = pd.DataFrame(online_orders)

online_orders_merge = online_orders.merge(online_customers,left_on='customer_id',right_on='id',how='inner')

online_orders_merge['date_sold'] = pd.to_datetime(online_orders_merge['date_sold'])

online_orders_filter = online_orders_merge[(online_orders_merge['state']=='Oregon') & (online_orders_merge['date_sold'].dt.year ==2022) & (online_orders_merge['date_sold'].dt.month ==4)]

online_orders_filter['total_revenue'] = online_orders_filter['cost_in_dollars'] * online_orders_filter['units_sold']

online_orders_fix = online_orders_filter.groupby('state')['total_revenue'].sum().reset_index()
    
Output:

state  |  total_revenue
Oregon        266
