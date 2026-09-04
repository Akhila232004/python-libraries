# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Writing to csv using `csv.DictWriter `
#  Author       : Team Tinitiate
# ==============================================================================



import csv
with open('C:/tinitiate/code/python/tinitiate-python-ebook/python-libraries/csv/data.csv', 'r') as csv_file:  
    # Replace the above path with your csv file path  
    csv_reader = csv.DictReader(csv_file)    
    
    with open('C:/tinitiate/code/python/tinitiate-python-ebook/python-libraries/csv/output_data.csv', 'w') as new_file:        
    # Replace the above path with your csv file path
        fieldnames =['FirstName','LastName','Email','Amount','MaxAmount','Status','Country','Start']

        # csv dict writer method       
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t') 

        # csv method to write the header
        csv_writer.writeheader()
    
        for line in csv_reader:  

            # csv method to write items in a sequence            
            csv_writer.writerow(line)
