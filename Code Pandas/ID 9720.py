>.<

Title: Find the business names that have inspection scores of less than 50
Link: https://platform.stratascratch.com/coding/9720-find-the-business-names-that-have-inspection-scores-of-less-than-50?code_type=2
Level: Easy

Find the business names that scored less than 50 in inspections.
Output the result along with the corresponding inspection date and the score.

Data sf_restaurant_health_violations:
business_id: bigint
business_name: text
business_address: text
business_city: text
business_state: text
business_postal_code: double
business_latitude: double
business_longitude: double
business_location: text
business_phone_number: double
inspection_id: text
inspection_date: datetime
inspection_score: double
inspection_type: text
violation_id: text
violation_description: text
risk_category: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

sf_restaurant = pd.DataFrame(sf_restaurant_health_violations)

sf_restaurant_score = sf_restaurant[sf_restaurant['inspection_score']<50]

sf_restaurant_score[['business_name','inspection_date','inspection_score']]
    
Output:

business_name  |  inspection_date      |  inspection_score
Lollipot          2018-05-22 00:00:00            45
Lollipot          2018-05-22 00:00:00            45
Lollipot          2018-05-22 00:00:00            45
Da Cafe            2016-09-07 00:00:00            48
Lollipot          2018-05-22 00:00:00            45
Lollipot          2018-05-22 00:00:00            45
Lollipot          2018-05-22 00:00:00            45
Da Cafe          2016-09-07 00:00:00              48
Da Cafe          2016-09-07 00:00:00              48
Da Cafe          2016-09-07 00:00:00              48
