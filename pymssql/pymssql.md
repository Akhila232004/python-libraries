![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# `pymssql`
* Python provides several modules to connect to databases such as Oracle, MySQL, SQL Server, PostgreSQL, and more. For MS SQL Server, the most commonly used package is `pymssql`, a third-party Python module.
* With `pymssql`, you can:
    * Establish a connection to MS SQL Server.
    * Execute DDL (Data Definition Language) commands (CREATE, ALTER, DROP).
    * Execute DML (Data Manipulation Language) commands (INSERT, UPDATE, DELETE).
    * Retrieve and process results using SELECT queries.
```bash
# To install 'pymssql' run the following command
python -m pip install pymssql
```

## Connecting to MS SQL Server Database
```python
import pymssql

# Create Connection Object
conn = pymssql.connect(server="127.0.0.1", port="1433", user="sa", password="tinitiate_01", database="tinitiate")
cursor = conn.cursor()



# Executing DDL (Data Definition Language)
try:
    cursor.execute("drop table dbo.ti_test");
except:
    pass;

# Create a table with multiple data types
cursor.execute(" create table dbo.ti_test ( col1 int, col2 varchar(100), col3 date, col4 text );" )

# Alter Table to add primary key
cursor.execute("alter table dbo.ti_test add constraint ti_test_pk primary key (col1);")



# Executing DML (Data Manipulation Language)
# Insert data into the table
cursor.execute("insert into dbo.ti_test values (1, 'Test', now(), 'THIS IS CLOB DATA .........');")
cursor.execute("insert into dbo.ti_test values (2, 'Test2', now(), 'THIS IS CLOB DATA .........');")



# Update data in the table
cursor.execute("update dbo.ti_test set col2 = 'DATA CHANGE' where col1 = 1;")



# Delete data in the table
cursor.execute("delete from dbo.ti_test where col1 = 2;")

cursor.execute("insert into dbo.ti_test values (3, 'Test3', now(), '333 THIS IS CLOB DATA .........');")
cursor.execute("insert into dbo.ti_test values (4, 'Test4', now(), '444 THIS IS CLOB DATA .........');")



# Commit changes
conn.commit()

cursor.execute("insert into dbo.ti_test values (5, 'Test5', now(), '555 THIS IS CLOB DATA .........');")

# To RollBack changes
conn.rollback()



# Executing Data Selection
# Fetch One Row
cursor.execute("select col1,col2,col3,col4 from dbo.ti_test;")

# Prints the Row count of the cursor
print(cursor.rowcount)

# Fetches a Single Row
rowdata = cursor.fetchone()
print(rowdata)

# Reading multiple datatypes and print to screen
cursor.execute("select col1,col2,col3,col4 from dbo.ti_test;")

# Use fetchall() to get the list of row data
for l_col1, l_col2, l_col3, l_col4 in cursor.fetchall():
    print("l_col1: ", l_col1)
    print("l_col2: ", l_col2)
    print("l_col3: ", l_col3)
    print("l_col4: ", l_col4)



# Close the Cursor
cursor.close()

# Close the Connection
conn.close()
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
