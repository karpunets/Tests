# -*- coding: utf-8 -*-

import allure
import pytest
import random

from bin.client import send_request
from bin.api import root_group_id, root_role_id
from bin.common import parse_request, equal_schema, random_string
from bin.helpers import get_property


class TestAuthorizationServer:
    url = "token"

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент для рута')
    def test_get_token_for_root(self):
        data = get_property("principal", "credential")
        response = send_request.post(TestAuthorizationServer.url, data)
        print(response.json())
        assert (response.status_code, "X-Smiddle-Auth-Token") == (200, response.json()['name'])

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент для разных системных ролей')
    @pytest.mark.parametrize("role_name",
                             ["ROOT", "ADMINISTRATOR", "SUPERVISOR", "USER"])
    def test_get_token_for_system_roles(self, add_user_with_role, role_name):
        user = add_user_with_role(role_name)
        data = parse_request("auth", {"$principal": user['login'],
                                      "$credential": "qwerty"})
        response = send_request.post(TestAuthorizationServer.url, data['request'])
        assert equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент с не правильными полномочиями')
    def test_get_token_with_wrong_credentials(self):
        data = {"principal": random_string(),
                "credential": random_string()}
        response = send_request.post(TestAuthorizationServer.url, data)
        expected_result = {'PRINCIPAL_NOT_FOUND': 'Not authorized. No user found'}
        assert (response.status_code, response.json()) == (500, expected_result)

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент с пустыми полномочиями(логин, пароль)')
    def test_get_token_with_empty_credentials(self):
        data = {"principal": None, "credential": None}
        response = send_request.post(TestAuthorizationServer.url, data)
        expected_result = {'PRINCIPAL_EMPTY': 'principal is empty', 'CREDENTIALS_EMPTY': 'credentials is empty'}
        assert (response.status_code, response.json()) == (400, expected_result)

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент для удаленного пользователя')
    def test_get_token_for_deleted_user(self, immutable_deleted_user):
        data = parse_request("auth", {"$principal": immutable_deleted_user['login'],
                                      "$credential": "qwerty"})
        response = send_request.post(TestAuthorizationServer.url, data['request'])
        expected_response = {'PRINCIPAL_NOT_FOUND': 'Not authorized. No user found'}
        assert (response.json(), response.status_code) == (expected_response, response.status_code)

    @allure.feature('Функциональный тест')
    @allure.story('Получаем токент для пользователя без прав доступа')
    def test_get_token_for_user_without_credentials(self, immutable_user):
        data = parse_request("auth", {"$principal": immutable_user['login'],
                                      "$credential": "qwerty"})
        response = send_request.post(TestAuthorizationServer.url, data['request'])
        expected_response = {'BAD_CREDENTIALS': 'Not authorized. Wrong credential.'}
        assert (response.json(), response.status_code) == (expected_response, response.status_code)

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


