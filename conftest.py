import json

import pytest
import requests
import Data.URLs_MAP as URL
import Data.Users as get_user

from Data.Users import make_50_users_for_get_user_list as take_user_list
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


@pytest.fixture(scope="module")
def setup_add_delete_user_for_GET_USER_LIST():
    user_id_list = {}
    # Получаем список пользователей для добавления
    user_list = take_user_list()
    for i in user_list:
        # Запрос на добавление пользователя
        response = requests.post(URL.add_user, data = json.dumps(user_list[i]), headers=headers)
        assert response.status_code == 200
        # Записываем ID добавленных пользователей
        user_id_list[i] = response.json()['id']
    one_user_user_id = user_id_list['one_user_get_userlist']
    deleted_user_user_id = user_id_list['deleted_user_get_user_list']
    yield one_user_user_id, deleted_user_user_id
    #Отправляем ИД юзера для удаления
    for i in user_id_list:
        payload = json.dumps({'userId':user_id_list[i]})
        response = requests.post(URL.delete_user, data=payload, headers=headers)
        assert response.status_code == 200



@pytest.fixture(scope="function")
def setup_add_delete_user_for_edit_user():

    ONE_user_test = get_user.edit_user
    payload = json.dumps(JSON_generator.get_JSON_request('add_user', **ONE_user_test))
    # Делаем запрос
    response = requests.post(URL.add_user, data=payload, headers=headers)
    #Добавились ли данные
    assert response.status_code == 200
    user_id = response.json()['id']
    #Отправляем данные и переходим к Teardown
    yield user_id, response.text
    #Отправляем ИД юзера для удаления

    data =JSON_generator.get_JSON_request('delete_user', **{'userId':user_id})
    payload = json.dumps(data)
    response = requests.post(URL.delete_user, data=payload, headers=headers)
    assert response.status_code == 200