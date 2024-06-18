"""
    Python Class Variables Evaluate on Declaration or Import !

    If you run this file (python one.py) or file two.py (python two.py),
    it will say 'This is class A' !
"""


class A:
    def __init__(self):
        print("This is class A !")


class B:
    a = A()
