# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Demonstration to get difference between dates
#  Author       : Team Tinitiate
# ==============================================================================



import datetime

D1_str = "2023-04-01"
D1 = datetime.datetime.strptime(D1_str, "%Y-%m-%d")
print("D1 ",D1)

D2_str = "2023-05-01"
D2 = datetime.datetime.strptime(D2_str, "%Y-%m-%d")
print("D2 ",D2)

# Difference between TWO Dates in DAYS, Difference in Hours, Minutes and Seconds
diff_in_days = abs(D2 - D1).days
print(diff_in_days)

# Do a Diff between Dates
date_diff = D2 - D1

# Get Diff in Hours using the total_seconds()/3600
diff_in_hours = date_diff.total_seconds() / 3600
print(diff_in_hours)

# Get Diff in Minutes using the total_seconds()/60
diff_in_minutes = date_diff.total_seconds() / 60
print(diff_in_minutes)

# Get Diff in Seconds using the total_seconds()
diff_in_seconds = date_diff.total_seconds() / 60
print(diff_in_seconds)
