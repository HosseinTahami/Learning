"""
Coroutines
    Python functions which have stop inside their body!
"""
import asyncio
import datetime

async def main(name):
    await asyncio.sleep(2)
    print(f"Hello, {name}")

print(datetime.datetime.second)
asyncio.run(main("Hossein"))
asyncio.run(main("Kevin"))
print(datetime.datetime.second)