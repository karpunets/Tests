import json

import pytest
import requests
import Data.URLs_MAP as URL
import Data.Users as get_user

from Data.Make_requests_and_answers import JSON_generator
from Data.Requests_default_map import defaul_request


headers = URL.headers


@pytest.fixture()
#Формирование запроса и получение результата по полученным данным
def make_request():

    def some_request(url, data, method='POST'):
        payload = json.dumps(data)
        response = requests.request(method, url, data=payload, headers=headers)
        return response

    return some_request


@pytest.fixture()
def setup_add_delete_user_for_GET_USER_LIST():

    # JSON тело с валидными параметрами
    ONE_user_test = get_user.one_user_get_userlist
    # Преобразовываем словарь в json
    payload = json.dumps(JSON_generator.get_JSON_request('add_user', **ONE_user_test))
    # Делаем запрос
    response = requests.post(URL.add_user, data=payload, headers=headers)
    #Добавились ли данные
    assert response.status_code == 200
    response_json = response.json()
    #Вытягиваем user_id с ответа
    user_id = response_json['id']
    #Отправляем данные и переходим к Teardown
    yield user_id, response.text
    #Отправляем ИД юзера для удаления
    data =JSON_generator.get_JSON_request('delete_user', **{'userId':user_id})
    payload = json.dumps(data)
    response = requests.post(URL.delete_user, data=payload, headers=headers)
    assert response.status_code == 200



@pytest.fixture(scope="function")
def setup_add_delete_user_for_edit_user():

    # JSON тело с валидными параметрами
    ONE_user_test = get_user.edit_user
    # Преобразовываем словарь в json
    payload = json.dumps(JSON_generator.get_JSON_request('add_user', **ONE_user_test))
    # Делаем запрос
    response = requests.post(URL.add_user, data=payload, headers=headers)
    #Добавились ли данные
    assert response.status_code == 200
    response_json = response.json()
    #Вытягиваем user_id с ответа
    user_id = response_json['id']
    #Отправляем данные и переходим к Teardown
    yield user_id, response.text
    #Отправляем ИД юзера для удаления
    data =JSON_generator.get_JSON_request('delete_user', **{'userId':user_id})
    payload = json.dumps(data)
    response = requests.post(URL.delete_user, data=payload, headers=headers)
    assert response.status_code == 200