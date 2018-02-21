import allure

import Data.URLs_MAP as URL
from bin.Make_requests_and_answers import JSON_generator as _

name = 'get_user_list'


@allure.feature('Позитивный тест')
@allure.story('Проверяем поиск по ФИО')
def test_Positive_f_l_p_names_one_user(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"fName": "get_userlist_fName_one",
                                       "lName": "get_userlist_lName_one",
                                       "pName": "get_userlist_pName_one"
                                       })

    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': setup_get_user_list[0],
                                          "fname": "get_userlist_fName_one",
                                          "lname": "get_userlist_lName_one",
                                          "pname": "get_userlist_pName_one",
                                          "agentId": "get_userlist_agentId_one",
                                          "login": "get_userlist_login_one",
                                          "loginAD": "get_userlist_loginAD_one",
                                          "phone": "666816321"
                                          })

    assert response.status_code == 200
    assert answer == response.json()

@allure.feature('Позитивный тест')
@allure.story('Проверяем поиск всех абонентов(не заполнены поля)')
def test_all_empty(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"data": "[]"})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    assert response.status_code == 200
    assert response.json()['row_count'] == 53


@allure.feature('Позитивный тест')
@allure.story('Поиск по Логину, роли и групе')
def test_Positive_roleid_goupid_login_one_user(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"roleId": 3,
                                       "groupId": 2,
                                       "login": "get_userlist_login_one"})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': setup_get_user_list[0],
                                          "fname": "get_userlist_fName_one",
                                          "lname": "get_userlist_lName_one",
                                          "pname": "get_userlist_pName_one",
                                          "agentId": "get_userlist_agentId_one",
                                          "login": "get_userlist_login_one",
                                          "loginAD": "get_userlist_loginAD_one",
                                          "phone": "666816321"
                                          })

    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Поиск по adLogin, agentId и телефону')
def test_Positive_AD_phone_agent_ID_one_user(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"adLogin": "get_userlist_loginAD_one",
                                       "agentId": "get_userlist_agentId_one",
                                       "phone": "666816321"})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': setup_get_user_list[0],
                                          "fname": "get_userlist_fName_one",
                                          "lname": "get_userlist_lName_one",
                                          "pname": "get_userlist_pName_one",
                                          "agentId": "get_userlist_agentId_one",
                                          "login": "get_userlist_login_one",
                                          "loginAD": "get_userlist_loginAD_one",
                                          "phone": "666816321"
                                          })

    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Пагинация: "page_number":2, 15 на страницу')
def test_Positive_pagination_n_ps(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"fname": "get_userlist_fName",
                                       "page_number": 2,
                                       "page_size": 15})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert response.json()['data'][0]['fname'] == "get_userlist_fName_22" and response.json()['data'][14]['fname'] == "get_userlist_fName_35"



@allure.feature('Позитивный тест')
@allure.story('Пагинация: Сортировка по фамилии DESC')
def test_Positive_pagination_srtfild_ord(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"sortfield": "lname",
                                       "order": "DESC"})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе

    assert response.status_code == 200
    assert response.json()['order'] == 'DESC'
    assert response.json()['data'][0]['login'] == 'root'


@allure.feature('Негативный тест')
@allure.story('Задаем больше 255 символов в параметры')
def test_Negative_more_256(setup_get_user_list, send_request):
    big_string = 'Q' * 257
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"fname": big_string,
                                       "lname": big_string,
                                       "pname": big_string,
                                       "agentId": big_string,
                                       "login": big_string,
                                       "loginAD": big_string,
                                       "phone": big_string})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = {
        "ADM_VALIDATION_USER_LAST_NAME_LENGTH": "LNAME length from 1 to 256",
        "ADM_VALIDATION_USER_PHONE_LENGTH": "PHONE length from 1 to 256",
        "ADM_VALIDATION_USER_AGENTID_LENGTH": "AGENTID length from 1 to 256",
        "ADM_VALIDATION_USER_PATRONYMIC_NAME_LENGTH": "PNAME length from 1 to 256",
        "ADM_VALIDATION_USER_FIRST_NAME_LENGTH": "FNAME length from 1 to 256",
        "ADM_VALIDATION_USER_ADLOGIN_LENGTH": "ADLOGIN length from 1 to 64",
        "ADM_VALIDATION_USER_LOGIN_LENGTH": "LOGIN length from 1 to 256"
    }
    print(response.json())
    assert response.status_code == 400
    # Совпадает ли ответ с предполагаемым
    #assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Ищем не существующее значение "roleId')
