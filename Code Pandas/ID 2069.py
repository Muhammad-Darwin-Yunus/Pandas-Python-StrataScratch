>.<

Title: Sales with Valid Promotion
Link: https://platform.stratascratch.com/coding/2069-sales-with-valid-promotion?code_type=2
Level: Easy

The marketing manager wants you to evaluate how well the previously ran advertising campaigns are working.
Particularly, they are interested in the promotion IDs from the online_promotions table.
Find the percentage of orders with promotion IDs from the online_promotions table applied.

Data online_promotions:
promotion_id: bigint

Data online_orders:
cost_in_dollars: bigint
customer_id: bigint
date_sold: date
product_id: bigint
promotion_id: bigint
units_sold: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
online_promotions = pd.DataFrame(online_promotions)
online_orders = pd.DataFrame(online_orders)

online_orders_id = set(online_promotions['promotion_id'])

online_orders['is_promo'] = online_orders['promotion_id'].isin(online_orders_id).astype(int)

online_orders_persentage = round(100.0 * online_orders['is_promo'].sum()/len(online_orders),2)

online_orders_fix = pd.DataFrame({'percentage_of_orders':[online_orders_persentage]})
    
Output:

percentage_of_orders
75.76
