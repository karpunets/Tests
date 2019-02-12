import pytest
import requests
import os
from json import dumps
from collections import deque
from bin.api import root_group_id
from bin.common import parse_request, random_string
from bin import req


@pytest.fixture(scope='session')
def get_role():
    # Получаем роль из параметров теста
    try:
        role_name_from_jenkins = os.environ['role_for_test']
    # Если не передали используем рут роль
    except KeyError:
        role_name_from_jenkins = 'ROOT'
    roles = {'ROOT':"Basic Yml0Ym9rX3Rlc3Q6Yml0Ym9rX3Rlc3Q=",
             # "Basic QVBJX2F1dG90ZXN0X1JPT1Q6QVBJX2F1dG90ZXN0X1JPT1Q=",  "Basic cm9vdDpTbWlkbGUwOThhZG0h"
             'ADMINISTRATOR': "Basic QVBJX2F1dG90ZXN0X0FETUlOSVNUUkFUT1I6QVBJX2F1dG90ZXN0X0FETUlOSVNUUkFUT1I=",
             'USER': "Basic QVBJX2F1dG90ZXN0X1VTRVI6QVBJX2F1dG90ZXN0X1VTRVI=",
             'SUPERVISOR': "Basic QVBJX2F1dG90ZXN0X1NVUEVSVklTT1I6QVBJX2F1dG90ZXN0X1NVUEVSVklTT1I="}
    auth = roles[role_name_from_jenkins]
    headers = {
        'content-type': "application/json;charset=UTF-8",
        'authorization': auth}
    data = {'headers': headers, 'role': role_name_from_jenkins}
    return data


@pytest.fixture(scope="session")
# Формирование запроса и получение результата по полученным данным
def send_request(get_role):
    def some_request(url, data=None, method='POST', params=None):
        headers = get_role['headers']
        payload = dumps(data)
        response = req.request(method, url, data=payload, headers=headers, params=params)
        return response

    return some_request


@pytest.fixture(scope='function')
def clear_result(send_request):
    data = {}
    yield data
    try:
        if isinstance(data['id'], list) or isinstance(data['id'], tuple):
            for i in data['id']:
                send_request(url=data['url'], params={'id': int(i)}, method = "DELETE")
        else:
            send_request(url=data['url'], params={'id': int(data['id'])}, method = "DELETE")
    except KeyError:
        pass


@pytest.fixture(scope="function")
def clear_data(request):
    url = getattr(request.cls, "url")
    group_id_list = []
    yield group_id_list
    for id_to_delete in group_id_list:
        req.delete(url, id_to_url=id_to_delete)

@pytest.fixture(scope="module")
def immutable_group_with_child():
    """
    :return: {}
    """
    groups_id = deque([], maxlen=5)
    data = parse_request('Tests/Manager_new/Test_data/post_group', {"$name": random_string(),
                                        "$parentGroupId": root_group_id()})
    response_parent = req.post("groups", data['request'])
    groups_id.appendleft(response_parent.json()['groupId'])
    data_child = parse_request('Tests/Manager_new/Test_data/post_group', {"$name": random_string(),
                                             "$parentGroupId": groups_id[0]})
    response_child = req.post("groups", data_child['request'])
    response = req.get("groups", id_to_url=groups_id[0])
    print(response.json())
    groups_id.appendleft(response_child.json()['groupId'])
    yield response.json()
    for id in groups_id:
        req.delete("groups", id_to_url=id)