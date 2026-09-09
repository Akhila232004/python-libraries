# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Connecting to a MySQL/MariaDB Database
#  Author       : Team Tinitiate
# ==============================================================================



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
