# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Billion Counter Sequential Execution
#  Author       : Team Tinitiate
# ==============================================================================



import datetime

today = datetime.datetime.now()
print("Start",today.strftime("%d-%b-%Y %H:%M:%S"))

a = 0
for c in range(1,1000000001):
    a = a+1

print(a)

today = datetime.datetime.now()
print("End",today.strftime("%d-%b-%Y %H:%M:%S"))
# OUTPUT:
# Start 08-Sep-2025 12:55:07
# 1000000000
# End 08-Sep-2025 12:56:24
