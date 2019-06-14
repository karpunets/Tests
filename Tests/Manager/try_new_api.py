# -*- coding: utf-8 -*-

import allure
import pytest
import random

from bin.project import send_request
from bin.validator import equal_schema
from bin.api import root_group_id
from bin.common import random_string
from Data.URLs_MAP import Manager, AuthServer
from bin.helpers import get_property


class TestAuthorizationServer:

    # @allure.feature('Функциональный тест')
    # @allure.story('Получаем токент для рута')
    # def test_get_token_for_root(self):
    #     data = get_property("principal", "credential")
    #     response = send_request.post(AuthServer.token, data)
    #     print(response.json())
    #     assert (response.status_code, "X-Smiddle-Auth-Token") == (200, response.json()['name'])

    # @allure.feature('Функциональный тест')
    # @allure.story('Получаем токент для разных системных ролей')
    # @pytest.mark.parametrize("role_name",
    #                          ["ROOT", "ADMINISTRATOR", "SUPERVISOR", "USER"])
    # def test_get_token_for_system_roles(self, add_user_with_role, role_name):
    #     user = add_user_with_role(role_name)
    #     data = parse_request("auth", {"$principal": user['login'],
    #                                   "$credential": "qwerty"})
    #     response = send_request.post(TestAuthorizationServer.url, data['request'])
    #     assert equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент с не правильными полномочиями')
    def test_get_token_with_wrong_credentials(self):
        data = {"$principal": random_string(),
                "$credential": random_string()}
        response = send_request.post(AuthServer.token, data)
        expected_result = {'PRINCIPAL_NOT_FOUND': 'Not authorized. No user found'}
        assert (response.status_code, response.json()) == (500, expected_result)

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент с пустыми полномочиями(логин, пароль)')
    def test_get_token_with_empty_credentials(self):
        data = {"principal": None, "credential": None}
        response = send_request.post(AuthServer.token, data)
        expected_result = {'PRINCIPAL_EMPTY': 'principal is empty', 'CREDENTIALS_EMPTY': 'credentials is empty'}
        assert (response.status_code, response.json()) == (400, expected_result)

    # @allure.feature('Функциональный тест')
    # @allure.story('Получаем токент для удаленного пользователя')
    # def test_get_token_for_deleted_user(self, immutable_deleted_user):
    #     data = {"$principal": immutable_deleted_user['login'],
    #             "$credential": "qwerty"}
    #     response = send_request.post(TestAuthorizationServer.url, data['request'])
    #     expected_response = {'PRINCIPAL_NOT_FOUND': 'Not authorized. No user found'}
    #     assert (response.json(), response.status_code) == (expected_response, response.status_code)

    # @allure.feature('Функциональный тест')
    # @allure.story('Получаем токент для пользователя без прав доступа')
    # def test_get_token_for_user_without_credentials(self, immutable_user):
    #     data = parse_request("auth", {"$principal": immutable_user['login'],
    #                                   "$credential": "qwerty"})
    #     response = send_request.post(TestAuthorizationServer.url, data['request'])
    #     expected_response = {'BAD_CREDENTIALS': 'Not authorized. Wrong credential.'}
    #     assert (response.json(), response.status_code) == (expected_response, response.status_code)

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент для выключеного пользователя')
    def test_get_token_for_disabled_user(self, add_user_with_role):
        user = add_user_with_role("ROOT", enabled=False)
        data = parse_request("auth", {"$principal": user['login'],
                                      "$credential": "qwerty"})
        response = send_request.post(TestAuthorizationServer.url, data['request'])
        expected_response = {'USER_DISABLED': 'Account %s disabled.' % user['login']}
        assert (response.status_code, response.json()) == (500, expected_response)

    @allure.feature('Функциональный тест')
    @allure.story('Логинимся с полученым токеном и проверяем соответсвие логина')
    def test_signin_with_token_check_login(self, add_user_with_role):
        user = add_user_with_role('ADMINISTRATOR')
        data = parse_request("auth", {"$principal": user['login'],
                                      "$credential": "qwerty",
                                      "$sessionLiveTimeSec": 300})
        response_auth = send_request.post(TestAuthorizationServer.url, data['request'])
        response_auth = response_auth.json()
        headers = {'content-type': "application/json;charset=UTF-8"}
        headers[response_auth['name']] = response_auth['token']
        response_current_account = send_request.get('account', headers=headers)
        assert user['login'] == response_current_account.json()['login']

# @allure.feature('Функциональный тест')
# @allure.story('Создаем группу')
# def test_add_group():
#     data = {"$name": random_string(),
#             "$parentGroupId": root_group_id()}
#     response = send_request.post(Manager.groups, data)
#     assert equal_schema(response.json(), response.expected)
#     assert response.status_code == 201