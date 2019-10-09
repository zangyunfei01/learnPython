#!/usr/bin/env python3

import unittest
import requests
import json
from api_test.global_params import GlobalParams

'''GET /v2/members/list'''

url = "https://test-apis.520yidui.com/v2/members/list"
headers = {
    "Authorization": GlobalParams.Authorization,
    "MemberId": GlobalParams.MemberId}
params = {"category": "home", "page": 1}

r = requests.get(url, headers=headers, params=params, timeout=1)


def get_status_code(response):
    try:
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        print(response.status_code)
        return response.status_code


def get_response_body():
    return json.loads(r.content)


def required_params():
    params_without_category = {"category": "home"}
    params_without_home = {"category": "home", "page": 1}

    r1 = requests.get(url, headers=headers, params=params_without_category)
    r2 = requests.get(url, headers=headers, params=params_without_home)
    r3 = requests.get(url, headers=headers)
    return get_status_code(r1), get_status_code(r2), get_status_code(r3)
