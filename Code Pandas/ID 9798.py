>.<

Title: Find the average profit for major banks
Link: https://platform.stratascratch.com/coding/9798-find-the-average-profit-for-major-banks?code_type=2
Level: Easy

Find the average profit for major banks.

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

forbes_filter = forbes[forbes['industry']=='Major Banks']['profits'].mean()

forbes_fix = pd.DataFrame({'profits_major_banks':[forbes_filter]})
    
Output:

profits_major_banks
11.9
