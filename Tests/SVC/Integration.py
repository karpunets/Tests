import allure
import pytest
import random, json, time
from Data.test_data import ROOT_group_id, ROOT_user_id

import Data.URLs_MAP as URL
from bin.Make_requests_and_answers import parse, equal_schema, random_string


@allure.feature('Позитивный тест')
@allure.story('Создаем нового пользователя с userType = DEVICE')
def test_add_user_with_DEVICE_userType(send_request, delete_user):
    data = parse('post_users', {'$name':random_string(),
                                '$email':random_string(),
                                '$userType':"DEVICE"})
    response = send_request(URL.svc_users, data['request'])
    instance = response.json()
    assert response.status_code == 200
    delete_user.append(instance['id'])
    assert equal_schema(instance, data['schema'])


@allure.feature('Позитивный тест')
@allure.story('Создаем нового пользователя с существующим email')
def test_add_user_with_existing_email(send_request, add_user):
    existing_email = next(add_user)['email']
    data = parse('post_users', {'$name':random_string(),
                                '$email':existing_email,
                                '$userType':"DEVICE"})
    response = send_request(URL.svc_users, data['request'])
    expected_response = {'SVC_ENTITY_WITH_SUCH_FIELD_EXIST_EXCEPTION': 'SVCEntityWithSuchFieldAlreadyExistException: User with email="%s" already exists'%existing_email}
    assert response.status_code == 500
    assert response.json() == expected_response



@allure.feature('Позитивный тест')
@allure.story('Создаем нового пользователя с userType = CMS_USER')
def test_add_user_with_CMS_USER_userType(send_request):
    data = parse('post_users', {'$name':random_string(),
                                '$email':random_string(),
                                '$userType':"CMS_USER"})
    response = send_request(URL.svc_users, data['request'])
    expect_answer = {'SVC_REQUEST_VALIDATION_EXCEPTION': 'SVCRequestValidationException: Unable to add cms user'}
    assert response.status_code == 500
    assert response.json() == expect_answer


@allure.feature('Позитивный тест')
@allure.story('Создаем нового пользователя без имени i email')
def test_add_user_without_name_and_email(send_request):
    data = parse('post_users', {'$name':None,
                                '$email':None,
                                '$userType':"DEVICE"})
    response = send_request(URL.svc_users, data['request'])
    expect_answer = {'SVC_VALIDATION_USER_EMAIL_EMPTY': 'User email is empty',
                     'SVC_VALIDATION_USER_NAME_EMPTY': 'User name is empty'}
    assert response.status_code == 400
    assert response.json() == expect_answer



@allure.feature('Позитивный тест')
@allure.story('Получаем пользователей')
def test_get_users(send_request, add_user):
    user_id = next(add_user)['id']
    params = {"page_number":1,"page_size":100,"order":"ASC","sortedField":"name"}
    response = send_request(method = "GET", url = URL.svc_users, params=params)
    list_of_id = [user['id'] for user in response.json()["data"]]
    assert response.status_code == 200
    assert user_id in list_of_id




@allure.feature('Позитивный тест')
@allure.story('Получаем не существующую страницу с пользователями')
def test_get_users_with_unknown_page(send_request):
    params = {"page_number":2,"page_size":100,"order":"ASC","sortedField":"name"}
    response = send_request(method = "GET", url = URL.svc_users, params=params)
    assert response.status_code == 200



@allure.feature('Позитивный тест')
@allure.story('Удаляем пользователя и проверяем удалился ли')
def test_delete_user(send_request, add_user):
    user = next(add_user)
    response = send_request(method = "DELETE", url = URL.svc_users, params={'id':user['id']})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == user
    params = {"page_number":1,"page_size":200,"order":"ASC","sortedField":"name"}
    response_get = send_request(method = "GET", url = URL.svc_users, params=params)
    list_of_id = [user['id'] for user in response_get.json()["data"]]
    assert user['id'] not in list_of_id


@allure.feature('Позитивный тест')
@allure.story('Делаем синхронизацию пользователей с SVC')

def test_sync_users(send_request, get_cms_user):
    user = get_cms_user
    response_delete = send_request(method = "DELETE", url = URL.svc_users, params={'id':user['id']})
    print(response_delete.json())
    assert response_delete.status_code == 200
    response_sync = send_request(url = URL.svc_users_sync, data = {})
    print(response_sync.json())
    assert response_sync.status_code == 200
    params = {"page_number": 1, "page_size": 100, "order": "ASC", "sortedField": "name"}
    response_get = send_request(URL.svc_users, method="GET", params=params)
    list_of_emails = [user['email'] for user in response_get.json()["data"]]
    assert user['email'] in list_of_emails


