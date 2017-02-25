import unittest

class BaseTestClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(120, 100 + 20)
        self.assertFalse(10 > 20)
        self.assertGreater(120, 110)

    def testSub(self):
        self.assertEqual(70, 90 - 20)

if __name__ == '__main__':
    unittest.main()
