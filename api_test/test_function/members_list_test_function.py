import json
from api_test.data_provider.members_list_base_data import *


def get_base_response():
    # print(base_response)
    return base_response_type


def get_response(param):
    r = requests.get(url, params=param, headers=headers)
    # print(r)
    return r


def get_status_code_without_params():
    r = requests.get(url, headers=headers)
    try:
        r.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        # print(get_response().status_code)
        return r.status_code


def get_status_code(param):
    try:
        get_response(param).raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        # print(get_response().status_code)
        return get_response(param).status_code


def get_response_body():
    r = requests.get(url, params=params, headers=headers)
    # print(json.loads(r.content))
    return json.loads(r.content)


complete_response_body_dict = {}


def get_complete_response_body(new_dict):
    for k in new_dict:
        if type(new_dict[k]) == dict:
            return get_complete_response_body(new_dict[k])
        else:
            complete_response_body_dict[k] = new_dict[k]
    return complete_response_body_dict


def diff_response_body_count():
    diff_count = 0
    for k1, v1 in get_base_response().items():
        for k2, v2 in get_complete_response_body(get_response_body()[0]).items():
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

# get_base_response()
# get_response()
# print(type(get_response_body()))
# print(get_response_body()[0])
# print(type(get_response_body()[0]))
# print(get_response_type(get_response_body()[0]))
# diff_response_body_count()
# print(type(None))
