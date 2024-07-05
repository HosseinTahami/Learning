import time, datetime

def cook_meal():
    print("Start Cooking !")
    time.sleep(5)
    print("Cooking Done !")
    return "Meal is Ready !"

def wash_dishes():
    print("Start Washing Dishes !")
    time.sleep(4)
    print("Washing Done !")
    return "Dishes are Ready !"

def main():
    start_time = datetime.datetime.now()
    cook_meal() 
    wash_dishes()
    end_time = datetime.datetime.now()
    elapsed_time = end_time - start_time
    print(elapsed_time)


if __name__ == "__main__":
    main()

"""
    $ python main.py 
        Start Cooking !
        Cooking Done !
        Start Washing Dishes !
        Washing Done !
        0:00:09.000287
"""