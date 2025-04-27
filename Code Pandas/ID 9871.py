>.<

Title: Highly Reviewed Hotels
Link: https://platform.stratascratch.com/coding/9871-highly-reviewed-hotels?code_type=2
Level: Easy

List all hotels with their total number of reviews.
Show the results sorted by the number of reviews from highest to lowest and output the hotel name along with the reviews.

Data hotel_reviews:
hotel_address: text
additional_number_of_scoring: bigint
review_date: datetime
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

hotel_reviews_filter = hotel_reviews.groupby('hotel_name').agg(total_number_of_reviews=('total_number_of_reviews','max')).reset_index()

hotel_reviews_sort = hotel_reviews_filter.sort_values(by='total_number_of_reviews', ascending=False)
    
Output:

hotel_name                                        |    total_number_of_reviews
Park Plaza Westminster Bridge London                            12158
Strand Palace Hotel                                              9568
Britannia International Hotel Canary Wharf                        9086
Best Western Premier Hotel Couture                                8177
The Student Hotel Amsterdam City                                  7656
Golden Tulip Amsterdam West                                        7586
Holiday Inn London Kensington                                    5945
Ramada Apollo Amsterdam Centre                                    5770
St James Court A Taj Hotel London                                5394
WestCord Fashion Hotel Amsterdam                                5236
The Cumberland A Guoman Hotel                                    5180
Park Plaza Victoria Amsterdam                                    4820
NH Carlton Amsterdam                                            4231
Austria Trend Parkhotel Sch nbrunn Wien                        4026
Hotel Berna                                                    4017
Sunotel Central                                                3870
Best Western Blue Tower Hotel                                    3869
Hilton Garden Inn Milan North                                    3613
Petit Palace Boqueria Garden                                    3602
NH City Centre Amsterdam                                        3417
The Grosvenor                                                    3274
Pullman London St Pancras                                        3168
Sall s Hotel Pere IV                                            3130
Millennium Hotel London Mayfair                                3117
Dorsett Shepherds Bush                                        2890
NH Collection Amsterdam Barbizon Palace                        2865
London Marriott Hotel West India Quay                        2836
Atlantis Hotel Vienna                                        2823
DoubleTree By Hilton London Excel                            2726
LaGare Hotel Milano Centrale MGallery by Sofitel              2678
Clayton Crown Hotel London                                    2491
Golden Tulip Amsterdam Riverside                                2362
Novotel Paris Centre Tour Eiffel                                2310
Mayflower Hotel Apartments                                    2197
Radisson Blu Edwardian Kenilworth                            2011
Dikker en Thijs Fenice Hotel                                1971
ARCOTEL Wimberger                                            1886
Austria Trend Hotel Rathauspark Wien                        1884
Melia White House Hotel                                    1871
WestCord Art Hotel Amsterdam 4 stars                        1712
Hotel Vueling Bcn by HC                                    1696
Amadi Park Hotel                                            1615
Ambassade Hotel                                            1611
NH Amsterdam Centre                                        1574
Best Western The Boltons Hotel London Kensington            1573
Grand Hotel Amr th Amsterdam                                1530
Hilton London Angel Islington                                1462
Hotel Arena                                                  1403
Element Amsterdam                                            1369
Auteuil Tour Eiffel                                            1266
The Nadler Kensington                                        1209
The Chesterfield Mayfair                                    1166
Novotel London Excel                                        1158
Sofitel Vienna Stephansdom                                    1148
Mercure Wien Zentrum                                          1105
Hilton Amsterdam                                            1064
The Cavendish London                                        1039
Rosewood London                                            1008
Hilton Milan                                                988
Hotel Roemer Amsterdam                                        974
Abba Garden                                                    959
Hotel JL No76                                                914
NH Amsterdam Museum Quarter                                    854
The Drayton Court Hotel                                        750
Hallmark Hotel London Chigwell Prince Regent                    747
Fifty Four Boutique Hotel                                        684
Hotel Atmospheres                                                654
Batty Langley s                                                644
Hotel Moonlight                                                617
Courthouse Hotel Shoreditch                                    477
Knightsbridge Hotel                                            473
Ham Yard Hotel                                                  314
Baglioni Hotel London The Leading Hotels of the World            290
41                                                                244
Hotel Le Six                                                        177
InterContinental Amstel Amsterdam                                    151
