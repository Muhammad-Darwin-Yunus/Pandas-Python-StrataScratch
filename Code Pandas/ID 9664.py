>.<

Title: Highest Market Value For Each Sector
Link: https://platform.stratascratch.com/coding/9664-highest-market-value-for-each-sector?code_type=2
Level: Easy

Finding the highest market value for each sector.
Which sector is it best to invest in? Output the result along with the sector name.
Order the result based on the highest market value in descending order.

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

forbes_global_sector = forbes_global.groupby('sector')['marketvalue'].max().reset_index(name='highest_marketvalue')

forbes_global_sort = forbes_global_sector.sort_values('highest_marketvalue',ascending=False)

forbes_global_sort[['highest_marketvalue','sector']]
    
Output:

highest_marketvalue  |  sector
483.1                    Information Technology
422.3                    Energy
309.1                    Financials
277                      Health Care
259.6                    Industrials
247.9                    Consumer Discretionary
239.6                    Consumer Staples
197.7                    Telecommunication Services
182.3                    Materials
86                        Utilities
