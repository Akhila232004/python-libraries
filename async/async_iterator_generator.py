# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Async iterators and generators — __aiter__, __anext__,
#                 async def with yield, async comprehensions, aiter/anext builtins
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio


# =============================================================================
# 1. Async generator — async def + yield (simplest async iterator)
# =============================================================================

async def countdown(n):
    """Yields numbers from n down to 1, with a delay between each."""
    for i in range(n, 0, -1):
        await asyncio.sleep(0.2)
        yield i

async def main_basic_gen():
    async for value in countdown(5):
        print(f"  Countdown: {value}")

print("--- basic async generator ---")
asyncio.run(main_basic_gen())


# =============================================================================
# 2. Async generator simulating data streaming (e.g. from a network socket)
# =============================================================================

async def stream_events(topic, count):
    """Simulates events arriving one-by-one from a message broker."""
    for i in range(count):
        await asyncio.sleep(0.15)       # Event arrives after a delay
        yield {"topic": topic, "seq": i, "payload": f"msg-{i}"}

async def main_stream():
    async for event in stream_events("orders", 4):
        print(f"  Received: {event}")

print("\n--- streaming events ---")
asyncio.run(main_stream())


# =============================================================================
# 3. Async generator with exception handling inside the generator
# =============================================================================

async def safe_stream(items):
    for item in items:
        try:
            await asyncio.sleep(0.1)
            if item == "bad":
                raise ValueError(f"Bad item: {item}")
            yield item
        except ValueError as e:
            print(f"  [generator] skipping error: {e}")
            # Continue to next item — does not stop the generator

async def main_safe_stream():
    data = ["ok-1", "bad", "ok-2", "bad", "ok-3"]
    async for item in safe_stream(data):
        print(f"  Processed: {item}")

print("\n--- async generator with error handling ---")
asyncio.run(main_safe_stream())


# =============================================================================
# 4. Async generator with send() / throw() / aclose()
# =============================================================================

async def accumulator():
    """Receives values via asend() and yields running totals."""
    total = 0
    while True:
        value = yield total             # yield pauses; send() resumes with a value
        if value is None:
            break
        total += value
        await asyncio.sleep(0.05)

async def main_asend():
    gen   = accumulator()
    total = await gen.asend(None)       # Prime the generator (like next() on sync gen)
    print(f"  Initial total: {total}")

    for n in [10, 20, 30]:
        total = await gen.asend(n)
        print(f"  After sending {n}: total = {total}")

    await gen.aclose()                  # Close the generator cleanly

print("\n--- async generator asend / aclose ---")
asyncio.run(main_asend())


# =============================================================================
# 5. Class-based async iterator — __aiter__ + __anext__
# =============================================================================

class AsyncRange:
    """Async version of range() — pauses between each number."""

    def __init__(self, start, stop, step=1):
        self._current = start
        self._stop    = stop
        self._step    = step

    def __aiter__(self):
        return self                     # Iterator is its own iterable

    async def __anext__(self):
        if self._current >= self._stop:
            raise StopAsyncIteration    # Signal end of iteration
        await asyncio.sleep(0.1)
        value          = self._current
        self._current += self._step
        return value

async def main_class_iter():
    async for n in AsyncRange(0, 10, 2):
        print(f"  AsyncRange: {n}")

print("\n--- class-based async iterator ---")
asyncio.run(main_class_iter())


# =============================================================================
# 6. Async class with __aiter__ returning a separate async iterator object
# =============================================================================

class DatabaseRows:
    """Iterable that is NOT its own iterator — supports multiple concurrent iterations."""

    def __init__(self, table, count):
        self.table = table
        self.count = count

    def __aiter__(self):
        return DatabaseRowIterator(self.table, self.count)

class DatabaseRowIterator:
    def __init__(self, table, count):
        self.table   = table
        self.count   = count
        self._cursor = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._cursor >= self.count:
            raise StopAsyncIteration
        await asyncio.sleep(0.05)
        row = {"table": self.table, "row_id": self._cursor, "data": f"row-{self._cursor}"}
        self._cursor += 1
        return row

async def main_db_iter():
    rows = DatabaseRows("users", 4)
    async for row in rows:
        print(f"  {row}")

print("\n--- class iterator vs iterable separation ---")
asyncio.run(main_db_iter())


# =============================================================================
# 7. Async comprehensions and expressions
# =============================================================================

async def async_squares(n):
    for i in range(n):
        await asyncio.sleep(0.02)
        yield i * i

async def main_comprehensions():
    # Async list comprehension
    squares = [x async for x in async_squares(6)]
    print(f"  squares: {squares}")

    # Async set comprehension
    unique = {x async for x in async_squares(5)}
    print(f"  unique squares: {unique}")

    # Async dict comprehension
    mapping = {i: x async for i, x in enumerate(async_squares(4))}
    print(f"  mapping: {mapping}")

    # Async generator expression — lazy evaluation
    gen  = (x async for x in async_squares(4) if x > 2)
    results = []
    async for val in gen:
        results.append(val)
    print(f"  filtered: {results}")

print("\n--- async comprehensions ---")
asyncio.run(main_comprehensions())


# =============================================================================
# 8. aiter() and anext() — Python 3.10+ built-in shortcuts
# =============================================================================

async def main_aiter_anext():
    gen  = countdown(3)
    ait  = aiter(gen)                   # Same as gen.__aiter__()

    first  = await anext(ait)
    second = await anext(ait)
    default = await anext(ait, "no more")   # Provide default instead of StopAsyncIteration
    done    = await anext(ait, "no more")

    print(f"  first={first}, second={second}, default={default}, done={done}")

print("\n--- aiter() / anext() built-ins (Python 3.10+) ---")
asyncio.run(main_aiter_anext())


# =============================================================================
# 9. Chaining async generators — pipeline of generators
# =============================================================================

async def produce_numbers(n):
    for i in range(n):
        await asyncio.sleep(0.05)
        yield i

async def square(gen):
    async for n in gen:
        await asyncio.sleep(0.02)
        yield n * n

async def filter_even(gen):
    async for n in gen:
        if n % 2 == 0:
            yield n

async def main_pipeline():
    pipeline = filter_even(square(produce_numbers(10)))
    results  = [n async for n in pipeline]
    print(f"  Pipeline (even squares of 0..9): {results}")

print("\n--- async generator pipeline ---")
asyncio.run(main_pipeline())
