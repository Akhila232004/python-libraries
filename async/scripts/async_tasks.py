# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : asyncio Tasks — create_task, task states, cancellation,
#                 task callbacks and shields
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio


# -----------------------------------------------------------------------------
# 1. create_task — schedule a coroutine to run concurrently
# -----------------------------------------------------------------------------
async def worker(name, delay):
    print(f"[{name}] starting")
    await asyncio.sleep(delay)
    print(f"[{name}] done")
    return f"{name}-result"

async def main_basic():
    task1 = asyncio.create_task(worker("A", 1))
    task2 = asyncio.create_task(worker("B", 2))
    task3 = asyncio.create_task(worker("C", 0.5))

    # All three run concurrently from the moment create_task is called
    r1 = await task1
    r2 = await task2
    r3 = await task3
    print(f"Results: {r1}, {r2}, {r3}")

asyncio.run(main_basic())


# -----------------------------------------------------------------------------
# 2. Task states — pending, running, done, cancelled
# -----------------------------------------------------------------------------
async def main_states():
    task = asyncio.create_task(worker("State-demo", 1))

    print(f"Immediately after create_task:")
    print(f"  done()      = {task.done()}")
    print(f"  cancelled() = {task.cancelled()}")

    await task

    print(f"After await:")
    print(f"  done()      = {task.done()}")
    print(f"  result()    = {task.result()}")

asyncio.run(main_states())


# -----------------------------------------------------------------------------
# 3. Task cancellation — CancelledError must be re-raised
# -----------------------------------------------------------------------------
async def long_task():
    try:
        print("[long_task] started")
        await asyncio.sleep(10)
        print("[long_task] completed")          # Never printed if cancelled
    except asyncio.CancelledError:
        print("[long_task] caught CancelledError — cleaning up")
        raise                                   # Re-raise: required by asyncio protocol

async def main_cancel():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(1)                      # Let it run for 1 second

    print("[main] Cancelling task")
    cancelled = task.cancel()                   # Returns True if cancel was sent
    print(f"[main] cancel() returned: {cancelled}")

    try:
        await task
    except asyncio.CancelledError:
        print(f"[main] task.cancelled() = {task.cancelled()}")

asyncio.run(main_cancel())


# -----------------------------------------------------------------------------
# 4. Task callbacks — execute a function when a task finishes
# -----------------------------------------------------------------------------
def on_done(task):
    if task.cancelled():
        print(f"[callback] Task was cancelled")
    elif task.exception():
        print(f"[callback] Task raised: {task.exception()}")
    else:
        print(f"[callback] Task result: {task.result()}")

async def main_callback():
    task = asyncio.create_task(worker("Callback-demo", 0.5))
    task.add_done_callback(on_done)             # Synchronous callback
    await task                                  # Wait for completion

asyncio.run(main_callback())


# -----------------------------------------------------------------------------
# 5. asyncio.shield — protect a coroutine from cancellation
#    The inner task keeps running even if the outer await is cancelled
# -----------------------------------------------------------------------------
async def critical_work():
    print("[critical] started — cannot be cancelled")
    await asyncio.sleep(2)
    print("[critical] finished")
    return "critical-result"

async def main_shield():
    task = asyncio.create_task(critical_work())
    shielded = asyncio.shield(task)

    outer = asyncio.create_task(asyncio.wait_for(shielded, timeout=0.5))
    try:
        await outer
    except asyncio.TimeoutError:
        print("[main] Outer timed out, but inner task still runs")

    # Inner task continues — await it to get the result
    result = await task
    print(f"[main] Inner result: {result}")

asyncio.run(main_shield())


# -----------------------------------------------------------------------------
# 6. Task names — useful for debugging
# -----------------------------------------------------------------------------
async def named_worker():
    name = asyncio.current_task().get_name()
    print(f"Running as task named: {name}")
    await asyncio.sleep(0.1)

async def main_names():
    t1 = asyncio.create_task(named_worker(), name="FetchUser")
    t2 = asyncio.create_task(named_worker(), name="FetchOrders")
    await asyncio.gather(t1, t2)

asyncio.run(main_names())
