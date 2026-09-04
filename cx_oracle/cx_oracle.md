![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# `cx_Oracle`
* Python provides several modules to connect to databases such as Oracle, MySQL, SQL Server, PostgreSQL, and more. For Oracle, the most commonly used package is `cx_Oracle`, a third-party Python module.
* With `cx_Oracle`, you can:
    * Establish a connection to Oracle.
    * Execute DDL (Data Definition Language) commands (CREATE, ALTER, DROP).
    * Execute DML (Data Manipulation Language) commands (INSERT, UPDATE, DELETE).
    * Retrieve and process results using SELECT queries.
* `cx_Oracle` module needs to be downloaded separately to avoid errors like: "ImportError: DLL load failed: %1 is not a valid Win32 application." and also the Oracle Client.
* Make sure the Oracle Client, Python and the `cx_Oracle` module are of the same bit version 32 all or 64 all, this is very important for this to work.
```bash
# To install 'cx_Oracle' run the following command
python -m pip install cx_Oracle
```

## Connecting to an Oracle Database
```python
import cx_Oracle

# Connect
# Replace with your credentials and connection string
# Create a connection object, usage string
# USER/PASSWORD@INSTANCE-NAME-AS-IS-IN-TNSNAMES.ORA
connection = cx_Oracle.connect('BNCOM_STG/BNCOM_STG111@eordhistd')
# Prints Oracle Version Details
print("Oracle Version:", connection.version)
# pPrints Current Schema name
print("Connected User:", connection.username)
# Note there are also startup/shutdown commands supported by cx_oracle



# Executing DDL (Data Definition Language)
cursor = connection.cursor()

# Create
print("Create a table ti_test, with multiple datatypes")
cursor.execute("CREATE TABLE ti_test(col1 INT, col2 VARCHAR2(100), col3 DATE, col4 CLOB)")
# Alter
print("Alter table ti_test, add primary key")
cursor.execute("ALTER TABLE ti_test ADD CONSTRAINT ti_test_pk PRIMARY KEY (col1)")



# Executing DML (Data Manipulation Language)
# Insert rows
cursor.execute("INSERT INTO ti_test VALUES (1, 'Test1', SYSDATE, 'THIS IS CLOB DATA .....')")
cursor.execute("INSERT INTO ti_test VALUES (2, 'Test2', SYSDATE, 'THIS IS CLOB DATA .....')")

# Update a row
cursor.execute("UPDATE ti_test SET col2 = 'DATA CHANGE' WHERE col1 = 1")

# Delete a row
cursor.execute("DELETE FROM ti_test WHERE col1 = 2")

# Commit changes
connection.commit()
print("DML operations committed.")



# Executing DQL (Data Query Language)
# Read
cursor.execute("SELECT col1, col2, col3, col4 FROM ti_test")
for col1, col2, col3, col4 in cursor.fetchall():
    print("col1:", col1)
    print("col2:", col2)
    print("col3:", col3)
    print("col4:", col4)



# Cleanup
print("Dropping table ti_test...")
cursor.execute("DROP TABLE ti_test")

# Close the cursor object
cursor.close()
print("Cursor closed.")

# Close the connection once completed
connection.close()
print("Connection closed.")
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
