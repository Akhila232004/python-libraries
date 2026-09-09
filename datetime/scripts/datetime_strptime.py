# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Demonstration of `strptime`
#  Author       : Team Tinitiate
# ==============================================================================



import datetime

l_date_time_string = "2023-04-01"
l_datetime = datetime.datetime.strptime(l_date_time_string, "%Y-%m-%d")
print("l_datetime:", l_datetime)

l_date_string1 = "2023-04-01 12:30:45"
format4        = "%Y-%m-%d %H:%M:%S"
t1 = datetime.datetime.strptime(l_date_string1, format4)
print("t1:", t1)

# Get today's datetime in format4
today = datetime.datetime.now()
s = today.strftime(format4)
print("s:", s)

# Convert string s back to datetime.date
t2 = datetime.datetime.strptime(s, format4).date()
print("t2:", t2)
