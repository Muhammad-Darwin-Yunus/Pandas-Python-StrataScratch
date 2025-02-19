>.<

Title: Guest Or Host Kindness
Link: https://platform.stratascratch.com/coding/10072-guest-or-host-kindness?code_type=2
Level: Easy

Find whether hosts or guests give higher review scores based on their average review scores. Output the higher of the average review score rounded to the 2nd decimal spot (e.g., 5.11).

Data airbnb_reviews:
from_user: int
to_user: int
from_type: varchar
to_type: varchar
review_score: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

guest_host = pd.DataFrame(airbnb_reviews)

from_type_avg = guest_host.groupby('from_type')['review_score'].mean().reset_index()
from_type_avg['type'] = from_type_avg['from_type']
from_type_avg = from_type_avg[['type','review_score']]

to_type_avg = guest_host.groupby('to_type')['review_score'].mean().reset_index()
to_type_avg['type'] = to_type_avg['to_type']
to_type_avg = to_type_avg[['type','review_score']]

avg_score = pd.concat([from_type_avg,to_type_avg])

filter_avg_score = avg_score[avg_score['type'].isin(['guest','host'])]

result_avg_score = (filter_avg_score.groupby('type')['review_score'].max().reset_index().sort_values('review_score',ascending=False).round({'review_score':2}).head(1))

result_avg_score_fix = pd.DataFrame({'type':result_avg_score['type'],'review_score_highest':result_avg_score['review_score']})

Output:

type  |  review_score_highest
guest        5.29
