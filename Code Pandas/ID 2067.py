>.<

Title: Low Fat and Recyclable
Link: https://platform.stratascratch.com/coding/2067-low-fat-and-recyclable?code_type=2
Level: Easy

What percentage of all products are both low fat and recyclable?

Data facebook_products:
brand_name: text
is_low_fat: text
is_recyclable: text
product_category: bigint
product_class: text
product_family: text
product_id: bigint

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
facebook_products = pd.DataFrame(facebook_products)

facebook_products['is_both'] = ((facebook_products['is_low_fat']=='Y') & (facebook_products['is_recyclable']=='Y')).astype(int)

percentage_product = round(100.0 * facebook_products['is_both'].sum() /len(facebook_products),2)

percentage_product_fix = pd.DataFrame({'percentage_product':[percentage_product]})
    
Output:

percentage_product
8.33
