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

# id(second) and id(first   ) are equal
print(id(first))
print(id(second))
