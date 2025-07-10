>.<

Title: Find all business postal codes of restaurants with issues related to the water
Link: https://platform.stratascratch.com/coding/9719-find-all-business-postal-codes-of-restaurants-with-issues-related-to-the-water?code_type=2
Level: Easy

Find all business postal codes of restaurants with issues related to the water (violation description contains substring "water").

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

sf_restaurant_violation = sf_restaurant[sf_restaurant['violation_description'].str.contains('water',case=False,na=False)]['business_postal_code'].dropna().unique()

sf_restaurant_fix = pd.DataFrame({'business_postal_code':sf_restaurant_violation})
    
Output:

business_postal_code
94133
94115
94103
94118
