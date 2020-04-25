#!/usr/bin/env python3

import requests
import json
from api_automation.log import logger
from api_automation.common.headers import get_headers_by_test_account


class Lives:

    def __init__(self, url, headers, **kwargs):
        self.url = url
        self.headers = headers

    def get_response_body(self):
        try:
            r = requests.get(url=self.url, headers=self.headers)
            r.raise_for_status()
            response_body = json.loads(r.text)
            if len(response_body) == 0:
                return logger().info('response is null')
            else:
                logger().info(f'response body is {response_body}')
                return json.loads(r.text)
        except requests.RequestException as e:
            print(e)


if __name__ == '__main__':
    url = "https://api.520yidui.com/v2/lives"
    headers = get_headers_by_test_account("18310061886", "1886")
    lives = Lives(url, headers=headers)
    lives.get_response_body()
