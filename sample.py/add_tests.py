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

        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("2,4,6,8"), 20)
        self.assertEqual(add("10,27,11"), 48)
        self.assertEqual(add("1,4,9,16,25"), 55)

        self.assertEqual(add("3\n5\n7"), 15)
        self.assertEqual(add("1,2\n3"), 6)

        self.assertEqual(add("1000,2"), 1002)
        self.assertEqual(add("1001,2"), 2)
        self.assertEqual(add("9000\n9\n2000,1"), 10)


if __name__ == '__main__':
    unittest.main()