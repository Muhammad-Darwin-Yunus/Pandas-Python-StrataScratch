>.<

Title: Most Recent Employee Login Details
Link: https://platform.stratascratch.com/coding/2141-most-recent-employee-login-details?code_type=2
Level: Easy

Amazon's information technology department is looking for information on employees' most recent logins.
The output should include all information related to each employee's most recent login.

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

worker_logins_max_timestamp = worker_logins['login_timestamp'].max()

worker_logins_fix = worker_logins[worker_logins['login_timestamp'] == worker_logins_max_timestamp]
    
Output:

id  |  worker_id  |  login_timestamp      |  ip_address    |  country  |  region  |  city  |  device_type
19        7          2022-01-26 10:55:00    212.102.111.33 
