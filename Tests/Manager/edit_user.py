import pytest, allure
import Data.URLs_MAP as URL
import Data.Users as get

from Data.Make_requests_and_answers import JSON_generator as _

name = 'edit_user'

@allure.feature('Позитивный тест')
@allure.story('Редактируем ФИО')
def test_f_l_p_names_edit(add_delete_user, make_request):

    user_id =add_delete_user(get.edit_user)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': user_id[0],
                                       "fname": "edit_user_fName_one_edited",
                                       "lname": "edit_user_lName_one_edited",
                                       "pname": "edit_user_pName_one_edited",
                                       "email": "edit_user@smiddle.com",
                                       "fax": "edit_user_fax",
                                       "agentId": "edit_user_agentId_one",
                                       "login": "edit_user_login_one",
                                       "loginAD": "edit_user_loginAD_one",
                                       "phone": "666816322"
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': user_id[0],
                                          "fname": "edit_user_fName_one_edited",
                                          "lname": "edit_user_lName_one_edited",
                                          "pname": "edit_user_pName_one_edited",
                                          "email": "edit_user@smiddle.com",
                                          "fax": "edit_user_fax",
                                          "agentId": "edit_user_agentId_one",
                                          "login": "edit_user_login_one",
                                          "loginAD": "edit_user_loginAD_one",
                                          "phone": "666816322"
                                          })

    assert response.status_code == 200
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Редактируем e-mail, факс, agentId')
def test_email_fax_agentId_edit(add_delete_user, make_request):
    user_id = add_delete_user(get.edit_user)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': user_id[0],
                                       "fname": "edit_user_fName_one",
                                       "password": "edit_user_password_one",
                                       "lname": "edit_user_lName_one",
                                       "pname": "edit_user_pName_one",
                                       "email": "edit_user_edited@smiddle.com",
                                       "fax": "edit_user_fax_edited",
                                       "agentId": "edit_user_agentId_edited",
                                       "login": "edit_user_login_one",
                                       "loginAD": "edit_user_loginAD_one",
                                       "phone": "666816322"
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': user_id[0],
                                          "fname": "edit_user_fName_one",
                                          "lname": "edit_user_lName_one",
                                          "pname": "edit_user_pName_one",
                                          "email": "edit_user_edited@smiddle.com",
                                          "fax": "edit_user_fax_edited",
                                          "agentId": "edit_user_agentId_edited",
                                          "login": "edit_user_login_one",
                                          "loginAD": "edit_user_loginAD_one",
                                          "phone": "666816322"
                                          })

    assert response.status_code == 200
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Редактируем login, loginAD, номер телефона')
def test_login_loginAD_phone_edit(add_delete_user, make_request):
    user_id = add_delete_user(get.edit_user)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': user_id[0],
                                       "fname": "edit_user_fName_one",
                                       "password": "edit_user_password_one",
                                       "lname": "edit_user_lName_one",
                                       "pname": "edit_user_pName_one",
                                       "email": "edit_user@smiddle.com",
                                       "fax": "edit_user_fax",
                                       "agentId": "edit_user_agentId_one",
                                       "login": "edit_user_login_one_edited",
                                       "loginAD": "edit_user_loginAD_one_edited",
                                       "phone": "123456789"
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': user_id[0],
                                          "fname": "edit_user_fName_one",
                                          "password": "edit_user_password_one",
                                          "lname": "edit_user_lName_one",
                                          "pname": "edit_user_pName_one",
                                          "email": "edit_user@smiddle.com",
                                          "fax": "edit_user_fax",
                                          "agentId": "edit_user_agentId_one",
                                          "login": "edit_user_login_one_edited",
                                          "loginAD": "edit_user_loginAD_one_edited",
                                          "phone": "123456789"
                                          })

    assert response.status_code == 200
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Редактируем ФИО на уже существующую')
def test_f_l_p_names_edit_for_already_exsisting_name(add_delete_user, make_request):
    user_id = add_delete_user(get.edit_user, get.edit_user_existing)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': user_id[0],
                                       "fname": "edit_user_fName_one_existing",
                                       "lname": "edit_user_lName_one_existing",
                                       "pname": "edit_user_pName_one_existing",
                                       "email": "edit_user@smiddle.com",
                                       "fax": "edit_user_fax",
                                       "agentId": "edit_user_agentId_one",
                                       "login": "edit_user_login_one",
                                       "loginAD": "edit_user_loginAD_one",
                                       "phone": "666816322"
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': user_id[0],
                                          "fname": "edit_user_fName_one_existing",
                                       "lname": "edit_user_lName_one_existing",
                                       "pname": "edit_user_pName_one_existing",
                                          "email": "edit_user@smiddle.com",
                                          "fax": "edit_user_fax",
                                          "agentId": "edit_user_agentId_one",
                                          "login": "edit_user_login_one",
                                          "loginAD": "edit_user_loginAD_one",
                                          "phone": "666816322"
                                          })

    assert response.status_code == 200
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Редактируем ФИО удаленного пользователя')
def test_f_l_p_names_edit_deleted_user(add_delete_user, make_request):

    user_id =add_delete_user(get.edit_user_deleted)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': user_id[0],
                                                    "fname": "edit_user_fName_one_edited",
                                                    "lname": "edit_user_lName_one_edited",
                                                    "pname": "edit_user_pName_one_edited",
                                                    "email": "edit_user@smiddle.com",
                                                    "fax": "edit_user_fax",
                                                    "agentId": "edit_user_agentId_one",
                                                    "login": "edit_user_login_one",
                                                    "loginAD": "edit_user_loginAD_one",
                                                    "phone": "666816322",
                                                    "deleted":True
                                                         })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, ** {'id': user_id[0],
                                                        "fname": "edit_user_fName_one_edited",
                                                        "lname": "edit_user_lName_one_edited",
                                                        "pname": "edit_user_pName_one_edited",
                                                        "email": "edit_user@smiddle.com",
                                                        "fax":"edit_user_fax",
                                                        "agentId": "edit_user_agentId_one",
                                                        "login":"edit_user_login_one",
                                                        "loginAD":"edit_user_loginAD_one",
                                                        "phone":"666816322",
                                                    "deleted":True
                                                         })

    assert response.status_code == 200
    assert answer == response.json()

