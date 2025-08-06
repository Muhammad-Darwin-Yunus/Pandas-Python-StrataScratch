>.<

Title: Find industries that make a profit
Link: https://platform.stratascratch.com/coding/9682-find-industries-with-the-lowest-sales-but-still-makes-a-profit?code_type=2
Level: Easy

Find all industries with a positive average profit. For those industries extract their lowest sale.
Output the industry along with the corresponding lowest sale and average profit.
Sort the output based on the lowest sales in ascending order.

Data forbes_global_2010_2014:
company: text
sector: text
industry: text
continent: text
country: text
marketvalue: double
sales: double
profits: double
assets: double
rank: bigint
forbeswebpage: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

forbes_global = pd.DataFrame(forbes_global_2010_2014)

forbes_global_group = forbes_global.groupby('industry').agg(lowest_sales=('sales','min'), avg_profit =('profits','mean')).reset_index()

forbes_global_sort = forbes_global_group.sort_values('lowest_sales',ascending=True)
    
Output:

industry                    |  lowest_sales  |  avg_profit
Major Banks                        27.7            11.9
Electric Utilities                  32              1.27
Life & Health Insurance            34.5            -2.2
Software & Programming              37.9            16.95
Investment Services                  39.5            10.3
Beverages                            43.2            9.9
Pharmaceuticals                      43.7            10.5
Broadcasting & Cable                  46              6.7
Communications Equipment              47.9            8.2
Diversified Chemicals                50.4            6.55
Semiconductors                        52.7            18.4
Oil & Gas Operations                  55.6            16.47
Telecommunications services          55.6            14.13
Regional Banks                        56.5            23.44
Diversified Insurance                  59              5.64
Computer Services                      59.7            14.35
Conglomerates                          62.7            8.83
Diversified Metals & Mining            67.7            14.8
Medical Equipment & Supplies            71.3          13.8
Auto & Truck Manufacturers            79.8            9.03
Drug Retail                            84              -0.2
Household/Personal Care                84.7            10.9
Aerospace & Defense                    86.6              4.6
Food Processing                        99.4            10.8
Computer Hardware                      112.1            21.15
Managed Health Care                    122.5              5.6
Discount Stores                        476.5              16
