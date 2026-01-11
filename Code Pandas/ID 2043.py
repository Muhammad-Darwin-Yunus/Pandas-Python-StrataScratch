>.<

Title: Employees' Without Annual Review
Link: https://platform.stratascratch.com/coding/2043-employees-without-annual-review?code_type=2
Level: Easy

Return all employees who have never had an annual review.
Your output should include the employee's first name, last name, hiring date, and termination date.
List the most recently hired employees first.

Data uber_employees:
first_name: text
hire_date: date
id: bigint
last_name: text
salary: bigint
termination_date: date

Data uber_annual_review:
emp_id: bigint
id: bigint
review_date: date

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
uber_merged = uber_employees.merge(uber_annual_review,how='left',left_on='id',right_on='emp_id')

uber_merged_filter = uber_merged[uber_merged['emp_id'].isna()][['first_name','last_name','hire_date','termination_date']].sort_values('hire_date',ascending=False)
    
Output:

first_name	last_name	hire_date	termination_date
Sawsan	Ahmed	2019-11-22	
Anton	Darios	2019-11-22	
Amira	Kamal	2019-10-09	
Sameer	Mostafa	2019-10-09	
Markos	Tomas	2019-08-13	2019-11-22
Ismail	Bakr	2019-05-22	2019-10-09
Mohamed	Saeed	2019-03-20	
Jaya	Ananya	2019-01-20	
Sana	Pital	2018-12-23	
Ishaan	Kumar	2018-12-23	2019-10-09
Lee	Chen	2018-11-22	2019-08-13
Zhao	Liu	2018-11-22	2019-08-13
Wang	Wu	2018-08-13	2019-05-22
Kai	Luca	2018-05-22	
Eve	John	2018-05-20	
Adam	Matteo	2018-04-15	2019-08-13
Ian	Rolls	2017-11-22	2019-08-13
Cooper	Duet	2017-09-25	2019-05-22
Mathias	Francis	2017-09-25	2019-10-09
Carlos	Leo	2017-09-25	2019-10-09
Roberto	Levi	2017-07-20	2019-08-13
Robert	Logan	2017-05-22	2019-08-13
Santiago	Nelson	2017-04-15	2019-05-22
Rynolds	James	2016-12-23	2017-09-25
Ryan	Willis	2016-10-09	2017-07-20
Charles	Eli	2016-07-20	2019-01-20
Joshua	William	2016-04-15	2018-12-23
Thomas	Lucas	2016-03-20	2018-12-23
Matteo	Lebron	2016-01-20	2018-11-22
Robertson	James	2015-09-10	2018-11-22
Jackson	Robertson	2015-09-10	2018-08-13
Leo	Sky	2015-07-20	2018-05-22
Olivier	Twist	2015-01-20	2016-01-20
James	Power	2014-12-23	2016-07-20
Willis	Franklin	2014-11-22	2016-04-15
Harry	Frank	2014-10-09	2016-03-20
Kate	Medlton	2014-09-25	2016-01-20
William	Charles	2014-08-13	2015-03-14
Lucas	Merkel	2014-05-20	2015-02-03
Angela	Maton	2014-03-20	2015-01-20
Biden	Joe	2014-02-03	2014-12-23
Nguyen	Trung	2013-11-22	2016-03-20
Mostafa	Ahmed	2013-10-09	2016-01-20
Emad	Adam	2013-09-25	2015-09-10
Kero	Ian	2013-09-10	2015-09-10
Efthimus	James	2012-04-15	2014-01-20
Andrea	Willis	2012-03-20	2013-08-13
Anton	Harry	2012-03-14	2013-07-20
