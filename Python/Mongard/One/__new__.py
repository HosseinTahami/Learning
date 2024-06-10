"""
__new__

Constructor of a class is __new__ and  __init__ is only a initializer !
__new__ will be called first and after that the __init__ !

"""


class Person:

    def __init__(self, name):
        self.name = name

    def __new__(cls, name, *args, **kwargs):
        """
        __new__ should always return the __new__ father method, otherwise
        the object will not be created and it will be None
        """
        if name == 'admin':
            return None
        else:
            return super().__new__(cls, *args, **kwargs)


p1 = Person('Hossein')
print(p1)

p2 = Person('admin')
print(p2)

"""
https://www.mongard.ir/one_part/26/new-python/
"""
