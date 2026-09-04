# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Reading a csv file using `csv.reader `
#  Author       : Team Tinitiate
# ==============================================================================



import csv

with open('C:/tinitiate/code/python/csv/data.csv', 'r') as csv_file:
    # Replace the above path with your csv file path
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
        
    # Ignore Headers or first line of the data
    next(csv_reader)
    
    for line in csv_reader:

        # output of the reader is list
        print(line)

        # Getting specific column from the list in this case email
        print(line[2])
