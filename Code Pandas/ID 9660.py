>.<

Title: Count the number of students lectured by each teacher
Link: https://platform.stratascratch.com/coding/9660-count-the-number-of-students-lectured-by-each-teacher?code_type=2
Level: Easy

Count the number of students lectured by each teacher.
Output the result along with the name of the teacher.

Data sat_scores:
school: text
teacher: text
student_id: double
sat_writing: double
sat_verbal: double
sat_math: double
hrs_studied: double
id: bigint
average_sat: double
love: datetime

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

sat_scores = pd.DataFrame(sat_scores)

sat_scores_teacher = sat_scores.groupby('teacher')['student_id'].count().reset_index(name='number_of_students')

sat_scores_teacher[['number_of_students','teacher']]
    
Output:

number_of_students  |  teacher
13                    Frederickson
18                    Spellman
13                    Davis
17                    Brown
23                    Perry
20                    Rajaram
16                    Williams
15                    Tran