@allure.feature('Позитивный тест')
@allure.story('Редактируем пользователя')
def test_edit_user(send_request, add_user):
    user_id = next(add_user)['id']
    data = parse("put_users", {"$id":user_id,
                               "$email":random_string(),
                               "$name":random_string(),
                               "$userType":"DEVICE"})

    response = send_request(method = "PUT", url = URL.svc_users, data=data['request'])
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])



@allure.feature('Позитивный тест')
@allure.story('Редактируем пользователя с существующим email')
def test_edit_user_on_existing_email(send_request, add_user):
    existing_user_email = next(add_user)['email']
    user_id = next(add_user)['id']
    data = parse("put_users", {"$id":user_id,
                               "$email":existing_user_email,
                               "$name":random_string(),
                               "$userType":"DEVICE"})
    response = send_request(method = "PUT", url = URL.svc_users, data=data['request'])
    except_response = {'SVC_ENTITY_WITH_SUCH_FIELD_EXIST_EXCEPTION': 'SVCEntityWithSuchFieldAlreadyExistException: User with email="%s" already exists'%existing_user_email}
    assert response.status_code == 500
    assert response.json() == except_response



@allure.feature('Позитивный тест')
@allure.story('Удаляем пользователя с неизвестным id')
def test_delete_user_with_unknown_id(send_request):
    unknown_user_id = random.randint(1,999999)
    response = send_request(method = "DELETE", url = URL.svc_users, params={'id':unknown_user_id})
    expected_answer = {'SVC_REQUEST_VALIDATION_EXCEPTION': 'SVCRequestValidationException: Unable to remove CMS user. User with id=%d not found'%unknown_user_id}
    assert response.status_code == 500
    assert response.json() == expected_answer



@allure.feature('Позитивный тест')
@allure.story('Удаляем пользователя')
def test_delete_user(send_request, add_user):
    user = next(add_user)
    response = send_request(method = "DELETE", url = URL.svc_users, params={'id':user['id']})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == user


@allure.feature('Позитивный тест')
@allure.story('Создаем конференцию')
def test_add_conference(send_request, delete_conference, get_users):
    users = get_users["cms_user"]
    data = parse('post_conference', {'$name':random_string(),
                                '$description':random_string(),
                                '$users':users})
    print("DATA___________", data)
    response = send_request(URL.svc_conference, data['request'])
    print("RESPONSE__________", response.json())
    assert response.status_code == 200
    delete_conference.append(response.json()['id'])
    assert equal_schema(response.json(), data['schema'])

@allure.feature('Позитивный тест')
@allure.story('Создаем конференцию')
def test_add_conference_with_DEVICE_user_only(send_request, delete_conference, add_user):
    device_user = [next(add_user)]
    data = parse('post_conference', {'$name':random_string(),
                                '$description':random_string(),
                                '$users':device_user})
    print("DATA___________", data)
    response = send_request(URL.svc_conference, data['request'])
    print("RESPONSE__________", response.json())
    assert response.status_code == 200
    delete_conference.append(response.json()['id'])
    assert equal_schema(response.json(), data['schema'])

@allure.feature('Позитивный тест')
@allure.story('Создаем конференцию')
def test_add_conference_with_CMS_USER_only(send_request, delete_conference, get_users):
    users = get_users["cms_user"]
    data = parse('post_conference', {'$name':random_string(),
                                '$description':random_string(),
                                '$users':users})
    print("DATA___________", data)
    response = send_request(URL.svc_conference, data['request'])
    print("RESPONSE__________", response.json())
    assert response.status_code == 200
    delete_conference.append(response.json()['id'])
    assert equal_schema(response.json(), data['schema'])


@allure.feature('Позитивный тест')
@allure.story('Создаем конференцию без пользователей')
def test_add_conference_without_users(send_request, delete_conference):
    data = parse('post_conference', {'$name':random_string(),
                                    '$description':random_string()})
    response = send_request(URL.svc_conference, data['request'])
    assert response.status_code == 200
    delete_conference.append(response.json()['id'])
    assert response.json()['users'] == []


@allure.feature('Позитивный тест')
@allure.story('Создаем конференцию с пустым именем')
def test_add_conference_with_empty_name(send_request, get_users):
    users = get_users['device'] + get_users["cms_user"]
    data = parse('post_conference', {'$name':None,
                                    '$description':None,
                                     "$users":users})
    response = send_request(URL.svc_conference, data['request'])
    expected_response = {'SVC_VALIDATION_CONFERENCE_NAME_EMPTY': 'Conference name is empty'}
    assert response.status_code == 400
    assert response.json() == expected_response


