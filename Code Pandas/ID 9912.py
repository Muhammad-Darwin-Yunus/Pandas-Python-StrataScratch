>.<

Title: Lowest Priced Orders
Link: https://platform.stratascratch.com/coding/9912-lowest-priced-orders?code_type=2
Level: Easy

Find the lowest order cost of each customer.
Output the customer id along with the first name and the lowest order price.

Data customers:
address: text
city:text
first_name: text
id: bigint
last_name: text
phone_number: text

Data orders:
cust_id: bigint
id: bigint
order_date: date
order_details: text
total_order_cost: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

customers = pd.merge(customers,orders,left_on = 'id',right_on = 'cust_id',how='inner')

customers_group = customers.groupby(['id_x','first_name'])['total_order_cost'].min().reset_index()

customers_group = customers_group.rename(columns={'total_order_cost':'lowest_order_price','id_x':'id'})
    
Output:

id  |  first_name  |  lowest_order_price
3        Farida            30
7        Jill              25
15        Mia              20
5        Henry              80
12        Eva                20
4        William            60
