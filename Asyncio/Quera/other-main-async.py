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

    cooking_task = asyncio.create_task(cook_meal())
    washing_task = asyncio.create_task(wash_dishes())
    
    result_cooking = await cooking_task
    result_washing = await washing_task

    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(elapsed_time)

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