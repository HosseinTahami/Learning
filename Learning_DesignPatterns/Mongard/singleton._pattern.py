"""
__call__
"""


class Person:
    def __call__(self, *args, **kwds):
        print("Calling ...")


p1 = Person()
print(p1())  # Calling ...
print(p1)  # <__main__.Person object at ...>


"""
__new__ : This method create a class not the initializer and before the initializer method run this method will run
            first, for example at first it will check if name is bad boy the Dog class will not be created but if its not
            then it will let the the class be created and also __new__ get cls not self !
"""


class Dog:
    def __init__(self, name):
        self.name = name

    def __new__(cls, name, *args, **kwargs):
        if name == "bad boy":
            return None
        else:
            return super().__new__(cls, *args, **kwargs)


"""
Meta Class
"""


class A:
    pass


a1 = A()
print(a1.__class__)  # <class __main__.A object at ..>
print(a1.__class__.__class__)  # <class 'type'>

""" type(name, base, dict) -> new type"""
a2 = type("Person", (), {})
print(a2)  # <__main__.Person object at ... >


"""
Make sure our class only have one instance
&
Provide a global point of access to it

"""
import collections as c1
import collections as c2
from typing import Any

# id(c1) and id(c2) are equal
print(id(c1))
print(id(c2))


# Implementation
class A:
    _instance = None

    def __init__(self):
        raise RuntimeError("call get_instance() instead !")

    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


first_try = A()
second_try = A.get_instance

# id(second_try) and id(first_try) are equal
print(id(first_try))
print(id(second_try))


class Singleton(type):
    _instance = None

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self._instance is None:
            self._instance = super().__call__
        return self._instance


class B(metaclass=Singleton):
    pass


first = B()
second = B()

# id(second) and id(first) are equal
print(id(first))
print(id(second))
