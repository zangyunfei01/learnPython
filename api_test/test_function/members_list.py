import json
from api_test.data_provider.members_list_base_data import *


def get_status_code(response):
    try:
        response.raise_for_status()
    except requests.RequestException as e:
        print(e)
    else:
        return response.status_code


def get_response_body():
    return json.loads(r.content)

