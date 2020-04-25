#!/usr/bin/env python3

import unittest
from api_automation.test_function.chats_list import *


class TestChatsList(unittest.TestCase):
    url = 'https://api.520yidui.com/v2/chats/list'
    headers = get_headers_by_test_account('18310061886', '1886')
    params = {'page': 1, 'chat_type': 'be_likeds'}

    @classmethod
    def setUpClass(cls):
        print('\nchats list test begin!\n')

    @classmethod
    def tearDownClass(cls):
        print('\nchats list test finished!\n')

    def test_response_type(self):
        chats_list = ChatsList(self.url, self.headers, self.params)
        diff_count = chats_list.get_response_type_diff_count()
        self.assertEqual(diff_count, 0)


if __name__ == '__main__':
    unittest.main()
