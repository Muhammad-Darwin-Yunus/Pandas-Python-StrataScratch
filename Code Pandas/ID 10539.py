>.<

Title: User Activity Count
Link: https://platform.stratascratch.com/coding/10539-user-activity-count?code_type=2
Level: Easy

Count the unique activity types for each user, ensuring users with no activities are also included.
The output should show each user's ID and their activity type count, with zero for users who have no activities.

Data user_profiles:
user_id: int64
name: object
email: object
signup_date: datetime64[ns]

Data activity_log:
user_id: int64
activity_type: object
activity_timestamp: datetime64[ns]

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

data_merged = pd.merge(user_profiles,activity_log,on='user_id',how='left')

activity_users = data_merged.groupby('user_id')['activity_type'].nunique().reset_index()

activity_users['activity_type'].fillna(0,inplace=True)

activity_users

Output:

user_id  |  total_activity
  1            2
  2            3
  3            3
  6            2
  7            3
  8            3
  9            4
  10           1
