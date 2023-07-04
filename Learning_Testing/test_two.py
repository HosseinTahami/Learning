import unittest
from two import *

class TwoTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4,5), 9)
        self.assertEqual(add(-1,4), 3)
    
    def test_substract(self):
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(4, 2), 2)
    
    def test_multiply(self):
        self.assertEqual(multiply(1,8), 8)
        self.assertEqual(multiply(10,2), 20)
    
    def test_division(self):
        #self.assertEqual(division(12, 0), ZeroDivisionError)
        self.asserRaises(ZeroDivisionError, division, 34, 0 )
        #self.asserRaises(ZeroDivisionError, division, 34, 4 )
        self.assertEqual(division(12,3), 4)

if __name__ == '__main__' :
    unittest.main()

# python3 -m unittest -v test_two.py
#pythone -m unittest discover
