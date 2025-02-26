>.<

Title: Find all Lyft rides which happened on rainy days before noon
Link: https://platform.stratascratch.com/coding/10004-find-all-lyft-rides-which-happened-on-rainy-days-before-noon?code_type=3
Level: Easy

Find all Lyft rides which happened on rainy days before noon.

Data lyft_rides:
gasoline_cost: double
hour: bigint
index: bigint
travel_distance: double
weather: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

rainy = pd.DataFrame(lyft_rides)

before_noon = rainy[(rainy['hour']>12) & (rainy['weather']=='rainy')]
    
Output:

index  |  weather  |  hour  |  travel_distance  |  gasoline_cost
10        rainy      17            27.76                1.68
13        rainy      21            29.57                0.96
19        rainy      16            30.46                1.26
25        rainy      21            15.37                0.98
29        rainy      15            20.05                0.98
30        rainy      14            26.14                1.78
33        rainy      13            18.44                1.11
34        rainy      13            14.4                  0.69
46        rainy      20            22.13                1.13
47        rainy      15            28.04                0.99
49        rainy      18            29.1                  0.92
54        rainy      22            23.5                  1.32
55        rainy      18            16.1                  1.07
61        rainy      19            8.79                  0.73
63        rainy      16            30.8                  1.12
64        rainy      16            25.02                  1.53
69        rainy      23            35.47                  1.59
73        rainy      16            28.99                  1.26
77        rainy      14            16.01                  1.24
79        rainy      17            17.32                  1.27
84        rainy      14            25.61                  0.78
85        rainy      23            18.65                  1.18
102        rainy      19            13.51                  0.93
106        rainy      21	          12.75                  0.93
108        rainy      21            10.12                  1.09
126        rainy      22            24.06                  1.32
128        rainy      20            18.5                    1.18
133        rainy      15            20.38                    0.71
137        rainy      18            14.16                  1.28
141        rainy      18            22.07                  1.39
152        rainy      15            11.8                    1.04
159        rainy      20            21.66                   0.5
160        rainy      14            15.19                  1.24
172        rainy      18            24.27                  1.38
174        rainy      17            25.67                  1.69
177        rainy      17            15.42                  1.24
180        rainy      20            27.28                  1.18
192        rainy      16            25.83                  1.22
216        rainy      14            24.08                  1.28
217        rainy      15            22.7                    1.48
224        rainy      20            30.52                  1.22
225        rainy      18            21.48                  1.34
232        rainy      20            23.78                  1.16
233        rainy      19            22.18                  0.87
237        rainy      21            28.18                  1.26
241        rainy      19            15.13                  1.89
245        rainy      15            20.79                  1.56
247        rainy      21            18.73                  1.34
253        rainy      16            27.48                  1.17
259        rainy      14            22.26                  1
270        rainy      22            18.25                  1.3
277        rainy      18            13.12                  1
286        rainy      14            28.32                  1.29
290        rainy      16            29.54                  1.09
309        rainy      13            27.63                  1.92
320        rainy      19            28                      1.83
329        rainy      14            23.39                  0.91
330        rainy      22            21.21                  1.48
335        rainy      17            22.37                  1.25
336        rainy      15            18.21                  1.44
342        rainy      22            16.93                  1.43
343        rainy      20            25.94                  1.66
357        rainy      13            21                      1.04
362        rainy      21            20.94                  0.49
369        rainy      13            18.12                  1.27
373        rainy      18            14.08                  1.5
374        rainy      15            21.04                  1.38
387        rainy      23            25.8                    1.14
388        rainy      15            22.2                    0.78
389        rainy      13            19.5                    1.48
391        rainy      19            22.01                    1.62
407        rainy      14            13.48                    1.59
412        rainy      16            24.85                    0.94
417        rainy      21            22.25                    1.14
422        rainy      14            21.78                    1.07
427        rainy      17            20.7                     1.35
430        rainy      15            25.81                    0.97
442        rainy      18            7.93                      1.16
450        rainy      18            14.29                    1.12
455        rainy      21            21.35                    0.48
457        rainy      17            15.65                    1.52
461        rainy      17            17.97                    1.62
467        rainy      16            21.46                    1.19
471        rainy      19            8.86                      1.19
473        rainy      20            29.56                    0.73
485        rainy      18            29.82                    1.36
488        rainy      14            19.32                    0.81
490        rainy      15            22.15                    0.77
