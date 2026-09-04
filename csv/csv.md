![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# CSV Module
* Python `csv` module provides a simple way to read and write Comma-Separated Values (CSV) files. 
* A CSV file is a plain text file that contains tabular data, where each row is a record and each column is a field. The fields are separated by commas.
* The `csv` module provides these main classes for reading and writing CSV files:

  * `csv.reader`: This class is used to read CSV files. It returns a generator that yields each row of the file as a list of strings.

  * `csv.writer`: This class is used to write CSV files. It takes a file object as its argument and writes each row of the iterable as a list of strings to the file, separated by commas.

  * `csv.DictReader`: This class takes a file object as its argument and returns a generator that yields each row of the file as a dictionary. 

  * `csv.DictWriter`: This class takes a file object and a list of column names as its arguments and writes each row of the iterable as a dictionary to the file.

## Reading a csv file using `csv.reader`
* The `csv.reader` class takes a file object as its argument and returns a generator that yields each row of the file as a list of strings.
```python
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
```

## Writing to csv using `csv.writer`
* The `csv.writer` class takes a file object as its argument and writes each row of the iterable as a list of strings to the file, separated by commas.
```python
import csv
with open('C:/tinitiate/code/python/csv/data.csv', 'r') as csv_file:
    # Replace the above path with your csv file path
    csv_reader = csv.reader(csv_file)    
    
    with open('C:/tinitiate/code/python/csv/output_data.csv', 'w') as new_file:
    # Replace the above path with your csv file path

        # csv writer method
        csv_writer = csv.writer(new_file,delimiter='\t') 
    
        for line in csv_reader:    

            # csv method to write items in a sequence           
            csv_writer.writerow(line)
```

## Reading a csv file using `csv.DictReader`
* The `csv.DictReader` class takes a file object as its argument and returns a generator that yields each row of the file as a dictionary where keys are column headers. Makes accessing data by column name which make it easy and more readable.
```python
import csv
with open('C:/tinitiate/code/python/csv/data.csv', 'r') as csv_file:
    # Replace the above path with your csv file path
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        # output of the reader is dictionary
        print(line)       
        
        # Getting specific column from the list in this case email.
        print(line['LastName'])
```

## Writing to csv using `csv.DictWriter `
* The `csv.DictWriter` class takes a file object and a list of column names as its arguments and writes each row of the iterable as a dictionary to the file.
```python
import csv
with open('C:/tinitiate/code/python/csv/data.csv', 'r') as csv_file:  
    # Replace the above path with your csv file path  
    csv_reader = csv.DictReader(csv_file)    
    
    with open('C:/tinitiate/code/python/csv/output_data.csv', 'w') as new_file:        
    # Replace the above path with your csv file path
        fieldnames =['FirstName','LastName','Email','Amount','MaxAmount','Status','Country','Start']

        # csv dict writer method       
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t') 

        # csv method to write the header
        csv_writer.writeheader()
    
        for line in csv_reader:  

            # csv method to write items in a sequence            
            csv_writer.writerow(line)
```

## Writing to csv only specific columns using `csv.DictWriter`
```python
import csv
with open('C:/tinitiate/code/python/csv/data.csv', 'r') as csv_file:    
    # Replace the above path with your csv file path
    csv_reader = csv.DictReader(csv_file)    
    
    with open('C:/tinitiate/code/python/tinitiate-python-ebook/python-libraries/csv/output_data.csv', 'w') as new_file:  
    # Replace the above path with your csv file path      
        fieldnames =['FirstName','LastName','Email','Amount','Status','Country','Start']
        
        # fieldnames=fieldnames,
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t') 
    
        for line in csv_reader:    
            del line['MaxAmount']          
            csv_writer.writerow(line)
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|