>.<

Title: Total AdWords Earnings
Link: https://platform.stratascratch.com/coding/10164-total-adwords-earnings?code_type=2
Level: Easy

Find the total AdWords earnings for each business type.
Output the business types along with the total earnings.

Data google_adwords_earnings:
business_type: varchar
n_employees: int
year: int
adwords_earnings: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

adwords_earning = pd.DataFrame(google_adwords_earnings)

adwords_earning_total = adwords_earning.groupby('business_type')['adwords_earnings'].sum().reset_index()

Output:

business_type | adwords_earnings
media              247914579
transport          132323280
handyman            6042187
