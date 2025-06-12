>.<

Title: Find the overall friend acceptance count for a given date
Link: https://platform.stratascratch.com/coding/9780-find-the-overall-friend-acceptance-count-for-a-given-date?code_type=2
Level: Easy

Find the overall friend acceptance count for a given date.
Assume the date is 2nd of January 2019.

Data facebook_friendship_requests:
sender: bigint
receiver: bigint
date_sent: datetime
date_approved: datetime

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

facebook = pd.DataFrame(facebook_friendship_requests)

facebook_date = facebook.groupby('date_approved')['receiver'].count().reset_index(name='overall_friend')
    
Output:

date_approved        |  overall_friend
2019-02-02 00:00:00          1
2019-03-02 00:00:00          1
2019-01-02 00:00:00          2
