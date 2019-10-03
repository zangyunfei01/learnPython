import unittest

import self as self

from learn_unittest.test_math_function import TestMathFunction

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(TestMathFunction('test_add'))
    # suite.addTest(TestMathFunction('test_minus'))
    tests = [TestMathFunction('test_add'), TestMathFunction('test_minus'), TestMathFunction('test_multi'),
             TestMathFunction('test_divide')]
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
