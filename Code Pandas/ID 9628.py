>.<

Title: Reviews Bins on Reviews Number
Link: https://platform.stratascratch.com/coding/9628-reviews-bins-on-reviews-number?code_type=2
Level: Easy

To better understand how the number of reviews affects accommodation prices, classify each listing based on its number of reviews (use column number_of_reviews) into the following categories:
•  0 reviews: "NO"
•  1 to 5 reviews: "FEW"
•  6 to 15 reviews: "SOME"
•  16 to 40 reviews: "MANY"
•  More than 40 reviews: "A LOT"
For each record, output the price along with the corresponding category that describes its review count.

Data airbnb_search_details:
id: bigint
price: double
property_type: text
room_type: text
amenities: text
accommodates: bigint
bathrooms: bigint
bed_type: text
cancellation_policy: text
cleaning_fee: tinyint
city: text
host_identity_verified: text
host_response_rate: text
host_since: date
neighbourhood: text
number_of_reviews: bigint
review_scores_rating: double
zipcode: bigint
bedrooms: bigint
beds: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

airbnb_search_details = pd.DataFrame(airbnb_search_details)

airbnb_search_details['review_category'] = pd.cut(airbnb_search_details['number_of_reviews'],bins=[-1,0,5,15,40,float("inf")],labels=["NO", "FEW", "SOME", "MANY", "A LOT"])

airbnb_search_details[['price','review_category']]
    
Output:

price  |  review_category
555.68	FEW
366.36	SOME
482.83	A LOT
448.86	SOME
506.89	FEW
720.79	NO
516.48	FEW
529.33	A LOT
679.68	FEW
633.51	A LOT
485.98	MANY
598.9	FEW
741.76	NO
431.75	FEW
469.13	SOME
485.2	MANY
482.83	NO
313.55	NO
438.2	SOME
368.89	NO
336.73	NO
417.44	A LOT
423.41	MANY
389.18	A LOT
482.83	SOME
541.61	SOME
662.01	FEW
391.2	NO
470.05	FEW
412.71	MANY
407.75	FEW
501.06	SOME
539.36	NO
480.4	MANY
474.49	SOME
695.65	FEW
424.85	SOME
667.83	MANY
417.44	SOME
529.33	A LOT
430.41	MANY
385.01	A LOT
570.38	FEW
602.83	NO
455.39	MANY
459.51	A LOT
529.83	NO
506.89	A LOT
470.05	FEW
459.51	SOME
417.44	FEW
552.15	SOME
482.83	SOME
680.13	NO
497.67	FEW
685.65	SOME
361.09	SOME
507.52	FEW
519.3	SOME
661.87	FEW
417.44	MANY
455.39	A LOT
486.75	MANY
630.99	NO
270.81	MANY
474.49	MANY
438.2	FEW
486.75	A LOT
570.38	NO
501.06	FEW
448.86	SOME
478.75	SOME
409.43	FEW
389.18	SOME
551.75	MANY
404.31	SOME
674.52	NO
409.43	SOME
465.4	A LOT
355.53	FEW
494.16	MANY
444.27	NO
510.59	FEW
448.86	MANY
519.3	SOME
431.75	NO
552.15	NO
438.2	A LOT
431.75	FEW
434.38	FEW
621.26	NO
431.75	MANY
552.15	MANY
424.85	SOME
459.51	A LOT
400.73	SOME
552.15	SOME
548.06	A LOT
621.46	FEW
486.75	NO
340.12	A LOT
449.98	NO
400.73	FEW
431.75	MANY
478.75	SOME
504.34	SOME
552.15	MANY
570.04	NO
482.83	SOME
474.49	NO
570.38	SOME
538.91	FEW
519.3	FEW
717.01	FEW
501.06	NO
449.98	MANY
504.34	MANY
598.9	FEW
529.83	NO
519.3	FEW
674.52	NO
578.38	NO
487.52	FEW
548.06	SOME
424.85	SOME
561.68	MANY
524.7	SOME
424.85	A LOT
423.41	FEW
599.15	MANY
423.41	SOME
497.67	SOME
433.07	FEW
409.43	NO
478.75	SOME
529.83	NO
448.86	MANY
490.53	SOME
444.27	A LOT
420.47	NO
478.75	FEW
662.01	NO
380.67	FEW
321.89	NO
424.85	A LOT
366.36	MANY
534.71	SOME
444.27	NO
468.21	FEW
444.27	FEW
594.02	SOME
460.52	NO
470.05	FEW
436.94	FEW
431.75	NO
478.75	NO
510.59	FEW
368.89	SOME
409.43	MANY
477.91	FEW
