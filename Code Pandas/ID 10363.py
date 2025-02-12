>.<

Title: Weekly Orders Report
Link: https://platform.stratascratch.com/coding/10540-calculate-average-score?code_type=2
Level: Easy

For each week, starting on Sunday, calculate the total quantity across all orders for that week.
Include only the orders that are from the first quarter of 2023.
The output should contain 'week' and 'quantity'.

Data orders_analysis:
stage_of_order: object
week: datetime64[ns]
quantity: int64

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

orders_data = orders_analysis.groupby(['stage_of_order','week']).agg(quantity = ('quantity','sum')).reset_index()

orders_filter = orders_data[(orders_data['stage_of_order'] == 'ordered') & (orders_data['week'] >= '2023-01-01') & (orders_data['week'] <= '2023-03-31')]

orders_filter [['week','quantity']]

Output:

week                |  quantity
2023-01-02 00:00:00      102
2023-01-09 00:00:00      105
2023-01-16 00:00:00      108
2023-01-23 00:00:00      111
2023-01-30 00:00:00      114
2023-02-06 00:00:00      117
2023-02-13 00:00:00      240
2023-02-20 00:00:00      123
2023-02-27 00:00:00      126
2023-03-06 00:00:00      129
2023-03-13 00:00:00      132
2023-03-20 00:00:00      135
2023-03-27 00:00:00      138
