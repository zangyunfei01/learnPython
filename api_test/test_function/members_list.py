import json
from api_test.data_provider.members_list_base_data import *


def get_base_response():
    # print(base_response)
    return base_response_type


def get_response(key):
    if key == 'cp':
        params = {'category': 'home', 'page': 1}
    elif key == 'c':
        params = {'category': 'home'}
    elif key == 'p':
        params = {'page': 1}
    else:
        params = {}
    r = requests.get(url, params=params, headers=headers)
    # print(r.status_code)
    return r


def get_status_code(key):
    status_code = get_response(key).status_code
    while 100 <= status_code < 505:
        if 100 <= status_code < 200:
            continue
        elif 200 <= status_code < 400:
            print(status_code)
            return status_code
        elif 400 <= status_code < 500:
            print(f'请求错误，状态码：{status_code}')
            break
        else:
            print(f'服务器错误，状态码：{status_code}')
            break


def get_response_body(key):
    # print(json.loads(r.content))
    return json.loads(get_response(key).content)


complete_response_body_dict = {}


def get_complete_response_body(new_dict):
    for k in new_dict:
        if type(new_dict[k]) in (dict, list):
            return get_complete_response_body(new_dict[k])
        else:
            complete_response_body_dict[k] = new_dict[k]
    return complete_response_body_dict


def diff_response_body_count():
    diff_count = 0
    for k1, v1 in get_base_response().items():
        for k2, v2 in get_complete_response_body(get_response_body('cp')[0]).items():
            if k1 == k2:
                if type(v2) not in v1:
                    print('base_data:  ', k1, ':', v1)
                    print('real_data:  ', k2, ':', type(v2))
                    diff_count += 1
    if diff_count == 0:
        print('well done!')
    else:
        print('diff_count:', diff_count)
        # print(complete_response_body_dict)
    return diff_count


