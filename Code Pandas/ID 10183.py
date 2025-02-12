>.<

Title: Total Cost Of Orders
Link: https://platform.stratascratch.com/coding/10183-total-cost-of-orders?code_type=2
Level: Easy

Find the total cost of each customer's orders.
Output customer's id, first name, and the total order cost. Order records by customer's first name alphabetically.

Data customers:
id: int
first_name: varchar
last_name: varchar
city: varchar
address: varchar
phone_number: varchar

Data orders:
id: int
cust_id: int
order_date: datetime
order_details: varchar
total_order_cost: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)

total_orders = orders_df.groupby('cust_id')['total_order_cost'].sum().reset_index()

orders_merge = pd.merge(customers_df,total_orders,left_on='id',right_on='cust_id',how='left')

orders_merge['total_order_cost'] = orders_merge['total_order_cost'].fillna(0)

hasil_orders = orders_merge[['id','first_name','total_order_cost']].sort_values(by='first_name')

hasil_orders


Output:

id | first_name | total_order_cost
13    Emma              0
12    Eva              205
3      Farida          260
11    Frank              0
5      Henry            80
6      Jack              0
7      Jill              535
8      John              0
9      Justin            0
14      Liam              0
10      Lili              0
1      Mark                0
15    Mia                540
2      Mona              0
4      William          140
