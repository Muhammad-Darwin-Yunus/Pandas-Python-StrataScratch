>.<

Title: Total Order Per Status Per Service
Link: https://platform.stratascratch.com/coding/2049-total-order-per-status-per-service?code_type=2
Level: Easy

Uber is interested in identifying gaps in their business.
Calculate the count of orders for each status of each service.
Your output should include the service name, status of the order, and the number of orders.

Data uber_orders:
monetary_value: double
number_of_orders: bigint
order_date: date
service_name: text
status_of_order: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
uber_orders = pd.DataFrame(uber_orders)

uber_orders_group = uber_orders.groupby(['service_name','status_of_order'])['number_of_orders'].sum().reset_index(name='total_of_orders')
    
Output:

service_name	status_of_order	total_of_orders
Uber_BOX	Cancelled	29970
Uber_CLEAN	Cancelled	1740
Uber_FOOD	Cancelled	2033930
Uber_GLAM	Cancelled	1270
Uber_KILAT	Cancelled	1050
Uber_MART	Cancelled	85700
Uber_MASSAGE	Cancelled	7330
Uber_RIDE	Cancelled	5469180
Uber_SEND	Cancelled	485160
Uber_SHOP	Cancelled	660540
Uber_TIX	Cancelled	23120
Uber_BOX	Completed	65030
Uber_CLEAN	Completed	14510
Uber_FOOD	Completed	6715000
Uber_GLAM	Completed	7630
Uber_KILAT	Completed	17340
Uber_MART	Completed	196430
Uber_MASSAGE	Completed	42610
Uber_RIDE	Completed	30726460
Uber_SEND	Completed	3107340
Uber_SHOP	Completed	1365020
Uber_TIX	Completed	5970
Uber_TIX	Failed/Timeout	4370
Uber_BOX	No Driver Found	3510
Uber_CLEAN	No Driver Found	610
Uber_FOOD	No Driver Found	39260
Uber_GLAM	No Driver Found	2060
Uber_MART	No Driver Found	410
Uber_MASSAGE	No Driver Found	3120
Uber_RIDE	No Driver Found	1471780
Uber_SEND	No Driver Found	112160
Uber_SHOP	No Driver Found	27200
Uber_FOOD	Other	1670
Uber_RIDE	Other	5200
Uber_SHOP	Other	150
Uber_SEND	Other	250
Uber_MART	Other	0
Uber_KILAT	Other	0
Uber_MASSAGE	Other	410
Uber_KILAT	No Driver Found	1380
Uber_TIX	Other	0
Uber_CLEAN	Other	670
Uber_GLAM	Other	40
Uber_BOX	Other	0
