import time
import asyncio


async def sleeep():
    print("start sleep")
    await asyncio.sleep(3)
    print("stop sleep")


async def generate_file():
    print('start generate ', time.strftime('%X'))
    await asyncio.sleep(5)
    output = open('generated.txt', 'w')
    output.write(time.strftime('%X'))
    print('stop generate ', time.strftime('%X'))
    output.close()