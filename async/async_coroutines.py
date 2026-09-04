# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Coroutine basics — async def, await, asyncio.run(),
#                 sequential vs concurrent execution
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio
import time


# -----------------------------------------------------------------------------
# 1. Basic coroutine — async def + await
# -----------------------------------------------------------------------------
async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)          # Non-blocking pause; yields to event loop
    print(f"Goodbye, {name}!")

asyncio.run(greet("Alice"))


# -----------------------------------------------------------------------------
# 2. Coroutines return values — await captures the return
# -----------------------------------------------------------------------------
async def add(a, b):
    await asyncio.sleep(0.1)        # Simulate async work
    return a + b

async def main_return():
    result = await add(3, 4)
    print(f"3 + 4 = {result}")

asyncio.run(main_return())


# -----------------------------------------------------------------------------
# 3. Sequential vs concurrent — why concurrency matters
# -----------------------------------------------------------------------------
async def fetch(source, delay):
    print(f"  Start: {source}")
    await asyncio.sleep(delay)
    print(f"  Done : {source}")
    return f"data-from-{source}"


async def sequential():
    t0 = time.perf_counter()
    r1 = await fetch("API-1", 1)    # Waits 1s, then moves to next line
    r2 = await fetch("API-2", 2)    # Waits another 2s
    elapsed = time.perf_counter() - t0
    print(f"Sequential results: {r1}, {r2}")
    print(f"Sequential time: {elapsed:.2f}s  (expected ~3s)")


async def concurrent():
    t0 = time.perf_counter()
    # create_task schedules both immediately — they overlap
    task1 = asyncio.create_task(fetch("API-1", 1))
    task2 = asyncio.create_task(fetch("API-2", 2))
    r1 = await task1
    r2 = await task2
    elapsed = time.perf_counter() - t0
    print(f"Concurrent results: {r1}, {r2}")
    print(f"Concurrent time: {elapsed:.2f}s  (expected ~2s)")


print("\n--- Sequential ---")
asyncio.run(sequential())

print("\n--- Concurrent ---")
asyncio.run(concurrent())


# -----------------------------------------------------------------------------
# 4. Nested coroutines — coroutines calling other coroutines
# -----------------------------------------------------------------------------
async def step_one():
    await asyncio.sleep(0.2)
    return "step-one-done"

async def step_two(previous):
    await asyncio.sleep(0.2)
    return f"step-two-done (after {previous})"

async def pipeline():
    r1 = await step_one()
    r2 = await step_two(r1)
    print(f"Pipeline result: {r2}")

asyncio.run(pipeline())


# -----------------------------------------------------------------------------
# 5. asyncio.sleep(0) — yield control without actual delay
#    Useful to let the event loop check for other pending tasks
# -----------------------------------------------------------------------------
async def yield_demo():
    for i in range(3):
        print(f"Step {i}")
        await asyncio.sleep(0)      # Give event loop a chance to run other tasks

asyncio.run(yield_demo())
