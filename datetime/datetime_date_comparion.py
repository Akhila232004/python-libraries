# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Demonstration to compare dates
#  Author       : Team Tinitiate
# ==============================================================================



import datetime

# Comparision
D1_str = "2023-04-01"
D1 = datetime.datetime.strptime(D1_str, "%Y-%m-%d")
print("D1 ",D1)

D2_str = "2023-05-01"
D2 = datetime.datetime.strptime(D2_str, "%Y-%m-%d")
print("D2 ",D2)


if(D1 > D2):
    print(D1," is Greater than ",D2)
else:
    print(D1," is Less than ",D2)
