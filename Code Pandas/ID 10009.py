>.<

Title: Find the total costs and total customers acquired in each year
Link: https://platform.stratascratch.com/coding/10009-find-the-total-costs-and-total-customers-acquired-in-each-year?code_type=2
Level: Easy

Find the total costs and total customers acquired in each year.
Output the year along with corresponding total money spent and total acquired customers.

Data uber_advertising:
advertising_channel: text
customers_acquired: bigint
money_spent: bigint
year: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

total_customers = pd.DataFrame(uber_advertising)

cost_customers_year = total_customers.groupby('year').agg(total_money_spent=('money_spent','sum'),total_acquired_customers=('customers_acquired','sum')).reset_index()

Output:

year  |  total_money_spent  |  total_acquired_customers
2019      11373000                      11751
2018      1711055                        12350
2017      4329200                        13400
