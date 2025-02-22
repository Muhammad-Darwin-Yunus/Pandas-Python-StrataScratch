>.<

Title: Find all top-rated wineries based on points
Link: https://platform.stratascratch.com/coding/10021-find-all-top-rated-wineries-based-on-points?code_type=2
Level: Easy

Find all top-rated wineries based on points.
Consider a top-rated winery has been awarded points more or equal than 95.

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

wineries = pd.DataFrame(winemag_p1)

wineries = wineries[wineries['points']>95]

wineries['winery']

Output:

winery
Niebaum-Coppola
Joseph Phelps
Yao Ming
