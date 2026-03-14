>.<

Title: Customer Average Orders
Link: https://platform.stratascratch.com/coding/2013-customer-average-orders?code_type=2
Level: Easy

How many customers placed an order and what is the average order amount?

Data postmates_orders:
amount: double
city_id: bigint
courier_id: bigint
customer_id: bigint
id: bigint
order_timestamp_utc: timestamp
seller_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
postmates_orders = pd.DataFrame(postmates_orders)

postmates_orders_filter = postmates_orders.groupby('customer_id').agg(total_order=('amount','sum'),avg_order=('amount','mean')).reset_index()
    
Output:

customer_id	total_order	avg_order
102	657.65	131.53
104	725.87	181.47
100	600.08	150.02
101	477.58	119.39
103	323.31	107.77
