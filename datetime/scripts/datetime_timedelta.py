# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : `timedelta` demonstration for Add Days, Hours, Minutes, Seconds to a date
#  Author       : Team Tinitiate
# ==============================================================================



import datetime
from datetime import timedelta  

Date_str = '2023-04-01 12:30:22'
formatADT = "%Y-%m-%d %H:%M:%S"

D3 = datetime.datetime.strptime(Date_str, formatADT)
print("D3 DATE-TIME",D3)

# Add 5 Days to D3 using timedelta
# ================================
newDate = D3 + timedelta(days=5)
s = newDate.strftime(formatADT)
print('D3 + 5 Days', s)

# Add 5 Hours to D3 using timedelta
# =================================
newDate = D3 + timedelta(hours=5)
s = newDate.strftime(formatADT)
print('D3 + 5 Hours', s)

# Add 5 Minutes to D3 using timedelta
# ===================================
newDate = D3 + timedelta(minutes=5)
s = newDate.strftime(formatADT)
print('D3 + 5 Minutes', s)

# Add 5 Seconds to D3 using timedelta
# ===================================
newDate = D3 + timedelta(seconds=5)
s = newDate.strftime(formatADT)
print('D3 + 5 Seconds', s)

# Subtract 5 Days to D3 using timedelta
# ======================================
newDate = D3 + timedelta(days=-5)
s = newDate.strftime(formatADT)
print('D3 - 5 Days', s)
