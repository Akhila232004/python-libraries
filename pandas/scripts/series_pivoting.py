# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Pivoting Series
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Input Series with MultiIndex (name, subject)
scores_data = [90, 85, 75, 80]
names      = ['Alice', 'Bob', 'Alice', 'Bob']
subjects   = ['Math',  'Math', 'Science', 'Science']

scores_series = pd.Series(scores_data, index=pd.MultiIndex.from_tuples(zip(names, subjects), names=["Name", "Subject"]))

# Basic Pivot (wide table: rows = Name, cols = Subject)
pivot_basic = scores_series.unstack()  # DataFrame
print("Original Series:")
print(scores_series)

print("\nExample 1: Basic Pivot Table:")
print(pivot_basic.reset_index())  # if you want Name as a column

# Pivot with margins (row/column averages)
pivot = scores_series.unstack()  # Name x Subject

# Add a column with the average per Name (row-wise)
pivot["Average"] = pivot.mean(axis=1, numeric_only=True)

# Add a row with the average per Subject (column-wise)
col_means = pivot.mean(axis=0, numeric_only=True)
pivot_with_margins = pd.concat([pivot, col_means.to_frame().T], axis=0)
pivot_with_margins.index = list(pivot.index) + ["Average"]

print("\nExample 2: Pivot Table with Margins (row & column averages):")
print(pivot_with_margins.reset_index().rename(columns={"index": "Name"}))
