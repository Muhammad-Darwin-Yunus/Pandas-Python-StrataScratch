>.<

Title: Change of Currency Exchange Rates
Link: https://platform.stratascratch.com/coding/2063-change-of-currency-exchange-rates?code_type=2
Level: Easy

Find the year that Uber acquired more than 2000 customers through advertising using celebrities.

Data sf_exchange_rate:
date: date
exchange_rate: double
source_currency: text
target_currency: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
sf_exchange_rate = pd.DataFrame(sf_exchange_rate)

sf_exchange_rate['date'] = pd.to_datetime(sf_exchange_rate['date']).dt.date

e1 = sf_exchange_rate[(sf_exchange_rate['target_currency'] == 'USD') &(sf_exchange_rate['date'] == pd.to_datetime('2020-01-01').date())]

e2 = sf_exchange_rate[sf_exchange_rate['date'] == pd.to_datetime('2020-07-01').date()]

merged = pd.merge(e1, e2,on=['source_currency','target_currency'],suffixes=('_e1', '_e2'))

merged['difference'] = (pd.to_datetime(merged['date_e2']) - pd.to_datetime(merged['date_e1'])).dt.days

merged_fix = merged[['source_currency', 'difference']]
    
Output:

source_currency	difference
USD	182
EUR	182
GBP	182
INR	182
AUD	182
CAD	182
CHF	182
AED	182
SEK	182
EGP	182
KWD	182
PLN	182
UAH	182
