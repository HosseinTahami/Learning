import asyncio, datetime

async def cook_meal():
    print("Start Cooking !")
    await asyncio.sleep(5)
    print("Cooking Done !")
    return "Meal is Ready !"

async def wash_dishes():
    print("Start Washing Dishes !")
    await asyncio.sleep(4)
    print("Washing Done !")
    return "Dishes are Ready !"

async def main():

    start_time = datetime.datetime.now()
    batch = asyncio.gather(cook_meal(), wash_dishes())
    first_task_result, second_task_result = await batch
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    print("first_task_result:", first_task_result)
    print("second_task_result:", second_task_result)

if __name__ == "__main__":
    asyncio.run(main())

"""
    $ python main-async.py
        Start Cooking !
        Start Washing Dishes !
        Washing Done !
        Cooking Done !
        0:00:05.001192
"""