class TestGroups:
    url = "groups"

    @allure.feature('Функциональный тест')
    @allure.story('Получаем все группы')
    def test_get_groups(self):
        response = send_request.get(TestGroups.url)
        assert response.status_code == 200 and "ROOT" in response.json()[0]['name']

    @allure.feature('Функциональный тест')
    @allure.story('Получаем групу по ID')
    def test_get_group_by_id(self, group):
        response = send_request.get(TestGroups.url, id_to_url=group['groupId'])
        print(response.json())
        assert (response.status_code, response.json()) == (200, group)

    @allure.feature('Функциональный тест')
    @allure.story('Проверяем есть ли ранеее созданная группа в списке полученных груп')
    def test_get_group_bew_group_in_group_list(self, group):
        response = send_request.get(TestGroups.url)
        rootChildrenIds = [group['groupId'] for group in response.json()[0]['children']]
        assert response.status_code == 200 and group['groupId'] in rootChildrenIds

    @allure.feature('Проверка валидации')
    @allure.story('Получаем группу с неизвестным id')
    def test_get_group_with_unknownId(self):
        unknown_id = random_string()
        response = send_request.get(TestGroups.url, id_to_url=unknown_id)
        excepted_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'GROUP by groupId=%s not found' % unknown_id}
        assert (response.status_code, response.json()) == (400, excepted_response)

    @allure.feature('Функциональный тест')
    @allure.story('Создаем группу')
    @pytest.mark.idToDelete
    def test_add_group(self, clear_data):
        data = parse_request("post_group", {"$name": random_string(),
                                            "$parentGroupId": root_group_id()})
        response = send_request.post(TestGroups.url, data['request'])
        print(response.json())
        # clear_data.append(response.json()['groupId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу без имени')
    def test_addGroup_without_name(self):
        data = parse_request("post_group", {"$name": None,
                                            "$parentGroupId": root_group_id()})
        response = send_request.post(TestGroups.url, data['request'])
        print(response.json())
        excepted_response = {'ADM_VALIDATION_GROUP_NAME': 'Group name not specified'}
        assert (response.status_code, response.json()) == (400, excepted_response)

    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу без parentGroupId')
    def test_addGroup_without_group(self):
        data = parse_request("post_group", {"$name": random_string(),
                                            "$parentGroupId": None})
        response = send_request.post(TestGroups.url, data['request'])
        excepted_response = {'DATA_ACCESS_NO_RESULT_EXCEPTION': 'No entity found for query'}
        assert (response.status_code, response.json()) == (400, excepted_response)

    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу с неизвестным parendGroupId')
    def test_addGroup_with_unknown_parentGroupId(self):
        random_group_id = random_string()
        data = parse_request("post_group", {"$name": random_string(),
                                            "$parentGroupId": random_group_id
                                            })
        response = send_request.post(TestGroups.url, data['request'])
        expected_response = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % random_group_id}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональный тест')
    @allure.story('Создаем группу с сущесвующим именем')
    def test_addGroup_with_existing_name(self, immutable_group_with_child, clear_data):
        existin_group_name = immutable_group_with_child['name']
        data = parse_request("post_group", {"$name": existin_group_name,
                                            "$parentGroupId": root_group_id()})
        response = send_request.post(TestGroups.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['groupId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу')
    def test_edit_group(self, group):
        data = parse_request("put_group", {"$name": random_string(),
                                           "$groupId": group['groupId']})
        response = send_request.put(TestGroups.url, data['request'], id_to_url=group['groupId'])
        print(response.json())
        assert response.status_code == 200 and equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу на пустое имя')
    def test_edit_group_on_empty_name(self, group):
        data = parse_request("put_group", {"$name": None,
                                           "$groupId": group['groupId']})
        response = send_request.put(TestGroups.url, data['request'], id_to_url=group['groupId'])
        print(response.json())
        expected_response = {'ADM_VALIDATION_GROUP_NAME': 'Group name not specified'}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу с неизвестным groupId')
    def test_edit_group_with_unknown_groupId(self, group):
        unknown_group_id = random_string()
        data = parse_request("put_group", {"$name": random_string(),
                                           "$groupId": group['groupId']})
        response = send_request.put(TestGroups.url, data['request'], id_to_url=unknown_group_id)
        expected_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'GROUP by groupId=%s not found' % unknown_group_id}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональный тест')
    @allure.story('Удаляем группу')
    def test_delete_group(self, group):
        response = send_request.delete(TestGroups.url, id_to_url=group['groupId'])
        assert (response.status_code, response.json()) == (200, group)

    @allure.feature('Проверка валидации')
    @allure.story('Удаляем группу с неизвестным id')
    def test_delete_group_with_unknown_id(self):
        unknown_group_id = random_string()
        response = send_request.delete(TestGroups.url, id_to_url=unknown_group_id)
        expected_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'GROUP by groupId=%s not found' % unknown_group_id}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Проверка валидации')
    @allure.story('Удаляем группу у которой есть child')
    def test_delete_group_with_child(self, immutable_group_with_child):
        group_id = immutable_group_with_child['groupId']
        response = send_request.delete(TestGroups.url, id_to_url=group_id)
        print(response.json())
        expected_response = {'COMMON_NOT_ALLOWED_OPERATION': 'The group has subgroups'}
        assert (response.status_code, response.json()) == (400, expected_response)


