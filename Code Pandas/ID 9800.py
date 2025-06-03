>.<

Title: Find the total market value for the financial sector
Link: https://platform.stratascratch.com/coding/9800-find-the-total-market-value-for-the-financial-sector?code_type=2
Level: Easy

Find the total market value for the financial sector.

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

forbes = pd.DataFrame(forbes_global_2010_2014)

forbes_filter = forbes[forbes['sector']=='Financials']['marketvalue'].sum()

forbes_fix = pd.DataFrame({'marketvalue_financials':[forbes_filter]})
    
Output:

marketvalue_financials
4239.2
