>.<

Title: Find the date with the highest opening stock price
Link: https://platform.stratascratch.com/coding/9613-find-the-date-with-the-highest-opening-stock-price?code_type=2
Level: Easy

Find the date when Apple's opening stock price reached its maximum

Data aapl_historical_stock_price:
date: date
year: bigint
month: bigint
open: double
high: double
low: double
close: double
volume: bigint
id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

aapl_historical_stock_price = pd.DataFrame(aapl_historical_stock_price)

aapl_historical_stock_price_open = aapl_historical_stock_price.loc[aapl_historical_stock_price['open'].idxmax()]['date']

aapl_historical_stock_price_fix = pd.DataFrame({'date':[aapl_historical_stock_price_open]})
    
Output:

date
2012-12-31
