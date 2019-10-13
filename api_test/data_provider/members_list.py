#!/usr/bin/env python3

import requests
from api_test.data_provider.global_params import GlobalParams

'''GET /v2/members/list'''

url = "https://test-apis.520yidui.com/v2/members/list"
headers = {
    "Authorization": GlobalParams.Authorization,
    "MemberId": GlobalParams.MemberId}
required_params = {"category": "home", "page": 1}

r = requests.get(url, headers=headers, params=required_params, timeout=1)

