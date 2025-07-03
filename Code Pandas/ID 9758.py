>.<

Title: Find the best publishers based on total sales
Link: https://platform.stratascratch.com/coding/9758-find-the-best-publishers-based-on-total-sales?code_type=2ID 9758
Level: Easy

Find the best publishers based on total sales made by each publisher.
Output publishers alongside their total sales.
Order records based on the sales in descending order.

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

global_weekly = pd.DataFrame(global_weekly_charts_2013_2014)

global_group = global_weekly.groupby('publisher')['total'].sum().reset_index(name='total_sales')

global_order = global_group.sort_values('total_sales',ascending=False).head(1)
    
Output:

publisher        |  total_sales
Electronic Arts      13775846
