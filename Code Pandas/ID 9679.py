>.<

Title: Find the profit to sales ratio of Royal Dutch Shell
Link: https://platform.stratascratch.com/coding/9679-find-the-profit-to-sales-ratio-of-royal-dutch-shell?code_type=2
Level: Easy

What is the profit to sales ratio (profit/sales) of Royal Dutch Shell?
Output the result along with the company name.

Data forbes_global_2010_2014:
company: text
sector: text
industry: text
continent: text
country: text
marketvalue: double
sales: double
profits: double
assets: double
rank: bigint
forbeswebpage: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

forbes_global = pd.DataFrame(forbes_global_2010_2014)

forbes_global_company = forbes_global[forbes_global['company']=='Royal Dutch Shell'].reset_index()

forbes_global_company['profit_to_sales_ratio'] = forbes_global_company['profits']/forbes_global_company['sales']

forbes_global_company[['company','profit_to_sales_ratio']]
    
Output:

company            |  profit_to_sales_ratio
Royal Dutch Shell            0.04
