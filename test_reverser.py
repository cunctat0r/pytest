import unittest
from reverser import Reverser 

class SecondTestClass(unittest.TestCase):
    def setUp(self):
        self.test_val = "Hi world"
        self.reverser = Reverser()

    def test_reverse(self):
        self.assertEqual("dlrow iH", self.reverser.reverse(self.test_val))
    

if __name__ == '__main__':
    unittest.main()
