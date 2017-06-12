import json, pytest, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator
from Data.Requests_default_map import defaul_request


headers = URL.headers


@pytest.fixture(scope="function")
#Формирование запроса и получение результата по полученным данным
def make_request():

    def some_request(url, data, method='POST'):
        payload = json.dumps(data)
        response = requests.request(method, url, data=payload, headers=headers)
        return response

    return some_request

@pytest.fixture(scope="function")
def add_delete_user(request):
    users_id = []
    def add_user(*args):
        for user in args:
            payload = json.dumps(JSON_generator.get_JSON_request('add_user', **user))
            # Делаем запрос
            response = requests.post(URL.add_user, data=payload, headers=headers)
            assert response.status_code == 200
            # Добавились ли данные
            users_id.append(response.json()['id'])

        def user_delete():
            for id in users_id:
                data = JSON_generator.get_JSON_request('delete_user', **{'userId': id})
                payload = json.dumps(data)
                response = requests.post(URL.delete_user, data=payload, headers=headers)
                assert response.status_code == 200

        request.addfinalizer(user_delete)
        return users_id
    return add_user
