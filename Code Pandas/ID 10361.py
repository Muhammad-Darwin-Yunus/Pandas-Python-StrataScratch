>.<

Title: Peak Online Time
Link: https://platform.stratascratch.com/coding/10361-peak-online-time?code_type=2
Level: Easy

You are given a dataset from Amazon that tracks and aggregates user activity on their platform in certain time periods.
For each device type, find the time period with the highest number of active users.
The output should contain 'user_count', 'time_period', and 'device_type', where 'time_period' is a concatenation of 'start_timestamp' and 'end_timestamp', like ; "start_timestamp to end_timestamp".

Data user_activity:
start_timestamp: datetime64[ns]
end_timestamp: datetime64[ns]
user_count: int64
device_type: object
time_difference: float64

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

user_activity['time_period'] = user_activity['start_timestamp'].astype(str) + ' to ' + user_activity['end_timestamp'].astype(str)

active_user = user_activity.groupby(['device_type','time_period'],as_index=False).agg({
    'user_count':'sum'
})

max_user_count = active_user.groupby('device_type')['user_count'].idxmax()

hasil = active_user.loc[max_user_count]

hasil

Output:

device_type  |  time_period                                |  user_count
desktop        2024-01-25 10:14:00 to 2024-01-25 11:04:00        100
mobile          2024-01-25 16:38:00 to 2024-01-25 18:07:00        100
tablet          2024-01-25 01:22:00 to 2024-01-25 03:13:00        100
