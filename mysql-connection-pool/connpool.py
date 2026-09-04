# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Creating a pool
#  Author       : Team Tinitiate
# ==============================================================================



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
