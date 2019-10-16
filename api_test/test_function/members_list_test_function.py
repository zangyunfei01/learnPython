import json
from api_test.data_provider.members_list_base_data import *


def get_base_response():
    # print(base_response)
    return base_response


def get_response(category, page):
    params = {'category': category, 'page': page}
    r = requests.get(url, params=params, headers=headers)
    # print(r)
    return r


def get_status_code(category, page):
    try:
        get_response(category, page).raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        print(get_response(category, page).status_code)
        return get_response(category, page).status_code


def get_response_body(category, page):
    # print(json.loads(get_response(category, page).content))
    return json.loads(get_response(category, page).content)


def diff_response_body_count(category, page):
    diff_count = 0
    for k1, v1 in get_base_response().items():
        for k2, v2 in get_response_body(category, page)[0].items():
            if k1 == k2:
                if type(v2) != v1:
                    print(k1, v1)
                    print(k2, v2)
                    diff_count += 1
    print(diff_count)
    return diff_count


# get_base_response()
# get_response('home', 1)
# print(type(get_response_body('home', 1)))
# print(get_response_body('home', 1)[0])
diff_response_body_count('home', 1)


