import allure
import pytest
import random
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
# @allure.story('Создаем нового пользователя с userType = CMS_USER')
# def test_add_user_with_CMS_USER_userType(send_request):
#     data = parse('post_users', {'$name':random_string(),
#                                 '$email':random_string(),
#                                 '$userType':"CMS_USER"})
#     response = send_request(URL.svc_users, data['request'])
#     print(response.json())
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
#
#     response = send_request(URL.svc_users, data['request'])
#     print(response.json())
#     expect_answer = {'SVC_VALIDATION_USER_EMAIL_EMPTY': 'User email is empty',
#                      'SVC_VALIDATION_USER_NAME_EMPTY': 'User name is empty'}
#     assert response.status_code == 400
#     assert response.json() == expect_answer



@allure.feature('Позитивный тест')
@allure.story('Создаем нового пользователя без имени i email')
def test_add_user_without_name_23(send_request, add_user):
    user_id = add_user
    params = {"page_number":0,"page_size":1,"order":"ASC","sortedField":"name"}
    response = send_request(method = "GET", url = URL.svc_users, params=params)
    print(response.json())
    list_of_id = [user['id'] for user in response.json()["data"]]
    print(response.json())
    assert response.status_code == 200
    assert user_id in list_of_id