@allure.feature('Позитивный тест')
@allure.story('Создаем конференцию с пустым именем')
def test_add_conference_with_existing_name(send_request, add_conference, get_users):
    existing_name = next(add_conference)['name']
    users = get_users['device'] + get_users["cms_user"]
    data = parse('post_conference', {'$name':existing_name,
                                    '$description':random_string(),
                                     "$users":users})
    response = send_request(URL.svc_conference, data['request'])
    expected_response = {'SVC_ENTITY_WITH_SUCH_FIELD_EXIST_EXCEPTION': 'SVCEntityWithSuchFieldAlreadyExistException: Conference with name="%s" already exists'%existing_name}
    assert response.status_code == 500
    assert response.json() == expected_response

@allure.feature('Позитивный тест')
@allure.story('Редактируем конференцию')
def test_edit_conference(send_request, get_users, add_conference):
    users = get_users["cms_user"]
    conf = next(add_conference)
    print("CONF______", conf)
    conf_id = conf['id']
    data = parse('put_conference', {"$id":conf_id,
                                     '$name':random_string(),
                                '$description':random_string(),
                                '$users':users})
    print("DATA", data)
    response = send_request(URL.svc_conference, method="PUT", data=data['request'])
    print(response.json())
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])

@allure.feature('Позитивный тест')
@allure.story('Редактируем имя конференции на уже существующее')
def test_edit_conference_name_on_existing(send_request, get_users, add_conference):
    users = get_users["cms_user"]
    existing_name = next(add_conference)['name']
    conf_id = next(add_conference)['id']
    data = parse('put_conference', {"$id":conf_id,
                                     '$name':existing_name,
                                '$description':random_string(),
                                '$users':users})
    response = send_request(URL.svc_conference, method="PUT", data=data['request'])
    expect_response = {'SVC_ENTITY_WITH_SUCH_FIELD_EXIST_EXCEPTION': 'SVCEntityWithSuchFieldAlreadyExistException: Conference with name="%s" already exists.'%existing_name}
    assert response.status_code == 500
    assert response.json() == expect_response


@allure.feature('Позитивный тест')
@allure.story('Редактируем конференцию с неизвестным id')
def test_edit_conference_with_unknown_id(send_request, get_users):
    users = get_users['device'] + get_users["cms_user"]
    conf_id = random.randint(1,9999999)
    print(conf_id)
    data = parse('put_conference', {"$id":conf_id,
                                     '$name':random_string(),
                                '$description':random_string(),
                                '$users':users})
    response = send_request(URL.svc_conference, method = "PUT", data = data['request'])
    print(response.json())
    expect_response = {'SVC_REQUEST_VALIDATION_EXCEPTION': 'SVCRequestValidationException: Unable to update conference. Conference with id=%d not found.'%conf_id}
    assert response.status_code == 500
    assert response.json() == expect_response


@allure.feature('Позитивный тест')
@allure.story('Редактируем пользователей конференции, удаляем')
def test_edit_conference_users_on_empty(send_request, add_conference):
    conf = next(add_conference)
    print(conf)
    conf_id = conf['id']
    data = parse('put_conference', {"$id":conf_id,
                                     '$name':random_string(),
                                '$description':random_string(),
                                '$users':[]})
    response = send_request(URL.svc_conference, method="PUT", data=data['request'])
    print(response.json())
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])
#


@allure.feature('Позитивный тест')
@allure.story('Удаляем конференцию')
def test_delete_conference(send_request, add_conference):
    conf = next(add_conference)
    response = send_request(URL.svc_conference, method = "DELETE", params = {"id":conf['id']})
    print(response.json())
    assert response.status_code == 200


@allure.feature('Позитивный тест')
@allure.story('Создаем конференцию передавая только ід пользователей')
def test_add_conference_with_only_id_in_users(send_request, delete_conference, add_user):
    users = [{'id':next(add_user)['id']}]
    print(users)
    data = parse('post_conference', {'$name':random_string(),
                                '$description':random_string(),
                                '$users':users})
    print("DATA___________", data)
    response = send_request(URL.svc_conference, data['request'])
    print("RESPONSE__________", response.json())
    assert response.status_code == 200
    delete_conference.append(response.json()['id'])


@allure.feature('Позитивный тест')
@allure.story('Создаем конференцию')
def test_start_call(send_request, add_conference):
    conf_id = next(add_conference)['id']
    response = send_request(URL.svc_conference_start, data = {"id":conf_id})
    print(response.json())

