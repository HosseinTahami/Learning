"""
Polymorphism:
- Poly (Many)
- Morphism (Shapes)
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        ...


class Cat(Animal):
    def talk(self):
        print("Meow...")


class Dog(Animal):
    def talk(self):
        print("Woof...")


c1 = Cat("Rick")
d1 = Dog("Richard")

"""
Both of these methods are 'talk' but they have different results!
"""
c1.talk()
d1.talk()
