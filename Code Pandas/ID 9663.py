>.<

Title: Most Profitable Financial Company
Link: https://platform.stratascratch.com/coding/9663-find-the-most-profitable-company-in-the-financial-sector-of-the-entire-world-along-with-its-continent?code_type=2
Level: Easy

Find the most profitable company from the financial sector. Output the result along with the continent.

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

forbes_global_filter = (forbes_global[forbes_global['sector']=='Financials'].loc[lambda df: df['profits']==df['profits'].max(),['company','continent']])
    
Output:

company  |  continent
ICBC          Asia
