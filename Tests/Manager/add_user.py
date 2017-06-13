import pytest, allure, json, requests
import Data.URLs_MAP as URL
import Data.Users as get

from Data.Make_requests_and_answers import JSON_generator as _

name = "add_user"



@allure.feature('Позитивный тест')
@allure.story('Проверяем поиск по ФИО')
def test_Positive_add_one_user(make_request,delete_user):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"fname": "add_user_fName_one",
                                        "lname": "add_user_lName_one",
                                        "pname": "add_user_pName_one",
                                        "phone": "666816000",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_one",
                                        "loginAD": "add_user_loginAD_one",
                                        "agentId": "add_user_agentId_one"})

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.add_user, data=data)
    user_id = response.json()['id']
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': user_id,
                                          "fname": "add_user_fName_one",
                                        "lname": "add_user_lName_one",
                                        "pname": "add_user_pName_one",
                                        "phone": "666816000",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_one",
                                        "loginAD": "add_user_loginAD_one",
                                        "agentId": "add_user_agentId_one"
                                          })

    assert response.status_code == 200
    assert answer == response.json()
    delete_user["user1"] = user_id