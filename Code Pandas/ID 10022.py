>.<

Title: Find all wine varieties which can be considered cheap based on the price
Link: https://platform.stratascratch.com/coding/10022-find-all-wine-varieties-which-can-be-considered-cheap-based-on-the-price?code_type=2
Level: Easy

Find all wine varieties which can be considered cheap based on the price.
A variety is considered cheap if the price of a bottle lies between 5 to 20 USD.
Output unique variety names only.

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

wine_varieties = pd.DataFrame(winemag_p1)

wine_cheap = wine_varieties[(wine_varieties['price']>= 5) & (wine_varieties['price']<=20)]

wine_cheap_duplicat = wine_cheap['variety'].drop_duplicates()

wine_cheap_duplicat

Output:

variety
Prosecco
Riesling
Pinot Noir
Malbec-Syrah
Sauvignon Blanc
Merlot
Nero d'Avola
White Blend
Alvarinho
Garganega
Glera
Chardonnay
Gewarztraminer
Arinto
Red Blend
Assyrtiko
Viognier
Semillon
Syrah
Portuguese White
Sangiovese
Kuntra
Cabernet Sauvignon
Feteasca Neagra
Malbec
