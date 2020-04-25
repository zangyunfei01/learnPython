#!/usr/bin/env python3
from api_automation import get_headers_by_test_account
from api_automation import base_response_type
import requests
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class ChatsList:
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def get_response_body(self):
        try:
            r = requests.get(url=self.url, headers=self.headers, params=self.params)
            r.raise_for_status()
            response_body = json.loads(r.text)
            if len(response_body) == 0:
                return logger.info('response is null')
            else:
                logger.info(f'response body is {response_body}')
                return json.loads(r.text)
        except requests.RequestException as e:
            print(e)

    def get_last_msg(self):
        last_msg = []
        for x in self.get_response_body():
            for k, v in x.items():
                if v == 'last_msg':
                    last_msg.append(v)
        logger.info(f'last msg is :{last_msg}')
        return last_msg

    """获取结果中的所有字段值，只需要第一个object中所有数据即可,并展开"""

    new_dict = {}

    def get_complete_response_body(self, data_dict):
        for k, v in data_dict.items():
            if k in self.new_dict:
                k = k + k
            if type(v) == dict:
                self.get_complete_response_body(v)
            else:
                self.new_dict[k] = v
                # print(k, v)
        # print(self.new_dict)
        return self.new_dict

    def get_response_type_diff_count(self):
        n = 0
        first_data = self.get_response_body()[0]
        first_complete_data = self.get_complete_response_body(first_data)
        for x, y in base_response_type.items():
            for k, v in first_complete_data.items():
                if x == k and y != type(v):
                    print(f'第 {n + 1} 组不同的数据为：')
                    print(f'   base data type is {x} : {y}')
                    print(f'actural data type is {k} : {type(v)}')
                    n += 1
                # if x == k and y == type(v):
                #     print(f'base data type is    {x} : {y}')
                #     print(f'actural data type is {k} : {type(v)}')
        if n == 0:
            print('well done!')
        else:
            print(f'diff count is {n}')
        return n


if __name__ == '__main__':
    url = 'https://api.520yidui.com/v2/chats/list'
    headers = get_headers_by_test_account('18310061886', '1886')
    params = {'page': 1, 'chat_type': 'be_likeds'}
    chatslist = ChatsList(url, headers, params)
    first_data = chatslist.get_response_body()[0]
    chatslist.get_complete_response_body(first_data)
    diff_count = chatslist.get_response_type_diff_count()
