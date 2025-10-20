>.<

Title: Shipped by Speedy Express
Link: https://platform.stratascratch.com/coding/2116-shipped-by-speedy-express?code_type=2
Level: Easy

How many orders were shipped by Speedy Express in total?

Data shopify_orders:
order_id: bigint
shop_id: bigint
user_id: bigint
order_amount: bigint
total_items: bigint
payment_method: text
created_at: timestamp
resp_employee_id: bigint
carrier_id: double

Data shopify_carriers:
id: bigint
name: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

shopify_merge = pd.merge(shopify_orders,shopify_carriers,left_on='carrier_id',right_on='id',how='inner')

shopify_filter = shopify_merge[shopify_merge['name']=='Speedy Express']

shopify_group = (shopify_filter.groupby('name',as_index=False)['order_amount'].sum().rename(columns={'order_amount':'total_orders'}))
    
Output:

name          |  total_orders
Speedy Express	1809
