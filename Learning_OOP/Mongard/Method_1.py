class Car:
    def __init__(self, n, p) -> None: # initializer \ built-in
        self.name = n
        self.price = p
    
    def show(self):
        print(f'{self.name} costs {self.price}')



c1 = Car("Benz", 990)
c2 = Car("Pride", 100)
c1.show()