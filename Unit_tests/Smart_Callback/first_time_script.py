import pytest, allure, json, requests
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _

name = "add_user"


@allure.feature('Позитивный тест')
@allure.story('Добавляем пользователя')
def test_Positive_add_one_user(make_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"fname": "scb_user_fname",
                                        "lname": "scb_user_lname",
                                        "pname": "scb_user_pname",
                                        "phone": "1232",
                                        "login": "scb_user_login",
                                        "password": "scb_user_password",
                                        "loginAD": "scb_user_login_AD",
                                        "agentId": "scb_user_agentID",
    })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.add_user, data=data)
    user_id = response.json()['id']
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': user_id,
                                          "fname": "scb_user_fname",
                                        "lname": "scb_user_lname",
                                        "pname": "scb_user_pname",
                                        "phone": "1232",
                                        "login": "scb_user_login",
                                        "password": "scb_user_password",
                                        "loginAD": "scb_user_login_AD",
                                        "agentId": "scb_user_agentID",
                                          })
    assert response.status_code == 200
    assert answer == response.json()