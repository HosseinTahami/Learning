class Car:
    wheel_number = 4
    def __init__(self, name) -> None:
        self.name = name
    
    def show(self):
        print(f'I have a {self.name}')

class Motor(Car):
    wheel_number = 2
    def __init__(self, name, helmet:bool) -> None:
        super().__init__(name)
        self.helmet = helmet
        
    def show(self):
        super().show()
        print(f'I Ride {self.name}')
        
m1 = Motor('Honda')
m1.show()


#help(m1) # Method Resolution Order | MRO 

# https://www.mongard.ir/courses/python-beginner-course/episode/34/python-inheritance/