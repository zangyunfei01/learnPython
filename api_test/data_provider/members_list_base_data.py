#!/usr/bin/env python3

import requests
import api_test.data_provider.headers

'''GET /v2/members/list'''

url = "https://test-apis.520yidui.com/v2/members/list"
headers = api_test.data_provider.headers.get_headers_by_test_count('18700000003', '123456')

'''category和page均为非必需参数'''

base_response_type = {"id": [str],
                      "member_id": [int],
                      "avatar_url": [str],
                      "sex": [int],
                      "nickname": [str],
                      "age": [int],
                      "height": [int],
                      "is_trump": [bool],
                      "monologue_status": [int],
                      "monologue": [type(None), str],
                      "online": [int],
                      "vip": [bool],
                      "active": [str],
                      "current_location": {
                          "province": [str],
                          "city": [str],
                          "district": [str]
                      }
                      }

