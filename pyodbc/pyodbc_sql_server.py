# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Connecting to a SQL Server Database
#  Author       : Team Tinitiate
# ==============================================================================



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
