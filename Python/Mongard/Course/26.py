"""
@property ==> It is like method but do not need parentheses when you call it!
"""


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def email(self):
        return f'{self.first_name}_{self.last_name}@email.com'

    def __str__(self):
        return f'{self.full_name()} || {self.email}'


p1 = Person("Hossein", "Tahami")
print(p1)
p1.first_name = "Ali"
print(p1)
