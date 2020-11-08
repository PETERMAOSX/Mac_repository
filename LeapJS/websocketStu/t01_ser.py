import asyncio
import websockets

#协同程序
async def hello(websocket,path):
    name = await websockt.recv()
    print(f"< {name}")
    
    greeting = f"hello {name}!"
    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.server(hello,'localhost',8765)
#当启动这个链接的时候会调用这个函数
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
