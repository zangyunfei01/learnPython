#!/usr/bin/env python3
import unittest
from api_test.test_function.members_list import *


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('run only once before test cases')

    @classmethod
    def tearDownClass(cls):
        print('run only once after test cases')

    def test_status_code(self):
        try:
            r.raise_for_status()
        except requests.RequestException as e:
            print(e)
        else:
            return r.raise_for_status()

    def test_data_is_not_empty(self):
        try:
            self.assertIsNotNone(get_response_body())
        except Exception as e:
            print(e, 'response body is null')
        else:
            return get_response_body()


if __name__ == '__main__':
    unittest.main()
