"""
__call__:

Called when the instance is "called" as a function !
"""


class Dog:

    def __call__(self, *args, **kwargs):
        print("Woof...")


d1 = Dog()  # Create d1 instance or object
d1()  # the d1 instance or object is called like a function

"""
https://www.mongard.ir/one_part/27/python-call/
"""
