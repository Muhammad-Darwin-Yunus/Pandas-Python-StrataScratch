>.<

Title: Find the average number of searches from each user
Link: https://platform.stratascratch.com/coding/9640-find-the-average-number-of-searches-from-each-user?code_type=2
Level: Easy

Find the average number of searches made by each user and present the result with their corresponding user id.

Data airbnb_searches:
ds: date
id_user: text
ds_checkin: date
ds_checkout: date
n_searches: bigint
n_nights: double
n_guests_min: bigint
n_guests_max: bigint
origin_country: text
filter_price_min: double
filter_price_max: double
filter_room_types: text
filter_neighborhoods: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code
airbnb_searches = pd.DataFrame(airbnb_searches)

airbnb_searches_id_user = airbnb_searches.groupby('id_user')['n_searches'].mean().reset_index(name='average_searches')
    
Output:

id_user                              |  average_searches
67aece73-e112-4e9e-9e05-8a2a94b003b9	7.67
6cbb33d1-6ecc-4f74-8b6a-a43d07d484b6	16
aa9cf5bf-5667-4212-8018-1cb8beee530e	17
3e6c2466-74fe-44c0-a6f3-dda79755d30a	6
a09bf912-b21d-4859-b194-8512c30695f6	6.8
0f4ea370-702c-4f08-a00d-98e67c2a3574	19.67
b2fda15a-89bb-4e6e-ae81-8b21598e2482	15.5
b6a8b1f9-5b40-4edd-91f3-ee522b0f9e5b	12.33
86b39b70-965b-479d-a0b0-719b195acea2	5.25
a9f7ffb1-4970-492b-b448-4bd9d0fbeef3	6
fad1a097-a511-4f44-a603-6a271c1f159e	11
d328a4a0-df5f-4851-a864-a8845b45c1e0	7.67
eda96881-7b23-413a-9f6f-b45dc9fe2a5b	57.5
126ed661-fa20-4041-ac16-ec118bbcce3b	24
598f8459-96f6-4400-8bce-1474757dd589	16
02f0a750-34da-4268-94e8-f1a371f0460e	38.43
37a63847-b09a-4f32-81a5-97cfb8e84c6d	179
72f07b78-99e1-46ac-8452-19dd2053eca3	7
2889fccc-37ab-4a66-8d64-41b31314c7fc	79
0a8e121b-c09c-4de1-abcc-81bce87de29e	66
6a8cf97f-8a77-4b55-b79a-b560bca414a4	1
bb490ede-8a70-4d61-a2e8-625855a393e2	3
6c541a87-d864-4de8-ae05-70ae57b50976	11
1a66fe1c-fea6-4ec6-96c4-3ea3e0c7815e	52
bd8f3dd6-fecc-479a-a88f-1d0049600e9f	13.5
ca6a9321-d7f9-42e9-aeb1-5d1832034da0	12.25
bdaf2e68-86dd-40d9-a5a1-9cc95ea25d91	73
f4602827-8672-4545-8887-43702f8c7ecc	20
e764ddb5-126e-4474-8e4e-4bdc330b51d1	10.5
f5ba8f82-682e-4ec9-9c6e-cedc2cd628ca	3
1759c05e-f12a-4eaa-8059-3bcaca443c88	32
f54989cf-459b-409d-be6a-9534a53cc4a9	53.5
ea445eea-3fac-4edd-b1d6-569f57f6abe4	46
882f3764-05cc-436a-b23b-93fea22ea847	1
845e3c1d-6c06-4ef2-ade5-7eecefb56fbe	14.67
94139517-e7e9-4afb-8b5d-bb6f306bf751	16
5ed478e0-eae9-4537-826a-04ec779c1fd2	8.5
ebe81cf8-6037-43f2-81d2-fd386f5da74f	70.5
be8a5e0c-e3fb-4517-a799-e1ed8a05b6e6	27
b3e35a8f-5503-4d78-adb8-7693097dfca7	29
6133fb99-2391-4d4b-a077-bae40581f925	8
2acf0e64-9da0-47c9-b0f9-1eceab379f84	4.67
996d1871-8986-481b-8bbf-1a1420c68c90	7.5
679d857b-08b8-4748-b703-86735aa42296	14.5
5dacf820-a573-4ce2-9fd8-0d7ed979b822	14
70180687-5888-4946-9578-83ab678cb997	28
6cb23070-821b-467d-b4d0-af04645a0703	14
25cfc206-89aa-4e63-b2f4-3cbb8631d9fb	52.5
3c3ec192-acd7-4c91-8e82-18cff7d859ec	12
176a2fb8-1de3-483a-92a3-34a826a91f5a	12
9a45a950-b4f7-4f16-abe6-f9286abf2641	10
d61d88ae-7910-4832-8116-aab4603ab3b0	10
e3cdd90a-8097-4220-9722-2b914d761a84	3
18d343e3-0ef0-4bb7-8cd9-b83d3fbbb82f	3
62d09c95-c3d2-44e6-9081-a3485618227d	88
8375dde4-0de9-402c-8833-2127c1504601	11
9e5e2865-f257-4d19-9f79-9388ae925ad7	37
d528e24b-7c1f-446f-9bb0-a4ecb77c3acd	81
b8831610-31f2-4c58-8ada-63b3601ca476	7.5
b11cd744-101d-409b-9a55-7e151f2e79d5	109
924f864f-db83-4945-9a65-cf42a657ca68	6
e0d259e6-1b67-4964-a6dc-e8a8c69d3e01	2
7e309181-e61e-426b-baef-dd031d5660d3	7
4995debc-b753-4401-b556-a2bcbb897eba	13
a03f86ca-5c44-4e66-8695-71c380cfc48b	8
c0075f4f-0cb0-489b-9f12-bf1dff573488	17
