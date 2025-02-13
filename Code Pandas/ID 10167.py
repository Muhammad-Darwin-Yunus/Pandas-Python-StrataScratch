>.<

Title: Total Number Of Housing Units
Link: https://platform.stratascratch.com/coding/10167-total-number-of-housing-units?code_type=2
Level: Easy

Find the total number of housing units completed for each year.
Output the year along with the total number of housings. Order the result by year in ascending order.

Data housing_units_completed_us:
year: int
month: int
south: float
west: float
midwest: float
northeast: float

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

housing_units = pd.DataFrame(housing_units_completed_us)

housing_units = housing_units.groupby('year')[['south','west','midwest','northeast']].sum()

housing_units['total_housings'] = housing_units.sum(axis=1)

housing_units = housing_units[['total_housings']].reset_index()

Output:

year | total_house
2006	1979.5
2007	1503
2008	1119.5
2009	794.5
2010	651.7
2011	585
2012	649
2013	764.4
2014	462.8
