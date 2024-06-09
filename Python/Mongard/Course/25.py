"""
Access Point Types:
1. Public | Can be used everywhere !
2. Protected | Can be used inside the class and inheritance classes ! (No Errors)
3. Private | Can be used only inside the class itself ! (Show Errors)
"""


class Person:
    name = 'Hossein'  # Public
    _age = 22  # Protected
    __height = 173  # Private


class Male(Person):
    ...


print(Person._age)
p = Person()

try:
    """
    AttributeError:
    type object 'Person' has no attribute '__height'
    """
    print(Person.__height)
except:
    print(Person._Person__height)  # Name Mangling

print(p._Person__height)
