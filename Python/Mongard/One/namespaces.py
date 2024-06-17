"""
    NameSpaces:
        1. Built-In
            2. Global | globals()
                3. Enclosed
                    4. Local | locals()

    python search from Local to Built-In

"""

x = 1  # Global


def show():
    x = 2  # Enclosed

    def go():
        x = 3  # Local


print(dir(__builtins__))
"""
['ArithmeticError', 'AssertionError',
 'AttributeError', 'BaseException',
 'BlockingIOError','BrokenPipeError', ...]
"""

print(globals())

"""
{'__name__': '__main__', '__doc__': '\n
NameSpaces:\n  1. Built-In\n
2. Global\n  3. Enclosed\n 4. Local\n 
python search from Local to Built-In\n',
'__package__': None, '__loader__':... }
"""


def hello(x, y):
    z = 1
    print(locals())
    """ {'x': 3, 'y': 2, 'z':1} """


hello(3, 2)

########
j = 1


def one():
    j = 2
    print(j)


one()  # --> 2
print(j)  # --> 1
#########

#########
k = 1


def two():
    global k
    k = 2
    print(k)


two()  # -->  2
print(k)  # --> 2
#########

###############


def outer():
    x = 1

    def inner():
        x = 2
        print(x)  # --> 2
    inner()
    print(x)  # --> 1


outer()


###############


def outside():
    x = 1

    def inside():
        nonlocal x
        x = 2
        print(x)
    inside()
    print(x)  # --> 2


outside()  # --> 2

################
