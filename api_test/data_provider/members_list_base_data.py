#!/usr/bin/env python3

import requests
from api_test.data_provider.global_params import GlobalParams

'''GET /v2/members/list'''

url = "https://api.520yidui.com/v2/members/list"
test_url = "https://test-apis.520yidui.com/v2/members/list"
headers = {
    "Authorization": GlobalParams.Authorization,
    "MemberId": GlobalParams.MemberId}

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


def test(key):
    if key == 'cp':
        params = {'category': 'home', 'page': 1}
    elif key == 'c':
        params = {'category': 'home'}
    elif key == 'p':
        params = {'page': 1}
    else:
        params = {}
    r = requests.get(url, params=params, headers=headers)
    print(r)


test('cp')
