>.<

Title: April & May Sign Up's
Link: https://platform.stratascratch.com/coding/2159-april-may-sign-ups?code_type=2
Level: Easy

You have been asked to get a list of all the sign up IDs with transaction start dates in either April or May.
Since a sign up ID can be used for multiple transactions only output the unique ID.
Your output should contain a list of non duplicated sign-up IDs.

Data transactions:
transaction_id: bigint
signup_id: bigint
transaction_start_date: date
amt: double

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
transactions = pd.DataFrame(transactions)

transactions['transaction_start_date'] = pd.to_datetime(transactions['transaction_start_date'])

transactions_filter = transactions[(transactions['transaction_start_date'].dt.month == 4) | (transactions['transaction_start_date'].dt.month == 5)]

transactions_signup_id = transactions_filter['signup_id'].dropna().unique()

transactions_fix = pd.DataFrame(transactions_signup_id,columns=['signup_id'])
    
Output:

signup_id
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
