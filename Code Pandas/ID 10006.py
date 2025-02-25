>.<

Title: Find the average distance traveled in each hour
Link: https://platform.stratascratch.com/coding/10006-find-the-average-distance-traveled-in-each-hour?code_type=2
Level: Easy

Find the average distance traveled in each hour.
Output the hour along with the corresponding average traveled distance.
Sort records by the hour in ascending order.

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

average_distance = pd.DataFrame(lyft_rides)

average_distance_traveled = average_distance.groupby('hour')['travel_distance'].mean().reset_index()

average_distance_traveled_fix = pd.DataFrame({'hour':average_distance_traveled['hour'],'avg_travel_distance':average_distance_traveled['travel_distance']})

Output:

hour  |  avg_travel_distance
0            20.53
1            20.79
2            21.33
3            20.08
4            22.9
5            19.44
6            20.04
7            22.22
8            18.39
9            18.94
10            19.59
11            19.03
12            21.83
13            19.65
14            18.69
15            21.37
16            23.74
17            19.56
18            19.54
19            18.41
20            22.24
21            21.82
22            20.76
23            23.6
