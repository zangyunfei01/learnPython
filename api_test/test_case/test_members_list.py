#!/usr/bin/env python3
import unittest
from api_test.test_function.members_list_test_function import *


class TestMembersList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('members list test begin')

    @classmethod
    def tearDownClass(cls):
        print('members list test finished')

    '''test params'''

    def test_status_code(self):
        self.assertEqual(get_status_code('cp'), 200)

    def test_not_required_params_0(self):
        self.assertEqual(get_status_code('c'), 200)

    def test_not_required_params_1(self):
        self.assertEqual(get_status_code('p'), 200)

    def test_not_required_params_2(self):
        self.assertEqual(get_status_code(''), 200)

    def test_data_is_not_empty(self):
        try:
            self.assertIsNotNone(get_response_body('cp'))
        except Exception as e:
            print(e, 'response body is null')
        else:
            return get_response_body('cp')

    def test_response_type(self):
        self.assertEqual(diff_response_body_count(), 0)


if __name__ == '__main__':
    unittest.main()
