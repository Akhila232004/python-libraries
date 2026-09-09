# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : `Timestamp` and `DatetimeIndex ` in Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd
    
# Creating a Series with Timestamps as index
timestamps = pd.to_datetime(['2023-08-15 10:30:00', '2023-08-15 15:45:00'])
values = [100, 150]
    
sales_series = pd.Series(values, index=timestamps)
    
print("Sales Series with Timestamp Index:")
print(sales_series)
