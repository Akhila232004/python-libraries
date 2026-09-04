![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# MySql Connection Pool
* A Python MySQL connection pool is a mechanism that manages a collection of pre-established connections to a MySQL database, making them available for reuse by application threads or processes.
* Instead of creating a new database connection for each request, which is a time-consuming and resource-intensive operation, the application requests a connection from the pool.
* When the task is complete, the connection is returned to the pool for subsequent use.
* This can improve performance and reduce the number of database connections required, making the application more efficient and scalable.
* The `MySQLConnectionPool` class from the `mysql.connector` library provides a connection pool implementation for MySQL databases.
```bash
# To install 'mysql-connector-python' run the following command
python -m pip install mysql-connector-python
```

## Creating a pool
```python
# connpool.py
import time
import mysql.connector
from mysql.connector.errors import PoolError

# ---- Configure your DB & pool here ----
POOL_NAME  = "LoanDBConnPool"
POOL_SIZE  = 3
DB_CONFIG  = {
    "user":     "root",
    "password": "tinitiate",
    "host":     "127.0.0.1",
    "database": "testing",
    # optional extras:
    # "port": 3306,
    # "charset": "utf8mb4",
}

# Create the pool on first import by opening one connection with pool_name & pool_size
db1 = mysql.connector.connect(
    **DB_CONFIG,
    pool_name=POOL_NAME,
    pool_size=POOL_SIZE,
)

print(f"[ConnPool] Pool '{POOL_NAME}' created with size={POOL_SIZE}")
print(f"[ConnPool] Mother Connection ID: {db1.connection_id}")

def get_conn(retries: int = 5, wait_seconds: int = 2):
    """
    Borrow a connection from the pool.
    Retries up to `retries` times if the pool is exhausted, waiting `wait_seconds` each time.
    Returns: a pooled connection (remember to .close() to return it to the pool)
    Raises: PoolError if no connection is available after all retries
    """
    for attempt in range(1, retries + 1):
        try:
            conn = mysql.connector.connect(pool_name=POOL_NAME)
            print(f"[ConnPool] Acquired connection_id={conn.connection_id}")
            return conn
        except PoolError:
            if attempt == retries:
                # Give up after last attempt
                raise
            print(f"[ConnPool] Pool exhausted (attempt {attempt}/{retries}). "
                  f"Waiting {wait_seconds}s before retry...")
            time.sleep(wait_seconds)
```

## Using the pool
```python
## pool_caller.py
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
```
### How the pool behaves
* The pool is named and process-local. Importing `connpool` creates the pool once.
* `pool_size=3` means at most three simultaneous checked-out connections.
* `.close()` on pooled connections returns them to the pool (it doesn’t sever the TCP connection).
* If you try to exceed `pool_size`, the connector raises `mysql.connector.errors.PoolError`.

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
