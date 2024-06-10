"""
__new__

Constructor of a class is __new__ and  __init__ is only a initializer !
__new__ will be called first and after the __init__ !

"""


class Person:

    def __init__(self, name):
        self.name = name

    def __new__(cls, name, *args, **kwargs):
        if name == 'admin':
            return None
        else:
            return super().__new__(cls, *args, **kwargs)


p1 = Person('Hossein')
print(p1)

p2 = Person('admin')
print(p2)
