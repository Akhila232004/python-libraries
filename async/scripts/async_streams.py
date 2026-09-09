# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : asyncio Streams — TCP server with start_server(),
#                 client with open_connection(), echo server, line-protocol,
#                 multiple clients, graceful shutdown
#  Author       : Team Tinitiate
# ==============================================================================

import asyncio


# =============================================================================
# 1. Echo server + client — simplest TCP server pattern
# =============================================================================

async def echo_handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    """Called once per connected client."""
    addr = writer.get_extra_info('peername')
    print(f"  [Server] Client connected: {addr}")

    while True:
        data = await reader.read(1024)
        if not data:
            break                           # Client disconnected
        message = data.decode().strip()
        print(f"  [Server] Received: {message!r}")
        writer.write(f"ECHO: {message}\n".encode())
        await writer.drain()                # Flush write buffer

    print(f"  [Server] Client disconnected: {addr}")
    writer.close()
    await writer.wait_closed()

async def echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8881)
    writer.write(f"{message}\n".encode())
    await writer.drain()
    response = await reader.readline()
    print(f"  [Client] Got: {response.decode().strip()}")
    writer.close()
    await writer.wait_closed()

async def main_echo():
    server = await asyncio.start_server(echo_handler, '127.0.0.1', 8881)
    async with server:
        await echo_client("Hello, Server!")
        await echo_client("How are you?")

print("--- echo server ---")
asyncio.run(main_echo())


# =============================================================================
# 2. Line-protocol server — read complete lines with readline()
# =============================================================================

async def line_protocol_handler(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"  [Server] {addr} connected")
    try:
        while True:
            line = await reader.readline()  # Reads up to and including '\n'
            if not line:
                break
            command = line.decode().strip()
            print(f"  [Server] Command: {command!r}")
            if command.upper() == "QUIT":
                writer.write(b"BYE\n")
                await writer.drain()
                break
            else:
                writer.write(f"OK: {command}\n".encode())
                await writer.drain()
    finally:
        writer.close()
        await writer.wait_closed()

async def line_client(commands):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8882)
    for cmd in commands:
        writer.write(f"{cmd}\n".encode())
        await writer.drain()
        response = await reader.readline()
        print(f"  [Client] Response: {response.decode().strip()!r}")
    writer.close()
    await writer.wait_closed()

async def main_line_protocol():
    server = await asyncio.start_server(line_protocol_handler, '127.0.0.1', 8882)
    async with server:
        await line_client(["PING", "STATUS", "QUIT"])

print("\n--- line-protocol server ---")
asyncio.run(main_line_protocol())


# =============================================================================
# 3. Multiple concurrent clients — server handles them simultaneously
# =============================================================================

async def slow_handler(reader, writer):
    addr = writer.get_extra_info('peername')
    data = await reader.read(256)
    name = data.decode().strip()
    print(f"  [Server] {name} started processing")
    await asyncio.sleep(0.5)               # Simulate slow processing
    response = f"Result for {name}\n"
    writer.write(response.encode())
    await writer.drain()
    print(f"  [Server] {name} done")
    writer.close()
    await writer.wait_closed()

async def slow_client(port, name):
    reader, writer = await asyncio.open_connection('127.0.0.1', port)
    writer.write(f"{name}\n".encode())
    await writer.drain()
    response = await reader.readline()
    print(f"  [Client-{name}] received: {response.decode().strip()!r}")
    writer.close()
    await writer.wait_closed()

async def main_multiple_clients():
    server = await asyncio.start_server(slow_handler, '127.0.0.1', 8883)
    async with server:
        # Launch 5 clients concurrently — server handles all simultaneously
        clients = [slow_client(8883, f"user-{i}") for i in range(5)]
        await asyncio.gather(*clients)

print("\n--- multiple concurrent clients ---")
asyncio.run(main_multiple_clients())


# =============================================================================
# 4. Streaming data — server sends chunks, client reads them
# =============================================================================

async def stream_server_handler(reader, writer):
    await reader.read(32)               # Read client's request
    for i in range(5):
        chunk = f"chunk-{i}\n".encode()
        writer.write(chunk)
        await writer.drain()
        await asyncio.sleep(0.1)
    writer.close()
    await writer.wait_closed()

async def stream_client_reader(port):
    reader, writer = await asyncio.open_connection('127.0.0.1', port)
    writer.write(b"STREAM\n")
    await writer.drain()

    while True:
        line = await reader.readline()
        if not line:
            break
        print(f"  [Client] chunk received: {line.decode().strip()!r}")

    writer.close()
    await writer.wait_closed()

async def main_streaming():
    server = await asyncio.start_server(stream_server_handler, '127.0.0.1', 8884)
    async with server:
        await stream_client_reader(8884)

print("\n--- streaming server to client ---")
asyncio.run(main_streaming())


# =============================================================================
# 5. Server with graceful shutdown — stop accepting new connections cleanly
# =============================================================================

client_count = 0

async def counting_handler(reader, writer):
    global client_count
    client_count += 1
    writer.write(f"You are client #{client_count}\n".encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main_graceful_shutdown():
    global client_count
    client_count = 0

    server = await asyncio.start_server(counting_handler, '127.0.0.1', 8885)
    print("  [Server] Started")

    # Serve 3 clients then shut down
    async with server:
        for i in range(3):
            reader, writer = await asyncio.open_connection('127.0.0.1', 8885)
            line = await reader.readline()
            print(f"  [Client-{i}] {line.decode().strip()}")
            writer.close()
            await writer.wait_closed()

    print(f"  [Server] Gracefully shut down after {client_count} clients")

print("\n--- graceful shutdown ---")
asyncio.run(main_graceful_shutdown())
