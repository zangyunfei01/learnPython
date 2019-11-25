#!/usr/bin/python3

import requests
import json
import ddt
from api_test.data_provider.headers import get_headers_by_test_account
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

base_url = 'https://api.520yidui.com'
path = '/v2/chats/list'
headers = get_headers_by_test_account('18310061886', '1886')
params = {'page': 1, 'chat_type': 'be_likeds'}


def get_response_body():
    try:
        r = requests.get(url=base_url + path, headers=headers, params=params)
        r.raise_for_status()
        response_body = json.loads(r.text)
        if len(response_body) == 0:
            return logger.info('response is null')
        else:
            logger.info(f'response body is {response_body}')
            return response_body
    except requests.RequestException as e:
        print(e)


def get_last_msg():
    last_msg = []
    for x in get_response_body():
        for y, z in x.items():
            if y == 'last_msg':
                last_msg.append(z)
    logger.info(f'last msg is :{last_msg}')
    return last_msg


if __name__ == '__main__':
    print(len(get_last_msg()))
