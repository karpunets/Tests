import pytest
import allure


from Data.Make_requests_and_answers import JSON_generator
import Data.URLs_MAP as URL

@allure.feature('Позивтный тест')
@allure.story('Проверяем поиск по ФИО')
@pytest.mark.parametrize('request_params', )
def test_Positive_f_l_p_names_one_user(setup_add_delete_user, make_request):
    name = 'get_user_list'
    # Подготавливаем данные в JSON для запроса
    data = JSON_generator.get_request_JSON(name, **{"fName": "get_userlist_fName_one",
                                                    "lName": "get_userlist_lName_one",
                                                    "pName": "get_userlist_pName_one"
                                                         })
    # Делаем запрос и получаем ответ
    response = make_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = JSON_generator.get_response_JSON(name, **{'id': setup_add_delete_user[0],
                                                       "fname": "get_userlist_fName_one",
                                                       "lname": "get_userlist_lName_one",
                                                       "pname": "get_userlist_pName_one",
                                                       "agentId": "get_userlist_agentId_one",
                                                       "login":"get_userlist_login_one",
                                                       "loginAD":"get_userlist_loginAD_one",
                                                       "phone":"666816321"
                                                       })

    assert response.status_code == 200
    assert answer == response.json()

@allure.feature('Позивтный тест')
@allure.story('Проверяем поиск по всем абонентам(не заполнены поля)')
def test_all_empty(setup_add_delete_user, make_request):
    name = 'get_user_list'
    # Подготавливаем данные в JSON для запроса
    data = JSON_generator.get_request_JSON(name, **{"data": "[]"
                                                         })
    # Делаем запрос и получаем ответ
    response = make_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = JSON_generator.get_response_JSON(name, **{"data": "[]"
                                                       })

    assert response.status_code == 200
    assert answer == response.json()

@allure.feature('Позивтный тест')
@allure.story('Поиск по Логину, роли и групе')
def test_Positive_roleid_goupid_login_one_user(setup_add_delete_user, make_request):
    name = 'get_user_list'
    #Подготавливаем данные в JSON для запроса
    data = JSON_generator.get_request_JSON(name,**{"roleId":3,
                                                   "groupId":2,
                                                   "login":"get_userlist_login_one"})
    #Делаем запрос и получаем ответ
    response = make_request(url=URL.get_user_list, data=data)
    #Данные которые должны быть в ответе
    answer = JSON_generator.get_response_JSON(name,**{'id': setup_add_delete_user[0],
                                                       "fname": "get_userlist_fName_one",
                                                       "lname": "get_userlist_lName_one",
                                                       "pname": "get_userlist_pName_one",
                                                       "agentId": "get_userlist_agentId_one",
                                                       "login":"get_userlist_login_one",
                                                       "loginAD":"get_userlist_loginAD_one",
                                                       "phone":"666816321"
                                                       })

    assert response.status_code == 200
    #Совпадает ли ответ с предполагаемым
    assert answer == response.json()

@allure.feature('Позивтный тест')
@allure.story('Поиск по adLogin, agentId и телефону ')

def test_Positive_AD_phone_agent_ID_one_user(setup_add_delete_user, make_request):
    name = 'get_user_list'
    #Подготавливаем данные в JSON для запроса
    data = JSON_generator.get_request_JSON(name,**{"adLogin":"get_userlist_loginAD_one",
                                                   "agentId":"get_userlist_agentId_one",
                                                   "phone":"666816321"})
    #Делаем запрос и получаем ответ
    response = make_request(url=URL.get_user_list, data=data)
    #Данные которые должны быть в ответе
    answer = JSON_generator.get_response_JSON(name,**{'id': setup_add_delete_user[0],
                                                       "fname": "get_userlist_fName_one",
                                                       "lname": "get_userlist_lName_one",
                                                       "pname": "get_userlist_pName_one",
                                                       "agentId": "get_userlist_agentId_one",
                                                       "login":"get_userlist_login_one",
                                                       "loginAD":"get_userlist_loginAD_one",
                                                       "phone":"666816321"
                                                       })

    assert response.status_code == 200
    #Совпадает ли ответ с предполагаемым
    assert answer == response.json()

