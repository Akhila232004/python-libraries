# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Timeout patterns — asyncio.wait_for(), asyncio.timeout()
#                 (Python 3.11+), retry on timeout, per-task timeouts
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio


# -----------------------------------------------------------------------------
# 1. asyncio.wait_for() — cancel if coroutine exceeds the time limit
# -----------------------------------------------------------------------------
async def slow_operation(name, duration):
    print(f"  [{name}] starting, will take {duration}s")
    await asyncio.sleep(duration)
    return f"[{name}] completed"

async def main_wait_for_basic():
    try:
        result = await asyncio.wait_for(slow_operation("Op-1", 5), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("  Operation timed out after 2.0 seconds")

print("--- wait_for basic ---")
asyncio.run(main_wait_for_basic())


# -----------------------------------------------------------------------------
# 2. wait_for — operation completes within timeout (no exception)
# -----------------------------------------------------------------------------
async def main_wait_for_success():
    try:
        result = await asyncio.wait_for(slow_operation("Fast", 1), timeout=3.0)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Timed out")

print("\n--- wait_for success ---")
asyncio.run(main_wait_for_success())


# -----------------------------------------------------------------------------
# 3. asyncio.timeout() context manager — Python 3.11+
#    Preferred style in modern Python; can wrap multiple awaits in one block
# -----------------------------------------------------------------------------
async def main_timeout_ctx():
    try:
        async with asyncio.timeout(2.0):
            print("  Starting step 1")
            await asyncio.sleep(0.5)
            print("  Starting step 2")
            await asyncio.sleep(2.0)    # This will be cancelled — 0.5 + 2.0 > 2.0
            print("  This will not print")
    except asyncio.TimeoutError:
        print("  Context manager timed out mid-sequence")

print("\n--- asyncio.timeout() context manager (3.11+) ---")
asyncio.run(main_timeout_ctx())


# -----------------------------------------------------------------------------
# 4. Per-task timeout — each task has its own independent timeout
# -----------------------------------------------------------------------------
async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} data"

async def fetch_with_timeout(name, delay, timeout):
    try:
        result = await asyncio.wait_for(fetch(name, delay), timeout=timeout)
        return result
    except asyncio.TimeoutError:
        return f"{name} TIMED OUT"

async def main_per_task_timeout():
    results = await asyncio.gather(
        fetch_with_timeout("API-1", 1.0, 2.0),     # Completes
        fetch_with_timeout("API-2", 3.0, 2.0),     # Times out
        fetch_with_timeout("API-3", 0.5, 2.0),     # Completes
    )
    for r in results:
        print(f"  {r}")

print("\n--- per-task timeouts ---")
asyncio.run(main_per_task_timeout())


# -----------------------------------------------------------------------------
# 5. Retry on timeout — attempt up to N times before giving up
# -----------------------------------------------------------------------------
async def unreliable_service(attempt):
    if attempt < 3:
        await asyncio.sleep(5)          # Slow on first two attempts
    else:
        await asyncio.sleep(0.1)        # Fast on third attempt
    return "success"

async def with_retry(coro_factory, timeout, max_retries):
    for attempt in range(1, max_retries + 1):
        try:
            print(f"  Attempt {attempt}...")
            result = await asyncio.wait_for(coro_factory(attempt), timeout=timeout)
            print(f"  Succeeded on attempt {attempt}: {result}")
            return result
        except asyncio.TimeoutError:
            print(f"  Attempt {attempt} timed out")
    raise RuntimeError(f"Failed after {max_retries} attempts")

async def main_retry():
    try:
        await with_retry(unreliable_service, timeout=1.0, max_retries=4)
    except RuntimeError as e:
        print(f"  Gave up: {e}")

print("\n--- retry on timeout ---")
asyncio.run(main_retry())


# -----------------------------------------------------------------------------
# 6. Timeout with cleanup — ensure resources are released on timeout
# -----------------------------------------------------------------------------
class Resource:
    async def acquire(self):
        print("  [Resource] acquiring...")
        await asyncio.sleep(0.1)
        print("  [Resource] acquired")

    async def release(self):
        print("  [Resource] releasing...")
        await asyncio.sleep(0.1)
        print("  [Resource] released")

async def use_resource_with_timeout():
    resource = Resource()
    await resource.acquire()
    try:
        result = await asyncio.wait_for(slow_operation("WithResource", 5), timeout=1.0)
    except asyncio.TimeoutError:
        print("  Timed out — cleaning up resource")
    finally:
        await resource.release()

print("\n--- timeout with cleanup ---")
asyncio.run(use_resource_with_timeout())
