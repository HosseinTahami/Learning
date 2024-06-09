a = 10  # Global Scope


def show():
    b = 20  # Local Scope
    print(a)  # Print 10 (The Global one)


def hello():
    """
    The variable 'a' is a new variable
    and differs from the Global one !
    """
    a = 20
    print(a)  # print 20 (The local one)


def what():
    """
    UnboundLocalError:
    local variable 'a' referenced before assignment
    """
    print(a)
    a = 10


def say():
    """
    This will change the variable 'a' which is a global variable 
    and will not create a new variable
    """
    global a
    a = 20
