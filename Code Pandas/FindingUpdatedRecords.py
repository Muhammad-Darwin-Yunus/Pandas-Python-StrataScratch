>.<

Title: Finding Updated Records
Link: https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=2
Level: Easy

We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information.
Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary.
Order your list by employee ID in ascending order.

Data ms_employee_salary:
id: int
first_name: varchar
last_name: varchar
salary: int
department_id: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

update_salaries = ms_employee_salary.groupby('id').agg(first_name=('first_name','first'),last_name=('last_name','first'),department_id=('department_id','first'),salary=('salary','max')).reset_index()

update_salaries

Output:

id | first_name | last_name | department_id | current_salary
1    Todd          Wilson        1006            110000
2    Justin        Simon          1005          130000
3    Kelly        Rosario        1002            42689
4    Patricia      Powell        1004            170000
5    Sherry        Golden        1002            44101
6    Natasha      Swanson        1005            90000
7    Diane        Gordon          1002          74591
8    Mercedes    Rodriguez        1005          61048
9    Christy      Mitchell        1001          150000
10    Sean        Crawford        1006          190000
11    Kevin        Townsend        1002          166861
12    Joshua      Johnson          1004          123082
13    Julie        Sanchez          1001          210000
14    John        Coleman          1001            152434
15    Anthony      Valdez          1001            96898
16    Briana        Rivas          1005            151668
17    Jason        Burnett         1006            42525
18    Jeffrey        Harris          1002            20000
19    Michael        Ramsey          1003          63159
20    Cody          Gonzalez        1004            112809
21    Stephen        Berry          1002            123617
22    Brittany      Scott          1002              162537
23    Angela        Williams      1004              100875
24    William      Flores          1003              142674
25    Pamela      Matthews        1005              57944
26    Allison      Johnson        1001              128782
27    Anthony     Ball            1003              34386
28    Alexis      Beck            1005              12260
29    Jason        Olsen          1006              51937
30    Stephen      Smith          1001              194791
31    Kimberly      Brooks        1003              95327
32    Eric        Zimmerman        1006            83093
33    Peter        Holt            1002             69945
34    Justin      Dunn            1003              67992
35    John        Ball            1004              47795
36    Jesus      Ward            1005              36078
37    Philip    Gillespie        1006              36424
38    Nicole      Lewis          1001              114079
39    Linda      Clark            1002              186781
40    Colleen    Carrillo        1004              147723
41    John        George          1001              21642
42    Traci      Williams          1003            180000
43    Joseph      Rogers          1005              22800
44    Trevor      Carter          1001              38670
45    Kevin      Duncan          1003                45210
46    Joshua      Ewing            1003              73088
47    Kimberly      Dean          1003              71416
48    Robert      Lynch          1004                117960
49    Amber      Harding          1002                77764
50    Victoria    Wilson          1002                176620
51    Theresa      Everett        1002                31404
52    Kara        Smith          1004                192838
53    Teresa        Cohen        1001                98860
54    Wesley        Tucker        1005                90221
55    Michael        Morris        1005               106799
56    Rachael      Williams        1002                103585
57    Patricia      Harmon          1005              147417
58    Edward        Sharp            1005              41077
59    Kevin        Robinson          1005              100924
60    Charles      Pearson            1004              173317
61    Ryan          Brown            1003                120000
62    Dale        Hayes              1005                97662
63    Richard      Sanford            1001                136083
64    Danielle      Williams          1006                120000
65    Deborah      Martin            1004                  67389
66    Dustin        Bush              1004                  47567
67    Tyler        Green              1002                  111085
68    Antonio      Carpenter          1002                  83684
69    Ernest        Peterson          1005                  115993
70    Karen        Fernandez          1003                  101238
71    Kristine      Casey              1003                  67651
72    Christine      Frye              1004                  137244
73    William        Preston            1003                  155225
74    Richard        Cole              1003                    180361
75    Julia        Ramos                1006                  105000
