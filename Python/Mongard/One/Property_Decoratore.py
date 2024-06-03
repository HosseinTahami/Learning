"""
@property
"""

class Person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        self._email = f'{self.fname}_{self.lname}@gmail.com'
    
    def full_name(self):
        return f'{self.fname} {self.lname}'
    
    @property # getter
    def email(self):
        return f'{self.fname}_{self.lname}@gmail.com'
    
    @email.setter # property_name.setter decorator
    def email(self, value):
        self._email = value
    
    @email.deleter # property_name.deleter decorator
    def email(self, value):
        print('Deleting...')
        del self._email
        
        
        
p1 = Person('Hossein', 'Tahami')
p1.fname = 'Ali'
print('First Name:', p1.fname, '/ Last Name:', p1.lname, '/ Email:', p1._email)
print(p1.full_name())
print(p1.email)

