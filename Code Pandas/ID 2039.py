>.<

Title: Products Report Summary
Link: https://platform.stratascratch.com/coding/2039-products-report-summary?code_type=2
Level: Easy

Find the number of unique transactions and total sales for each of the product categories in 2017.
Output the product categories, number of transactions, and total sales in descending order.
The sales column represents the total cost the customer paid for the product so no additional calculations need to be done on the column.
Only include product categories that have products sold.

data wfm_transactions:
customer_id: bigint
product_id: bigint
sales: bigint
store_id: bigint
transaction_date: date
transaction_id: bigint

data wfm_products:
product_brand: text
product_category: text
product_description: text
product_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
wfm_merged = wfm_transactions.merge(wfm_products, how='left', left_on='product_id',right_on='product_id')

wfm_td = wfm_merged[wfm_merged['transaction_date'].dt.year==2017]

wfm_group = (wfm_td.groupby('product_category').agg(number_of_transactions=('transaction_id','nunique'), total_sales=('sales','sum')).reset_index())

wfm_sales = wfm_group[wfm_group['total_sales']>0]

wfm_order = wfm_sales.sort_values('total_sales', ascending=False)
    
Output:

product_category	number_of_transactions	total_sales
OTS	34	10960
Seafood	38	10897
Meat	22	9026
Chicken	26	8723
Tools	20	4004
Toys	6	2939
Vegie	14	1454
Cosmotics	11	1219
Deli	10	966
Dairy	10	893
