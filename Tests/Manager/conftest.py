import json, pytest, requests
import Data.URLs_MAP as URL

import Data.Test_data as get
from Data.Make_requests_and_answers import JSON_generator
from Data.Requests_default_map import defaul_request




@pytest.fixture(scope="function")
def add_delete_user(request, send_request):
    users_id = []
    # Добавляем пользователя с переданными данными
    def add_user(*args):
        for user in args:
            payload = json.dumps(JSON_generator.get_JSON_request('add_user', **user))
            # Делаем запрос
            response = send_request(URL.add_user, data=payload)
            assert response.status_code == 200
            # Наполняем список ІД добавленных пользователей
            users_id.append(response.json()['id'])
        # Удаляем добавленных ранее пользователей
        def user_delete():
            for id in users_id:
                data = JSON_generator.get_JSON_request('delete_user', **{'userId': id})
                payload = json.dumps(data)
                response = send_request(url = URL.delete_user, data=payload)
                assert response.status_code == 200

        request.addfinalizer(user_delete)
        return users_id
    return add_user

@pytest.fixture(scope="function")
def delete_user(send_request):
    # Создаем словарь для возможности добавления ІД польщователя с теста
    user_id = {}
    yield user_id
    for i in user_id:
        data = JSON_generator.get_JSON_request('delete_user', **{'userId': user_id[i]})
        payload = json.dumps(data)
        response = send_request(url = URL.delete_user, data=payload)
        assert response.status_code == 200


@pytest.fixture(scope='function')
def make_50_users():
    # Количество пользователей для теста
    users_count = 50
    user_list = {}
    # Создаем список JSONов для создания пользователей
    for i in range(1, users_count + 1):
        data = {"fname": "get_userlist_fName_%s" % i,
                "lname": "get_userlist_lName_%s" % i,
                "pname": "get_userlist_pName_%s" % i,
                "phone": "%s" % i,
                "login": "get_userlist_login_%s" % i,
                "password": "get_userlist_password_%s" % i,
                "loginAD": "get_userlist_loginAD_%s" % i,
                "agentId": "get_userlist_agentId_%s" % i,
                "scMode": "0",
                "unmappedCalls": False,
                "enabled": True,
                "deleted": False,
                "dateCreate": 1494845540000,
                "groups": [{"id": 2}],
                "roles": [{"id": 3}]}
        # Пол
        request = defaul_request('add_user')
        #
        data = JSON_generator.generate_JSON(request, data)
        #
        user_list["Pagination_user_%s" % i] = data
    #
    user_list['one_user_get_userlist'] = get.one_user_get_userlist
    user_list['deleted_user_get_user_list'] = get.deleted_user_get_user_list
    return user_list


@pytest.fixture(scope="module")
def setup_get_user_list(make_50_users):
    user_id_list = {}
    # Получаем список пользователей для добавления
    user_list = make_50_users()
    for i in user_list:
        # Запрос на добавление пользователя
        response = requests.post(URL.add_user, data = json.dumps(user_list[i]), headers=URL.headers)
        # Записываем ID добавленных пользователей
        user_id_list[i] = response.json()['id']
    one_user_user_id = user_id_list['one_user_get_userlist']
    deleted_user_user_id = user_id_list['deleted_user_get_user_list']
    yield one_user_user_id, deleted_user_user_id
    #Отправляем ИД юзера для удаления
    for i in user_id_list:
        payload = json.dumps({'userId':user_id_list[i]})
        response = requests.post(URL.delete_user, data=payload, headers=URL.headers)