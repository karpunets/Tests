import json, pytest, requests, os
import Data.URLs_MAP as URL


@pytest.fixture(scope='session')
def get_role():
    #Получаем роль из параметро теста
    try:
        role_name_from_jenkins = os.environ['role_for_test']
    # Если не передали используем рут роль
    except KeyError:
        role_name_from_jenkins = 'ROOT'
    roles = {'ROOT' : "Basic QVBJX2F1dG90ZXN0X1JPT1Q6QVBJX2F1dG90ZXN0X1JPT1Q=",
            'ADMINISTRATOR' : "Basic QVBJX2F1dG90ZXN0X0FETUlOSVNUUkFUT1I6QVBJX2F1dG90ZXN0X0FETUlOSVNUUkFUT1I=",
            'USER' : "Basic QVBJX2F1dG90ZXN0X1VTRVI6QVBJX2F1dG90ZXN0X1VTRVI=",
            'SUPERVISOR' : "Basic QVBJX2F1dG90ZXN0X1NVUEVSVklTT1I6QVBJX2F1dG90ZXN0X1NVUEVSVklTT1I="}
    auth = roles[role_name_from_jenkins]
    headers = {
        'content-type': "application/json;charset=UTF-8",
        'authorization': auth}
    data = {'headers': headers, 'role' : role_name_from_jenkins}
    return data


@pytest.fixture(scope="session")
#Формирование запроса и получение результата по полученным данным
def make_request(get_role):

    def some_request(url, data=None, method='POST', params = None):
        headers = get_role['headers']
        payload = json.dumps(data)
        response = requests.request(method, url, data=payload, headers=headers, params=params)
        return response

    return some_request


@pytest.fixture(scope='function')
def clear_result():
    data = {}
    yield data
    try:
        if isinstance(data['id'], list) or isinstance(data['id'], tuple):
            for i in data['id']:
                requests.delete(url=data['url'], params={'id':int(i)}, headers=URL.headers)
        else:
            requests.delete(url=data['url'], params={'id': int(data['id'])}, headers=URL.headers)
    except KeyError:
        pass

