>.<

Title: Combine Workers First and Last Names
Link: https://platform.stratascratch.com/coding/9834-combine-the-first-and-last-names-of-workers?code_type=2
Level: Easy

Combine the first and last names of workers with a space in-between in a column 'full_name'.

Data worker:
worker_id: bigint
first_name: text
last_name: text
salary: bigint
joining_date: datetime
department: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

worker = pd.DataFrame(worker)

worker['full_name'] = worker['first_name'] + ' ' + worker['last_name']

worker['full_name']
    
Output:

full_name
Monika Arora
Niharika Verma
Vishal Singhal
Amitah Singh
Vivek Bhati
Vipul Diwan
Satish Kumar
Geetika Chauhan
Agepi Argon
Moe Acharya
Nayah Laghari
Jai Patel
