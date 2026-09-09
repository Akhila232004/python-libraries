# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Connecting to a PostgreSQL Database
#  Author       : Team Tinitiate
# ==============================================================================



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
