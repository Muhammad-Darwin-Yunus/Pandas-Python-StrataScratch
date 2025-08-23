>.<

Title: Find the industry which has the lowest average sales compared to all industries
Link: https://platform.stratascratch.com/coding/9666-find-the-industry-which-has-the-lowest-sales-compared-to-all-industries?code_type=2
Level: Easy

Find the industry with lowest average sales. Output that industry.

Data forbes_global_2010_2014:
assets: double
company: text
continent: text
country: text
industry: text
marketvalue: double
profits: double
rank: bigint
sales: double
sector: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

forbes_global = pd.DataFrame(forbes_global_2010_2014)

forbes_global_industry = forbes_global.groupby('industry')['sales'].mean().reset_index(name='sales')

forbes_global_sales = forbes_global_industry.sort_values('sales',ascending=True).head(1)

forbes_global_sales['industry']
    
Output:

industry
Communications Equipment
