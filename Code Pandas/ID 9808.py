>.<

Title: Find business types present in the dataset
Link: https://platform.stratascratch.com/coding/9808-find-business-types-present-in-the-dataset?code_type=2
Level: Easy

Find business types present in the dataset.

Data google_adwords_earnings:
business_type: text
n_employees: bigint
year: bigint
adwords_earnings: bigint

>.<

Solution:

# Start writing code

google = pd.DataFrame(google_adwords_earnings)

google[['business_type']].drop_duplicates().reset_index(drop=True)
    
Output:

business_type
handyman
media
transport
