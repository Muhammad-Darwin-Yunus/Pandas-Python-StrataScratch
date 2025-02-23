>.<

Title: Find prices for Spanish, Italian, and French wines
Link: https://platform.stratascratch.com/coding/10020-find-prices-for-spanish-italian-and-french-wines?code_type=2
Level: Easy

Find prices for Spanish, Italian, and French wines. Output the price.

Data winemag_p1:
country: text
description: text
designation: text
id: bigint
points: bigint
price: double
province: text
region_1: text
region_2: text
variety: text
winery: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

spanish_italian_french_wines = pd.DataFrame(winemag_p1)

spanish_italian_french_wines_filter = spanish_italian_french_wines[spanish_italian_french_wines['country'].isin(['Spain','Italy','France'])]

spanish_italian_french_wines_not_null = spanish_italian_french_wines_filter[spanish_italian_french_wines_filter['price'].notna()]

spanish_italian_french_wines_sort = spanish_italian_french_wines_not_null.sort_values(by='country',ascending=True)

spanish_italian_french_wines_sort[['country','price']]

Output:

country  |  price
France        27
France        25
France        294
France        17
France        62
France        42
France        8
France        50
Italy          22
Italy          19
Italy          15
Italy          28
Italy          55
Italy          29
Italy          190
Italy          39
Italy          18
Italy          18
Italy          63
Italy          24
Italy          50
Italy          12
Spain          22
Spain          18
Spain          60
Spain          22
