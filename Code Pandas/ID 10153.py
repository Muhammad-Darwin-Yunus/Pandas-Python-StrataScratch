>.<

Title: Find the number of Yelp businesses that sell pizza
Link: https://platform.stratascratch.com/coding/10153-find-the-number-of-yelp-businesses-that-sell-pizza?code_type=2
Level: Easy

Find the number of Yelp businesses that sell pizza.

Data yelp_business:
business_id: varchar
name: varchar
neighborhood: varchar
address: varchar
city: varchar
state: varchar
postal_code: varchar
latitude: float
longitude: float
stars: float
review_count: int
is_open: int
categories: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

sell_pizza = pd.DataFrame(yelp_business)

sell_pizza = sell_pizza[sell_pizza['categories'].str.contains('pizza',case=False,na=False)]

sell_pizza[['business_id','name','categories']]

Output:

business_id           |        name                        |  categories
dRb2Xq8jorJV6tDCgmaQUg	  Papa John's Pizza                    Restaurants;Pizza
MYB1ZMspBk1Xc_awp_PtSw	  Naked City Pizza Express            Sandwiches;Chicken Wings;Restaurants;Pizza
XVDR44P_74FmA0ANanm4CQ	  House of Pizza                      Greek;Restaurants;Pizza;Italian
CV05rBOr5DdDGvxUZkRFmg	  Angeline's                          Restaurants;Nightlife;Pizza;Cocktail Bars;Bars;Italian
EsE8KTPqAJ2MjJdmuAifRw	  Dante's Inferno Flats                Italian;Restaurants;Pizza
YiaOpyu4qx0x1nJC_G33TQ	  Grimaldi's Pizzeria                  Pizza;Restaurants
xTW5PkLEdMBs2f2W8RGy0g	  Miele's Italian and Banquet Hall      Desserts;Italian;Pizza;Event Planning & Services;Buffets;Sandwiches;Food;Venues & Event Spaces;Restaurants
2CQc-0KPuF2S8axUdGH24w	  Punto fisso                          Financial Services;Wine Bars;Restaurants;Italian;Pizza;Financial Advising;Caterers;Nightlife;Food;Wedding Planning;Event Planning & Services;Bars
wk3wGDfJb1V-ciZpyhoNAA	  Bic's Pub and Grill                  Pubs;American (Traditional);Nightlife;Bars;Pizza;Restaurants
NBYN4Nks_EsPHyAlJ_mdNw	  Bistro Merlot                        Salad;Pizza;Restaurants;Event Planning & Services;Vietnamese;Caterers
