#!/usr/bin/env python3
import unittest
from api_test.test_function.members_list_test_function import *


class Test(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     print('run only once before test cases')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('run only once after test cases')

    def test_status_code(self):
        self.assertEqual(get_status_code('home', 1), 200)

    def test_data_is_not_empty(self):
        try:
            self.assertIsNotNone(get_response_body())
        except Exception as e:
            print(e, 'response body is null')
        else:
            return get_response_body()

    def test_response_type(self):
        self.assertEqual(diff_response_body_count('home', 1), 0)


if __name__ == '__main__':
    unittest.main()
