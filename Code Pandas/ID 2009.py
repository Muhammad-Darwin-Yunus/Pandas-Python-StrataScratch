>.<

Title: Users With Two Statuses
Link: https://platform.stratascratch.com/coding/2009-users-with-two-statuses?code_type=2
Level: Easy

Find users who are both a viewer and streamer.

Data twitch_sessions:
session_end: varchar
session_id: int
session_start: varchar
session_type: varchar
user_id: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
twitch_sessions = pd.DataFrame(twitch_sessions)

twitch_sessions_group = twitch_sessions.groupby('user_id')['session_type'].nunique()

twitch_sessions_session_type = twitch_sessions_group[twitch_sessions_group ==2].reset_index()
    
Output:

user_id	session_type
0	2
1	2
2	2
3	2
6	2
7	2
