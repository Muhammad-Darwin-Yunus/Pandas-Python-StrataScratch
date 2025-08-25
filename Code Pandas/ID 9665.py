>.<

Title: Count the number of companies in the IT sector in each country
Link: https://platform.stratascratch.com/coding/9665-count-the-number-of-companies-in-the-it-sector-in-each-country?code_type=2
Level: Easy

Count the number of companies in the Information Technology sector in each country.
Output the result along with the corresponding country name.
Order the result based on the number of companies in the descending order.

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

forbes_global_country = forbes_global.groupby('country')['sector'].count().reset_index(name='number_of_companies_IT')

forbes_global_sort = forbes_global_country.sort_values('number_of_companies_IT',ascending=False)

forbes_global_sort[['number_of_companies_IT','country']]
    
Output:

number_of_companies_IT  |  country
38                          United States
10                          China
7                            France
7                            Germany
6                            Japan
5                            Switzerland
5                            Australia
4                            United Kingdom
4                            Russia
3                            Brazil
3                            Canada
2                            South Korea
2                            Netherlands
2                            Italy
2                            Spain
1                            Saudi Arabia
1                            Belgium
1                            Norway
1                            Hong Kong
