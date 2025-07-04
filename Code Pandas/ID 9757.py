>.<

Title: Find the genres that yielded the highest sales
Link: https://platform.stratascratch.com/coding/9757-find-the-genres-that-yielded-the-highest-sales?code_type=2
Level: Easy

Find the genres that yielded the highest sales.
Output the genre alongside its total sales.
Order results based on the total sales in descending order.

Data global_weekly_charts_2013_2014:
pos: bigint
game: text
platform: text
publisher: text
genre: text
week: bigint
weekly: bigint
total: bigint
week_ending: datetime
id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

global_weekly_charts = pd.DataFrame(global_weekly_charts_2013_2014)

global_sales = global_weekly_charts.groupby('genre')['total'].sum().reset_index(name='total_sales')

global_order = global_sales.sort_values('total_sales',ascending=False).head(1)
    
Output:

genre    |  total_sales
Shooter      12258049