def test_Negative_roleId(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"roleId": 99999999})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'data': [],
                                          'row_count': 0})

    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Ищем не существующее значение "groupId')
def test_Negative_groupId(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"groupId": 9999})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'data': [],
                                          'row_count': 0})

    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Ищем не существующее значение "login"')
def test_Negative_login(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"login": "NO_SUCH_DATA"})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'data': [],
                                          'row_count': 0})
    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Ищем не существующее значение "adLogin"')
def test_Negative_adlogin(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"adLogin": "NO_SUCH_DATA"})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'data': [],
                                          'row_count': 0})

    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Ищем не существующее значение "agentId"')
def test_Negative_agentId(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"agentId": "NO_SUCH_DATA"})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'data': [],
                                          'row_count': 0})

    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()

@allure.feature('Негативный тест')
@allure.story('Ищем не существующее значение номера телефона')
def test_Negative_phone(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"phone": "99999999"})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'data': [],
                                          'row_count': 0})
    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()

@allure.feature('Негативный тест')
@allure.story('Указываем не существующую страницу')
def test_Negative_pagination_num_size(setup_get_user_list, send_request):

    #Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name,**{"fname": "get_userlist_fName_one",
                                                   "page_number":999,
                                                   "page_size":100})
    #Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    #Данные которые должны быть в ответе
    answer = {'page_number': 1, "page_size": 100}

    assert response.status_code == 200
    #Совпадает ли ответ с предполагаемым
    for key in answer:
        assert answer[key] == response.json()[key]


@allure.feature('Позитивный тест')
@allure.story('Проверяем поиск по ФИО удаленного пользователя')
def test_Positive_f_l_p_names_deleted_user(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"fName": "get_userlist_fName_deleted",
                                       "lName": "get_userlist_lName_deleted",
                                       "pName": "get_userlist_pName_deleted",
                                       "showDeletedOnly": True
                                       })

    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': setup_get_user_list[1],
                                          "fname": "get_userlist_fName_deleted",
                                          "lname": "get_userlist_lName_deleted",
                                          "pname": "get_userlist_pName_deleted",
                                          "agentId": "get_userlist_agentId_deleted",
                                          "login": "get_userlist_login_deleted",
                                          "loginAD": "get_userlist_loginAD_deleted",
                                          "phone": "6668163212",
                                          'deleted': True
                                          })

    assert response.status_code == 200
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Поиск по Логину, роли и групе удаленного пользователя')
def test_Positive_roleid_goupid_login_deleted_user(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"roleId": 3,
                                       "groupId": 2,
                                       "login": "get_userlist_login_deleted",
                                       "showDeletedOnly": True})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': setup_get_user_list[1],
                                          "fname": "get_userlist_fName_deleted",
                                          "lname": "get_userlist_lName_deleted",
                                          "pname": "get_userlist_pName_deleted",
                                          "agentId": "get_userlist_agentId_deleted",
                                          "login": "get_userlist_login_deleted",
                                          "loginAD": "get_userlist_loginAD_deleted",
                                          "phone": "6668163212",
                                          'deleted': True
                                          })

    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()


@allure.feature('Позитивный тест')
@allure.story('Поиск по adLogin, agentId и телефону удаленного пользователя')
def test_Positive_AD_phone_agent_ID_deleted_user(setup_get_user_list, send_request):
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"adLogin": "get_userlist_loginAD_deleted",
                                       "agentId": "get_userlist_agentId_deleted",
                                       "phone": "6668163212",
                                       "showDeletedOnly": True})
    # Делаем запрос и получаем ответ
    response = send_request(url=URL.get_user_list, data=data)
    # Данные которые должны быть в ответе
    answer = _.get_JSON_response(name, **{'id': setup_get_user_list[1],
                                          "fname": "get_userlist_fName_deleted",
                                          "lname": "get_userlist_lName_deleted",
                                          "pname": "get_userlist_pName_deleted",
                                          "agentId": "get_userlist_agentId_deleted",
                                          "login": "get_userlist_login_deleted",
                                          "loginAD": "get_userlist_loginAD_deleted",
                                          "phone": "6668163212",
                                          'deleted': True
                                          })

    assert response.status_code == 200
    # Совпадает ли ответ с предполагаемым
    assert answer == response.json()
