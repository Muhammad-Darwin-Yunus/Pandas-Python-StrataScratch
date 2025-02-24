>.<

Title: Average Cost Of Each Request
Link: https://platform.stratascratch.com/coding/10007-average-cost-of-each-request?code_type=2
Level: Easy

Find the average cost of each request status.
Request status can be either 'success' or 'fail'.
Output the request status along with the average cost.

Data uber_ride_requests:
distance_to_travel: double
driver_to_client_distance: double
monetary_cost: double
request_id: bigint
request_status: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

average_cost = pd.DataFrame(uber_ride_requests)

request = average_cost.groupby('request_status')['monetary_cost'].mean().reset_index()

request_fix = pd.DataFrame({'request_status':request['request_status'],'avg_cost':request['monetary_cost']})

Output:

request_status  |  avg_cost
success              11.76
fail                  13.54