@allure.feature('Позитивный тест')
@allure.story('Редактируем e-mail, факс, agentId удаленного пользователя')
def test_email_fax_agentId_edit_deleted_user(add_delete_user, make_request):

    user_id =add_delete_user(get.edit_user_deleted)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{ 'id': user_id[0],
                                                     "fname": "edit_user_fName_one",
                                                     "password": "edit_user_password_one",
                                                     "lname": "edit_user_lName_one",
                                                     "pname": "edit_user_pName_one",
                                                     "email": "edit_user_edited@smiddle.com",
                                                     "fax":"edit_user_fax_edited",
                                                     "agentId": "edit_user_agentId_edited",
                                                     "login":"edit_user_login_one",
                                                     "loginAD":"edit_user_loginAD_one",
                                                     "phone":"666816322",
                                                    "deleted":True
                                                     })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, ** {'id': user_id[0],
                                                        "fname": "edit_user_fName_one",
                                                        "lname": "edit_user_lName_one",
                                                        "pname": "edit_user_pName_one",
                                                        "email": "edit_user_edited@smiddle.com",
                                                        "fax":"edit_user_fax_edited",
                                                        "agentId": "edit_user_agentId_edited",
                                                        "login":"edit_user_login_one",
                                                        "loginAD":"edit_user_loginAD_one",
                                                        "phone":"666816322",
                                                    "deleted":True
                                                         })

    assert response.status_code == 200
    assert answer == response.json()

