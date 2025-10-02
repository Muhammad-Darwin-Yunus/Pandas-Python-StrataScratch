>.<

Title: Sorting By Second Character
Link: https://platform.stratascratch.com/coding/2166-sorting-by-second-character?code_type=2
Level: Easy

You've been asked to arrange a column of random IDs in ascending alphabetical order based on their second character.

Data random_id:
id: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

random_id = pd.DataFrame(random_id)

random_id['chart2'] = random_id['id'].str[1]

random_id_sort = random_id.sort_values(by='chart2')

random_id_id = random_id_sort[['id']].reset_index(drop=True)
    
Output:

id
2ABS5
4AOS9
3ASD1
3CYS1
3CUY1
3CGY1
2CBS6
3DUU1
2DQS4
2DYS7
4DSS1
5MQS2
3NOS8
5NES1
2PTY1
2POI9
2SUI8
3TQS1
5TLS2
5ZQS3
