>.<

Title: Finding Doctors 
Link: https://platform.stratascratch.com/coding/10356-finding-doctors?code_type=2
Level: Easy

Find doctors with the last name of 'Johnson' in the employee list.
The output should contain both their first and last names.

Data employee_list:
first_name: varchar
last_name: varchar
profession: varchar
employee_id: int
birthday: datetime
birth_month: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
employee_list = pd.DataFrame(employee_list)

baris_dokter = employee_list[employee_list['last_name'].str.contains('Johnson',case='False',na='False')]

baris_dokter = baris_dokter[baris_dokter['profession']=='Doctor'].reset_index()

baris_dokter['fullname'] = baris_dokter['first_name'] + ' ' + baris_dokter['last_name']

gabung_baris = baris_dokter[['fullname']].reset_index(drop='True')

gabung_baris

Output:

first_name | last_name | fullname     | profession
Sarah        Johnson    Sarah Johnson    Doctor
Emma          Johnson    Emma Johnson    Doctor
Nancy        Johnson    Nancy Johnson    Doctor
Jack          Johnson    Jack Johnson    Doctor
Hannah        Johnson    Hannah Johnson  Doctor
Elizabeth    Johnson    Elizabeth Johnson  Doctor
Emma          Johnson    Emma Johnson      Doctor
Emily        Johnson    Emily Johnson      Doctor
Isabella      Johnson    Isabella Johnson  Doctor
Madison      Johnson    Madison Johnson    Doctor
