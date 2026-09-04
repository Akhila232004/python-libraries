# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Writing to csv using `csv.writer`
#  Author       : Team Tinitiate
# ==============================================================================



import csv
with open('C:/tinitiate/code/python/tinitiate-python-ebook/python-libraries/csv/data.csv', 'r') as csv_file:
    # Replace the above path with your csv file path
    csv_reader = csv.reader(csv_file)    
    
    with open('C:/tinitiate/code/python/tinitiate-python-ebook/python-libraries/csv/output_data.csv', 'w') as new_file:
    # Replace the above path with your csv file path

        # csv writer method
        csv_writer = csv.writer(new_file,delimiter='\t') 
    
        for line in csv_reader:    

            # csv method to write items in a sequence           
            csv_writer.writerow(line)
