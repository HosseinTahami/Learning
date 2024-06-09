"""
Encapsulation (For Important Attributes)

    - Setter
    - Getter
    - Deleter

    Now There is no Direct access to the important Attributes !
"""


class Person:

    """
    In Person Class we are Encapsulating 'age' attribute
    but not in the python way !

    This Type of Encapsulating is usually used in Java language !
    """

    def __init__(self, age):
        self.__age = age  # Private Attribute

    def getter_age(self):
        return self.__age

    def setter_age(self, new_age):
        self.__age = new_age

    def deleter_age(self):
        del self.__age


p1 = Person(32)


class Car:

    """
    Encapsulating 'price' Attribute in python way !
    """

    def __init__(self, price):
        self.__price = price

    @property
    def Price(self):
        return self.__price

    @Price.setter
    def Price(self, new_price):
        self.__price = new_price

    @Price.deleter
    def Price(self):
        del self.__price


c1 = Car(5000)
print(c1.Price)
c1.Price = 2000
print(c1.Price)
del c1.Price
try:
    print(c1.Price)
except AttributeError:
    print("There is no price Attribute Anymore!")


"""
https://www.mongard.ir/one_part/30/python-encapsulation/
"""
