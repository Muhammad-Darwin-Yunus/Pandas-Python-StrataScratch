>.<

Title: Unique Users Per Client Per Month
Link: https://platform.stratascratch.com/coding/2024-unique-users-per-client-per-month?code_type=2
Level: Easy

Write a query that returns the number of unique users per client for each month.
Assume all events occur within the same year, so only month needs to be be in the output as a number from 1 to 12.

Data fact_events:
client_id: text
customer_id: text
event_id: bigint
event_type: text
id: bigint
time_id: date
user_id: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
fact_events = pd.DataFrame(fact_events)

fact_events_group = (fact_events.groupby(['client_id',fact_events['time_id'].dt.month])['user_id'].nunique().reset_index())
    
Output:

client_id	month	users_num
desktop	2	13
desktop	3	16
desktop	4	11
mobile	2	9
mobile	3	14
mobile	4	9
