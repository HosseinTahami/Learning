import unittest
from three import *

class ThreeTest(unittest.TestCase):
    
    def setUp(self):
        self.p1 = Person('Hossein', 'Tahami')
        self.p2 = Person('Ali', 'Pourzad')
        
    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'Hossein Tahami')
        self.assertEqual(self.p2.fullname(), 'Ali Pourzad')
    
    def test_email(self):        
        self.assertEqual(self.p1.email(), 'HosseinTahami@email.com')
        self.assertEqual(self.p2.email(), 'AliPourzad@email.com')
        
    def tearDown(self):
        print('Nice Job Buddy you are becoming a retarted Developer !')
    
if __name__ == '__main__' :
    unittest.main()
    