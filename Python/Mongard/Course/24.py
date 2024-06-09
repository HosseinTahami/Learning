class Car:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name} costs {self.price}$ !")

    def __str__(self):
        return f'{self.name} || {self.price}'

    def __add__(self, other):
        return self.price + other.price

    def __len__(self):
        return len(self.name)


c1 = Car('Benz', 950)
c2 = Car('Pride', 20)

print(c1)  # ==> Benz || 950
print(c1 + c2)  # ==> 950 + 20
print(len(c2))  # ==> Pride | 5 Character
