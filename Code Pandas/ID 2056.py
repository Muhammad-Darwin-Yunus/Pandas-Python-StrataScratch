>.<

Title: Number of Shipments Per Month
Link: https://platform.stratascratch.com/coding/2056-number-of-shipments-per-month?code_type=2
Level: Easy

Write a query that will calculate the number of shipments per month.
The unique key for one shipment is a combination of shipment_id and sub_id.
Output the year_month in format YYYY-MM and the number of shipments in that month.

Data amazon_shipment:
shipment_date: date
shipment_id: bigint
sub_id: bigint
weight: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment = pd.DataFrame(amazon_shipment)

amazon_shipment['shipment_date'] = pd.to_datetime(amazon_shipment['shipment_date'])

amazon_shipment_group = (amazon_shipment.assign(date_ym = amazon_shipment['shipment_date'].dt.to_period('M').astype(str)).groupby('date_ym').agg(number_of_shipments=('shipment_id','count')).reset_index())
    
Output:

date_ym	number_of_shipments
2021-08	3
2021-09	6
