>.<

Title: Total Shipment Weight
Link: https://platform.stratascratch.com/coding/2058-total-shipment-weight?code_type=2
Level: Easy

Calculate the total weight for each shipment and add it as a new column.
Your output needs to have all the existing rows and columns in addition to the  new column that shows the total weight for each shipment.
One shipment can have multiple rows.

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

amazon['total_weight'] = amazon.groupby('shipment_id')['weight'].transform('sum')

amazon
    
Output:

shipment_id  |  sub_id  |  weight  |  shipment_date  |  total_weight
101              1          10        2021-08-30            40
101              2          20        2021-09-01            40
101              3          10        2021-09-05            40
102              1          50        2021-09-02            50
103              1          25        2021-09-01            55
103              2          30        2021-09-02            55
104              1          30        2021-08-25            40
104              2          10        2021-08-26            40
105              1          20        2021-09-02            20
