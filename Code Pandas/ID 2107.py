>.<

Title: Primary Key Violation
Link: https://platform.stratascratch.com/coding/2107-primary-key-violation?code_type=2
Level: Easy

Write a query to return all Customers (cust_id) who are violating primary key constraints in the Customer Dimension (dim_customer) i.e. those Customers who are present more than once in the Customer Dimension.
For example if cust_id 'C123' is present thrice then the query should return two columns, value in first should be 'C123', while value in second should be 3

Data dim_customer:
cust_id: text
cust_name: text
cust_city: text
cust_dob: date
cust_pin_code: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
dim_customer = pd.DataFrame(dim_customer)

dim_customer_group = (dim_customer.groupby('cust_id')['cust_id'].size().reset_index(name='more_than_once'))

dim_customer_cust = dim_customer_group[dim_customer_group['more_than_once']>1]
    
Output:

cust_id  |  more_than_once
C274            3
C276            2
C281            2
