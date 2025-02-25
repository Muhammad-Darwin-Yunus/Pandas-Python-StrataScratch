>.<

Title: Hour Of Highest Gas Expense
Link: https://platform.stratascratch.com/coding/10005-hour-of-highest-gas-expense?code_type=2
Level: Easy

Find the hour with the highest gasoline cost. Assume there's only 1 hour with the highest gas cost.

Data lyft_rides:
gasoline_cost: double
hour: bigint
index: bigint
travel_distance: double
weather: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

gas = pd.DataFrame(lyft_rides)

gas_expense = gas.groupby('hour')['gasoline_cost'].max().reset_index()

gas_expense_sort = gas_expense.sort_values('gasoline_cost',ascending=False).head(1)

gas_expense_sort_fix = pd.DataFrame({'hour_gasoline_cost':gas_expense_sort['hour']})

Output:

hour_gasoline_cost
10
