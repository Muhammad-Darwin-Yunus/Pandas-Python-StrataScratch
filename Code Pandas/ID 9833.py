>.<

Title: Replace the letter 'a' with 'A' in the first name
Link: https://platform.stratascratch.com/coding/9833-replace-the-letter-a-with-a-in-the-first-name?code_type=2
Level: Easy

Replace the letter 'a' with 'A' in the first name.

Data worker:
worker_id: bigint
first_name: text
last_name: text
salary: bigint
joining_date: datetime
department: text

>.<

Solution:

select replace(first_name,'a',upper('a')) first_name
from worker;
    
Output:

first_name
MonikA
NihArikA
VishAl
AmitAh
Vivek
Vipul
SAtish
GeetikA
Agepi
Moe
NAyAh
JAi