@allure.feature('Позитивный тест')
@allure.story('Редактируем login, loginAD, номер телефона удаленного пользователя')
def test_login_loginAD_phone_edit_deleted_user(add_delete_user, make_request):
    user_id =add_delete_user(get.edit_user_deleted)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{ 'id': user_id[0],
                                                     "fname": "edit_user_fName_one",
                                                     "password": "edit_user_password_one",
                                                    "lname": "edit_user_lName_one",
                                                    "pname": "edit_user_pName_one",
                                                     "email": "edit_user@smiddle.com",
                                                     "fax":"edit_user_fax",
                                                    "agentId": "edit_user_agentId_one",
                                                    "login":"edit_user_login_one_edited",
                                                    "loginAD":"edit_user_loginAD_one_edited",
                                                    "phone":"123456789",
                                                    "deleted":True
                                                     })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, ** {'id': user_id[0],
                                                        "fname": "edit_user_fName_one",
                                                         "password": "edit_user_password_one",
                                                        "lname": "edit_user_lName_one",
                                                        "pname": "edit_user_pName_one",
                                                         "email": "edit_user@smiddle.com",
                                                         "fax":"edit_user_fax",
                                                        "agentId": "edit_user_agentId_one",
                                                        "login":"edit_user_login_one_edited",
                                                        "loginAD":"edit_user_loginAD_one_edited",
                                                        "phone":"123456789",
                                                    "deleted":True
                                                         })

    assert response.status_code == 200
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Изменяем логин на уже существующий')
def test_edit_login_for_existing(add_delete_user, make_request):
    user_id = add_delete_user(get.edit_user, get.edit_user_existing)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': user_id[0],
                                       "fname": "edit_user_fName_one",
                                       "password": "edit_user_password_one",
                                       "lname": "edit_user_lName_one",
                                       "pname": "edit_user_pName_one",
                                       "email": "edit_user@smiddle.com",
                                       "fax": "edit_user_fax",
                                       "agentId": "edit_user_agentId_one",
                                       "login": "edit_user_login_existing",
                                       "loginAD": "edit_user_loginAD_one_edited",
                                       "phone": "666816322"
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = {"COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS":"CommonEntityWithSuchFieldExists: login =edit_user_agentId_existing already exists"}
    print(response.text)
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Изменяем agentId(Cisco AgentId) на уже существующий')
def test_edit_agentId_for_existing(add_delete_user, make_request):
    user_id = add_delete_user(get.edit_user, get.edit_user_existing)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': user_id[0],
                                       "fname": "edit_user_fName_one",
                                       "password": "edit_user_password_one",
                                       "lname": "edit_user_lName_one",
                                       "pname": "edit_user_pName_one",
                                       "email": "edit_user@smiddle.com",
                                       "fax": "edit_user_fax",
                                       "agentId": "edit_user_agentId_existing",
                                       "login": "edit_user_login_existing",
                                       "loginAD": "edit_user_loginAD_one_edited",
                                       "phone": "666816322"
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = {"COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS":"CommonEntityWithSuchFieldExists: AGENT ID =edit_user_agentId_existing already exists"}
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Изменяем телефон на уже существующий')
def test_edit_phone_for_existing(add_delete_user, make_request):
    user_id = add_delete_user(get.edit_user, get.edit_user_existing)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': user_id[0],
                                       "fname": "edit_user_fName_one",
                                       "password": "edit_user_password_one",
                                       "lname": "edit_user_lName_one",
                                       "pname": "edit_user_pName_one",
                                       "email": "edit_user@smiddle.com",
                                       "fax": "edit_user_fax",
                                       "agentId": "edit_user_agentId_one",
                                       "login": "edit_user_login_one_edited",
                                       "loginAD": "edit_user_loginAD_one_edited",
                                       "phone": "6668163333"
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = {"COMMON_EXCEPTION":"CommonException: Not deleted user with phone = 6668163333 already exist!"}
    print(response.text)
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Изменяем логин удаленного пользователя на уже существующий НЕ удаленный')
def test_edit_login_deleted_on_existing_not_deleted(add_delete_user, make_request):
    user_id = add_delete_user(get.edit_user_deleted, get.edit_user_existing)
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{  'id': user_id[0],
                                         "fname": "edit_user_fName_deleted",
                                         "password": "edit_user_password_deleted",
                                         "lname": "edit_user_lName_deleted",
                                         "pname": "edit_user_pName_deleted",
                                         "email": "edit_user@smiddle.com",
                                         "fax": "edit_user_fax_deleted",
                                         "agentId": "edit_user_agentId_deleted",
                                         "login": "edit_user_login_existing",
                                         "loginAD": "edit_user_loginAD_deleted",
                                         "phone": "666816323",
                                         "deleted": True
                                       })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer ={"COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS":"CommonEntityWithSuchFieldExists: login =edit_user_agentId_existing already exists"}
    print(response.text)
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Изменяем телефон удаленного пользователя на уже существующие')
@pytest.mark.parametrize("users", [(get.edit_user_deleted, get.edit_user_existing),(get.edit_user_deleted, get.edit_user_deleted_existing) ])
def test_login_loginAD_phone_edit(add_delete_user, make_request, users):
    user_id = add_delete_user(users[0], users[1])
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"id":user_id[0],
                                       "fname": "edit_user_fName_deleted",
                                         "password": "edit_user_password_deleted",
                                         "lname": "edit_user_lName_deleted",
                                         "pname": "edit_user_pName_deleted",
                                         "email": "edit_user@smiddle.com",
                                         "fax": "edit_user_fax_deleted",
                                         "agentId": "edit_user_agentId_deleted",
                                         "login": "edit_user_login_deleted",
                                         "loginAD": "edit_user_loginAD_deleted",
                                         "phone": "6668163333",
                                        "deleted": True
                                         })

    # Делаем запрос и получаем ответ
    response = make_request(url=URL.edit_user, data=data)
    # Данные которые должны быть в ответе
    answer = {"id":user_id[0],
                                          "fname": "edit_user_fName_deleted",
                                         "lname": "edit_user_lName_deleted",
                                         "pname": "edit_user_pName_deleted",
                                         "email": "edit_user@smiddle.com",
                                         "fax": "edit_user_fax_deleted",
                                         "agentId": "edit_user_agentId_deleted",
                                         "login": "edit_user_login_deleted",
                                         "loginAD": "edit_user_loginAD_deleted",
                                         "phone": "6668163333",
                                         }

    print(response.json())

    assert response.status_code == 200
    for key in answer:
        assert answer[key] == response.json()[key]