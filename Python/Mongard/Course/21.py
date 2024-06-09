"""
Variable Types in OOP:
1. Instance
2. Class
"""


class Car:
    wheels_number = 4
    obj_num = 0  # Number of Objects which was created !

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Car.obj_num += 1

    def show(self):
        print(f"{self.name} costs {self.price} and has {self.wheels_number} wheels !")


c1 = Car('Pride', 100)
c2 = Car('Benz', 900)

c1.show()
c1.wheels_number = 5
c1.show()

print(c1.__dict__)  # {'name': 'Pride', 'price': 100, 'wheels_number': 5}
print(c2.__dict__)  # {'name': 'Benz', 'price': 900}
print(Car.__dict__)
print(Car.obj_num)
