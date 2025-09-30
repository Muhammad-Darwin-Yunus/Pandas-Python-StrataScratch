>.<

Title: Dirty Hotel Rooms
Link: https://platform.stratascratch.com/coding/9602-dirty-hotel-rooms?code_type=2
Level: Easy

Find hotels in the Netherlands that got complaints from guests about room dirtiness (word "dirty" in its negative review).
Output all the columns in your results

Data hotel_reviews:
hotel_address: text
additional_number_of_scoring: bigint
review_date: date
average_score: double
hotel_name: text
reviewer_nationality: text
negative_review: text
review_total_negative_word_counts: bigint
total_number_of_reviews: bigint
positive_review: text
review_total_positive_word_counts: bigint
total_number_of_reviews_reviewer_has_given: bigint
reviewer_score: double
tags: text
days_since_review: text
lat: double
lng: double

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

hotel_reviews = pd.DataFrame(hotel_reviews)

hotel_reviews_filter = hotel_reviews[(hotel_reviews['hotel_address'].str.contains('Netherlands',na=False,case=False)) & (hotel_reviews['negative_review'].str.contains('dirty',na=False,case=False))]['hotel_address']
    
Output:

hotel_address
Staalmeesterslaan 410 Slotervaart 1057 PH Amsterdam Netherlands
Vijzelstraat 4 Amsterdam City Center 1017 HK Amsterdam Netherlands
Vijzelstraat 4 Amsterdam City Center 1017 HK Amsterdam Netherlands
Staalmeesterslaan 410 Slotervaart 1057 PH Amsterdam Netherlands
Prins Hendrikkade 59 72 Amsterdam City Center 1012 AD Amsterdam Netherlands
s Gravesandestraat 55 Oost 1092 AA Amsterdam Netherlands
Provincialeweg 38 Zuidoost 1108 AB Amsterdam Netherlands
Spaarndammerdijk 304 Westerpark 1013 ZX Amsterdam Netherlands
Professor Tulpplein 1 Amsterdam City Center 1018 GX Amsterdam Netherlands
Stadhouderskade 7 Oud West 1054 ES Amsterdam Netherlands
Staalmeesterslaan 410 Slotervaart 1057 PH Amsterdam Netherlands
Roemer Visscherstraat 8 10 Oud West 1054 EV Amsterdam Netherlands
Molenwerf 1 1014 AG Amsterdam Netherlands
Spuistraat 288 292 Amsterdam City Center 1012 VX Amsterdam Netherlands
Prins Hendrikkade 108 Amsterdam City Center 1011 AK Amsterdam Netherlands
Wibautstraat 129 Oost 1091 GL Amsterdam Netherlands
