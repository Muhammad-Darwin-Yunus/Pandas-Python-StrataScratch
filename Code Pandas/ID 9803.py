>.<

Title: Find the total assets of the energy sector
Link: https://platform.stratascratch.com/coding/9803-find-the-total-assets-of-the-energy-sector?code_type=2
Level: Easy

Find the total assets of the energy sector.

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

forbes_filter = forbes[forbes['sector']=='Energy']['assets'].sum()

forbes.fix = pd.DataFrame({'total_assets_energy':[forbes_filter]})
    
Output:

total_assets_energy
3624.1
