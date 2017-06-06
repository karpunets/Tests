import pytest
import allure

from Data.Make_requests_and_answers import JSON_generator as _
import Data.URLs_MAP as URL


@allure.feature('Позивтный тест')
@allure.story('Редактируем ФИО')
def test_Positive_f_l_p_names_edit(setup_add_delete_user_for_edit_user, make_request):
    name = 'edit_user'

    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': setup_add_delete_user_for_edit_user[0],
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
    answer = _.get_JSON_response(name, **{'id': setup_add_delete_user_for_edit_user[0],
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


@allure.feature('Позивтный тест')
@allure.story('Редактируем e-mail, факс, agentId')
def test_Positive_email_fax_agentId_edit(setup_add_delete_user_for_edit_user, make_request):
    name = 'edit_user'

    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': setup_add_delete_user_for_edit_user[0],
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
    answer = _.get_JSON_response(name, **{'id': setup_add_delete_user_for_edit_user[0],
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


@allure.feature('Позивтный тест')
@allure.story('Редактируем login, loginAD, номер телефона')
def test_Positive_login_loginAD_phone_edit(setup_add_delete_user_for_edit_user, make_request):
    name = 'edit_user'
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': setup_add_delete_user_for_edit_user[0],
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
    answer = _.get_JSON_response(name, **{'id': setup_add_delete_user_for_edit_user[0],
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


@allure.feature('Позивтный тест')
@allure.story('Редактируем ФИО на уже существующую')
def test_Positive_f_l_p_names_edit(setup_add_delete_user_for_edit_user, make_request):
    name = 'edit_user'

    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': setup_add_delete_user_for_edit_user[0],
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
    answer = _.get_JSON_response(name, **{'id': setup_add_delete_user_for_edit_user[0],
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


# @allure.feature('Позивтный тест')
# @allure.story('Редактируем ФИО удаленного пользователя')
# def test_Positive_f_l_p_names_edit(setup_add_delete_user_for_edit_user, make_request):
#     name = 'edit_user'
#
#     # Подготавливаем данные в JSON для запроса
#     data = _.get_JSON_request(name, **{'id': setup_add_delete_user_for_edit_user[0],
#                                                     "fname": "edit_user_fName_one_edited",
#                                                     "lname": "edit_user_lName_one_edited",
#                                                     "pname": "edit_user_pName_one_edited",
#                                                     "email": "edit_user@smiddle.com",
#                                                     "fax": "edit_user_fax",
#                                                     "agentId": "edit_user_agentId_one",
#                                                     "login": "edit_user_login_one",
#                                                     "loginAD": "edit_user_loginAD_one",
#                                                     "phone": "666816322"
#                                                          })
#
#     # Делаем запрос и получаем ответ
#     response = make_request(url=URL.edit_user, data=data)
#     # Данные которые должны быть в ответе
#     answer = _.get_JSON_response(name, ** {'id': setup_add_delete_user_for_edit_user[0],
#                                                         "fname": "edit_user_fName_one_edited",
#                                                         "lname": "edit_user_lName_one_edited",
#                                                         "pname": "edit_user_pName_one_edited",
#                                                         "email": "edit_user@smiddle.com",
#                                                         "fax":"edit_user_fax",
#                                                         "agentId": "edit_user_agentId_one",
#                                                         "login":"edit_user_login_one",
#                                                         "loginAD":"edit_user_loginAD_one",
#                                                         "phone":"666816322"
#                                                          })
#
#     assert response.status_code == 200
#     assert answer == response.json()
#
# @allure.feature('Позивтный тест')
# @allure.story('Редактируем e-mail, факс, agentId удаленного пользователя')
# def test_Positive_email_fax_agentId_edit(setup_add_delete_user_for_edit_user, make_request):
#     name = 'edit_user'
#
#     # Подготавливаем данные в JSON для запроса
#     data = _.get_JSON_request(name, **{ 'id': setup_add_delete_user_for_edit_user[0],
#                                                      "fname": "edit_user_fName_one",
#                                                      "password": "edit_user_password_one",
#                                                      "lname": "edit_user_lName_one",
#                                                      "pname": "edit_user_pName_one",
#                                                      "email": "edit_user_edited@smiddle.com",
#                                                      "fax":"edit_user_fax_edited",
#                                                      "agentId": "edit_user_agentId_edited",
#                                                      "login":"edit_user_login_one",
#                                                      "loginAD":"edit_user_loginAD_one",
#                                                      "phone":"666816322"
#                                                      })
#
#     # Делаем запрос и получаем ответ
#     response = make_request(url=URL.edit_user, data=data)
#     # Данные которые должны быть в ответе
#     answer = _.get_JSON_response(name, ** {'id': setup_add_delete_user_for_edit_user[0],
#                                                         "fname": "edit_user_fName_one",
#                                                         "lname": "edit_user_lName_one",
#                                                         "pname": "edit_user_pName_one",
#                                                         "email": "edit_user_edited@smiddle.com",
#                                                         "fax":"edit_user_fax_edited",
#                                                         "agentId": "edit_user_agentId_edited",
#                                                         "login":"edit_user_login_one",
#                                                         "loginAD":"edit_user_loginAD_one",
#                                                         "phone":"666816322"
#                                                          })
#
#     assert response.status_code == 200
#     assert answer == response.json()
#
# @allure.feature('Позивтный тест')
# @allure.story('Редактируем login, loginAD, номер телефона удаленного пользователя')
# def test_Positive_login_loginAD_phone_edit(setup_add_delete_user_for_edit_user, make_request):
#     name = 'edit_user'
#     # Подготавливаем данные в JSON для запроса
#     data = _.get_JSON_request(name, **{ 'id': setup_add_delete_user_for_edit_user[0],
#                                                      "fname": "edit_user_fName_one",
#                                                      "password": "edit_user_password_one",
#                                                     "lname": "edit_user_lName_one",
#                                                     "pname": "edit_user_pName_one",
#                                                      "email": "edit_user@smiddle.com",
#                                                      "fax":"edit_user_fax",
#                                                     "agentId": "edit_user_agentId_one",
#                                                     "login":"edit_user_login_one_edited",
#                                                     "loginAD":"edit_user_loginAD_one_edited",
#                                                     "phone":"123456789"
#                                                      })
#
#     # Делаем запрос и получаем ответ
#     response = make_request(url=URL.edit_user, data=data)
#     # Данные которые должны быть в ответе
#     answer = _.get_JSON_response(name, ** {'id': setup_add_delete_user_for_edit_user[0],
#                                                         "fname": "edit_user_fName_one",
#                                                          "password": "edit_user_password_one",
#                                                         "lname": "edit_user_lName_one",
#                                                         "pname": "edit_user_pName_one",
#                                                          "email": "edit_user@smiddle.com",
#                                                          "fax":"edit_user_fax",
#                                                         "agentId": "edit_user_agentId_one",
#                                                         "login":"edit_user_login_one_edited",
#                                                         "loginAD":"edit_user_loginAD_one_edited",
#                                                         "phone":"123456789"
#                                                          })
#
#     assert response.status_code == 200
#     assert answer == response.json()



@allure.feature('Негативный тест')
@allure.story('Изменяем логин на уже существующий')
def test_Positive_login_loginAD_phone_edit(setup_add_delete_user_for_edit_user, make_request):
    name = 'edit_user'
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': setup_add_delete_user_for_edit_user[0],
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
    answer = _.get_JSON_response(name, **{'id': setup_add_delete_user_for_edit_user[0],
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


@allure.feature('Негативный тест')
@allure.story('Изменяем телефон на уже существующий')
def test_Positive_login_loginAD_phone_edit(setup_add_delete_user_for_edit_user, make_request):
    name = 'edit_user'
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{'id': setup_add_delete_user_for_edit_user[0],
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
    answer = _.get_JSON_response(name, **{'id': setup_add_delete_user_for_edit_user[0],
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

    # @allure.feature('Негативный тест')
    # @allure.story('Изменяем логин удаленного пользователя на уже существующий')
    # def test_Positive_login_loginAD_phone_edit(setup_add_delete_user_for_edit_user, make_request):
    #     name = 'edit_user'
    #     # Подготавливаем данные в JSON для запроса
    #     data = _.get_JSON_request(name, **{ 'id': setup_add_delete_user_for_edit_user[0],
    #                                                      "fname": "edit_user_fName_one",
    #                                                      "password": "edit_user_password_one",
    #                                                     "lname": "edit_user_lName_one",
    #                                                     "pname": "edit_user_pName_one",
    #                                                      "email": "edit_user@smiddle.com",
    #                                                      "fax":"edit_user_fax",
    #                                                     "agentId": "edit_user_agentId_one",
    #                                                     "login":"edit_user_login_one_edited",
    #                                                     "loginAD":"edit_user_loginAD_one_edited",
    #                                                     "phone":"123456789"
    #                                                      })
    #
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_user, data=data)
    #     # Данные которые должны быть в ответе
    #     answer = _.get_JSON_response(name, ** {'id': setup_add_delete_user_for_edit_user[0],
    #                                                         "fname": "edit_user_fName_one",
    #                                                          "password": "edit_user_password_one",
    #                                                         "lname": "edit_user_lName_one",
    #                                                         "pname": "edit_user_pName_one",
    #                                                          "email": "edit_user@smiddle.com",
    #                                                          "fax":"edit_user_fax",
    #                                                         "agentId": "edit_user_agentId_one",
    #                                                         "login":"edit_user_login_one_edited",
    #                                                         "loginAD":"edit_user_loginAD_one_edited",
    #                                                         "phone":"123456789"
    #                                                          })
    #
    #     assert response.status_code == 200
    #     assert answer == response.json()
    #
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Изменяем телефон удаленного пользователя на уже существующий')
    # def test_Positive_login_loginAD_phone_edit(setup_add_delete_user_for_edit_user, make_request):
    #     name = 'edit_user'
    #     # Подготавливаем данные в JSON для запроса
    #     data = _.get_JSON_request(name, **{ 'id': setup_add_delete_user_for_edit_user[0],
    #                                                      "fname": "edit_user_fName_one",
    #                                                      "password": "edit_user_password_one",
    #                                                     "lname": "edit_user_lName_one",
    #                                                     "pname": "edit_user_pName_one",
    #                                                      "email": "edit_user@smiddle.com",
    #                                                      "fax":"edit_user_fax",
    #                                                     "agentId": "edit_user_agentId_one",
    #                                                     "login":"edit_user_login_one_edited",
    #                                                     "loginAD":"edit_user_loginAD_one_edited",
    #                                                     "phone":"123456789"
    #                                                      })
    #
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_user, data=data)
    #     # Данные которые должны быть в ответе
    #     answer = _.get_JSON_response(name, ** {'id': setup_add_delete_user_for_edit_user[0],
    #                                                         "fname": "edit_user_fName_one",
    #                                                          "password": "edit_user_password_one",
    #                                                         "lname": "edit_user_lName_one",
    #                                                         "pname": "edit_user_pName_one",
    #                                                          "email": "edit_user@smiddle.com",
    #                                                          "fax":"edit_user_fax",
    #                                                         "agentId": "edit_user_agentId_one",
    #                                                         "login":"edit_user_login_one_edited",
    #                                                         "loginAD":"edit_user_loginAD_one_edited",
    #                                                         "phone":"123456789"
    #                                                          })
    #
    #     assert response.status_code == 200
    #     assert answer == response.json()