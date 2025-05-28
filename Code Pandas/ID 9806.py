>.<

Title: Find all records with words that start with the letter 'g'
Link: https://platform.stratascratch.com/coding/9806-find-all-records-with-words-that-start-with-the-letter-g?code_type=2
Level: Easy

Find all records with words that start with the letter 'g'.
Output words1 and words2 if any of them satisfies the condition.

Data google_word_lists:
words1: text
words2: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

google = pd.DataFrame(google_word_lists)

google_sort = google[google['words1'].str.startswith('g') | google['words2'].str.startswith('g')][['words1','words2']]
    
Output:

words1                    |  words2
google,facebook,microsoft    flower,nature,sun
sun,nature                    google,apple
