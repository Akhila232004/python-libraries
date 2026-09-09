# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Real-world async HTTP patterns using aiohttp —
#                 concurrent fetching, rate limiting with Semaphore,
#                 retry with backoff, streaming responses, POST requests
#  Requires     : pip install aiohttp
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio
import aiohttp


# =============================================================================
# 1. Basic concurrent GET requests — fetch multiple URLs at once
# =============================================================================

async def fetch(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        body = await response.json()
        return {"url": url, "status": response.status, "id": body.get("id")}

async def main_basic():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
    ]
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls])
    for r in results:
        print(f"  {r}")

print("--- concurrent GET ---")
asyncio.run(main_basic())


# =============================================================================
# 2. Rate-limited fetching — Semaphore caps concurrent requests
#    Avoids overwhelming the server or exceeding API rate limits.
# =============================================================================

MAX_CONCURRENT = 3

async def fetch_limited(session, semaphore, url):
    async with semaphore:
        async with session.get(url) as response:
            return {"url": url, "status": response.status}

async def main_rate_limited():
    base = "https://jsonplaceholder.typicode.com/todos"
    urls = [f"{base}/{i}" for i in range(1, 11)]
    sem  = asyncio.Semaphore(MAX_CONCURRENT)

    async with aiohttp.ClientSession() as session:
        tasks   = [fetch_limited(session, sem, url) for url in urls]
        results = await asyncio.gather(*tasks)

    print(f"  Fetched {len(results)} URLs, {MAX_CONCURRENT} at a time")
    statuses = {r["status"] for r in results}
    print(f"  HTTP statuses seen: {statuses}")

print("\n--- rate-limited fetching ---")
asyncio.run(main_rate_limited())


# =============================================================================
# 3. Retry with exponential backoff — handle transient failures gracefully
# =============================================================================

async def fetch_with_retry(session, url, retries=3, backoff=0.5):
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                if resp.status >= 500:
                    raise aiohttp.ClientResponseError(
                        resp.request_info, resp.history, status=resp.status
                    )
                return await resp.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            last_exc = e
            wait = backoff * (2 ** (attempt - 1))   # 0.5s, 1s, 2s...
            print(f"  Attempt {attempt} failed ({e}). Retrying in {wait}s...")
            await asyncio.sleep(wait)
    raise RuntimeError(f"All {retries} attempts failed: {last_exc}")

async def main_retry():
    async with aiohttp.ClientSession() as session:
        try:
            data = await fetch_with_retry(
                session,
                "https://jsonplaceholder.typicode.com/posts/1"
            )
            print(f"  Success: title = {data['title'][:40]!r}")
        except RuntimeError as e:
            print(f"  Gave up: {e}")

print("\n--- retry with backoff ---")
asyncio.run(main_retry())


# =============================================================================
# 4. POST requests — create resources concurrently
# =============================================================================

async def create_post(session, payload):
    url = "https://jsonplaceholder.typicode.com/posts"
    async with session.post(url, json=payload) as response:
        result = await response.json()
        return {"status": response.status, "id": result.get("id")}

async def main_post():
    payloads = [
        {"title": "Post A", "body": "content A", "userId": 1},
        {"title": "Post B", "body": "content B", "userId": 2},
        {"title": "Post C", "body": "content C", "userId": 3},
    ]
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[create_post(session, p) for p in payloads])
    for r in results:
        print(f"  Created: {r}")

print("\n--- concurrent POST ---")
asyncio.run(main_post())


# =============================================================================
# 5. Streaming response — process large response body in chunks
#    Avoids loading the entire response into memory at once.
# =============================================================================

async def stream_response(session, url):
    total_bytes = 0
    async with session.get(url) as response:
        print(f"  Streaming from {url} (status {response.status})")
        async for chunk in response.content.iter_chunked(256):
            total_bytes += len(chunk)
    print(f"  Streamed {total_bytes} bytes total")

async def main_stream():
    async with aiohttp.ClientSession() as session:
        await stream_response(session, "https://jsonplaceholder.typicode.com/posts")

print("\n--- streaming large response ---")
asyncio.run(main_stream())


# =============================================================================
# 6. Session configuration — headers, timeout, connector limits
# =============================================================================

async def main_configured_session():
    connector = aiohttp.TCPConnector(
        limit=10,               # Max 10 open connections total
        limit_per_host=5,       # Max 5 to any single host
    )
    timeout = aiohttp.ClientTimeout(
        total=10,               # Entire request must finish in 10s
        connect=3,              # TCP connect must finish in 3s
    )
    headers = {
        "User-Agent": "TinitiateBot/1.0",
        "Accept":     "application/json",
    }

    async with aiohttp.ClientSession(
        connector=connector,
        timeout=timeout,
        headers=headers,
    ) as session:
        async with session.get("https://jsonplaceholder.typicode.com/users/1") as resp:
            user = await resp.json()
            print(f"  Fetched user: {user['name']} ({user['email']})")

print("\n--- configured ClientSession ---")
asyncio.run(main_configured_session())


# =============================================================================
# 7. Fan-out pattern — fetch details for each item in a list concurrently
#    Common pattern: paginated list → parallel detail fetches
# =============================================================================

async def fetch_user(session, user_id):
    async with session.get(f"https://jsonplaceholder.typicode.com/users/{user_id}") as r:
        data = await r.json()
        return {"id": data["id"], "name": data["name"], "city": data["address"]["city"]}

async def main_fanout():
    async with aiohttp.ClientSession() as session:
        users = await asyncio.gather(*[fetch_user(session, i) for i in range(1, 6)])
    print("  Users:")
    for u in users:
        print(f"    {u}")

print("\n--- fan-out detail fetching ---")
asyncio.run(main_fanout())
