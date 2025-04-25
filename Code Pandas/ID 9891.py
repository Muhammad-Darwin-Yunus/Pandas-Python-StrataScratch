>.<

Title: Customer Details
Link: https://platform.stratascratch.com/coding/9891-customer-details?code_type=2
Level: Easy

Find the details of each customer regardless of whether the customer made an order.
Output the customer's first name, last name, and the city along with the order details.
Sort records based on the customer's first name and the order details in ascending order.

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

customers = pd.merge(customers,orders,left_on='id',right_on='cust_id',how='inner')

customers_sort = customers.sort_values(by=['first_name','order_details'], ascending=[True,True])

customers_sort[['first_name','last_name','city','order_details']]
    
Output:

first_name  |  last_name  |  city            |  order_details
Eva              Lucas      Arizona                Coat
Eva              Lucas      Arizona                Shirts
Eva              Lucas      Arizona                Slipper
Farida          Joseph      San Francisco            Coat
Farida          Joseph      San Francisco           Shirts
Farida          Joseph	    San Francisco          Shoes
Farida          Joseph      San Francisco          Skirt
Henry          Jackson      Miami                  Shoes
Jill            Michael      Austin                Coat
Jill            Michael      Austin                Coat
Jill            Michael      Austin                Coat
Jill            Michael      Austin                Dresses
Jill            Michael      Austin                Shoes
Jill            Michael      Austin                Skirt
Jill            Michael      Austin                Suit
Jill            Michael      Austin                Suit
Mia            Owen          Miami                Boats
Mia            Owen          Miami                Dresses
Mia            Owen          Miami                Jeans
Mia            Owen          Miami                Shirts
Mia            Owen          Miami                Shirts
Mia            Owen          Miami                Skirt
Mia            Owen          Miami                Slipper
William        Daniel        Denver                Shirts
William        Daniel        Denver                Shoes
