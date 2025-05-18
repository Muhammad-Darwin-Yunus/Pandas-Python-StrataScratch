>.<

Title: Sort Workers in Ascending Order by First Name and Descending Order by Department
Link: https://platform.stratascratch.com/coding/9836-sort-workers-in-ascending-order-by-the-first-name-and-in-descending-order-by-department-name?code_type=2
Level: Easy

Sort workers in ascending order by the first name and then in descending order by department name.

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

worker_sort = worker.sort_values(by=['first_name','department'],ascending=[True, False])

worker_sort['fullname'] = worker_sort['first_name'] + ' ' + worker_sort['last_name']

worker_sort['fullname']
    
Output:

fullname
Agepi Argon
Amitah Singh
Geetika Chauhan
Jai Patel
Moe Acharya
Monika Arora
Nayah Laghari
Niharika Verma
Satish Kumar
Vipul Diwan
Vishal Singhal
Vivek Bhati
