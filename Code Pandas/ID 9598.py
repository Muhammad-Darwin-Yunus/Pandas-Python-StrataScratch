>.<

Title: Find non-HS SAT scores
Link: https://platform.stratascratch.com/coding/9598-find-non-hs-sat-scores?code_type=2
Level: Easy

Find SAT scores of students whose high school names do not end with 'HS'.

Data sat_scores:
school: text
teacher: text
student_id: double
sat_writing double
sat_verbal: double
sat_math: double
hrs_studied: double
id: bigint
average_sat: double
love: datetime

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

sat_scores = pd.DataFrame(sat_scores)

sat_scores_school = sat_scores[~sat_scores['school'].str.endswith('HS')]['average_sat']
    
Output:

average_sat
395
360
697
211
563
268
394
242
324
742
686
365
413
785
667
512
407
208
759
458
669
521
220
780
512
246
581
303
512
636
541
457
514
578
539
213
423
598
671
454
741
593
266
560
382
702
242
619
464
344
471
