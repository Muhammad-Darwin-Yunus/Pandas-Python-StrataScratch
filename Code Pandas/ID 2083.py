>.<

Title: Pending Claims
Link: https://platform.stratascratch.com/coding/2083-pending-claims?code_type=2
Level: Easy

Count how many claims submitted in December 2021 are still pending.
A claim is pending when it has neither an acceptance nor rejection date.

Data cvs_claims:
account_id: text
claim_id: bigint
date_accepted: date
date_rejected: date
date_submitted: date

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
cvs_claims = pd.DataFrame(cvs_claims)

cvs_claims_filter = cvs_claims[cvs_claims['date_rejected'].isnull()]['claim_id'].count()

cvs_claims_fix = pd.DataFrame({'claim_pending':[cvs_claims_filter]})
    
Output:

claim_pending
11
