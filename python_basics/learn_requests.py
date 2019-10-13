#!/usr/bin/env python3

import requests
import json

RequestType = ['GET', 'POST', 'PUT', 'DELETE']

ApiType = ['go', 'ruby']

URL = {
    'ruby': 'https://test-apis.520yidui.com/v2/members/mine',
    'go': 'http://test-api-go.520yidui.com/v2/members/mine'
}

params = {
    'target_id': '732112abeb0ad2f9fab9dbb66d2a4dd6'
}

headers = {
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJpZCI6NzQyNzQsImV4cGlyZV9hdCI6IjIwMTktMDctMzEgMDQ6NDQ6NDMgKzA4MDAifQ.HpF3_D3wPLKuIIbUB8uyIalqMzd0poGMxBCBwix_3gY'
}

data = {
    'superior_id': 81,
    'recommend_id': 81
}


def response(api_type, request_type):
    if api_type == 'go':
        url = URL['go']
    elif api_type == 'ruby':
        url = URL['ruby']

    if request_type == 'GET':
        r = requests.get(url, params=params, headers=headers)
    elif request_type == 'POST':
        r = requests.post(url, data=data, headers=headers)
    print('%s data_provider url:' % api_type, r.url)

    if 200 <= r.status_code < 300:
        print('Direct response:', r.status_code, '\n')
    elif 300 <= r.status_code < 400:
        print('Redirect:', r.status_code, '\n')
        return
    elif 400 <= r.status_code < 500:
        print('Incorrect request:', r.status_code, '\n')
        return
    elif r.status_code > 500:
        print('Incorrect response:', r.status_code, '\n')

    d = json.loads(r.content)
    # print(type(d))
    print(d, '\n')
    return d


def diff():
    d1, d2 = response('ruby', 'GET'), response('go', 'GET')
    if len(d1) != len(d2):
        print('参数长度不一致:')
        print('第一组参数长度为：%s，第二组参数长度为：%s' % (len(d1), len(d2)))
    for k1 in d1:
        for k2 in d2:
            if k1 == k2:
                if d1[k1] != d2[k2]:
                    print('第一组数据为：', k1, d1[k1])
                    print('第二组数据为：', k2, d2[k2], '\n')
                    print('-----------------------')


# response('ruby', 'GET')
diff()


def test_assert():
    d1, d2 = response('ruby', 'GET'), response('go', 'GET')
    assert len(d1) == len(d2)