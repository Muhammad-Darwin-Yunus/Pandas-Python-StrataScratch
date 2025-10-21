>.<

Title: Products with No Sales
Link: https://platform.stratascratch.com/coding/2109-products-with-no-sales?code_type=2
Level: Easy

Write a query to get a list of products that have not had any sales.
Output the ID and market name of these products.

Data fct_customer_sales:
cust_id: text
prod_sku_id: text
order_date: date
order_value: bigint
order_id: text

Data dim_product:
prod_sku_id: text
prod_sku_name: text
prod_brand: text
market_name: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
fct_customer_sales = pd.merge(fct_customer_sales,dim_product,on='prod_sku_id',how='inner')

fct_customer_sales_group = fct_customer_sales[['prod_sku_id','market_name']].drop_duplicates()
    
Output:

prod_sku_id  |  market_name
P474          Apple Macbook Pro 13''
P472          Apple IPhone 13
P487          GoPro Max
P476          Apple IPad
P478          Samsung Galaxy S21
P489          JBL Tuner XL
P482          Samsung Galaxy Tab 8
P480          Samsung Galaxy Watch4
P477          Apple IPad Pro
P475          Apple Makbook Air 13''
P486          GoPro Hero 10
P479          Samsung Galaxy S22+
P484          Dell Inspiron 13
P485          Canon PowerShot G7 X Mark III
