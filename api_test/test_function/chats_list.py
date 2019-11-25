#!/usr/bin/env python3
from api_test.data_provider.headers import get_headers_by_test_account
import requests
import json
import ddt

"""
获取chats/list的喜欢我的人的所有last_msg
"""


class ChatsList:
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def get_response_body(self):
        r = requests.get(url=self.url, headers=self.headers, params=self.params)
        return json.loads(r.text)


if __name__ == '__main__':
    url = 'https://api.520yidui.com/v2/chats/list'
    headers = get_headers_by_test_account('18310061886', '1886')
    params = {'page': 1, 'chat_type': 'be_likeds'}
    chatslist = ChatsList(url, headers, params)
    print(chatslist.get_response_body())
