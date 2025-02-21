>.<

Title: Find the number of open businesses
Link: https://platform.stratascratch.com/coding/10051-find-the-number-of-open-businesses?code_type=2
Level: Easy

Find the number of open businesses.

Data yelp_business:
address: text
business_id: text
categories: text
city: text
is_open: bigint
latitude: double
longitude: double
name: text
neighborhood: text
postal_code: text
review_count: bigint
stars: double
state: text

>.<

Solution:

# Import your libraries
import pandas as pd

# Start writing code

open_business = pd.DataFrame(yelp_business)

number_open_business = open_business[open_business['is_open']==1]

number_open_business[['business_id','is_open']]

Output:

business_id            |  is_open
G5ERFWvPfHy7IDAUYlWL2A      1
0jDvRJS-z9zdMgOUXgr6rA      1
6HmDqeNNZtHMK0t2glF_gg      1
CX8pfLn7Bk9o2-8yDMp_2w      1
lbxfIXUNUdSRO2t7z2PxPA      1
xxCrRqqICzQyR0Q-iqCrNw      1
WdQP8kl9SzcOdubWz0Rs5g      1
g6KfICYxIFoXnz7KHzQDpw      1
Lhtl6hEr4BaAR4aA3RQDNQ      1
JJWQxF7ljXKVvCxn3ug-CA      1
3rptIkeGoVRdPF4v6omLOg      1
JGvyv9jO8kfEnf4WtnpzfQ      1
dRb2Xq8jorJV6tDCgmaQUg      1
-M9S1wlZTvv6T9EOo5X2Yw      1
-03HVYxkeYWaafEpNJo1SA      1
Wd81DI2DICRtANydqJlFtQ      1
zXY_rBLlE2Kb_D1FZ8bH9g      1
aYSSqa0M5DZHjLT_jK5ezw      1
diH4Pf4mYd1P-zZsQErVTQ      1
m5h7_IeiGaY4Z1ns1y8veQ      1
rkSUOnANSaB3E9qMHhfpcA      1
xhzUfaJ9BTa3EbD0bTeKWQ      1
JbWQtVLQDEOBlvbVWk2OFg      1
J8DxZ7enKZ0aAuF40e3rew      1
zPSPUa9cgl68ydGNZt6gYQ      1
ct1uN_FOIyY1er8iLTsS6w      1
cDpUshHyJHDEc19TSTulJw      1
YjfRCKCTqkcL1yTKPIwDlg      1
4m5g6GUGDN9NqkfA0dk9fA      1
Ett_hy5k5_hI4GvPN9cyHg      1
MYB1ZMspBk1Xc_awp_PtSw      1
FBptd43MkPFZxVLRMz0PFw      1
iQfx6lghJJbrb-fz-toOCQ      1
9O0jWqGnHkBsXMOd-KOl4w      1
z7ns1g4S82kaBdIAC_RMRw      1
VdoNOOcO8HmLHbmxE_3psA      1
D3Tpd4SrPAnZ1PaGVRGBfQ      1
p3My4o49oL_aOY2M2QLu8w      1
Ch7Kx4JPJePFvjpXw0PAVQ      1
CV05rBOr5DdDGvxUZkRFmg      1
wHP1G6mEJJz5nDdA17R78w      1
m1Arqxfo66oyOqPrLTSYzw      1
RtcVbq18T0vNODpGwHzcVQ      1
RWuk_fBzdWc__FBEsPozZw      1
EsE8KTPqAJ2MjJdmuAifRw      1
tqEQd2LD0DeAqkE9tbZ7zA      1
GaSR7qrkR5x0ubKe0av0rQ      1
YiaOpyu4qx0x1nJC_G33TQ      1
owuI8y4A3iiYQlAp-fOmWQ      1
mRDyt98UXamjbSOX9NinlA      1
gazJFJoMqPP_aG76kAWcYw      1
gBEWJ4b2OvUmN4Oh7ju3hw      1
NizoFauSY9EgFKXdz5WoNg      1
QcTTRBfrd0rMzzuCDec_Cw      1
xTW5PkLEdMBs2f2W8RGy0g      1
sU26m6RAkTtaNUjiJUFqRw      1
1MxyFhzNpeIvTQHjtp-bSg      1
yWmGplCGCnQBy9LJFaGa6A      1
ZStsZ_B3RNY6mLNFfpYQfA      1
HJ5GABl8RsLYjiWC9Zf7PQ      1
cTudgI-2jn-GlnZUmULy5Q      1
xl8jk0FbszttHyI_vjozkA      1
nUR_AQd_6Dhpx3sb2T6meg      1
dJGMbloBEtXTAWSQBqS5pw      1
ImIYQbWPsvLVSS0GyVz0og      1
XbtNbyIGaTitIuEgzEBCzg      1
Wvst5nUM1Yd64cdjIPOD6w      1
lTxZFiWEd2NNF4Eh7_mlRg      1
WCMt5LU2NnkmzjKNhTB7UA      1
R6QCy5sVlySKgqvHb-HhTg      1
BXyOtdsnUfGxMYtoM7lIwQ      1
eyU4hQOMAG--PUFK-lihDA      1
d7y2sEZQGTUQIxKJ4fFS-w      1
vV6oNhupyM8gEhjmhqLPjQ      1
l4xrBZAKLXpSR4iprqTw8A      1
ICdzSGuv70gpSk7aqpIrHw      1
wk3wGDfJb1V-ciZpyhoNAA      1
xPy6fq53MdGMxtbvxBD4RA      1  
