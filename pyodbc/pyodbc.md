![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# `pyodbc`
* PYTHON provides mechanisms to connect to various databases and perform database operations like create, insert, select.
* There are many Open and Commercial Database connectivity modules available for download.
* Almost all popular databases have Modules to connect to python.
* `pyodbc` is a open source module within the Python programming language that acts as a library for connecting to and interacting with ODBC (Open Database Connectivity) databases.
* `pyodbc` is a lightweight, fast ODBC bridge for Python. It lets you talk to SQL Server, MySQL/MariaDB, PostgreSQL, Oracle, SQLite, and any ODBC-capable DB using a single API.
```bash
# To install 'pyodbc' run the following command
python -m pip install pyodbc
```

## When to use `pyodbc`
* You want one library that can connect to many databases.
* Your organization already uses ODBC drivers/DSNs.
* You need fast inserts (supports `fast_executemany`) and parameterized SQL.

## You need a native ODBC driver for your database
| Database      | Driver (Windows)              | Driver (Linux/Mac)     | Notes                                      |
| ------------- | ----------------------------- | ---------------------- | ------------------------------------------ |
| SQL Server    | ODBC Driver 18 for SQL Server | `msodbcsql18`          | Prefer v18; supports TLS/Always Encrypted. |
| MySQL/MariaDB | MySQL ODBC 8.x                | `mysql-connector-odbc` | SHA2 auth often needed.                    |
| PostgreSQL    | psqlODBC                      | `psqlodbc`             | Usually in distro repos.                   |
| SQLite        | Built-in ODBC                 | `libsqliteodbc`        | Or use `sqlite3` module as an alternative. |
* If you don't have a native driver, you can install from vendor pages.

## Connecting to a SQL Server Database
```python
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;DATABASE=DemoDB;UID=sa;PWD=StrongPassw0rd!;"
    "TrustServerCertificate=Yes;"
)
cur = conn.cursor()

# DDL: Create table
cur.execute("""
IF OBJECT_ID('dbo.pyodbc_demo') IS NOT NULL DROP TABLE dbo.pyodbc_demo;
CREATE TABLE dbo.pyodbc_demo (
  id   INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  created_at DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
""")
conn.commit()

# INSERT (parameterized)
cur.execute("INSERT INTO dbo.pyodbc_demo (id, name) VALUES (?, ?)", 1, "Alice")
cur.execute("INSERT INTO dbo.pyodbc_demo (id, name) VALUES (?, ?)", 2, "Bob")
conn.commit()

# UPDATE
cur.execute("UPDATE dbo.pyodbc_demo SET name=? WHERE id=?", "Bobby", 2)
conn.commit()

# SELECT
cur.execute("SELECT id, name, created_at FROM dbo.pyodbc_demo ORDER BY id")
for row in cur.fetchall():
    print(row.id, row.name, row.created_at)

# DELETE
cur.execute("DELETE FROM dbo.pyodbc_demo WHERE id=?", 1)
conn.commit()

cur.close()
conn.close()
```

## Connecting to a MySQL/MariaDB Database
```python
import pyodbc

conn = pyodbc.connect(
    "DRIVER={MySQL ODBC 8.0 ANSI Driver};"
    "SERVER=localhost;DATABASE=testdb;UID=root;PWD=secret;PORT=3306;"
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS pyodbc_demo (id INT PRIMARY KEY, name VARCHAR(50))")
cur.execute("INSERT INTO pyodbc_demo (id, name) VALUES (?, ?)", 1, "Alice")
conn.commit()
cur.close(); conn.close()
```

## Connecting to a PostgreSQL Database
```python
import pyodbc

conn = pyodbc.connect(
    "DRIVER={PostgreSQL Unicode};"
    "SERVER=localhost;PORT=5432;DATABASE=testdb;UID=postgres;PWD=secret;"
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS pyodbc_demo (id INT PRIMARY KEY, name TEXT)")
cur.execute("INSERT INTO pyodbc_demo (id, name) VALUES (?, ?)", 1, "Alice")
conn.commit()
cur.close(); conn.close()
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
