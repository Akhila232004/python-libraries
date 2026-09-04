# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : asyncio.gather() and asyncio.wait() — concurrent execution,
#                 exception handling, FIRST_COMPLETED, ALL_COMPLETED patterns
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio


# -----------------------------------------------------------------------------
# 1. asyncio.gather() — run multiple coroutines concurrently
#    Returns results in INPUT order, regardless of completion order
# -----------------------------------------------------------------------------
async def job(name, delay, value):
    print(f"  {name}: started (delay={delay}s)")
    await asyncio.sleep(delay)
    print(f"  {name}: done")
    return value

async def main_gather_basic():
    results = await asyncio.gather(
        job("C", 3, "third"),
        job("A", 1, "first"),
        job("B", 2, "second"),
    )
    # Results are in INPUT order: C, A, B — not completion order A, B, C
    print(f"Results in input order: {results}")

print("--- gather basic ---")
asyncio.run(main_gather_basic())


# -----------------------------------------------------------------------------
# 2. gather with return_exceptions=True
#    Exceptions are captured in the result list instead of being raised
# -----------------------------------------------------------------------------
async def might_fail(name, should_fail=False):
    await asyncio.sleep(0.5)
    if should_fail:
        raise RuntimeError(f"{name} exploded!")
    return f"{name} success"

async def main_gather_exceptions():
    results = await asyncio.gather(
        might_fail("Task-1"),
        might_fail("Task-2", should_fail=True),
        might_fail("Task-3"),
        might_fail("Task-4", should_fail=True),
        return_exceptions=True
    )
    for i, r in enumerate(results, 1):
        if isinstance(r, Exception):
            print(f"  Task-{i} FAILED: {r}")
        else:
            print(f"  Task-{i} OK: {r}")

print("\n--- gather with return_exceptions ---")
asyncio.run(main_gather_exceptions())


# -----------------------------------------------------------------------------
# 3. gather without return_exceptions — first exception cancels and re-raises
# -----------------------------------------------------------------------------
async def main_gather_raise():
    try:
        results = await asyncio.gather(
            might_fail("X"),
            might_fail("Y", should_fail=True),
            might_fail("Z"),
        )
    except RuntimeError as e:
        print(f"  Exception propagated: {e}")

print("\n--- gather raises on first exception ---")
asyncio.run(main_gather_raise())


# -----------------------------------------------------------------------------
# 4. asyncio.wait() — FIRST_COMPLETED: act as soon as any task finishes
# -----------------------------------------------------------------------------
async def task(name, delay):
    await asyncio.sleep(delay)
    return name

async def main_wait_first():
    tasks = [
        asyncio.create_task(task("Slow",   3)),
        asyncio.create_task(task("Medium", 2)),
        asyncio.create_task(task("Fast",   1)),
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    print("  First to finish:")
    for t in done:
        print(f"    {t.result()}")

    print(f"  Still pending: {len(pending)} task(s) — cancelling them")
    for t in pending:
        t.cancel()

    # Await cancelled tasks to suppress CancelledError warnings
    await asyncio.gather(*pending, return_exceptions=True)

print("\n--- wait FIRST_COMPLETED ---")
asyncio.run(main_wait_first())


# -----------------------------------------------------------------------------
# 5. asyncio.wait() — ALL_COMPLETED: same as gather but returns sets not list
# -----------------------------------------------------------------------------
async def main_wait_all():
    tasks = [asyncio.create_task(task(f"task-{i}", i * 0.5)) for i in range(1, 5)]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    print(f"  All done ({len(done)} tasks):")
    for t in done:
        print(f"    {t.result()}")

print("\n--- wait ALL_COMPLETED ---")
asyncio.run(main_wait_all())


# -----------------------------------------------------------------------------
# 6. asyncio.wait() — FIRST_EXCEPTION: stop as soon as one task fails
# -----------------------------------------------------------------------------
async def risky(name, fail=False):
    await asyncio.sleep(0.5)
    if fail:
        raise ValueError(f"{name} failed")
    return name

async def main_wait_first_exception():
    tasks = [
        asyncio.create_task(risky("ok-1")),
        asyncio.create_task(risky("bad",   fail=True)),
        asyncio.create_task(risky("ok-2")),
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

    for t in done:
        if t.exception():
            print(f"  Exception caught: {t.exception()}")
        else:
            print(f"  Done: {t.result()}")

    for t in pending:
        t.cancel()
    await asyncio.gather(*pending, return_exceptions=True)

print("\n--- wait FIRST_EXCEPTION ---")
asyncio.run(main_wait_first_exception())


# -----------------------------------------------------------------------------
# 7. gather as fan-out / fan-in pipeline
#    Common pattern: expand one request into many sub-requests, collect results
# -----------------------------------------------------------------------------
async def fetch_user(user_id):
    await asyncio.sleep(0.2)            # Simulate DB query
    return {"id": user_id, "name": f"User-{user_id}"}

async def fetch_all_users(user_ids):
    users = await asyncio.gather(*[fetch_user(uid) for uid in user_ids])
    return users

async def main_fanout():
    ids   = list(range(1, 8))
    users = await fetch_all_users(ids)
    print(f"  Fetched {len(users)} users concurrently:")
    for u in users:
        print(f"    {u}")

print("\n--- gather fan-out ---")
asyncio.run(main_fanout())
