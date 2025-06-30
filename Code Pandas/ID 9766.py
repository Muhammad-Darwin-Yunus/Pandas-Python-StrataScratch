>.<

Title: Find the complaint id for the processed complaints of type 1
Link: https://platform.stratascratch.com/coding/9766-find-the-complaint-id-for-the-processed-complaints-of-type-1?code_type=2
Level: Easy

Find the complaint id for the processed complaints of type 1.

Data facebook_complaints:
complaint_id: bigint
type: bigint
processed: tinyint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

facebook = pd.DataFrame(facebook_complaints)

facebook_filter = facebook[(facebook['type']==1) & (facebook['processed']==1)]

facebook_filter['complaint_id']
    
Output:

complaint_id
3
4
