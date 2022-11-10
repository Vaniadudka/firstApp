from kl8 import *
import unittest

class My_test(unittest.TestCase):
    def test_args(self):
        self.assertEqual(add(2, 2), 4)
        self.assertMinusEqual(add(4, 2), 2)
        self.assertMultiLineEqual(add(2, 2), 4)
        self.assertDivisionLineEqual(add(4, 2), 2)


    def test_kwargs(self):
        self.assertEqual(add(a=10, b=20), 30)
        self.assertMinusEqual(add(a=30, b=20), 10)
        self.assertMultiLineEqual(add(a=10, b=3), 30)
        self.assertDivisionLineEqual(add(a=30, b=3), 10)


    def test_mixed(self):
        self.assertEqual(add(3, x=8), 11)
        self.assertMinusEqual(add(11, x=8), 3)
        self.assertMultiLineEqual(add(3, x=4), 12)
        self.assertDevisionLineEqual(add(12, x=4), 3)


    def test_deff(self):
        x = 10
        y  = 0
        self.assertEqual(add(0, -5, y, a=x), 5)
        self.assertMinusEqual(add(0, 15, y, a=x), 5)
        self.assertMultiLineEqual(add(0, 5, y, a=x), 50)
        self.assertDictvisionlineEqual(add(0, 50, y, a=x), 5)



    def test_wrong_datatype(self):
        self.assertEqual(add("5", "abc", 10), 15)
        self.assertEqual(add("15", "abc", 10), 5)
        self.assertEqual(add("5", "abc", 10), 50)
        self.assertEqual(add("50", "abc", 10), 5)

if __name__ == "__main__":
    unittest.main()