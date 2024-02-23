from five import *
import pytest

def test_add():
    
    assert add(3, 6) == 9
    assert add(8, -2) == 6

def test_subtract():
    
    assert subtract(2, -4) == 6
    assert subtract(4, 4) != 99

def test_multiply():
    
    assert multiply(4, 0) == 0
    assert multiply(3, 2) == 6
    
def test_division():
    
    assert division(4, 2) == 2
    #assert division(3, 0) == ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        division(3, 0)


# pytest test_five.py