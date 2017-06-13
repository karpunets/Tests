import pytest, allure, json, requests
import Data.URLs_MAP as URL
import Data.Users as get

from Data.Make_requests_and_answers import JSON_generator as _

name = "add_user"


@allure.feature('Позитивный тест')
@allure.story('Добавляем пользователя')
def test_Positive_add_one_user(make_request,delete_user):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"fname": "add_user_fName_one",
                                        "lname": "add_user_lName_one",
                                        "pname": "add_user_pName_one",
                                        "phone": "666816000",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_one",
                                        "loginAD": "add_user_loginAD_one",
                                        "agentId": "add_user_agentId_one",
                                        "email": "add_user_one@smiddle.com",
                                        "fax": "add_user_fax_one"
    })

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
                                        "agentId": "add_user_agentId_one",
                                        "email": "add_user_one@smiddle.com",
                                        "fax": "add_user_fax_one"
                                          })
    delete_user["user1"] = user_id
    assert response.status_code == 200
    assert answer == response.json()

@allure.feature('Позитивный тест с существующей ФИО')
@allure.story('Добавляем пользователя')
def test_add_user_with_existing_FIO(make_request,delete_user, add_delete_user):
    # Подготавливаем данные в JSON для запроса
    add_delete_user(get.add_user_existing)
    data = _.get_JSON_request(name, **{"fname": "add_user_fName_existing",
                                        "lname": "add_user_lName_existing",
                                        "pname": "add_user_pName_existing",
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
                                          "fname": "add_user_fName_existing",
                                        "lname": "add_user_lName_existing",
                                        "pname": "add_user_pName_existing",
                                        "phone": "666816000",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_one",
                                        "loginAD": "add_user_loginAD_one",
                                        "agentId": "add_user_agentId_one"
                                          })
    delete_user["user1"] = user_id
    assert response.status_code == 200
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Добавляем пользователя с существующим факсом, loginAD, email')
def test_add_user_with_existing_email_fax_loginAD(make_request,delete_user, add_delete_user):
    # Подготавливаем данные в JSON для запроса
    add_delete_user(get.add_user_existing)
    data = _.get_JSON_request(name, **{"fname": "add_user_fName_one",
                                        "lname": "add_user_lName_one",
                                        "pname": "add_user_pName_one",
                                        "phone": "666816000",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_one",
                                        "loginAD": "add_user_loginAD_existing",
                                        "agentId": "add_user_agentId_one",
                                        "email": "add_user_existing@smiddle.com",
                                        "fax": "add_user_fax_existing"}
    )

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
                                        "loginAD": "add_user_loginAD_existing",
                                        "agentId": "add_user_agentId_one",
                                        "email": "add_user_existing@smiddle.com",
                                        "fax": "add_user_fax_existing"
                                          })
    delete_user["user1"] = user_id
    assert response.status_code == 200
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Добавляем пользователя с существующим login')
def test_add_user_with_existing_login(make_request, add_delete_user):
    # Подготавливаем данные в JSON для запроса
    add_delete_user(get.add_user_existing)
    data = _.get_JSON_request(name, **{"fname": "add_user_fName_one",
                                        "lname": "add_user_lName_one",
                                        "pname": "add_user_pName_one",
                                        "phone": "666816000",
                                        "login": "add_user_login_existing",
                                        "password": "add_user_password_one",
                                        "loginAD": "add_user_loginAD_one",
                                        "agentId": "add_user_agentId_one",
                                        "email": "add_user_one@smiddle.com",
                                        "fax": "add_user_fax_one"})

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.add_user, data=data)
    # Данные которые должны быть в ответе
    # answer =
    print(response.text)
    assert response.status_code == 500
    # assert answer == response.json()

@allure.feature('Негативный тест')
@allure.story('Добавляем пользователя с существующим loginId')
def test_add_user_with_existing_loginId(make_request, add_delete_user):
    # Подготавливаем данные в JSON для запроса
    add_delete_user(get.add_user_existing)
    data = _.get_JSON_request(name, **{"fname": "add_user_fName_one",
                                        "lname": "add_user_lName_one",
                                        "pname": "add_user_pName_one",
                                        "phone": "666816000",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_one",
                                        "loginAD": "add_user_loginAD_one",
                                        "agentId": "add_user_agentId_existing",
                                        "email": "add_user_one@smiddle.com",
                                        "fax": "add_user_fax_one"})

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.add_user, data=data)
    # Данные которые должны быть в ответе
    answer = {"COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS":"CommonEntityWithSuchFieldExists: AGENT ID =add_user_agentId_existing already exists"}
    assert response.status_code == 500
    assert answer == response.json()

@allure.feature('Негативный тест')
@allure.story('Добавляем пользователя с существующим phone')
def test_add_user_with_existing_phone(make_request, add_delete_user):
    # Подготавливаем данные в JSON для запроса
    add_delete_user(get.add_user_existing)
    data = _.get_JSON_request(name, **{"fname": "add_user_fName_one",
                                        "lname": "add_user_lName_one",
                                        "pname": "add_user_pName_one",
                                        "phone": "6668164444",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_one",
                                        "loginAD": "add_user_loginAD_one",
                                        "agentId": "add_user_agentId_existing",
                                        "email": "add_user_one@smiddle.com",
                                        "fax": "add_user_fax_one"})

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.add_user, data=data)
    # Данные которые должны быть в ответе
    answer = {'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'CommonEntityWithSuchFieldExists: AGENT ID =add_user_agentId_existing already exists'}
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('Позитивный тест с существующей ФИО, телефон, loginAD, agentId')
@allure.story('Добавляем пользователя')
def test_add_user_with_existing_FIO_phone_loginAD_agentId_deleted_user(make_request,delete_user, add_delete_user):
    # Подготавливаем данные в JSON для запроса
    add_delete_user(get.add_user_deleted_existing)
    data = _.get_JSON_request(name, **{"fname": "add_user_fName_deleted_existing",
                                        "lname": "add_user_lName_deleted_existing",
                                        "pname": "add_user_pName_deleted_existing",
                                        "phone": "666816000",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_deleted_existing",
                                        "loginAD": "add_user_loginAD_deleted_existing",
                                        "agentId": "add_user_agentId_deleted_existing",
                                        "email": "add_user_deleted_existing@smiddle.com",
                                        "fax": "add_user_fax_deleted_existing"
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.add_user, data=data)
    user_id = response.json()['id']
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': user_id,
                                          "fname": "add_user_fName_deleted_existing",
                                        "lname": "add_user_lName_deleted_existing",
                                        "pname": "add_user_pName_deleted_existing",
                                        "phone": "666816000",
                                        "login": "add_user_login_one",
                                        "password": "add_user_password_deleted_existing",
                                        "loginAD": "add_user_loginAD_deleted_existing",
                                        "agentId": "add_user_agentId_deleted_existing",
                                        "email": "add_user_deleted_existing@smiddle.com",
                                        "fax": "add_user_fax_deleted_existing"
                                          })
    delete_user["user1"] = user_id
    assert response.status_code == 200
    assert answer == response.json()
