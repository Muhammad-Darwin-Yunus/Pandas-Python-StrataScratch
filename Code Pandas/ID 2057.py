>.<

Title: Weight For First Shipment
Link: https://platform.stratascratch.com/coding/2057-weight-for-first-shipment?code_type=2
Level: Easy

Write a query to find the weight for each shipment's earliest shipment date.
Output the shipment id along with the weight.

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

amazon = pd.DataFrame(amazon_shipment)

amazon_date = amazon.sort_values('shipment_date')

amazon_earliest = amazon_date.groupby('shipment_id').first().reset_index()

amazon_output = amazon_earliest[['shipment_id','weight']]
    
Output:

shipment_id  |  weight
101                10
102                50
103                25
104                30
105                20
