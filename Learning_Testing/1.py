def add(x, y):
    
    """
    >>> add(7, 6)
    13
    >>> add(-1, 4)
    3
    >>> add(9, 0)
    9
    """
    return x + y

def subtract(x, y):
    """
    >>> subtract(1,2)
    -1
    >>> subtract(-2,-6)
    4
    """
    return x - y

def multiply(x, y):
    """
    >>> multiply(0, 2)
    0
    >>> multiply(1,45)
    45
    >>> multiply(-1,-3)
    3
    """
    return x * y

# python -m doctest -v 1.py

#You can put the docstring outside the functions