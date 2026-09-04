![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# `pymysql`
* Python provides several modules to connect to databases such as Oracle, MySQL, SQL Server, PostgreSQL, and more. For MySQL/MariaDB, the most commonly used package is `pymysql`, a third-party Python module.
* With `pymysql`, you can:
    * Establish a connection to MySQL/MariaDB.
    * Execute DDL (Data Definition Language) commands (CREATE, ALTER, DROP).
    * Execute DML (Data Manipulation Language) commands (INSERT, UPDATE, DELETE).
    * Retrieve and process results using SELECT queries.
```bash
# To install 'pymysql' run the following command
python -m pip install pymysql
```

## Connecting to MySQL/MariaDB Database
```python
import pymysql

# Create Connection Object
conn = pymysql.connect(host='localhost', port=3306, user='my_user_name', passwd='my_password', database='mysql')
cursor = conn.cursor()



# Executing DDL (Data Definition Language)
# Try to Drop the table if it exists
try:
    cursor.execute("drop table ti_test");
except:
    pass;

# Create a table with multiple data types
cursor.execute(" create table ti_test ( col1 int, col2 varchar(100), col3 date, col4 text );" )

# Alter Table to add primary key
cursor.execute("alter table ti_test add constraint ti_test_pk primary key (col1);")



# Executing DML (Data Manipulation Language)
# Insert data into the table
cursor.execute("insert into ti_test values (1, 'Test', curdate(), 'THIS IS CLOB DATA .........');")
cursor.execute("insert into ti_test values (2, 'Test2', curdate(), 'THIS IS CLOB DATA .........');")



# Update data in the table
cursor.execute("update ti_test set col2 = 'DATA CHANGE' where col1 = 1;")



# Delete data in the table
cursor.execute("delete from ti_test where col1 = 2;")

cursor.execute("insert into ti_test values (3, 'Test3', curdate(), '333 THIS IS CLOB DATA .........');")
cursor.execute("insert into ti_test values (4, 'Test4', curdate(), '444 THIS IS CLOB DATA .........');")



# Commit changes
conn.commit()

cursor.execute("insert into ti_test values (5, 'Test5', curdate(), '555 THIS IS CLOB DATA .........');")

# To RollBack changes
conn.rollback()



# Executing Data Selection
# Fetch One Row
cursor.execute("select col1,col2,col3,col4 from ti_test;")

# Prints the Row count of the cursor
print(cursor.rowcount)

# Fetches a Single Row
rowdata = cursor.fetchone()
print(rowdata)

# Reading multiple datatypes and print to screen
cursor.execute("select col1,col2,col3,col4 from ti_test;")

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
