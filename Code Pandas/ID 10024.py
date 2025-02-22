>.<

Title: Wine varieties tasted by 'Roger Voss'
Link: https://platform.stratascratch.com/coding/10024-wine-varieties-tasted-by-roger-voss?code_type=2
Level: Easy

Find wine varieties tasted by 'Roger Voss' and with a value in the 'region_1' column of the dataset.
Output unique variety names only.

Data winemag_p2:
country: text
description: text
designation: text
id: bigint
points: bigint
price: double
province: text
region_1: text
region_2: text
variety: text
winery: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

wine_varieties = pd.DataFrame(winemag_p2)

roger_voss = wine_varieties[wine_varieties['taster_name']=='Roger Voss']

roger_voss_non_null = roger_voss[roger_voss['region_1'].notna()]

roger_voss_duplicat = roger_voss_non_null.drop_duplicates()

roger_voss_duplicat['region_1']

Output:

region_1
Bordeaux
Champagne
Alsace
Bourgogne Hautes Cates de Nuits
Saumur
Savigny-las-Beaune
Touraine
Vouvray
Vin de France
Sancerre
Pouilly-Fuissa
Alto Adige
Margaux
Fronton
Saint-umilion
Gaillac
Bourgogne
