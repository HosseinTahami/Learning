# 'Car' Blueprint
class Car:
    pass


# 'pride', 'benz' Object | Instance
pride = Car()
benz = Car()

# '.' Dot Notation
# 'name', 'price' Attribute  | Property
pride.name = 'Pride'
benz.name = 'Benz'

pride.price = 100
benz.price = 700

print(benz.price)
print(f'{benz.name} cost {benz.price}$ !')
