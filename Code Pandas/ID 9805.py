>.<

Title: Find drafts which contains the word 'optimism'
Link: https://platform.stratascratch.com/coding/9805-find-drafts-which-contains-the-word-optimism?code_type=2
Level: Easy

Find drafts which contains the word 'optimism'.

Data google_file_store:
filename: text
contents:text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

google = pd.DataFrame(google_file_store)

google_sort = google[google['contents'].str.contains('optimism',case=False,na=False)]['filename']
    
Output:

filename
draft2.txt
final.txt
