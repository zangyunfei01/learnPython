import json
from api_test.data_provider.members_list import *


def get_status_code(response):
    try:
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        return response.status_code


def get_response_body():
    print(type(json.loads(r.content)))
    return json.loads(r.content)


def required_params():
    params_without_category = {"page": 1}
    params_without_page = {"category": "home"}

    r1 = requests.get(url, headers=headers, params=params_without_category)
    r2 = requests.get(url, headers=headers, params=params_without_page)
    r3 = requests.get(url, headers=headers)
    return get_status_code(r1), get_status_code(r2), get_status_code(r3)