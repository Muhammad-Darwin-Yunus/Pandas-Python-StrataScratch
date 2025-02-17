>.<

Title: Calculate Samantha's and Lisa's total sales revenue
Link: https://platform.stratascratch.com/coding/10127-calculate-samanthas-and-lisas-total-sales-revenue?code_type=2
Level: Easy

What is the total sales revenue of Samantha and Lisa?

Data sales_performance:
salesperson: varchar
widget_sales: int
sales_revenue: int
id: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

sales_revenue = pd. DataFrame(sales_performance)

sales_performance = sales_performance[sales_performance['salesperson'].isin(['Samantha','Lisa'])]

# Import your libraries
import pandas as pd

# Start writing code

sales_revenue = pd. DataFrame(sales_performance)

sales_performance = sales_performance[sales_performance['salesperson'].isin(['Samantha','Lisa'])]

sales_performance = sales_performance.groupby('salesperson')['sales_revenue'].sum().reset_index()

combined_sales = pd.DataFrame({
    'salesperson':['Samantha, Lisa'],
    'sales_revenue':[sales_performance['sales_revenue'].sum()]
})

Output:

salesperson    |  sales_revenue
Samantha_Lisa        112650
