>.<

Title: Unique Employee Logins
Link: https://platform.stratascratch.com/coding/2156-unique-employee-logins?code_type=2
Level: Easy

You have been tasked with finding the worker IDs of individuals who logged in between the 13th to the 19th inclusive of December 2021.
In your output, provide the unique worker IDs for the dates requested.

Data worker_logins:
id: bigint
worker_id: bigint
login_timestamp: timestamp
ip_address: text
country: text
region: text
city: text
device_type: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
worker_logins = pd.DataFrame(worker_logins)

worker_logins['login_timestamp'] = pd.to_datetime(worker_logins['login_timestamp'])

worker_logins_filter = worker_logins[(worker_logins['login_timestamp'].dt.year == 2021) & (worker_logins['login_timestamp'].dt.month == 12) & (worker_logins['login_timestamp'].dt.day.between(13,19))]['id'].drop_duplicates()
    
Output:

id
0
1
2
3
10
