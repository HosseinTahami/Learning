"""
Meta Class

"""


class A:
    """
    __new__ should always return the __new__ father method, otherwise
    the object will not be created and it will be None
    """
    def __new__(cls, *args, **kwargs):
        print(cls)  # <class '__main__.A'>
        return super().__new__(cls, *args, **kwargs)


a = A()
print(a)  # <__main__.A object at ...>
print(a.__class__)  # <class '__main__.A'>
print(a.__class__.__class__)  # <class 'type'>

"""
You can create an class and object with 'type'
'type' is a Meta Class and the most powerful in python
"""
p1 = type('Person', (), {})
print(p1)  # <class '__main__.Person'>


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class db(metaclass=Singleton):
    pass


db1 = db()
db2 = db()
print('first instance:', id(db1), '||', 'second instance:', id(db2))
