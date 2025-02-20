>.<

Title: Reviews of Hotel Arena
Link: https://platform.stratascratch.com/coding/10166-reviews-of-hotel-arena?code_type=2
Level: Easy

Find the number of rows for each review score earned by 'Hotel Arena'.
Output the hotel name (which should be 'Hotel Arena'), review score along with the corresponding number of rows with that score for the specified hotel.

Data hotel_reviews:
hotel_address: varchar
additional_number_of_scoring: int
review_date: datetime
average_score: float
hotel_name: varchar
reviewer_nationality: varchar
negative_review: varchar
review_total_negative_word_counts: int
total_number_of_reviews: int
positive_review: varchar
review_total_positive_word_counts: int
total_number_of_reviews_reviewer_has_given: int
reviewer_score: float
tags: varchar
days_since_review: varchar
lat: float
lng: float
>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

hotel_arena = pd.DataFrame(hotel_reviews)

hotel_name_review = hotel_arena[hotel_arena['hotel_name']=='Hotel Arena']

result = hotel_name_review.groupby(['hotel_name','reviewer_score']).size().reset_index(name='count')

Output:

hotel_name   | reviewer_score | count
Hotel Arena          7.5          2
Hotel Arena          9.6          2
Hotel Arena          4.6          1
Hotel Arena          3.8          1
Hotel Arena          4.2          1
Hotel Arena          8.8          2
Hotel Arena          8.3          2
Hotel Arena          6.3          1
Hotel Arena          7.1          1
Hotel Arena          5.4          1
Hotel Arena          5.8          2
