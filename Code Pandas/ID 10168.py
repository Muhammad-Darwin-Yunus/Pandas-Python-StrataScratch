>.<

Title: Number Of Records By Variety
Link: https://platform.stratascratch.com/coding/10168-number-of-records-by-variety?code_type=2
Level: Easy

Find the total number of records that belong to each variety in the dataset.
Output the variety along with the corresponding number of records.
Order records by the variety in ascending order.

Data iris:
sepal_length: float
sepal_width: float
petal_length: float
petal_width: float
variety: varchar

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

number_variety = pd.DataFrame(iris)

number_variety_record = number_variety.groupby('variety')['sepal_length'].count().reset_index()

number_variety_rename = number_variety_record.rename(columns={'sepal_length':'total_variety'})

Output:

variety | total_variety
Setosa      50
Versicolor  50
Virginica    50
