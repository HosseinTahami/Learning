"""
- Abstract Class: A class which contains one or more abstract methods.
    Prevents user from creating an object from that class
    Compels user to override abstract methods in a child class

- Abstract Method: A method that has a declaration but does not have an implementation.
"""
# abc: abstract base class

from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def show(self):
        ...


class B(A):

    def show(self):
        print("Show method !")


try:
    a = A()
except TypeError:
    print("Can not create object from class A !")

b1 = B()


"""
Link:
https://www.mongard.ir/one_part/29/python-abstract-class/
"""
