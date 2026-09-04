# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Reading a csv file using `csv.DictReader`
#  Author       : Team Tinitiate
# ==============================================================================



import csv
with open('C:/tinitiate/code/python/tinitiate-python-ebook/python-libraries/csv/data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # output of the reader is dictionary
        print(line)       
        
        # Getting specific column from the list in this case email.
        print(line['LastName'])
