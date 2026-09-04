# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : asyncio synchronization primitives — Lock, Event, Semaphore,
#                 Condition; use cases, patterns, and pitfalls
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio


# =============================================================================
# LOCK — mutual exclusion: one coroutine at a time
# =============================================================================

counter = 0

async def increment_locked(lock, name):
    global counter
    async with lock:
        current = counter
        await asyncio.sleep(0.05)       # Critical section — simulate work
        counter = current + 1
        print(f"  [{name}] counter = {counter}")

async def main_lock():
    global counter
    counter = 0
    lock    = asyncio.Lock()
    tasks   = [asyncio.create_task(increment_locked(lock, f"T{i}")) for i in range(5)]
    await asyncio.gather(*tasks)
    print(f"  Final counter (correct): {counter}")

print("--- Lock ---")
asyncio.run(main_lock())


# Lock.locked() — check if lock is held, acquire/release without context manager
async def main_lock_manual():
    lock = asyncio.Lock()
    await lock.acquire()
    print(f"  Lock held: {lock.locked()}")
    lock.release()
    print(f"  Lock held after release: {lock.locked()}")

print("\n--- Lock.locked() ---")
asyncio.run(main_lock_manual())


# =============================================================================
# EVENT — signal: one coroutine wakes one or many others
# =============================================================================

async def waiter(event, name):
    print(f"  [{name}] waiting for start signal...")
    await event.wait()
    print(f"  [{name}] received signal — proceeding!")

async def starter(event, delay):
    print(f"  [Starter] preparing for {delay}s...")
    await asyncio.sleep(delay)
    print(f"  [Starter] signalling all waiters!")
    event.set()                         # Unblocks all waiting coroutines at once

async def main_event():
    event = asyncio.Event()
    await asyncio.gather(
        waiter(event, "Worker-1"),
        waiter(event, "Worker-2"),
        waiter(event, "Worker-3"),
        starter(event, delay=1),
    )

print("\n--- Event ---")
asyncio.run(main_event())


# Event.clear() — reset so it can be waited on again (one-shot vs repeating signal)
async def main_event_clear():
    event = asyncio.Event()

    for round_num in range(1, 3):
        event.clear()                   # Reset before each round

        async def set_event():
            await asyncio.sleep(0.3)
            event.set()

        async def wait_event(name):
            await event.wait()
            print(f"  [{name}] round {round_num} — event received")

        await asyncio.gather(
            wait_event("Listener-A"),
            wait_event("Listener-B"),
            set_event(),
        )

print("\n--- Event.clear() ---")
asyncio.run(main_event_clear())


# =============================================================================
# SEMAPHORE — rate limiter: at most N coroutines in critical section
# =============================================================================

async def limited_request(semaphore, request_id):
    async with semaphore:
        print(f"  [Request-{request_id}] executing")
        await asyncio.sleep(0.5)        # Simulate HTTP call
        print(f"  [Request-{request_id}] done")
        return request_id

async def main_semaphore():
    semaphore = asyncio.Semaphore(3)    # Max 3 concurrent requests
    tasks     = [limited_request(semaphore, i) for i in range(8)]
    results   = await asyncio.gather(*tasks)
    print(f"  Completed: {results}")

print("\n--- Semaphore ---")
asyncio.run(main_semaphore())


# BoundedSemaphore — like Semaphore but raises ValueError if released more than acquired
async def main_bounded():
    sem = asyncio.BoundedSemaphore(2)
    await sem.acquire()
    await sem.acquire()
    sem.release()
    sem.release()
    try:
        sem.release()                   # One too many releases
    except ValueError as e:
        print(f"  BoundedSemaphore error: {e}")

print("\n--- BoundedSemaphore ---")
asyncio.run(main_bounded())


# =============================================================================
# CONDITION — notifiable lock: wait for a condition to become true
# =============================================================================

buffer     = []
MAX_BUFFER = 3

async def producer_cond(condition, items):
    for item in items:
        async with condition:
            while len(buffer) >= MAX_BUFFER:
                print(f"  [P] buffer full — waiting")
                await condition.wait()      # Release lock and wait for notify
            buffer.append(item)
            print(f"  [P] added {item} → buffer={buffer}")
            condition.notify()              # Wake one waiting consumer
        await asyncio.sleep(0.2)

async def consumer_cond(condition, name, count):
    consumed = 0
    while consumed < count:
        async with condition:
            while not buffer:
                print(f"  [{name}] buffer empty — waiting")
                await condition.wait()
            item = buffer.pop(0)
            consumed += 1
            print(f"  [{name}] consumed {item} → buffer={buffer}")
            condition.notify()              # Wake waiting producer
        await asyncio.sleep(0.5)

async def main_condition():
    condition = asyncio.Condition()
    items     = [f"item-{i}" for i in range(6)]

    await asyncio.gather(
        producer_cond(condition, items),
        consumer_cond(condition, "Consumer-A", 3),
        consumer_cond(condition, "Consumer-B", 3),
    )

print("\n--- Condition ---")
asyncio.run(main_condition())
