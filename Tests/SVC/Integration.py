import allure
import pytest
import random, json
from Data.test_data import ROOT_group_id, ROOT_user_id

import Data.URLs_MAP as URL
from bin.Make_requests_and_answers import parse, equal_schema, random_string


# @allure.feature('Позитивный тест')
# @allure.story('Создаем нового пользователя с userType = DEVICE')
# def test_add_user_with_DEVICE_userType(send_request, delete_user):
#     data = parse('post_users', {'$name':random_string(),
#                                 '$email':random_string(),
#                                 '$userType':"DEVICE"})
#     response = send_request(URL.svc_users, data['request'])
#     instance = response.json()
#     assert response.status_code == 200
#     delete_user.append(instance['id'])
#     assert equal_schema(instance, data['schema'])
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Создаем нового пользователя с существующим email')
# def test_add_user_with_existing_email(send_request, add_user):
#     existing_email = next(add_user)['email']
#     data = parse('post_users', {'$name':random_string(),
#                                 '$email':existing_email,
#                                 '$userType':"DEVICE"})
#     response = send_request(URL.svc_users, data['request'])
#     expected_response = {'SVC_ENTITY_WITH_SUCH_FIELD_EXIST_EXCEPTION': 'SVCEntityWithSuchFieldAlreadyExistException: User with email="%s" already exists'%existing_email}
#     assert response.status_code == 500
#     assert response.json() == expected_response
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Создаем нового пользователя с userType = CMS_USER')
# def test_add_user_with_CMS_USER_userType(send_request):
#     data = parse('post_users', {'$name':random_string(),
#                                 '$email':random_string(),
#                                 '$userType':"CMS_USER"})
#     response = send_request(URL.svc_users, data['request'])
#     expect_answer = {'SVC_REQUEST_VALIDATION_EXCEPTION': 'SVCRequestValidationException: Unable to add cms user'}
#     assert response.status_code == 500
#     assert response.json() == expect_answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Создаем нового пользователя без имени i email')
# def test_add_user_without_name_and_email(send_request):
#     data = parse('post_users', {'$name':None,
#                                 '$email':None,
#                                 '$userType':"DEVICE"})
#     response = send_request(URL.svc_users, data['request'])
#     expect_answer = {'SVC_VALIDATION_USER_EMAIL_EMPTY': 'User email is empty',
#                      'SVC_VALIDATION_USER_NAME_EMPTY': 'User name is empty'}
#     assert response.status_code == 400
#     assert response.json() == expect_answer
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем пользователей')
# def test_get_users(send_request, add_user):
#     user_id = next(add_user)['id']
#     params = {"page_number":1,"page_size":100,"order":"ASC","sortedField":"name"}
#     response = send_request(method = "GET", url = URL.svc_users, params=params)
#     list_of_id = [user['id'] for user in response.json()["data"]]
#     assert response.status_code == 200
#     assert user_id in list_of_id
#
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем не существующую страницу с пользователями')
# def test_get_users_with_unknown_page(send_request):
#     params = {"page_number":2,"page_size":100,"order":"ASC","sortedField":"name"}
#     response = send_request(method = "GET", url = URL.svc_users, params=params)
#     assert response.status_code == 200
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем пользователя и проверяем удалился ли')
# def test_delete_user(send_request, add_user):
#     user = next(add_user)
#     response = send_request(method = "DELETE", url = URL.svc_users, params={'id':user['id']})
#     assert response.status_code == 200
#     assert response.json() == user
#     params = {"page_number":1,"page_size":200,"order":"ASC","sortedField":"name"}
#     response_get = send_request(method = "GET", url = URL.svc_users, params=params)
#     list_of_id = [user['id'] for user in response_get.json()["data"]]
#     assert user['id'] not in list_of_id
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Делаем синхронизацию пользователей с SVC')
# def test_sync_users(send_request, get_cms_user):
#     user = get_cms_user
#     response_delete = send_request(method = "DELETE", url = URL.svc_users, params={'id':user['id']})
#     assert response_delete.status_code == 200
#     response_sync = send_request(url = URL.svc_users_sync, data = {})
#     assert response_sync.status_code == 200
#     params = {"page_number": 1, "page_size": 100, "order": "ASC", "sortedField": "name"}
#     response_get = send_request(URL.svc_users, method="GET", params=params)
#     list_of_emails = [user['email'] for user in response_get.json()["data"]]
#     assert user['email'] in list_of_emails
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем пользователя')
# def test_edit_user(send_request, add_user):
#     user_id = next(add_user)['id']
#     data = parse("put_users", {"$id":user_id,
#                                "$email":random_string(),
#                                "$name":random_string(),
#                                "$userType":"DEVICE"})
#
#     response = send_request(method = "PUT", url = URL.svc_users, data=data['request'])
#     assert response.status_code == 200
#     assert equal_schema(response.json(), data['schema'])
#


@allure.feature('Позитивный тест')
@allure.story('Редактируем пользователя')
def test_edit_user(send_request, add_user):
    existing_user_email = next(add_user)['email']
    user_id = next(add_user)['id']
    data = parse("put_users", {"$id":user_id,
                               "$email":existing_user_email,
                               "$name":random_string(),
                               "$userType":"DEVICE"})
    response = send_request(method = "PUT", url = URL.svc_users, data=data['request'])
    print(response.json())
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])



#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем пользователя с неизвестным id')
# def test_delete_user_with_unknown_id(send_request):
#     unknown_user_id = random.randint(1,999999)
#     response = send_request(method = "DELETE", url = URL.svc_users, params={'id':unknown_user_id})
#     expected_answer = {'SVC_REQUEST_VALIDATION_EXCEPTION': 'SVCRequestValidationException: Unable to remove CMS user. User with id=%d not found'%unknown_user_id}
#     assert response.status_code == 500
#     assert response.json() == expected_answer





# def test_add_user_with_cms_user_email(send_request, get_deleted_cms_user):
#     user_email = get_deleted_cms_user['email']
#     data = parse('post_users', {'$name': random_string(),
#                                 '$email':user_email,
#                                 '$userType':"DEVICE"})
#     response_add = send_request(URL.svc_users, data['request'])
#     print(response_add.json())
#     response_sync = send_request(url=URL.svc_users_sync, data={})
#     print(response_sync.json())
#
# def test_get(send_request):
#     params = {"page_number": 1, "page_size": 100, "order": "ASC", "sortedField": "name"}
#     data = {"value": "a."}
#     response = send_request(url=URL.svc_users_search, data=data, params=params)
#     print(response.json())