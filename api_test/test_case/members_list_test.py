#!/usr/bin/env python3
import unittest
from api_test.api.members_list import *


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('run only once before test cases')

    @classmethod
    def tearDownClass(cls):
        print('run only once after test cases')

    def test_status_code(self):
        self.assertEqual(get_status_code(r), 200)

    def test_response_body_not_null(self):
        self.assertNotEqual(get_response_body(), None)

    def test_required_params(self):
        self.assertEqual(required_params(), (200, 200, 200))


if __name__ == '__main__':
    unittest.main()
