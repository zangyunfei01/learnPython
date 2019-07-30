#!/usr/bin/env python3

import requests
import json

url = {
    'ruby': 'https://test-apis.520yidui.com/v2/members/info',
    'go': 'http://test-api-go.520yidui.com/v2/members/info'
}

params = {
    'target_id': '732112abeb0ad2f9fab9dbb66d2a4dd6'
}

headers = {
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJpZCI6NzQyNzQsImV4cGlyZV9hdCI6IjIwMTktMDctMzAgMDQ6NDQ6MjYgKzA4MDAifQ.74AnGxtcxwKDpqpdaPWYQP881cmmirmvchQe4MI9u2w'
}

data = {
    'superior_id': 81,
    'recommend_id': 81
}


def response(api_type):
    if api_type == 'ruby':
        r = requests.get(url['ruby'], params=params, headers=headers)
        if 300 <= r.status_code < 400:
            print('Redirect:', r.status_code)
            return
        elif 400 <= r.status_code < 500:
            print('Incorrect request:', r.status_code)
            return
        elif r.status_code > 500:
            print('Incorrect response:', r.status_code)
        d = json.loads(r.content)
        # print(type(d))
        print(d)
        return d
    if api_type == 'go':
        r = requests.get(url['go'], params=params, headers=headers)
        d = json.loads(r.content)
        print(d)
        return d


def diff():
    d1, d2 = response('ruby'), response('go')
    if len(d1) != len(d2):
        print('参数长度不一致:')
        print('第一组参数长度为：%s，第二组参数长度为：%s' % (len(d1), len(d2)))
    for k1 in d1:
        for k2 in d2:
            if k1 == k2:
                if d1[k1] != d2[k2]:
                    print('第一组数据为：', k1, d1[k1])
                    print('第二组数据为：', k2, d2[k2])
                    print('-----------------------')


def response_test(request_type, api_type):
    if request_type.get:
        r = requests.get(url[api_type], params=params, headers=headers)
    elif request_type.post:
        r = requests.post(url[api_type], data=data, headers=headers)
        if 300 <= r.status_code < 400:
            print('Redirect:', r.status_code)
            return
        elif 400 <= r.status_code < 500:
            print('Incorrect request:', r.status_code)
            return
        elif r.status_code > 500:
            print('Incorrect response:', r.status_code)
        d = json.loads(r.content)
        # print(type(d))
        print(d)
        return d


# diff()
response('ruby')
response('go')
# print(requests.post(url['ruby'], data=data, headers=headers))
