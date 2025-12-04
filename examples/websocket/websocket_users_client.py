"""Client using the asyncio API."""

import asyncio

from websockets.asyncio.client import connect


async def hello():
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Привет world!")
        for _ in range(5):
            message = await websocket.recv()
            print(message)


if __name__ == "__main__":
    asyncio.run(hello())
