# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Demonstration of `strftime`
#  Author       : Team Tinitiate
# ==============================================================================



import datetime

# Convert Date to String
today = datetime.datetime.today()
# format YYYYMMDD
format1 = "%Y%m%d"
# Print Format
s = today.strftime(format1)
print(s)

# Format DD-MON-YYYY
format2 = "%d-%b-%Y"
# Print Format
s = today.strftime(format2)
print(s)


# Format DD-MON-YYYY HH24:MI:SS
format3 = "%d-%b-%Y %H:%M:%S"
# Print Format
s = today.strftime(format3)
print(s)
