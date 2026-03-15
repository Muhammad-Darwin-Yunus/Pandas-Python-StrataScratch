>.<

Title: Session Type Duration
Link: https://platform.stratascratch.com/coding/2011-session-type-duration?code_type=2
Level: Easy

Calculate the average session duration (in seconds) for each session type?

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

twitch_sessions['session_duration_seconds'] = (twitch_sessions['session_end'] - twitch_sessions['session_start']).dt.total_seconds()

twitch_sessions_filter = twitch_sessions.groupby('session_type',as_index=False)['session_duration_seconds'].mean()
    
Output:

session_type	session_duration_seconds
streamer	1310.82
viewer	1908
