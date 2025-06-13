>.<

Title: Find the maximum step reached for every feature
Link: https://platform.stratascratch.com/coding/9774-find-the-maximum-step-reached-for-every-feature?code_type=2
Level: Easy

Find the maximum step reached for every feature.
Output the feature id along with its maximum step.

Data facebook_product_features_realizations:
feature_id: bigint
user_id:bigint
step_reached: bigint
timestamp: timestamp

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

facebook = pd.DataFrame(facebook_product_features_realizations)

facebook_max = facebook.groupby('feature_id')['step_reached'].max().reset_index(name='max_step_reach')
    
Output:

feature_id  |  max_step_reach
0                  5
1                  7
