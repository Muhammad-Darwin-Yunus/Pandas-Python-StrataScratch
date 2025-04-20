>.<

Title: Order Details
Link: https://platform.stratascratch.com/coding/9913-order-details?code_type=2
Level: Easy

Find order details made by Jill and Eva.
Consider the Jill and Eva as first names of customers.
Output the order date, details and cost along with the first name.
Order records based on the customer id in ascending order.

Data customers:
address: text
city: text
first_name: text
id: bigint
last_name: text
phone_number: text

Data orders:
cust_id: bigint
id: bigint
order_date: datetime
order_details: text
total_order_cost: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

customers = pd.merge(customers,orders,left_on = 'id',right_on = 'cust_id',how='inner')

customers_filter = customers[customers['first_name'].str.contains('Jill',case=False,na=False) | customers['first_name'].str.contains('Eva',case=False,na=False)]

customers_sort = customers_filter.sort_values(by='cust_id',ascending=True)

customers_sort[['first_name','order_date','order_details','total_order_cost']]
    
Output:

first_name  |  order_date          |  order_details  |  total_order_cost
Jill          2019-02-01 00:00:00        Coat                25
Jill          2019-03-10 00:00:00        Shoes                80
Jill          2019-04-19 00:00:00        Suit                150
Jill          2019-04-01 00:00:00        Suit                50
Jill          2019-04-02 00:00:00        Skirt                30
Jill          2019-04-03 00:00:00        Dresses              50
Jill          2019-04-04 00:00:00        Coat                25
Jill          2019-04-19 00:00:00        Coat                125
Eva          2019-01-11 00:00:00          Shirts              60
Eva          2019-03-11 00:00:00          Slipper            20
Eva          2019-01-11 00:00:00          Coat                125
