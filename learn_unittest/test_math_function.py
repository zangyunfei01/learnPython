#!/usr/bin/env python3


import unittest
from learn_unittest.math_function import *


class TestMathFunction(unittest.TestCase):
    """test math_function.py"""

    @classmethod
    def setUpClass(cls):
        print("run only once before class \n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("run only once after class \n")

    def setUp(self):
        print("run before every function")

    def tearDown(self):
        print("run after every function \n")

    def test_add(self):
        """test add function"""
        print(1)
        self.assertEqual(add(2, 3), 5)
        self.assertNotEqual(add(2, 3), 6)

    def test_minus(self):
        """test munus function"""
        print(2)
        self.assertEqual(minus(3, 2), 1)

    def test_multi(self):
        """test multi function"""
        print(3)
        self.assertEqual(multi(2, 3), 6)

    @unittest.skip("ye le yi")
    def test_divide(self):
        """test divide function"""
        print(4)
        self.assertEqual(divide(3, 2), 1.5)


if __name__ == '__main__':
    unittest.main()
