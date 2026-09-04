# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Async context managers — __aenter__ / __aexit__,
#                 asynccontextmanager decorator, async resource pooling
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio
from contextlib import asynccontextmanager


# =============================================================================
# 1. Basic async context manager — class-based
# =============================================================================

class AsyncFile:
    """Simulates an async file handle (like aiofiles)."""

    def __init__(self, path):
        self.path    = path
        self._handle = None

    async def __aenter__(self):
        print(f"  Opening {self.path} ...")
        await asyncio.sleep(0.1)            # Simulate async open (network filesystem, etc.)
        self._handle = f"handle({self.path})"
        print(f"  File open: {self._handle}")
        return self                         # `as f` receives this object

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"  Closing {self.path} ...")
        await asyncio.sleep(0.05)           # Simulate async flush/close
        self._handle = None
        print(f"  File closed.")
        return False                        # False = do not suppress exceptions

    async def write(self, data):
        print(f"  Writing to {self.path}: {data!r}")
        await asyncio.sleep(0.05)

async def main_class_cm():
    async with AsyncFile("/data/output.txt") as f:
        await f.write("Hello, async world!")
        await f.write("Second line.")

print("--- class-based async context manager ---")
asyncio.run(main_class_cm())


# =============================================================================
# 2. Exception handling in __aexit__
# =============================================================================

class SafeTransaction:
    async def __aenter__(self):
        print("  [TX] BEGIN")
        await asyncio.sleep(0.05)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"  [TX] ROLLBACK due to {exc_type.__name__}: {exc_val}")
        else:
            print("  [TX] COMMIT")
        await asyncio.sleep(0.05)
        return False                        # Don't suppress the exception

async def main_exception_cm():
    try:
        async with SafeTransaction():
            print("  Doing DB work...")
            await asyncio.sleep(0.1)
            raise ValueError("Constraint violation!")
    except ValueError:
        print("  Caught outside: transaction was rolled back")

    async with SafeTransaction():
        print("  Doing DB work (success)...")
        await asyncio.sleep(0.1)

print("\n--- exception handling in __aexit__ ---")
asyncio.run(main_exception_cm())


# =============================================================================
# 3. asynccontextmanager decorator — simplest way to write an async CM
# =============================================================================

@asynccontextmanager
async def db_connection(url):
    print(f"  [DB] Connecting to {url}...")
    await asyncio.sleep(0.1)
    conn = {"url": url, "active": True}
    try:
        yield conn                          # Code inside `async with` runs here
    except Exception as e:
        print(f"  [DB] Error encountered: {e}")
        raise
    finally:
        print(f"  [DB] Closing connection to {url}")
        await asyncio.sleep(0.05)
        conn["active"] = False

async def main_decorator_cm():
    async with db_connection("postgresql://localhost/mydb") as conn:
        print(f"  Executing query on {conn['url']}")
        await asyncio.sleep(0.2)

print("\n--- asynccontextmanager decorator ---")
asyncio.run(main_decorator_cm())


# =============================================================================
# 4. Nested async context managers
# =============================================================================

@asynccontextmanager
async def acquire_lock(name):
    print(f"  Acquiring lock: {name}")
    await asyncio.sleep(0.05)
    try:
        yield f"lock:{name}"
    finally:
        print(f"  Releasing lock: {name}")
        await asyncio.sleep(0.05)

async def main_nested_cm():
    async with acquire_lock("table-users") as l1:
        async with acquire_lock("table-orders") as l2:
            print(f"  Holding {l1} and {l2}")
            await asyncio.sleep(0.1)

print("\n--- nested context managers ---")
asyncio.run(main_nested_cm())


# =============================================================================
# 5. Async resource pool — context manager controlling a pool of connections
# =============================================================================

class ConnectionPool:
    def __init__(self, size):
        self._sem  = asyncio.Semaphore(size)
        self._pool = [f"conn-{i}" for i in range(size)]
        self._lock = asyncio.Lock()

    @asynccontextmanager
    async def acquire(self):
        async with self._sem:               # Block until a slot is free
            async with self._lock:
                conn = self._pool.pop()
            try:
                print(f"  Acquired {conn}")
                yield conn
            finally:
                async with self._lock:
                    self._pool.append(conn)
                print(f"  Released {conn}")

async def use_pool(pool, name):
    async with pool.acquire() as conn:
        print(f"  [{name}] using {conn}")
        await asyncio.sleep(0.3)

async def main_pool():
    pool  = ConnectionPool(size=2)          # Pool of 2 connections, 5 users
    tasks = [use_pool(pool, f"user-{i}") for i in range(5)]
    await asyncio.gather(*tasks)

print("\n--- async resource pool ---")
asyncio.run(main_pool())


# =============================================================================
# 6. Using async with for multiple resources simultaneously (Python 3.10+)
# =============================================================================

async def main_multi_cm():
    async with (
        db_connection("postgresql://db1") as db1,
        db_connection("postgresql://db2") as db2,
    ):
        print(f"  Cross-DB query: {db1['url']} ↔ {db2['url']}")
        await asyncio.sleep(0.1)

print("\n--- multiple CMs in one async with (Python 3.10+) ---")
asyncio.run(main_multi_cm())
