>.<

Title: List all companies working in the financial sector with headquarters in Europe or Asia
Link: https://platform.stratascratch.com/coding/9662-list-all-companies-working-in-the-financial-sector-with-headquarters-in-europe-or-asia?code_type=2
Level: Easy

List all companies working in the financial sector with headquarters in Europe or Asia.

Data forbes_global_2010_2014:
assets: double
company: text
continent: text
country: text
industry: text
marketvalue: double
profits: double
rank: bigint
sales: double
sector: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

forbes_global = pd.DataFrame(forbes_global_2010_2014)

forbes_global_filter = forbes_global[(forbes_global['sector']=='Financials') & (forbes_global['continent']=='Asia') | (forbes_global['continent']=='Europe')]

forbes_global_company = forbes_global_filter.drop_duplicates('company')

forbes_global_company['company']
    
Output:

company
ICBC
China Construction Bank
Agricultural Bank of China
Bank of China
Royal Dutch Shell
HSBC Holdings
BP
Volkswagen Group
BNP Paribas
Total
Allianz
Daimler
AXA Group
Nestle
Mitsubishi UFJ Financial
Vodafone
Eni
Banco Santander
BMW Group
EDF
Statoil
Siemens
Novartis
Sumitomo Mitsui Financial
Sberbank
Ping An Insurance Group
Anheuser-Busch InBev
Bank of Communications
China Life Insurance
TelefÃ³nica
Enel
BASF
UBS
Zurich Insurance Group
Sanofi
Credit Agricole
Roche Holding
Munich Re
ING Group
Barclays
LifeShield Assurance Group
EnergyPro Electric Utilities
