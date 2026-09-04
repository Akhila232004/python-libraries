# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : asyncio.Queue — producer-consumer patterns, backpressure,
#                 multiple producers/consumers, task_done/join, priority queue
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio


# -----------------------------------------------------------------------------
# 1. Basic queue — single producer, single consumer
# -----------------------------------------------------------------------------
async def producer(queue):
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    for item in items:
        print(f"  [Producer] putting: {item}")
        await queue.put(item)
        await asyncio.sleep(0.3)
    await queue.put(None)               # Sentinel — signals consumer to stop

async def consumer(queue):
    while True:
        item = await queue.get()        # Blocks until an item is available
        if item is None:
            break
        print(f"  [Consumer] processing: {item}")
        await asyncio.sleep(0.6)        # Consumer is slower than producer
        queue.task_done()

async def main_basic():
    queue = asyncio.Queue(maxsize=3)    # Blocks producer when 3 items are waiting
    await asyncio.gather(producer(queue), consumer(queue))

print("--- basic producer-consumer ---")
asyncio.run(main_basic())


# -----------------------------------------------------------------------------
# 2. Queue with task_done() and join() — wait until all work is processed
# -----------------------------------------------------------------------------
async def producer_join(queue, items):
    for item in items:
        await queue.put(item)
        print(f"  [P] queued: {item}")

async def consumer_join(queue, name):
    while True:
        item = await queue.get()
        print(f"  [{name}] got: {item}")
        await asyncio.sleep(0.4)
        queue.task_done()               # Signal that this item is fully processed

async def main_join():
    queue = asyncio.Queue()
    items = [f"job-{i}" for i in range(6)]

    await asyncio.gather(
        producer_join(queue, items),
        consumer_join(queue, "Worker"),
    )
    await queue.join()                  # Wait until every task_done() has been called
    print("  All jobs processed!")

print("\n--- queue.join() ---")
asyncio.run(main_join())


# -----------------------------------------------------------------------------
# 3. Multiple producers and multiple consumers
# -----------------------------------------------------------------------------
async def multi_producer(queue, producer_id, count):
    for i in range(count):
        item = f"P{producer_id}-job{i}"
        await queue.put(item)
        print(f"  [P{producer_id}] produced: {item}")
        await asyncio.sleep(0.2)

async def multi_consumer(queue, consumer_id):
    while True:
        item = await queue.get()
        print(f"  [C{consumer_id}] consumed: {item}")
        await asyncio.sleep(0.5)
        queue.task_done()

async def main_multi():
    queue = asyncio.Queue(maxsize=5)

    # 2 producers, 3 consumers
    producers = [asyncio.create_task(multi_producer(queue, i, 4)) for i in range(2)]
    consumers = [asyncio.create_task(multi_consumer(queue, i)) for i in range(3)]

    await asyncio.gather(*producers)    # Wait for all producers to finish
    await queue.join()                  # Wait for all items to be processed

    for c in consumers:                 # Cancel idle consumers
        c.cancel()
    await asyncio.gather(*consumers, return_exceptions=True)
    print("  All done!")

print("\n--- multiple producers and consumers ---")
asyncio.run(main_multi())


# -----------------------------------------------------------------------------
# 4. Queue inspection — qsize, empty, full, get_nowait, put_nowait
# -----------------------------------------------------------------------------
async def main_inspection():
    queue = asyncio.Queue(maxsize=3)

    await queue.put("first")
    await queue.put("second")
    await queue.put("third")

    print(f"  qsize()  = {queue.qsize()}")
    print(f"  empty()  = {queue.empty()}")
    print(f"  full()   = {queue.full()}")

    try:
        queue.put_nowait("overflow")    # Raises QueueFull immediately
    except asyncio.QueueFull:
        print("  Queue is full — put_nowait raised QueueFull")

    item = queue.get_nowait()           # Raises QueueEmpty if nothing available
    print(f"  get_nowait() returned: {item}")
    print(f"  qsize() after get: {queue.qsize()}")

print("\n--- queue inspection ---")
asyncio.run(main_inspection())


# -----------------------------------------------------------------------------
# 5. asyncio.PriorityQueue — lower number = higher priority
# -----------------------------------------------------------------------------
async def priority_producer(queue):
    tasks = [(3, "low-priority"), (1, "high-priority"), (2, "medium-priority")]
    for priority, name in tasks:
        print(f"  [P] adding: ({priority}, {name})")
        await queue.put((priority, name))

async def priority_consumer(queue, count):
    for _ in range(count):
        priority, name = await queue.get()
        print(f"  [C] processing: ({priority}, {name})")
        queue.task_done()

async def main_priority():
    queue = asyncio.PriorityQueue()
    await priority_producer(queue)
    await priority_consumer(queue, 3)   # Items come out in priority order: 1, 2, 3

print("\n--- PriorityQueue ---")
asyncio.run(main_priority())


# -----------------------------------------------------------------------------
# 6. asyncio.LifoQueue — last in, first out (stack behaviour)
# -----------------------------------------------------------------------------
async def main_lifo():
    queue = asyncio.LifoQueue()

    for item in ["first", "second", "third"]:
        await queue.put(item)
        print(f"  [P] pushed: {item}")

    while not queue.empty():
        item = await queue.get()
        print(f"  [C] popped: {item}")   # third, second, first

print("\n--- LifoQueue ---")
asyncio.run(main_lifo())
