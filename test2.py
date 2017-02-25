import unittest

class FirstTestClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(120, 100 + 20)

class SecondTestClass(unittest.TestCase):
    def setUp(self):
        self.val = 90
    
    def test_sub(self):        
        self.assertEqual(self.val, 100 - 10)
        self.val -= 40
        self.assertEqual(50, self.val)

    def test_mul(self):        
        self.assertEqual(180, self.val * 2)
        self.assertGreater(181, self.val * 2)

if __name__ == '__main__':
    unittest.main()
