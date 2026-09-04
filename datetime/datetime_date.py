# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Demonstration of `datetime.date`
#  Author       : Team Tinitiate
# ==============================================================================



from datetime import date

# Get the date
today = date.today()
print(today)

# Breakdown date data
today = date.today()
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())
