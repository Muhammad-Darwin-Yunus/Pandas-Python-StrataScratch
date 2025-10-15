>.<

Title: Sales Revenue
Link: https://platform.stratascratch.com/coding/2127-sales-revenue?code_type=2
Level: Easy

Calculate the sales revenue for the year 2021.

Data amazon_sales:
order_id: text
order_date: date
order_total: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
amazon_sales = pd.DataFrame(amazon_sales)

amazon_sales['order_date'] = pd.to_datetime(amazon_sales['order_date']) 

amazon_sales_fiter = amazon_sales[amazon_sales['order_date'].dt.year == 2021]['order_total'].sum()

amazon_sales_fix = pd.DataFrame({'sales_revenue' : [amazon_sales_fiter]})
    
Output:

sales_revenue
2545
