>.<

Title: Active Users Per Platform
Link: https://platform.stratascratch.com/coding/2072-active-users-per-platform?code_type=2
Level: Easy

For each platform (e.g. Windows, iPhone, iPad etc.), calculate the number of users.
Consider unique users and not individual sessions.
Output the name of the platform with the corresponding number of users.

Data user_sessions:
platform: text
session_endtime: timestamp
session_id: bigint
session_starttime: timestamp
user_id: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
user_sessions = pd.DataFrame(user_sessions)

user_sessions_group = user_sessions.groupby('platform')['user_id'].nunique().reset_index(name='total_user')
    
Output:

platform  |  total_user
Android        1
IPad          1
IPhone        2
Windows        4
