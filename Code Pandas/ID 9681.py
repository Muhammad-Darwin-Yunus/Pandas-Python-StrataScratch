>.<

Title: Highest Market Value Per Sector
Link: https://platform.stratascratch.com/coding/9681-highest-market-value-per-sector?code_type=2
Level: Easy

Find the highest market value for each sector.
Output the sector name along with the result.

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

forbes_global_sector = forbes_global.groupby('sector')['marketvalue'].max().reset_index(name='highest_market_value')
    
Output:

sector                    |  highest_market_value
Financials                          309.1
Energy                              422.3
Industrials                          259.6
Consumer Discretionary              247.9
Information Technology              483.1
Telecommunication Services          197.7
Consumer Staples                    239.6
Health Care                          277
Materials                            182.3
Utilities                            86
