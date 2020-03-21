import unittest
from add import add

class MyFirstTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(""), 0)


if __name__ == '__main__':
    unittest.main()