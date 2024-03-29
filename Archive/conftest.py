import pytest
import os
from json import dumps
from bin import req




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


@pytest.fixture(scope="session")
# Формирование запроса и получение результата по полученным данным
def send_request(get_role):
    def some_request(url, data=None, method='POST', params=None):
        headers = get_role['headers']
        payload = dumps(data)
        response = req.request(method, url, data=payload, headers=headers, params=params)
        return response

    return some_request


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