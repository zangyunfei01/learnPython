#!/usr/bin/env python3

import requests
from api_test.data_provider.global_params import GlobalParams

'''GET /v2/members/list'''

url = "https://test-apis.520yidui.com/v2/members/list"
headers = {
    "Authorization": GlobalParams.Authorization,
    "MemberId": GlobalParams.MemberId}

base_response = {"id": str,
                 "member_id": int,
                 "avatar_url": str,
                 "sex": int,
                 "nickname": str,
                 "age": int,
                 "height": int,
                 "is_trump": bool,
                 "monologue_status": int,
                 "monologue": str,
                 "online": int,
                 "vip": bool,
                 "active": str,
                 "current_location": dict
                 }

base_response_temp = {"id": int,
                      "member_id": int,
                      "avatar_url": str,
                      "sex": int,
                      "nickname": str,
                      "age": int,
                      "height": int,
                      "is_trump": bool,
                      "monologue_status": int,
                      "monologue": str,
                      "online": int,
                      "vip": bool,
                      "active": str,
                      "current_location": dict
                      }

