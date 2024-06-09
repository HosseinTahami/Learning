"""
Method Resolution Order
"""


class Car:  # Parent | Superclass
    wheel_number = 4

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'I have a {self.name} !')


class Motor(Car):  # Child | Subclass

    wheel_number = 2  # Over Ride

    def __init__(self, name, price):
        super().__init__(name)
        self.price = price


m1 = Motor("Honda", 2300)
m1.show()
help(m1)
