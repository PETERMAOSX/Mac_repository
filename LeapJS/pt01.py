# import time
# import asyncio
# async def hello():
#     time.sleep(1)

# def run():
#     for i in range(5):
#         hello()
#         print("Hello World:%s" % time.time())
# run()
import time
import asyncio

count = 0
async def hello():
    global count
    count += 1
    asyncio.sleep(1)
    print("Hello World:%s"%time.time())
def run():
    for i in range(5):
        loop.run_until_complete(hello())
        print(count)
loop = asyncio.get_event_loop()
if __name__ == "__main__":
    run()