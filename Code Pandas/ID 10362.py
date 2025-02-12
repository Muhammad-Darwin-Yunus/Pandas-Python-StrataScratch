>.<

Title: Top Monthly Sellers
Link: https://platform.stratascratch.com/coding/10362-top-monthly-sellers?code_type=2
Level: Easy

You are provided with an already aggregated dataset from Amazon that contains detailed information about sales across different products and marketplaces.
Your task is to list the top 3 sellers in each product category for January.
In case of ties, rank them the same and include all sellers tied for that position.
The output should contain seller_id ,total_sales ,product_category , market_place, and sales_date.

Data sales_data:
seller_id: object
total_sales: float64
product_category: object
market_place: object
sales_date: datetime64[ns]

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

sales_data['sales_date'] = pd.to_datetime(sales_data['sales_date'])

sales_data_january = sales_data[sales_data['sales_date'].dt.month == 1]

sellers_data = sales_data_january.groupby('product_category', as_index=False).agg({
    'seller_id':'first',
    'total_sales':sum,
    'market_place':'first',
    'sales_date':'min'
})

sellers_data['rank'] = sellers_data['total_sales'].rank(method='first',ascending=False)

rank_sellers = sellers_data[sellers_data['rank']<=3].sort_values(by='total_sales',ascending=False)

rank_sellers

Output:

product_category  |  seller_id  |  total_sales  |  market_place  |  sales_date            |  rank
electronics            s236          437716.95          in          2024-01-01 00:00:00        1
toys                    s272          273914.28          us          2024-01-01 00:00:00        2
books                  s918          139336.81          uk          2024-01-01 00:00:00        3
