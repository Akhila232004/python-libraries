# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using the pool
#  Author       : Team Tinitiate
# ==============================================================================



import mysql.connector
from mysql.connector.errors import PoolError
import connpool   # importing this creates the pool
# We’ll also use the helper:
# connpool.get_conn(retries=..., wait_seconds=...)

# Borrow two connections, so the pool has only 1 slot left (POOL_SIZE is 3)
db2 = mysql.connector.connect(pool_name=connpool.POOL_NAME)
print("Connection db2:", db2.connection_id)

db3 = mysql.connector.connect(pool_name=connpool.POOL_NAME)
print("Connection db3:", db3.connection_id)

# Try to borrow a 4th connection: with POOL_SIZE=3, this will fail
# unless we release one (db2/db3/db1). Demonstrate both behaviors.

print("\n--- Attempting to get db4 while pool is full ---")
try:
    # This will attempt and retry internally (see connpool.get_conn)
    db4 = connpool.get_conn(retries=2, wait_seconds=1)
    print("Unexpected: acquired db4:", db4.connection_id)
except PoolError:
    print("As expected: Pool is maxed out. Releasing one connection and retrying...")

    # Release one connection back to the pool
    db2.close()
    print("Closed db2, returned to pool")

    # Now this should succeed immediately
    db4 = connpool.get_conn()
    print("Now acquired db4:", db4.connection_id)

# ---- Your app work would go here using db3/db4, e.g. queries, transactions, etc. ----
# For example:
# with db4.cursor() as cur:
#     cur.execute("SELECT NOW()")
#     print(cur.fetchone())

# Cleanup: ALWAYS return borrowed connections to the pool
for c in (db3, db4):
    try:
        c.close()
    except Exception:
        pass

# You can also close db1 if you like (the original connection that created the pool):
try:
    connpool.db1.close()
except Exception:
    pass

print("\nDone. All connections returned to the pool.")