# @allure.feature('Позивтный тест')
# @allure.story('Пагинация')
# def test_Positive_pagination_n_ps(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"fname": "get_userlist_fName",
#                                                    "page_number":2,
#                                                    "page_size":15})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'id': setup_add_delete_user[0],
#                                                        "fname": "get_userlist_fName_one",
#                                                        "lname": "get_userlist_lName_one",
#                                                        "pname": "get_userlist_pName_one",
#                                                        "agentId": "get_userlist_agentId_one",
#                                                        "login":"get_userlist_login_one",
#                                                        "loginAD":"get_userlist_loginAD_one",
#                                                        "phone":"666816321"
#                                                        })
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()


# def test_Positive_pagination_srtfild_ord(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"sortfield": "lname",
#                                                    "order":"DESC"})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'id': setup_add_delete_user[0],
#                                                        "fname": "get_userlist_fName_one",
#                                                        "lname": "get_userlist_lName_one",
#                                                        "pname": "get_userlist_pName_one",
#                                                        "agentId": "get_userlist_agentId_one",
#                                                        "login":"get_userlist_login_one",
#                                                        "loginAD":"get_userlist_loginAD_one",
#                                                        "phone":"666816321"
#                                                        })
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()


# def test_Negative_more_256(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     big_string = 'Q'*257
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"fname": big_string,
#                                                        "lname": big_string,
#                                                        "pname": big_string,
#                                                        "agentId": big_string,
#                                                        "login":big_string,
#                                                        "loginAD":big_string,
#                                                        "phone":big_string})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = {
#   "ADM_VALIDATION_USER_LAST_NAME_LENGTH": "LNAME length from 1 to 256",
#   "ADM_VALIDATION_USER_PHONE_LENGTH": "PHONE length from 1 to 256",
#   "ADM_VALIDATION_USER_AGENTID_LENGTH": "AGENTID length from 1 to 256",
#   "ADM_VALIDATION_USER_PATRONYMIC_NAME_LENGTH": "PNAME length from 1 to 256",
#   "ADM_VALIDATION_USER_FIRST_NAME_LENGTH": "FNAME length from 1 to 256",
#   "ADM_VALIDATION_USER_ADLOGIN_LENGTH": "ADLOGIN length from 1 to 64",
#   "ADM_VALIDATION_USER_LOGIN_LENGTH": "LOGIN length from 1 to 256"
# }
#
#     assert response.status_code == 400
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()

# def test_Negative_roleId(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"roleId": 9999})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'data':[],
#                                                       'row_count': 0})
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()


# def test_Negative_groupId(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"groupId": 9999})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'data':[],
#                                                       'row_count': 0})
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()

# def test_Negative_login(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"login": "NO_SUCH_DATA"})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'data':[],
#                                                       'row_count': 0})
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()

# def test_Negative_adlogin(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"adLogin": "NO_SUCH_DATA"})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'data':[],
#                                                       'row_count': 0})
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()

# def test_Negative_agentId(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"agentId": "NO_SUCH_DATA"})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'data':[],
#                                                       'row_count': 0})
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()


# def test_Negative_phone(setup_add_delete_user, make_request):
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"phone": "99999999"})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'data':[],
#                                                       'row_count': 0})
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     assert answer == response.json()
#
# def test_Negative_pagination_num_size(setup_add_delete_user, make_request):                          ?????????????????????????????????????????????
#     name = 'get_user_list'
#     #Подготавливаем данные в JSON для запроса
#     data = JSON_generator.get_request_JSON(name,**{"fname": "get_userlist_fName_one",
#                                                    "page_number":999,
#                                                    "page_size":100})
#     #Делаем запрос и получаем ответ
#     response = make_request(url=URL.get_user_list, data=data)
#     #Данные которые должны быть в ответе
#     answer = JSON_generator.get_response_JSON(name,**{'id': setup_add_delete_user[0],
#                                                        "fname": "get_userlist_fName_one",
#                                                        "lname": "get_userlist_lName_one",
#                                                        "pname": "get_userlist_pName_one",
#                                                        "agentId": "get_userlist_agentId_one",
#                                                        "login":"get_userlist_login_one",
#                                                        "loginAD":"get_userlist_loginAD_one",
#                                                        "phone":"666816321",
#                                                           "page_number": 1,
#                                                           "page_size": 100
#                                                        })
#
#     assert response.status_code == 200
#     #Совпадает ли ответ с предполагаемым
#     #assert answer == response.json()
#     print(answer)
#     print(response.json())

