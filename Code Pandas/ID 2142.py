>.<

Title: Third Heaviest Shipment
Link: https://platform.stratascratch.com/coding/2142-third-heaviest-package?code_type=2
Level: Easy

You've been asked by Amazon to find the shipment_id and weight of the third heaviest shipment.
Output the shipment_id, and total_weight for that shipment_id.
In the event of a tie, do not skip ranks.

Data amazon_shipment:
shipment_id: bigint
sub_id: bigint
weight: bigint
shipment_date: date

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment = pd.DataFrame(amazon_shipment)

amazon_shipment_grouped = (amazon_shipment.groupby('shipment_id',as_index=False)['weight'].sum().rename(columns={'weight':'total_weight'}))

amazon_shipment_grouped['rank'] = amazon_shipment_grouped['total_weight'].rank(method='dense',ascending=False)

amazon_shipment_fix = amazon_shipment_grouped[amazon_shipment_grouped['rank']==3][['shipment_id','total_weight']]
    
Output:

shipment_id  |  total_weight
101                  40
104                  40
