"""
Singleton:

Ensure the class only have one instance and provide a global point of access to it.
"""


"""
Implementing Singleton in a general way
"""


class A:

    _instance = None

    def __init__(self):
        """
        With this Error creating object via A() is impossible !
        """
        raise RuntimeError('Use get_instance() method !')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


"""
Implementing Singleton in Python way
"""


class Singleton(type):
    _instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class B(metaclass=Singleton):
    ...
