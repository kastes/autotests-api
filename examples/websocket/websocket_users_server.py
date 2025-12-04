"""Echo server using the asyncio API."""

import asyncio

from websockets.asyncio.server import serve


async def echo(websocket):
    async for message in websocket:
        print(f"Получено сообщение от клиента: {message}")
        for n in range(1, 6):
            await websocket.send(f"{n} Сообщение пользователя: {message}")


async def main():
    async with serve(echo, "localhost", 8765) as server:
        print("WebSocket сервер на localhost:8765")
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
