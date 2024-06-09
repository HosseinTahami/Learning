"""
Method: Function inside a class !
"""


class Car:

    """
    Initializer
    Built-In Function
    Magic Method
    """

    def __init__(self, n, p):
        self.name = n
        self.price = p

    def show(self):
        print(f"{self.name} costs {self.price}$ !")


c1 = Car('Pride', 100)
c2 = Car('Benz', 700)


c1.show()
print(f"{c2.name} costs {c2.price}$ !")
