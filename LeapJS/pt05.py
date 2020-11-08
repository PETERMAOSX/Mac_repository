import asyncio
import websockets
import json
async def sendData(uri, data):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(data))

def main():
    text = "sample data"
    asyncio.get_event_loop().run_until_complete(
        sendData("ws://localhost:5678", {"msg": text})
    )

main()