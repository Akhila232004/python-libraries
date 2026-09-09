# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Pivoting DataFrames
#  Author       : Team Tinitiate
# ==============================================================================



import pandas as pd

# Creating the DataFrame with provided data
data = {'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Subject': ['Math', 'Math', 'Science', 'Science'],
        'Score': [90, 85, 75, 80]}

scores_df = pd.DataFrame(data)

# Basic Pivot Table
pivot_table_basic = scores_df.pivot_table(values='Score', index='Name', columns='Subject', aggfunc='mean')

# Pivot Table with Margins
pivot_table_with_margins = scores_df.pivot_table(values='Score', index='Name', columns='Subject', aggfunc='mean', margins=True, margins_name='Overall')

print("Original DataFrame:")
print(scores_df)
print("\nExample 1: Basic Pivot Table:")
print(pivot_table_basic)
print("\nExample 2: Pivot Table with Margins:")
print(pivot_table_with_margins)
