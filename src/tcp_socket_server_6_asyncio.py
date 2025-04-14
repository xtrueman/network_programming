#!/usr/bin/env python3
"""
Final version of asyncio socket server.
Using standard high-level API with streams.
"""
import asyncio

HOST, PORT = ('localhost', 12345)

async def handle_connection(reader, writer):
    addr = writer.get_extra_info("peername")
    print("Connected by", addr)
    while True:
        # Receive
        try:
            data = await reader.read(1024)  # New
        except ConnectionError:
            print(f"Client suddenly closed while receiving from {addr}")
            break

        print(f"Received {data} from: {addr}")
        if not data:
            break

        # Process
        if data == b"close":
            break
        data = data.upper()

        # Send
        print(f"Sending: {data} to: {addr}")
        try:
            writer.write(data)  # New
            await writer.drain()
        except ConnectionError:
            print(f"Client suddenly closed, cannot send")
            break
    # Disconnect
    writer.close()
    print("Disconnected by", addr)


async def main(host, port):
    server = await asyncio.start_server(handle_connection, host, port)
    print(f"Start server...")
    async with server:
        await server.serve_forever()

asyncio.run( main(HOST, PORT) )
