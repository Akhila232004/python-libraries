# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Running sync code from async — run_in_executor(),
#                 asyncio.to_thread(), ThreadPoolExecutor, ProcessPoolExecutor,
#                 mixing sync and async, CPU-bound work
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio
import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# =============================================================================
# Sync functions — these BLOCK if called directly in async code
# =============================================================================

def blocking_io(name, duration):
    """Simulates blocking I/O: legacy SDK, file read, JDBC driver, etc."""
    time.sleep(duration)
    return f"{name} completed in {duration}s"


def cpu_heavy(n):
    """CPU-bound computation — benefits from ProcessPoolExecutor."""
    result = sum(math.factorial(i) for i in range(n))

    # Avoid converting the extremely large integer to a string.
    # Python 3.11+ limits huge integer-to-string conversions.
    digits = int(result.bit_length() * math.log10(2)) + 1

    return (
        f"factorial sum up to {n} computed successfully "
        f"({digits} digits)"
    )


def sync_transform(data):
    """Simulates a blocking data transformation (e.g. calling a C extension)."""
    time.sleep(0.1)
    return [x * 2 for x in data]


# =============================================================================
# 1. run_in_executor — ThreadPoolExecutor for blocking I/O
#    The event loop is NOT blocked; other coroutines continue running.
# =============================================================================

async def main_thread_pool():
    loop = asyncio.get_event_loop()

    with ThreadPoolExecutor(max_workers=4) as pool:
        # Single call
        result = await loop.run_in_executor(
            pool,
            blocking_io,
            "Task-A",
            1
        )

        print(f"  {result}")

        # Multiple blocking calls concurrently
        tasks = [
            loop.run_in_executor(
                pool,
                blocking_io,
                f"Task-{i}",
                0.5
            )
            for i in range(4)
        ]

        results = await asyncio.gather(*tasks)

        for r in results:
            print(f"  {r}")


# =============================================================================
# 2. asyncio.to_thread — Python 3.9+ shortcut for thread pool
#    Simpler API; uses a default thread pool managed by the event loop.
# =============================================================================

async def main_to_thread():
    # Single call
    result = await asyncio.to_thread(
        blocking_io,
        "B",
        0.5
    )

    print(f"  {result}")

    # Concurrent blocking calls with gather
    tasks = [
        asyncio.to_thread(
            blocking_io,
            f"file-{i}",
            0.3
        )
        for i in range(3)
    ]

    results = await asyncio.gather(*tasks)

    for r in results:
        print(f"  {r}")


# =============================================================================
# 3. ProcessPoolExecutor — for CPU-bound work
#    Bypasses the GIL by running each worker in a separate OS process.
#    Functions must be picklable and defined at module level.
# =============================================================================

async def main_process_pool():
    loop = asyncio.get_event_loop()

    with ProcessPoolExecutor(max_workers=2) as pool:
        # Run two CPU-heavy computations in separate processes
        r1, r2 = await asyncio.gather(
            loop.run_in_executor(
                pool,
                cpu_heavy,
                5000
            ),
            loop.run_in_executor(
                pool,
                cpu_heavy,
                4000
            ),
        )

        print(f"  Process 1: {r1}")
        print(f"  Process 2: {r2}")


# =============================================================================
# 4. Default executor — None uses the loop's built-in ThreadPoolExecutor
# =============================================================================

async def main_default_executor():
    loop = asyncio.get_event_loop()

    result = await loop.run_in_executor(
        None,
        blocking_io,
        "default-pool",
        0.5
    )

    print(f"  {result}")


# =============================================================================
# 5. Mixing sync and async in a pipeline
#    Use case: async fetch → sync transform → async save
# =============================================================================

async def async_fetch(source):
    print(f"  [fetch] fetching from {source}")

    await asyncio.sleep(0.2)

    return list(range(5))


async def async_save(data, destination):
    print(f"  [save] saving {len(data)} items to {destination}")

    await asyncio.sleep(0.1)

    print("  [save] done")


async def pipeline(source, destination):
    raw = await async_fetch(source)

    processed = await asyncio.to_thread(
        sync_transform,
        raw
    )

    await async_save(
        processed,
        destination
    )


async def main_pipeline():
    await asyncio.gather(
        pipeline(
            "api://data-1",
            "db://table-1"
        ),
        pipeline(
            "api://data-2",
            "db://table-2"
        ),
    )


# =============================================================================
# 6. Custom executor per task type — separate pools for I/O and CPU
# =============================================================================

async def main_multi_executor():
    loop = asyncio.get_event_loop()

    io_pool = ThreadPoolExecutor(
        max_workers=8,
        thread_name_prefix="io"
    )

    cpu_pool = ProcessPoolExecutor(
        max_workers=2
    )

    try:
        io_tasks = [
            loop.run_in_executor(
                io_pool,
                blocking_io,
                f"io-{i}",
                0.3
            )
            for i in range(4)
        ]

        cpu_tasks = [
            loop.run_in_executor(
                cpu_pool,
                cpu_heavy,
                3000
            )
            for _ in range(2)
        ]

        io_results, cpu_results = await asyncio.gather(
            asyncio.gather(*io_tasks),
            asyncio.gather(*cpu_tasks),
        )

        print("  I/O results:")

        for r in io_results:
            print(f"    {r}")

        print("  CPU results:")

        for r in cpu_results:
            print(f"    {r}")

    finally:
        io_pool.shutdown(wait=False)
        cpu_pool.shutdown(wait=False)


# =============================================================================
# 7. asyncio.loop.set_default_executor — replace the default thread pool
# =============================================================================

async def main_custom_default():
    loop = asyncio.get_event_loop()

    loop.set_default_executor(
        ThreadPoolExecutor(
            max_workers=16
        )
    )

    result = await asyncio.to_thread(
        blocking_io,
        "custom-default",
        0.2
    )

    print(f"  {result}")


# =============================================================================
# Main function
# =============================================================================

async def main():
    print("--- ThreadPoolExecutor ---")
    await main_thread_pool()

    print("\n--- asyncio.to_thread (Python 3.9+) ---")
    await main_to_thread()

    print("\n--- ProcessPoolExecutor ---")
    await main_process_pool()

    print("\n--- default executor (None) ---")
    await main_default_executor()

    print("\n--- mixed sync/async pipeline ---")
    await main_pipeline()

    print("\n--- custom I/O + CPU executor pools ---")
    await main_multi_executor()

    print("\n--- set_default_executor ---")
    await main_custom_default()


# =============================================================================
# Program entry point
# =============================================================================

if __name__ == "__main__":
    asyncio.run(main())