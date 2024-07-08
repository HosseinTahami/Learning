import asyncio

async def question():
    print("Why can't programmers tell jokes?")
    await asyncio.sleep(3)


async def answer():
    print("Timing!")


async def main():
    await asyncio.gather(question(), answer())


if __name__ == "__main__":
    asyncio.run(main())