class TestRoles:
    url = "roles"

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с первым child от рута')
    def test_add_role_with_first_root_child(self, immutable_group_with_child, clear_data):
        data = parse_request('post_roles', {"$name": random_string(),
                                            "$groupId": immutable_group_with_child['groupId']})
        response = send_request.post(TestRoles.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['roleId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль')
    def test_add_role_without_name(self, immutable_group_with_child):
        data = parse_request('post_roles', {"$name": None,
                                            "$groupId": immutable_group_with_child['groupId']})
        response = send_request.post(TestRoles.url, data['request'])
        expected_response = {'ADM_VALIDATION_ROLE_NAME': 'Role name not specified'}
        print(response.json())
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с root групой')
    def test_add_role_with_root_group(self, clear_data):
        data = parse_request('post_roles', {"$name": random_string(),
                                            "$groupId": root_group_id()})
        response = send_request.post(TestRoles.url, data['request'])
        clear_data.append(response.json()['roleId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с templateRole')
    def test_add_role_with_templateRole(self, clear_data):
        data = parse_request('post_roles', {"$name": random_string(),
                                            "$groupId": root_group_id(),
                                            "$templateRole": {"roleId": root_role_id()}})
        response = send_request.post(TestRoles.url, data['request'])
        clear_data.append(response.json()['roleId'])
        assert (response.status_code, response.json()['templateRole']['roleId']) == (201, root_role_id())

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с вторым по вложености child')
    def test_add_role_with_second_child(self, immutable_group_with_child, clear_data):
        child_group_id = immutable_group_with_child['children'][0]['groupId']
        data = parse_request('post_roles', {"$name": random_string(),
                                            "$groupId": child_group_id})
        response = send_request.post(TestRoles.url, data['request'])
        clear_data.append(response.json()['roleId'])
        assert (response.status_code, response.json()['group']['groupId']) == (
            201, immutable_group_with_child['groupId'])

    # Не правильный текст валидации
    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль без группы')
    def test_add_role_without_group(self):
        data = parse_request('post_roles', {"$name": random_string(),
                                            "$groupId": None})
        response = send_request.post(TestRoles.url, data['request'])
        print(response.json())
        expected_response = {'ADM_VALIDATION_ROLE_GROUP_EMPTY': 'Role group not specified'}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с неизвестной групой')
    def test_add_role_with_unknown_group(self):
        unknown_group_id = random_string()
        data = parse_request('post_roles', {"$name": random_string(),
                                            "$groupId": unknown_group_id})
        response = send_request.post(TestRoles.url, data['request'])
        expected_response = {
            'ADM_VALIDATION_GROUP_NOT_FOUND': 'Group by the following group id not found: %s' % unknown_group_id}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с сущесвующим именем')
    def test_add_role_with_existing_name(self, role):
        existing_name = role['name']
        print(role)
        data = parse_request('post_roles', {"$name": existing_name,
                                            "$groupId": role['group']['groupId']})
        response = send_request.post(TestRoles.url, data['request'])
        expected_response = {'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'Name is not unique'}
        assert (response.status_code, response.json()) == (409, expected_response)

    @allure.feature('Функциональний тест')
    @allure.story('Получаем все роли')
    def test_get_roles(self, role):
        response = send_request.get(TestRoles.url)
        role.pop("templateRole")
        assert response.status_code == 200 and role in response.json()

    @allure.feature('Функциональний тест')
    @allure.story('Получаем конкретную роль по id')
    def test_get_role_by_id(self, role):
        response = send_request.get(TestRoles.url, id_to_url=role['roleId'])
        role.pop("templateRole")
        assert (response.status_code, response.json()) == (200, role)

    @allure.feature('Функциональний тест')
    @allure.story('Получаем конкретную роль по не известному id')
    def test_get_role_by_unknown_id(self):
        unknown_role_id = random_string()
        response = send_request.get(TestRoles.url, id_to_url=unknown_role_id)
        expected_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'ROLE by roleId=%s not found' % unknown_role_id}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональний тест')
    @allure.story('Удаляем роль')
    def test_delete_role(self, role):
        role.pop("templateRole")
        response = send_request.delete(TestRoles.url, id_to_url=role['roleId'])
        assert (response.status_code, response.json()) == (200, role)

    @allure.feature('Функциональний тест')
    @allure.story('Удаляем роль с неизвестным id')
    def test_delete_role_by_unknown_id(self):
        unknown_role_id = random_string()
        response = send_request.delete(TestRoles.url, id_to_url=unknown_role_id)
        expected_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'ROLE by roleId=%s not found' % unknown_role_id}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональний тест')
    @allure.story('Редактируем роль')
    def test_edit_role(self, role, immutable_group_with_child):
        data = parse_request('put_roles', {"$roleId": role['roleId'],
                                           "$name": random_string(),
                                           "$groupId": immutable_group_with_child['groupId']
                                           })
        response = send_request.put(TestRoles.url, data['request'], id_to_url=role['roleId'])
        assert response.status_code == 200 and equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональний тест')
    @allure.story('Редактируем роль на пустое имя')
    def test_edit_role_on_empty_name(self, role, immutable_group_with_child):
        data = parse_request('put_roles', {"$roleId": role['roleId'],
                                           "$name": None,
                                           "$groupId": immutable_group_with_child['groupId']
                                           })
        response = send_request.put(TestRoles.url, data['request'], id_to_url=role['roleId'])
        print(response.json())
        expected_response = {'ADM_VALIDATION_ROLE_NAME': 'Role name not specified'}
        assert (response.json(), response.status_code) == (expected_response, 400)

    @allure.feature('Функциональний тест')
    @allure.story('Редактируем роль на не существующую групу')
    def test_edit_role_on_unknown_group(self, role):
        unknown_group_id = random_string()
        data = parse_request('put_roles', {"$roleId": role['roleId'],
                                           "$name": random_string(),
                                           "$groupId": unknown_group_id
                                           })
        response = send_request.put(TestRoles.url, data['request'], id_to_url=role['roleId'])
        expected_response = {
            'ADM_VALIDATION_GROUP_NOT_FOUND': 'Group by the following group id not found: %s' % unknown_group_id}
        assert (response.json(), response.status_code) == (expected_response, 400)

    @allure.feature('Функциональний тест')
    @allure.story('Редактируем имя роли на существующее')
    def test_edit_role_name_on_existing(self, role, immutable_role):
        existing_name = immutable_role['name']
        data = parse_request('put_roles', {"$roleId": role['roleId'],
                                           "$name": existing_name,
                                           "$groupId": role['group']['groupId']
                                           })
        response = send_request.put(TestRoles.url, data['request'], id_to_url=role['roleId'])
        expected_response = {'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'Login is not unique'}
        assert (response.json(), response.status_code) == (expected_response, 409)


class TestUsers:
    url = "users"

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя только с обязательными полями')
    def test_add_user_with_required_fields(self, clear_data, immutable_role, userGroupRoles):
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$roleId": immutable_role['roleId'],
                                            "$userGroupRoles": userGroupRoles})

        response = send_request.post(TestUsers.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['userId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя со всеми полями')
    def test_add_user_with_all_fields(self, clear_data, immutable_role, userGroupRoles):
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$roleId": immutable_role['roleId'],
                                            "$agentId": random_string(),
                                            "$ADlogin": random_string(),
                                            "$pname": random_string(),
                                            "$email": random_string() + '@.com.ua',
                                            "$phone": str(random.randint(11111, 99999999)),
                                            "$fax": random_string(),
                                            "$userGroupRoles": userGroupRoles
                                            })
        response = send_request.post(TestUsers.url, data['request'])
        print(data['schema'])
        print(response.json())
        clear_data.append(response.json()['userId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя с уже существующим login')
    def test_add_user_with_existing_login(self, immutable_role, userGroupRoles, immutable_user):
        existing_login = immutable_user['login']
        data = parse_request("post_users", {"$login": existing_login,
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$userGroupRoles": userGroupRoles,
                                            "$roleId": immutable_role['roleId']})
        response = send_request.post(TestUsers.url, data['request'])
        expected_response = {'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'Login is not unique'}
        assert (response.status_code, response.json()) == (409, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя с существующими полями (кроме уникальных)')
    def test_add_user_with_existing_fields_which_are_not_unique(self, clear_data, immutable_role,
                                                                userGroupRoles, immutable_user):
        existing_field = immutable_user
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": existing_field['fname'],
                                            "$lname": existing_field['lname'],
                                            "$userGroupRoles": userGroupRoles,
                                            "$roleId": immutable_role['roleId'],
                                            "$agentId": random_string(),
                                            "$ADlogin": existing_field['loginAD'],
                                            "$pname": existing_field['pname'],
                                            "$email": existing_field['email'],
                                            "$phone": str(random.randint(1111111, 999999999)),
                                            "$fax": existing_field['phone']
                                            })
        response = send_request.post(TestUsers.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['userId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя с уже существующим phone')
    def test_add_user_with_existing_phone(self, immutable_role, userGroupRoles, immutable_user):
        existing_phone = immutable_user['phone']
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$userGroupRoles": userGroupRoles,
                                            "$roleId": immutable_role['roleId'],
                                            "$phone": existing_phone})
        response = send_request.post(TestUsers.url, data['request'])
        print(response.json())
        expected_response = {'COMMON_EXCEPTION': 'Not deleted user with phone = %s already exist!' % existing_phone}
        assert (response.status_code, response.json()) == (500, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя с уже существующим agentId')
    def test_add_user_with_existing_agentId(self, immutable_role, userGroupRoles, immutable_user):
        existing_agent_id = immutable_user['agentId']
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$userGroupRoles": userGroupRoles,
                                            "$roleId": immutable_role['roleId'],
                                            "$agentId": existing_agent_id})
        response = send_request.post(TestUsers.url, data['request'])
        print(response.json())
        expected_response = {'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'AGENT ID =%s already exists' % existing_agent_id}
        assert (response.status_code, response.json()) == (409, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя без login, fname, lname')
    def test_add_user_without_login_fname_lname(self, immutable_role, userGroupRoles):
        data = parse_request("post_users", {"$login": None,
                                            "$fname": None,
                                            "$lname": None,
                                            "$userGroupRoles": userGroupRoles,
                                            "$roleId": immutable_role['roleId']})
        response = send_request.post(TestUsers.url, data['request'])
        print(response.json())
        expected_response = {'ADM_VALIDATION_USER_LAST_NAME_LENGTH': 'Last name length from 1 to 256',
                             'ADM_VALIDATION_USER_FIRST_NAME_LENGTH': 'First name length from 1 to 256',
                             'ADM_VALIDATION_USER_LOGIN_LENGTH': 'Login length from 1 to 104'}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя без roleId')
    def test_add_user_without_groupId_roleId(self, userGroupRoles):
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$userGroupRoles": userGroupRoles,
                                            "$roleId": None})
        response = send_request.post(TestUsers.url, data['request'])
        expected_response = {'ADM_VALIDATION_ROLES_NOT_FOUND': 'Roles by the following role ids not found: null'}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя без groupId')
    def test_add_user_without_groupId(self, immutable_role):
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$groupId": None,
                                            "$roleId": immutable_role['roleId']})
        response = send_request.post(TestUsers.url, data['request'])
        expected_response = {'ADM_VALIDATION_USER_USER_GROUP_ROLES': 'User group roles is empty'}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Проверяем коррекстность добавления userGroupRoles при создании пользователя')
    def test_add_user_check_userGroupRoles(self, clear_data, immutable_role, userGroupRoles):
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$roleId": immutable_role['roleId'],
                                            "$userGroupRoles": userGroupRoles})
        response = send_request.post(TestUsers.url, data['request'])
        response_user_group_roles = response.json()['userGroupRoles']
        response_group_roles_set = set(
            response_user_group_roles[0]['group'].items() | response_user_group_roles[0]['roles'][0].items())
        added_user_group_roles = set(userGroupRoles[0]['roles'][0].items() | userGroupRoles[0]['group'].items())
        clear_data.append(response.json()['userId'])
        assert added_user_group_roles.issubset(response_group_roles_set)

    @allure.feature('функциональный тест')
    @allure.story('Добавляем пользователя, указывая в userGroupRoles роль, которой нет в roleId')
    def test_add_user_with_role_in_userGroupRoles_which_not_exist_in_roleId(self, userGroupRoles):
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$roleId": root_role_id(),
                                            "$userGroupRoles": userGroupRoles})
        response = send_request.post(TestUsers.url, data['request'])
        expected_response = {
            'ADM_VALIDATION_USER_NOT_ALLOWED_ROLE_IN_GROUP': 'Roles in groups by the following role ids not allowed: %s' %
                                                             userGroupRoles[0]['roles'][0]['roleId']}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Получаем пользователя по userId')
    def test_get_user(self, immutable_user):
        response = send_request.get(TestUsers.url, id_to_url=immutable_user['userId'])
        assert (response.json(), response.status_code) == (immutable_user, 200)

    @allure.feature('функциональный тест')
    @allure.story('Получаем пользователя по неизвестному id')
    def test_get_user_with_unknown_id(self):
        unknown_user_id = random_string()
        response = send_request.get(TestUsers.url, id_to_url=unknown_user_id)
        expected_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'USER not found by userId=%s' % unknown_user_id}
        assert (response.json(), response.status_code) == (expected_response, 400)

    @allure.feature('функциональный тест')
    @allure.story('Получаем удаленного пользователя по userId')
    def test_get_deleted_user(self, immutable_deleted_user):
        response = send_request.get(TestUsers.url, id_to_url=immutable_deleted_user['userId'])
        assert (response.json(), response.status_code) == (immutable_deleted_user, 200)

    @allure.feature('функциональный тест')
    @allure.story('Удаляем пользователя по userId')
    def test_delete_user(self, user):
        response = send_request.delete(TestUsers.url, id_to_url=user['userId'])
        assert (response.json(), response.status_code) == (user, 200)

    @allure.feature('функциональный тест')
    @allure.story('Удаляем пользователя по неизвестному userId')
    def test_delete_user_by_unknown_userId(self):
        unknown_user_id = random_string()
        response = send_request.delete(TestUsers.url, id_to_url=unknown_user_id)
        expected_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'USER not found by userId=%s' % unknown_user_id}
        assert (response.json(), response.status_code) == (expected_response, 400)

    @allure.feature('функциональный тест')
    @allure.story('Получаем disabled пользователя')
    def test_get_user_enabled_false(self, add_user_with_role):
        disabled_user = add_user_with_role(enabled=False)
        response = send_request.get(TestUsers.url, id_to_url=disabled_user['userId'])
        assert (response.json(), response.status_code) == (disabled_user, 200)

    @allure.feature('функциональный тест')
    @allure.story('Удаляем disabled пользователя')
    def test_delete_user_enabled_false(self, add_user_with_role):
        disabled_user = add_user_with_role(enabled=False)
        response = send_request.delete(TestUsers.url, id_to_url=disabled_user['userId'])
        assert (response.json(), response.status_code) == (disabled_user, 200)

    @allure.feature('функциональный тест')
    @allure.story('Удаляем disabled пользователя')
    def test_recover_deleted_user(self, immutable_deleted_user):
        pass
