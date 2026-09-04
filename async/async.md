![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; Venkata Bhattaram | TINITIATE.COM 

##### [Back To Contents](../../README.md)

# Python Async Programming

* Python `asyncio` module provides infrastructure for writing **asynchronous, concurrent** code using the `async`/`await` syntax.
* Async programming allows a program to perform tasks concurrently **without** using multiple threads — a single thread handles many tasks by switching between them during wait periods.
* Best suited for **I/O-bound** tasks: network requests, file reads, database queries — anywhere the CPU is waiting, not working.
* **NOT** a replacement for multiprocessing for CPU-bound work (use `ProcessPoolExecutor` for that).

Key concepts:
- **Event Loop** : The central scheduler — runs coroutines, switches between them on `await`.
- **Coroutine** : A function defined with `async def` that can be paused with `await`.
- **Task** : A scheduled coroutine — runs concurrently on the event loop via `create_task()`.
- **Future** : Low-level object representing a value not yet computed.

## Python Files

| File | Topics Covered |
|------|----------------|
| [async_coroutines.py](async_coroutines.py) | `async def`, `await`, `asyncio.run()`, return values from coroutines, sequential vs concurrent timing, nested coroutines, `asyncio.sleep(0)` |
| [async_tasks.py](async_tasks.py) | `create_task()`, task states (`done()`, `cancelled()`, `result()`), cancellation + `CancelledError`, `add_done_callback()`, `asyncio.shield()`, named tasks |
| [async_gather_wait.py](async_gather_wait.py) | `asyncio.gather()`, `return_exceptions`, exception propagation without flag, `asyncio.wait()` with `FIRST_COMPLETED` / `FIRST_EXCEPTION` / `ALL_COMPLETED`, fan-out pattern |
| [async_timeout.py](async_timeout.py) | `asyncio.wait_for()`, `asyncio.timeout()` context manager (Python 3.11+), per-task independent timeouts, retry-on-timeout factory, resource cleanup in `finally` |
| [async_queue.py](async_queue.py) | `asyncio.Queue`, sentinel stop pattern, `task_done()` / `join()`, multiple producers/consumers, `qsize` / `empty` / `full` / `get_nowait` / `put_nowait`, `PriorityQueue`, `LifoQueue` |
| [async_sync_primitives.py](async_sync_primitives.py) | `Lock` (with `locked()`, manual acquire/release), `Event` (with `clear()` for repeating signals), `Semaphore`, `BoundedSemaphore`, `Condition` with bounded buffer |
| [async_context_manager.py](async_context_manager.py) | `__aenter__` / `__aexit__`, rollback/commit pattern in `__aexit__`, `asynccontextmanager` decorator, nested CMs, async resource pool, multi-CM syntax (Python 3.10+) |
| [async_iterator_generator.py](async_iterator_generator.py) | Async generators, data streaming, error handling inside a generator, `asend()` / `aclose()`, `__aiter__` / `__anext__`, iterable vs iterator class separation, async comprehensions (list/set/dict/generator), `aiter()` / `anext()` builtins (Python 3.10+), generator pipeline chaining |
| [async_streams.py](async_streams.py) | Echo server/client, `readline()` line-protocol server, multiple concurrent clients, server-to-client chunk streaming, graceful shutdown |
| [async_executor.py](async_executor.py) | `run_in_executor()`, `asyncio.to_thread()` (Python 3.9+), `ThreadPoolExecutor`, `ProcessPoolExecutor`, default executor (`None`), mixed sync/async pipeline, separate I/O + CPU pools, `set_default_executor()` |
| [async_http.py](async_http.py) | `aiohttp` concurrent GET/POST, rate limiting with `Semaphore`, retry with exponential backoff, response streaming in chunks, `ClientSession` config (connector limits, timeout, headers), fan-out detail fetching |

## Synchronous vs Asynchronous

> **File:** [async_coroutines.py](async_coroutines.py) — the `sequential()` and `concurrent()` functions measure wall-clock time to show that concurrent tasks overlap while sequential tasks stack.

* In **synchronous** code, tasks run one after another — each waits for the previous to finish.
* In **asynchronous** code, while one task is waiting (network, disk), the event loop runs another.

```
Sync:  [Task1 ----wait---- done][Task2 ----wait---- done]   total = T1 + T2
Async: [Task1 start][Task2 start][Task1 done][Task2 done]   total = max(T1, T2)
```

## Coroutines — async def and await

> **File:** [async_coroutines.py](async_coroutines.py) — also shows: coroutines that return values (captured with `await`); nested coroutines calling each other in a pipeline; `asyncio.sleep(0)` to yield control to the event loop without any real delay (useful in tight loops to stay cooperative without artificial waits).

* A **coroutine** is defined with `async def` and can contain `await` expressions.
* `await` suspends the current coroutine and yields control to the event loop.
* `asyncio.run()` is the standard entry point — creates the event loop and runs one top-level coroutine.

```python
import asyncio

async def greet(name):
    print(f"Hello, {name}!")
    await asyncio.sleep(1)       # Suspend here — event loop can run other coroutines
    print(f"Goodbye, {name}!")

asyncio.run(greet("Alice"))
```

## asyncio.sleep() vs time.sleep()

> **File:** [async_coroutines.py](async_coroutines.py)

* `asyncio.sleep(n)` is **non-blocking** — suspends the coroutine, lets the event loop run others.
* `time.sleep(n)` is **blocking** — freezes the entire event loop thread. Never use inside async code.
* `asyncio.sleep(0)` yields to the event loop for one cycle with no real delay — useful to stay cooperative inside a CPU-bound loop.

```python
import asyncio
import time

async def demo_non_blocking():
    print("Non-blocking start")
    await asyncio.sleep(2)      # Yields control — other tasks run during these 2s
    print("Non-blocking done")

async def demo_why_blocking_is_bad():
    print("Blocking start")
    time.sleep(2)               # Entire event loop frozen — no other task can run!
    print("Blocking done")

asyncio.run(demo_non_blocking())
```

## Tasks — asyncio.create_task()

> **File:** [async_tasks.py](async_tasks.py) — also covers: task state inspection (`task.done()`, `task.cancelled()`, `task.result()`); `add_done_callback()` for a synchronous callback that fires when a task finishes or is cancelled; `asyncio.shield()` to protect a critical coroutine from being cancelled when the outer `await` times out; named tasks (`name=` parameter) for cleaner debug logs.

* `asyncio.create_task(coro)` schedules a coroutine to run **concurrently** — it starts immediately.
* Awaiting a coroutine directly (`await coro()`) is sequential — next line waits for it to finish.
* Tasks can also be **cancelled** before they complete.

```python
import asyncio

async def fetch_data(source, delay):
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)
    print(f"Done: {source}")
    return f"Data from {source}"

async def main():
    # Sequential: total = 1 + 2 = 3 seconds
    # r1 = await fetch_data("API-1", 1)
    # r2 = await fetch_data("API-2", 2)

    # Concurrent with create_task: total = max(1,2) = 2 seconds
    task1 = asyncio.create_task(fetch_data("API-1", 1))
    task2 = asyncio.create_task(fetch_data("API-2", 2))

    r1 = await task1
    r2 = await task2
    print(r1, r2)

asyncio.run(main())
```

* **Task Cancellation**: a running task can be cancelled externally.

```python
import asyncio

async def long_running():
    try:
        print("Task started")
        await asyncio.sleep(10)
        print("Task complete")
    except asyncio.CancelledError:
        print("Task was cancelled!")
        raise                          # Must re-raise so asyncio knows it was cancelled

async def main():
    task = asyncio.create_task(long_running())
    await asyncio.sleep(2)             # Let the task run for 2 seconds
    task.cancel()                      # Request cancellation
    try:
        await task                     # Wait for cancellation to propagate
    except asyncio.CancelledError:
        print("Confirmed: task cancelled")

asyncio.run(main())
```

* **`asyncio.shield()`** — wraps a task so that cancelling the outer `await` does not cancel the underlying task. The inner coroutine keeps running; only the shield is cancelled. Useful for protecting cleanup or critical commit operations.
* **`add_done_callback(fn)`** — registers a plain (non-async) function that is called synchronously when the task finishes, is cancelled, or raises. Receives the task object; inspect with `task.result()` / `task.exception()` / `task.cancelled()`.
* **Named tasks** — pass `name="MyTask"` to `create_task()` and read it back with `asyncio.current_task().get_name()` for cleaner log output.

## asyncio.gather() — Run Multiple Coroutines Concurrently

> **File:** [async_gather_wait.py](async_gather_wait.py) — also demonstrates: gather **without** `return_exceptions` (first exception is re-raised and other tasks may be left running); a fan-out / fan-in pipeline pattern (expand one list of IDs into many concurrent fetches then collect results).

* `asyncio.gather(*coros)` runs all coroutines concurrently and waits for all to finish.
* Returns a list of results in the **same order** as the coroutines passed, regardless of completion order.
* With `return_exceptions=True`, exceptions are returned as results instead of being raised.

```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} result"

async def main():
    # All three run concurrently — total ~3s not 1+2+3=6s
    results = await asyncio.gather(
        task("A", 1),
        task("B", 2),
        task("C", 3),
    )
    print(results)   # ['A result', 'B result', 'C result']  in order

asyncio.run(main())
```

* **Handling exceptions with gather**:

```python
import asyncio

async def might_fail(name, fail=False):
    await asyncio.sleep(1)
    if fail:
        raise ValueError(f"{name} failed!")
    return f"{name} ok"

async def main():
    results = await asyncio.gather(
        might_fail("X"),
        might_fail("Y", fail=True),
        might_fail("Z"),
        return_exceptions=True          # Exceptions captured as list items, not raised
    )
    for r in results:
        if isinstance(r, Exception):
            print(f"Error: {r}")
        else:
            print(f"Success: {r}")

asyncio.run(main())
```

## asyncio.wait() — First Completed and All Completed

> **File:** [async_gather_wait.py](async_gather_wait.py) — also demonstrates `FIRST_EXCEPTION` mode (returns as soon as any task raises, leaving others pending) and cancelling pending tasks with `await asyncio.gather(*pending, return_exceptions=True)` to suppress `CancelledError` warnings.

* `asyncio.wait(tasks)` gives fine-grained control: stop when first finishes or when all finish.
* Returns two sets: `done` and `pending`.
* `return_when` accepts: `asyncio.FIRST_COMPLETED`, `asyncio.FIRST_EXCEPTION`, `asyncio.ALL_COMPLETED`.
* Unlike `gather`, `wait` requires **Task** objects (not bare coroutines) — wrap with `create_task()` first.

```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return name

async def main():
    tasks = [
        asyncio.create_task(task("Fast",   1)),
        asyncio.create_task(task("Medium", 2)),
        asyncio.create_task(task("Slow",   3)),
    ]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    print("First to finish:")
    for t in done:
        print(" ", t.result())

    for t in pending:
        t.cancel()                      # Cancel the rest

asyncio.run(main())
```

## asyncio.wait_for() — Timeout

> **File:** [async_timeout.py](async_timeout.py) — also demonstrates: per-task independent timeouts (each task in a `gather` has its own timeout via `wait_for`); a retry factory pattern that passes a coroutine-factory function and retries up to N times; always releasing resources in a `finally` block even after timeout cancellation.

* `asyncio.wait_for(coro, timeout)` cancels the coroutine if it exceeds the time limit.
* Raises `asyncio.TimeoutError` when the timeout is reached.
* The cancelled coroutine receives `CancelledError` internally — use `finally` to clean up resources.

```python
import asyncio

async def slow_operation():
    print("Starting slow operation...")
    await asyncio.sleep(5)
    return "Completed"

async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=2.0)
        print(result)
    except asyncio.TimeoutError:
        print("Operation timed out after 2 seconds!")

asyncio.run(main())
```

* **Python 3.11+ `asyncio.timeout()` context manager** — preferred in modern Python because it can cover multiple `await` expressions in a single block:

```python
import asyncio

async def main():
    try:
        async with asyncio.timeout(2.0):
            await asyncio.sleep(5)       # Will be cancelled after 2s
    except asyncio.TimeoutError:
        print("Timed out via context manager")

asyncio.run(main())
```

## asyncio.Queue — Producer-Consumer Pattern

> **File:** [async_queue.py](async_queue.py) — also demonstrates: `queue.join()` (blocks until every consumed item has called `task_done()` — the standard "wait for all work" pattern); queue inspection without blocking (`qsize()`, `empty()`, `full()`, `get_nowait()`, `put_nowait()`); `asyncio.PriorityQueue` where items are tuples `(priority, value)` and lower numbers are dequeued first; `asyncio.LifoQueue` for stack (last-in-first-out) behaviour.

* `asyncio.Queue` is a first-in-first-out (FIFO) queue safe for use across coroutines.
* `maxsize=n` blocks producers when the queue is full — natural backpressure.
* Producers call `await queue.put(item)`; consumers call `await queue.get()`.
* Call `queue.task_done()` after processing; `await queue.join()` waits until all items are processed.
* Pass `None` (or another sentinel value) to signal consumers to stop — there is no built-in stop signal.

```python
import asyncio

async def producer(queue, items):
    for item in items:
        print(f"Producing: {item}")
        await queue.put(item)
        await asyncio.sleep(0.5)
    await queue.put(None)               # Sentinel value signals consumer to stop

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consuming: {item}")
        await asyncio.sleep(1)          # Simulate processing time
        queue.task_done()

async def main():
    queue  = asyncio.Queue(maxsize=3)
    items  = ["item-1", "item-2", "item-3", "item-4", "item-5"]

    await asyncio.gather(
        producer(queue, items),
        consumer(queue),
    )

asyncio.run(main())
```

* **Multiple producers and consumers**:

```python
import asyncio

async def producer(queue, producer_id, count):
    for i in range(count):
        item = f"P{producer_id}-item{i}"
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.3)

async def consumer(queue, consumer_id):
    while True:
        item = await queue.get()
        print(f"Consumer-{consumer_id} got: {item}")
        await asyncio.sleep(0.5)
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=5)

    producers = [asyncio.create_task(producer(queue, i, 3)) for i in range(2)]
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(3)]

    await asyncio.gather(*producers)
    await queue.join()                  # Wait until all items are processed

    for c in consumers:
        c.cancel()

asyncio.run(main())
```

## asyncio.Lock — Mutual Exclusion

> **File:** [async_sync_primitives.py](async_sync_primitives.py) — also shows `Lock.locked()` to check whether the lock is currently held, and manual `await lock.acquire()` / `lock.release()` when the `async with` pattern is not suitable (e.g. acquiring in one function and releasing in another).

* `asyncio.Lock` prevents multiple coroutines from accessing shared state simultaneously.
* Only one coroutine can hold the lock at a time — others `await` until it is released.
* Use `async with lock:` — automatically acquires and releases.
* Without a lock, `await` inside a critical section allows another coroutine to interleave and corrupt shared state.

```python
import asyncio

counter = 0
lock    = asyncio.Lock()

async def increment(name):
    global counter
    async with lock:                    # Acquire lock — only one at a time
        current = counter
        await asyncio.sleep(0.1)        # Simulate some work
        counter = current + 1
        print(f"{name}: counter = {counter}")

async def main():
    tasks = [asyncio.create_task(increment(f"task-{i}")) for i in range(5)]
    await asyncio.gather(*tasks)
    print(f"Final counter: {counter}")

asyncio.run(main())
```

## asyncio.Event — Coroutine Signaling

> **File:** [async_sync_primitives.py](async_sync_primitives.py) — also demonstrates `event.clear()` to reset the event so it can be waited on again in subsequent rounds (one-shot vs repeating signal pattern).

* `asyncio.Event` lets one coroutine **signal** one or more others that something happened.
* `await event.wait()` blocks until `event.set()` is called from another coroutine.
* `event.set()` unblocks **all** waiters simultaneously.
* `event.clear()` resets it so it can be waited on again in the next round.

```python
import asyncio

async def waiter(event, name):
    print(f"{name}: waiting for signal...")
    await event.wait()
    print(f"{name}: got the signal!")

async def trigger(event):
    print("Doing preparatory work...")
    await asyncio.sleep(2)
    print("Sending signal!")
    event.set()                         # Unblocks ALL waiters

async def main():
    event = asyncio.Event()
    await asyncio.gather(
        waiter(event, "Worker-1"),
        waiter(event, "Worker-2"),
        waiter(event, "Worker-3"),
        trigger(event),
    )

asyncio.run(main())
```

## asyncio.Semaphore — Limit Concurrency

> **File:** [async_sync_primitives.py](async_sync_primitives.py) — also shows `asyncio.BoundedSemaphore`, which raises `ValueError` if `release()` is called more times than `acquire()` — useful to catch programming errors where a semaphore slot is released without being acquired.

* `asyncio.Semaphore(n)` allows at most `n` coroutines to run a critical section simultaneously.
* Essential for rate-limiting: e.g. max 5 concurrent HTTP requests to avoid overwhelming a server.
* `BoundedSemaphore` is a stricter variant — it raises `ValueError` on over-release.

```python
import asyncio

semaphore = asyncio.Semaphore(3)        # At most 3 tasks in critical section

async def limited_task(name):
    async with semaphore:
        print(f"{name} started")
        await asyncio.sleep(1)
        print(f"{name} finished")

async def main():
    tasks = [asyncio.create_task(limited_task(f"task-{i}")) for i in range(8)]
    await asyncio.gather(*tasks)        # 8 tasks but only 3 run at a time

asyncio.run(main())
```

## asyncio.Condition — Coordinated Waiting

> **File:** [async_sync_primitives.py](async_sync_primitives.py) — demonstrates a bounded buffer with one producer and two consumers where both sides wait on the same `Condition`: the producer waits when the buffer is full; consumers wait when it is empty; each side calls `condition.notify()` after changing the buffer so the other side can re-evaluate.

* `asyncio.Condition` combines a lock with a notification mechanism.
* Coroutines can `await condition.wait()` until `condition.notify()` or `condition.notify_all()` is called.
* `condition.wait()` atomically **releases the lock and suspends** — the lock is re-acquired before returning.
* Useful for producer-consumer where consumers wait for data and producers notify.

```python
import asyncio

condition = asyncio.Condition()
data_ready = False
shared_data = None

async def consumer_cond(name):
    async with condition:
        while not data_ready:
            print(f"{name}: waiting for data...")
            await condition.wait()      # Releases lock and waits for notification
        print(f"{name}: got data = {shared_data}")

async def producer_cond():
    global data_ready, shared_data
    await asyncio.sleep(1)
    async with condition:
        shared_data = [1, 2, 3]
        data_ready  = True
        print("Producer: data ready, notifying all")
        condition.notify_all()          # Wake all waiting consumers

async def main():
    await asyncio.gather(
        consumer_cond("Consumer-A"),
        consumer_cond("Consumer-B"),
        producer_cond(),
    )

asyncio.run(main())
```

## Async Context Managers — async with

> **File:** [async_context_manager.py](async_context_manager.py) — also demonstrates: inspecting `exc_type` in `__aexit__` to implement commit/rollback (return `False` to let the exception propagate); nested `async with` blocks acquiring two locks in order; an async resource pool built from `Semaphore` + `Lock`; and the Python 3.10+ multi-resource syntax `async with (cm1 as a, cm2 as b):` to open two context managers in one statement.

* An async context manager implements `__aenter__` and `__aexit__` coroutine methods.
* Both setup and teardown can contain `await` expressions.
* `contextlib.asynccontextmanager` decorator is the simplest way to write one.
* Return `False` (or `None`) from `__aexit__` to propagate exceptions; return `True` to suppress them.

```python
import asyncio

class AsyncDatabaseConnection:
    def __init__(self, url):
        self.url = url
        self.conn = None

    async def __aenter__(self):
        print(f"Connecting to {self.url}...")
        await asyncio.sleep(0.5)        # Simulate async connection
        self.conn = f"conn({self.url})"
        print("Connected!")
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection...")
        await asyncio.sleep(0.1)        # Simulate async close
        self.conn = None
        print("Connection closed.")

async def main():
    async with AsyncDatabaseConnection("postgresql://localhost/db") as conn:
        print(f"Using: {conn}")
        await asyncio.sleep(0.3)        # Simulate query

asyncio.run(main())
```

* **Using `asynccontextmanager` decorator**:

```python
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def managed_connection(url):
    print(f"Opening connection to {url}")
    await asyncio.sleep(0.2)
    conn = f"conn({url})"
    try:
        yield conn                      # Code inside `async with` block runs here
    finally:
        print(f"Closing connection to {url}")
        await asyncio.sleep(0.1)

async def main():
    async with managed_connection("redis://localhost") as conn:
        print(f"Querying via {conn}")

asyncio.run(main())
```

## Async Iterators and Generators — async for

> **File:** [async_iterator_generator.py](async_iterator_generator.py) — also demonstrates: error handling *inside* an async generator (catch an exception per item, skip it, and continue yielding); the `asend()` / `aclose()` protocol for two-way communication with an async generator (like a sync generator's `send()` / `close()`); separating the *iterable* class (`__aiter__` returns a new iterator) from the *iterator* class (`__anext__`) so the same iterable supports multiple concurrent iterations; async set, dict, and generator comprehensions; `aiter()` / `anext()` builtins (Python 3.10+); chaining async generators into a multi-stage pipeline.

* An async iterator implements `__aiter__` (returns self) and `__anext__` (coroutine returning next item).
* Raise `StopAsyncIteration` to signal end of iteration.
* **Async generators** use `yield` inside `async def` — the simplest way to create async iterators.

```python
import asyncio

# Async generator — simulates data streaming from a source
async def stream_records(count):
    for i in range(count):
        await asyncio.sleep(0.3)        # Simulate data arriving asynchronously
        yield {"id": i, "value": i * 10}

async def main():
    async for record in stream_records(5):
        print(f"Received: {record}")

asyncio.run(main())
```

* **Async iterator class**:

```python
import asyncio

class AsyncRange:
    def __init__(self, start, stop):
        self.current = start
        self.stop    = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        value         = self.current
        self.current += 1
        return value

async def main():
    async for value in AsyncRange(0, 5):
        print(f"Value: {value}")

asyncio.run(main())
```

* **Collecting async generator output with a list comprehension** (Python 3.10+):

```python
import asyncio

async def async_squares(n):
    for i in range(n):
        await asyncio.sleep(0.05)
        yield i * i

async def main():
    squares = [x async for x in async_squares(6)]
    print(squares)  # [0, 1, 4, 9, 16, 25]

asyncio.run(main())
```

## asyncio Streams — TCP Server and Client

> **File:** [async_streams.py](async_streams.py) — also demonstrates: a line-protocol server using `reader.readline()` that dispatches on command strings; handling multiple concurrent clients automatically (each `start_server` connection spawns a new handler coroutine); a server that pushes data chunks to the client; graceful shutdown where the server exits the `async with server:` block after serving a fixed number of clients.

* `asyncio.start_server()` creates a TCP server without manually managing sockets.
* Each client connection invokes a handler coroutine receiving `StreamReader` and `StreamWriter`.
* `asyncio.open_connection()` is the client counterpart.
* `reader.read(n)` reads up to `n` bytes; `reader.readline()` reads up to and including `\n` — use the latter for text line-protocols.
* Always call `await writer.drain()` after `writer.write()` to flush the buffer and respect backpressure.

```python
import asyncio

# Server handler — called once per connected client
async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"[Server] Client connected: {addr}")

    data    = await reader.read(1024)
    message = data.decode().strip()
    print(f"[Server] Received: {message}")

    response = f"ECHO: {message}\n"
    writer.write(response.encode())
    await writer.drain()                # Flush the write buffer
    writer.close()
    await writer.wait_closed()

async def tcp_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    writer.write(b"Hello Server!\n")
    await writer.drain()

    response = await reader.read(1024)
    print(f"[Client] Got: {response.decode().strip()}")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    async with server:
        await tcp_client()              # Connect one client then exit

asyncio.run(main())
```

## Running Sync Code in Async — run_in_executor

> **File:** [async_executor.py](async_executor.py) — also demonstrates: `asyncio.to_thread()` (Python 3.9+ shortcut that uses the loop's default thread pool); `ProcessPoolExecutor` for true CPU parallelism (bypasses the GIL — note that worker functions must be defined at module level to be picklable); passing `None` as the executor to use the event loop's built-in default thread pool; a mixed sync/async pipeline where async fetch → sync transform (in thread) → async save; using separate named thread/process pools per task type; `loop.set_default_executor()` to replace the built-in pool globally.

* Calling a blocking/sync function directly inside a coroutine blocks the entire event loop.
* `loop.run_in_executor(executor, func, *args)` runs sync code in a thread or process pool.
* `asyncio.to_thread(func, *args)` (Python 3.9+) is the simpler thread-pool shortcut.
* Use `ThreadPoolExecutor` for blocking I/O; use `ProcessPoolExecutor` for CPU-bound work.
* Pass `None` as the executor to use the event loop's built-in default `ThreadPoolExecutor`.

```python
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def blocking_io(name, duration):
    time.sleep(duration)               # Blocking — but safe in a thread
    return f"{name} done after {duration}s"

def cpu_bound(n):
    return sum(i * i for i in range(n))

async def main():
    loop = asyncio.get_event_loop()

    # Thread pool — best for blocking I/O
    with ThreadPoolExecutor(max_workers=4) as pool:
        result = await loop.run_in_executor(pool, blocking_io, "File-read", 1)
        print(result)

    # asyncio.to_thread — Python 3.9+ shortcut for thread pool
    result = await asyncio.to_thread(blocking_io, "API-call", 1)
    print(result)

    # Process pool — for CPU-bound work (true parallelism, bypasses GIL)
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound, 1_000_000)
        print(f"Sum of squares: {result}")

asyncio.run(main())
```

## Real-World Pattern: Concurrent HTTP Requests (aiohttp)

> **File:** [async_http.py](async_http.py) — also demonstrates: retry with exponential backoff (0.5 s → 1 s → 2 s) that treats HTTP 5xx as a transient failure; concurrent POST requests using `session.post()` with a JSON payload; streaming a large response body in chunks with `response.content.iter_chunked(n)` to avoid loading it all into memory; `ClientSession` configuration with `TCPConnector` (total and per-host connection limits) and `ClientTimeout` (total and connect phases); a fan-out pattern that fetches a paginated list then concurrently resolves detail records for each item.

* `aiohttp` is the standard async HTTP client/server library for Python.
* Install: `pip install aiohttp`
* Use one `ClientSession` per application — do not create a session per request.
* `asyncio.gather()` + `aiohttp` = fetch hundreds of URLs concurrently.

```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        body = await response.text()
        return {"url": url, "status": response.status, "length": len(body)}

async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/uuid",
        "https://httpbin.org/ip",
    ]

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls])

    for r in results:
        print(r)

asyncio.run(main())
```

* **Rate-limited concurrent fetching** (Semaphore + aiohttp):

```python
import asyncio
import aiohttp

MAX_CONCURRENT = 5
semaphore = asyncio.Semaphore(MAX_CONCURRENT)

async def fetch_limited(session, url):
    async with semaphore:
        async with session.get(url) as response:
            return {"url": url, "status": response.status}

async def main():
    urls = [f"https://httpbin.org/get?n={i}" for i in range(20)]

    async with aiohttp.ClientSession() as session:
        tasks   = [fetch_limited(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    print(f"Fetched {len(results)} URLs, all statuses: {set(r['status'] for r in results)}")

asyncio.run(main())
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|
