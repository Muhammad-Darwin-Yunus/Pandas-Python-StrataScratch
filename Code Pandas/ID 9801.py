>.<

Title: Find the number of USA companies that are on the list
Link: https://platform.stratascratch.com/coding/9801-find-the-number-of-american-companies-that-are-on-the-list?code_type=2
Level: Easy

Find the number of USA companies that are on the list.

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

forbes_filter = forbes[forbes['country']=='United States']['country'].count()

forbes_fix = pd.DataFrame({'total_companies_USA':[forbes_filter]})
    
Output:

total_companies_USA
38
