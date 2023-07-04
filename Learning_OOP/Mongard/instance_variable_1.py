# variable => 1.instance 2.class

class Car:
    
    wheel_number = 4
    obj_nums = 0
    def __init__(self, n, p) -> None:
        self.name = n
        self.price = p
        __class__.obj_nums += 1
    def show(self):
        print(f'{self.name} costs {self.price}$ and has {self.wheel_number} wheels')
        print(f'{self.name} costs {self.price}$ and has {Car.wheel_number} wheels')
        print(f'{self.name} costs {self.price}$ and has {__class__.wheel_number} wheels')

c1 = Car('Benz', '990')
c2 = Car('Pride', '100')
c1.wheel_number = 5
c1.show()
c2.show()
print(c1.__dict__)
print(Car.__dict__)
print(c2.__dict__)
print(Car.obj_nums)

# https://www.mongard.ir/courses/python-beginner-course/episode/32/python-class-variable/