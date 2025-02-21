>.<

Title: Find the number of US-based wineries that have expensive wines (price >= 200)
Link: https://platform.stratascratch.com/coding/10027-find-the-number-of-us-based-wineries-that-have-expensive-wines-price-200?code_type=2
Level: Easy

Find the number of US-based wineries that have expensive wines.
A wine is considered to be expensive if its price is $200 or more.

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

us_wine = pd.DataFrame(winemag_p1)

us_wine_expensive = us_wine.groupby('id').agg(country=('country','first'),price=('price','first')).reset_index()

us_wine_expensive_filter = us_wine_expensive[(us_wine_expensive['price']>=200)&(us_wine_expensive['country']=='US')]
Output:

id    |  country  |  price
74057      US        625
83298      US        350
135895    US          225
116551    US          200
116564    US          200
