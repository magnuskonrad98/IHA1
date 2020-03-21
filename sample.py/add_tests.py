import unittest
from add import add

class MyFirstTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(""), 0)

        self.assertEqual(add("1"), 1)
        self.assertEqual(add("4"), 4)

        self.assertEqual(add("1,2"), 3)
        self.assertEqual(add("5,7"), 12)
        self.assertEqual(add("4,6"), 10)


if __name__ == '__main__':
    unittest.main()