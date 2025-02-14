>.<

Title: Number Of Acquisitions
Link: https://platform.stratascratch.com/coding/10162-number-of-acquisitions?code_type=2
Level: Easy

Find the number of acquisitions that occurred in each quarter of each year.
Output the acquired quarter in YYYY-Qq format along with the number of acquisitions and order results by the quarters with the highest number of acquisitions first.

Data crunchbase_acquisitions:
company_permalink: varchar
company_name: varchar
company_category_code: varchar
company_country_code: varchar
company_state_code: varchar
company_region: varchar
company_city: varchar
acquirer_permalink: varchar
acquirer_name: varchar
acquirer_category_code: varchar
acquirer_country_code: varchar
acquirer_state_code: varchar
acquirer_region: varchar
acquirer_city: varchar
acquired_at: datetime
acquired_month: datetime
acquired_quarter: datetime
acquired_year: int
price_amount: float
price_currency_code: varchar
id: int

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

number_acquisitions = pd.DataFrame(crunchbase_acquisitions)

number_acquisitions = number_acquisitions.groupby('acquired_quarter')['id'].count().reset_index()

number_acquisitions = number_acquisitions.rename(columns={'id':'number_acquisitions'})

number_acquisitions_sort = number_acquisitions.sort_values(by='number_acquisitions',ascending=False)

number_acquisitions_sort

Output:

acquired_quarter | number_acquisitions
2013-Q4                  337
2011-Q3                  319
2011-Q1                  317
2010-Q1                  308
2013-Q3                  297
2011-Q2                  291
2010-Q2                  291
2013-Q2                  270
2010-Q4                  268
2012-Q1                  262
2009-Q4                  260
2011-Q4                  258
2010-Q3                  255
2008-Q3                  253
2012-Q3                  239
2012-Q2                  233
2012-Q4                  231
2013-Q1                  222
2008-Q2                  213
2009-Q1                  205
2009-Q3                  188
2008-Q4                  182
2009-Q2                  178
2008-Q1                  135
2014-Q1                  134
2007-Q2                  83
2007-Q4                  79
2007-Q1                  78
2007-Q3                  69
2006-Q1                  62
2006-Q2                  44
2006-Q4                  43
2006-Q3                  42
2005-Q1                  41
2005-Q3                  37
2004-Q1                  35
2005-Q4                  32
2005-Q2                  28
2004-Q4                  27
1999-Q2                  26
2000-Q1                  21
1999-Q4                  20
2004-Q3                  17
2001-Q1                  17
2003-Q3                  16
2000-Q3                  15
2004-Q2                  15
2003-Q1                  14
1999-Q1                  13
1999-Q3                  13
2002-Q3                  13
2000-Q2                  13
2003-Q4                  12
2001-Q2                  12
2002-Q2                  10
2001-Q3                  9
2003-Q2                  9
1997-Q2                  8
1998-Q4                  8
1997-Q3                  8
1997-Q4                  7
1998-Q1                  7
2000-Q4                  7
2002-Q1                  7
2002-Q4                  7
1998-Q3                  6
1998-Q2                  6
1994-Q4                  6
1995-Q3                  5
1995-Q1                  5
1987-Q2                  4
1996-Q1                  4
1996-Q2                  4
1997-Q1                  4
1995-Q4                  4
1993-Q2                  3
1996-Q4                  3
1993-Q3                  3
2001-Q4                  3
1992-Q2                  2
1995-Q2                  2
1991-Q1                  2
1996-Q3                  2
1982-Q3                  1
1966-Q1                  1
1988-Q3                  1
1988-Q1                  1
1994-Q3                  1
1989-Q1                  1
1984-Q2                  1
1991-Q3                  1
1989-Q2                  1
1991-Q4                  1
1974-Q3                  1
1992-Q1                  1
1993-Q1                  1
1980-Q1                  1
