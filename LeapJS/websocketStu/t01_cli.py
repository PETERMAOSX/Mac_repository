import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        name = input("What's you name?")
        await websocket.send(name)
        print(f"> {name}")

        greening = await websocket.recv()
        print(f"< {greening}")

asyncio.get_event_loop().run_until_complete(hello())