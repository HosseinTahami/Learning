"""
Method Types in OOP:
1. Instance
2. Class
3. Static
"""
import datetime


class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    # Instance Method | Regular Method
    def show(self):
        print(f'{self.name} is {self.height} centimeter and {self.age} years old !')

    # Class Method
    @classmethod
    def from_birth(cls, name, height, date_of_birth):
        return cls(name, height, datetime.datetime.now().year - date_of_birth)

    # Static Method
    @staticmethod
    def is_adult(age):
        if age >= 18:
            print("True")
        else:
            print("False")


p1 = Person.from_birth("Hossein", 173, 2000)
p1.show()
Person.is_adult(23)
