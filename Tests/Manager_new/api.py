# -*- coding: utf-8 -*-

import allure
import pytest
import random
from bin.session import Client
from bin.session import rootGroupId
from bin.session import getHeadersForUser
from bin.helpers import  make_user_group_roles
from bin.Make_requests_and_answers import parse_request, equal_schema, random_string


class TestGroups:
    url = "groups"

    @allure.feature('Функциональный тест')
    @allure.story('Получаем все группы')
    def test_get_groups(self):
        response = Client.get(TestGroups.url)
        assert response.status_code == 200 and "ROOT" in response.json()[0]['name']

    @allure.feature('Функциональный тест')
    @allure.story('Получаем групу по ID')
    def test_get_group_by_id(self, group):
        response = Client.get(TestGroups.url, id=group['groupId'])
        assert (response.status_code, response.json()) == (200, group)

    @allure.feature('Функциональный тест')
    @allure.story('Проверяем есть ли ранеее созданная группа в списке полученных груп')
    def test_get_group_bew_group_in_group_list(self, group):
        response = Client.get(TestGroups.url)
        rootChilderIds = [group['groupId'] for group in response.json()[0]['children']]
        assert response.status_code == 200 and group['groupId'] in rootChilderIds

    @allure.feature('Проверка валидации')
    @allure.story('Получаем группу с неизвестным id')
    def test_get_group_with_unknownId(self):
        unknownId = random_string()
        response = Client.get(TestGroups.url, id=unknownId)
        exceptedResponse = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % unknownId}
        assert (response.status_code, response.json()) == (400, exceptedResponse)

    @allure.feature('Функциональный тест')
    @allure.story('Создаем группу')
    @pytest.mark.idToDelete
    def test_add_group(self, clear_data):
        data = parse_request("post_group", {"$name": random_string(),
                                           "$parentGroupId": rootGroupId()})
        response = Client.post(TestGroups.url, data['request'])
        clear_data.append(response.json()['groupId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    #
    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу без имени')
    def test_addGroup_without_name(self):
        data = parse_request("post_group", {"$name": None,
                                           "$parentGroupId": rootGroupId()})
        response = Client.post(TestGroups.url, data['request'])
        exceptedResponse = {'ADM_VALIDATION_GROUP_NAME': 'NAME not specified'}
        assert (response.status_code, response.json()) == (400, exceptedResponse)

    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу без parentGroupId')
    def test_addGroup_without_group(self):
        data = parse_request("post_group", {"$name": random_string(),
                                           "$parentGroupId": None})
        response = Client.post(TestGroups.url, data['request'])
        exceptedResponse = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=null not found'}
        assert (response.status_code, response.json()) == (400, exceptedResponse)

    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу с неизвестным parendGroupId')
    def test_addGroup_with_unknown_parentGroupId(self):
        randonGroupId = random_string()
        data = parse_request("post_group", {"$name": random_string(),
                                           "$parentGroupId": randonGroupId
                                            })
        response = Client.post(TestGroups.url, data['request'])
        expectedResponse = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % randonGroupId}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональный тест')
    @allure.story('Создаем группу с сущесвующим именем')
    def test_addGroup_with_existing_name(self, immutable_group_with_child, clear_data):
        existinGroupName = immutable_group_with_child['name']
        data = parse_request("post_group", {"$name": existinGroupName,
                                           "$parentGroupId": rootGroupId()})
        response = Client.post(TestGroups.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['groupId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу')
    def test_edit_group(self, group):
        data = parse_request("put_group", {"$name": random_string(),
                                          "$groupId": group['groupId']})
        response = Client.put(TestGroups.url, data=data['request'], id=group['groupId'])
        assert response.status_code == 200 and equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу на пустое имя')
    def test_edit_group_on_empty_name(self, group):
        data = parse_request("put_group", {"$name": None,
                                          "$groupId": group['groupId']})
        response = Client.put(TestGroups.url, data=data['request'], id=group['groupId'])
        print(response.json())
        expectedResponse = {'ADM_VALIDATION_GROUP_NAME': 'NAME not specified'}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу с неизвестным groupId')
    def test_edit_group_with_unknown_groupId(self, group):
        unknownGroupId = random_string()
        data = parse_request("put_group", {"$name": random_string(),
                                          "$groupId": group['groupId']})
        response = Client.put(TestGroups.url, data=data['request'], id=unknownGroupId)
        expectedResponse = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % unknownGroupId}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональный тест')
    @allure.story('Удаляем группу')
    def test_delete_group(self, group):
        response = Client.delete(TestGroups.url, id=group['groupId'])
        assert (response.status_code, response.json()) == (200, group)

    @allure.feature('Проверка валидации')
    @allure.story('Удаляем группу с неизвестным id')
    def test_delete_group_with_unknown_id(self):
        unknownGroupId = random_string()
        response = Client.delete(TestGroups.url, id=unknownGroupId)
        expectedResponse = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % unknownGroupId}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Проверка валидации')
    @allure.story('Удаляем группу у которой есть child')
    def test_delete_group_with_child(self, immutable_group_with_child):
        groupId = immutable_group_with_child['groupId']
        response = Client.delete(TestGroups.url, id=groupId)
        expectedResponse = {
            'COMMON_NOT_ALLOWED_OPERATION': 'CommonNotAllowedOperationException: This group has got children. Kill them first... If you dare...'}
        assert (response.status_code, response.json()) == (400, expectedResponse)


class TestRoles():
    # TODO: добавить интеграционный тест, в котором в пользователя будет назначина группа, ниже RootChild
    # TODO: добавить тест, в котором пользователь будет находится в двух RootChild

    url = "roles"

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с первым child от рута')
    def test_add_role_with_first_root_child(self, immutable_group_with_child, clear_data):
        data = parse_request('post_roles', {"$name": random_string(),
                                           "$groupId": immutable_group_with_child['groupId']})
        response = Client.post(TestRoles.url, data['request'])
        clear_data.append(response.json()['roleId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль')
    def test_add_role_without_name(self, immutable_group_with_child):
        data = parse_request('post_roles', {"$name": None,
                                           "$groupId": immutable_group_with_child['groupId']})
        response = Client.post(TestRoles.url, data['request'])
        expectedResponse = {'ADM_VALIDATION_ROLE_NAME': 'NAME not specified'}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с root групой')
    def test_add_role_with_root_group(self, clear_data):
        data = parse_request('post_roles', {"$name": random_string(),
                                           "$groupId": rootGroupId()})
        response = Client.post(TestRoles.url, data['request'])
        clear_data.append(response.json()['roleId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль вторым по вложености child')
    def test_add_role_with_second_child(self, immutable_group_with_child, clear_data):
        childGroupId = immutable_group_with_child['children'][0]['groupId']
        data = parse_request('post_roles', {"$name": random_string(),
                                           "$groupId": childGroupId})
        response = Client.post(TestRoles.url, data['request'])
        print(childGroupId, response.json())
        clear_data.append(response.json()['roleId'])
        assert (response.status_code, response.json()['group']['groupId']) == (
        201, immutable_group_with_child['groupId'])

    # Не правильный текст валидации
    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль без группы')
    def test_add_role_without_group(self):
        data = parse_request('post_roles', {"$name": random_string(),
                                           "$groupId": None})
        response = Client.post(TestRoles.url, data['request'])
        expected_response = {'ADM_VALIDATION_ROLE_GROUP_EMPTY': 'GROUP not specified'}
        assert (response.status_code, response.json()) == (400, expected_response)

    # Не правильный текст валидации
    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с неизвестной групой')
    def test_add_role_with_unknown_group(self):
        unknown_group_id = random_string()
        data = parse_request('post_roles', {"$name": random_string(),
                                           "$groupId": unknown_group_id})
        response = Client.post(TestRoles.url, data['request'])
        print(response.json())
        expected_response = {
            'ADM_VALIDATION_GROUP_NOT_FOUND': 'Group by the following group id not found: %s' % unknown_group_id}
        assert (response.status_code, response.json()) == (400, expected_response)

    # Имя роли должно быть уникальным только для компании
    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с сущесвующим именем')
    def test_add_role_with_existing_name(self, immutable_group_with_child, role):
        existing_name = role['name']
        data = parse_request('post_roles', {"$name": existing_name,
                                           "$groupId": immutable_group_with_child['groupId']})
        response = Client.post(TestRoles.url, data['request'])
        expected_response = {
            'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'CommonEntityWithSuchFieldExists: Name is not unique'}
        assert (response.status_code, response.json()) == (409, expected_response)

    @allure.feature('Функциональний тест')
    @allure.story('Получаем все роли')
    def test_get_roles(self, role):
        response = Client.get(TestRoles.url)
        assert response.status_code == 200 and role in response.json()

    @allure.feature('Функциональний тест')
    @allure.story('Получаем конкретную роль по id')
    def test_get_role_by_id(self, role):
        response = Client.get(TestRoles.url, id=role['roleId'])
        assert (response.status_code, response.json()) == (200, role)

    @allure.feature('Функциональний тест')
    @allure.story('Получаем конкретную роль по не известному id')
    def test_get_role_by_unknown_id(self):
        unknownRoleId = random_string()
        response = Client.get(TestRoles.url, id=unknownRoleId)
        expectedResponse = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: ROLE by roleId=%s not found' % unknownRoleId}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональний тест')
    @allure.story('Удаляем роль')
    def test_delete_role(self, role):
        response = Client.delete(TestRoles.url, id=role['roleId'])
        assert (response.status_code, response.json()) == (200, role)

    @allure.feature('Функциональний тест')
    @allure.story('Удаляем роль с неизвестным id')
    def test_delete_role_by_unknown_id(self):
        unknownRoleId = random_string()
        response = Client.delete(TestRoles.url, id=unknownRoleId)
        expectedResponse = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: ROLE by roleId=%s not found' % unknownRoleId}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональний тест')
    @allure.story('Редактируем роль')
    def test_edit_role(self, role, immutable_group_with_child):
        data = parse_request('put_roles', {"$roleId": role['roleId'],
                                          "$name": random_string(),
                                          "$groupId": immutable_group_with_child['groupId']
                                           })
        response = Client.put(TestRoles.url, data['request'], id=role['roleId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 200

    @allure.feature('Функциональний тест')
    @allure.story('Редактируем роль на пустое имя')
    def test_edit_role_on_empty_name(self, role, immutable_group_with_child):
        data = parse_request('put_roles', {"$roleId": role['roleId'],
                                          "$name": None,
                                          "$groupId": immutable_group_with_child['groupId']
                                           })
        response = Client.put(TestRoles.url, data['request'], id=role['roleId'])
        expected_response = {'ADM_VALIDATION_ROLE_NAME': 'NAME not specified'}
        assert (response.json(), response.status_code) == (expected_response, 400)

    @allure.feature('Функциональний тест')
    @allure.story('Редактируем роль на не существующую групу')
    def test_edit_role_on_unknown_group(self, role):
        unknown_group_id = random_string()
        data = parse_request('put_roles', {"$roleId": role['roleId'],
                                          "$name": random_string(),
                                          "$groupId": unknown_group_id
                                           })
        response = Client.put(TestRoles.url, data['request'], id=role['roleId'])
        print(response.json())
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
        response = Client.put(TestRoles.url, data['request'], id=role['roleId'])
        print(response.json())
        expected_response = {
            'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'CommonEntityWithSuchFieldExists: Name is not unique'}
        assert (response.json(), response.status_code) == (expected_response, 409)


class TestUsers:
    url = "users"

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя только с обязательными полями')
    def test_add_user_with_required_fields(self, clear_data, immutable_role, immutable_group_with_child):
        userGroupRoles = make_user_group_roles({immutable_group_with_child['groupId']:immutable_role['roleId']})
        print(userGroupRoles)
        data = parse_request("post_users", {"$login": random_string(),
                                           "$fname": random_string(),
                                           "$lname": random_string(),
                                           "$roleId": immutable_role['roleId'],
                                            "$userGroupRoles": userGroupRoles})
        response = Client.post(TestUsers.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['userId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя со всеми полями')
    def test_add_user_with_all_fields(self, clear_data, immutable_role, immutable_group_with_child):
        data = parse_request("post_users", {"$login": random_string(),
                                           "$fname": random_string(),
                                           "$lname": random_string(),
                                           "$groupId": immutable_group_with_child['groupId'],
                                           "$roleId": immutable_role['roleId'],
                                           "$agentId": random_string(),
                                           "$loginAD": random_string(),
                                            "$pname": random_string(),
                                            "$email": random_string() + '@.com.ua',
                                            "$phone": str(random.randint(11111, 99999999)),
                                            "$fax": random_string()
                                            })
        response = Client.post(TestUsers.url, data['request'])
        print(data['schema'])
        print(response.json())
        clear_data.append(response.json()['userId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя с уже существующим login')
    def test_add_user_with_existing_login(self, immutable_role, immutable_group_with_child, immutable_user):
        existing_login = immutable_user['login']
        data = parse_request("post_users", {"$login": existing_login,
                                           "$fname": random_string(),
                                           "$lname": random_string(),
                                           "$groupId": immutable_group_with_child['groupId'],
                                           "$roleId": immutable_role['roleId']})
        response = Client.post(TestUsers.url, data['request'])
        expected_response = {
            'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'CommonEntityWithSuchFieldExists: LOGIN or USER ID should be unique.'}
        assert (response.status_code, response.json()) == (409, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя с существующими полями (кроме уникальных)')
    def test_add_user_with_existing_fields_which_are_not_unique(self, clear_data, immutable_role,
                                                                immutable_group_with_child, immutable_user):
        existing_field = immutable_user
        data = parse_request("post_users", {"$login": random_string(),
                                           "$fname": existing_field['fname'],
                                           "$lname": existing_field['lname'],
                                           "$groupId": immutable_group_with_child['groupId'],
                                           "$roleId": immutable_role['roleId'],
                                           "$agentId": random_string(),
                                           "$loginAD": existing_field['loginAD'],
                                            "$pname": existing_field['pname'],
                                            "$email": existing_field['email'],
                                            "$phone": str(random.randint(1111111, 999999999)),
                                            "$fax": existing_field['phone']
                                            })
        response = Client.post(TestUsers.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['userId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя с уже существующим phone')
    @pytest.mark.xfail
    def test_add_user_with_existing_phone(self, immutable_role, immutable_group_with_child, immutable_user):
        existing_phone = immutable_user['phone']
        data = parse_request("post_users", {"$login": random_string(),
                                           "$fname": random_string(),
                                           "$lname": random_string(),
                                           "$groupId": immutable_group_with_child['groupId'],
                                           "$roleId": immutable_role['roleId'],
                                           "$phone": existing_phone})
        response = Client.post(TestUsers.url, data['request'])
        print(response.json())
        expected_response = {
            'COMMON_EXCEPTION': 'CommonException: Not deleted user with phone = %s already exist!' % existing_phone}
        assert (response.status_code, response.json()) == (409, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя с уже существующим agentId')
    def test_add_user_with_existing_agentId(self, immutable_role, immutable_group_with_child, immutable_user):
        existing_agentId = immutable_user['agentId']
        data = parse_request("post_users", {"$login": random_string(),
                                           "$fname": random_string(),
                                           "$lname": random_string(),
                                           "$groupId": immutable_group_with_child['groupId'],
                                           "$roleId": immutable_role['roleId'],
                                           "$agentId": existing_agentId})
        response = Client.post(TestUsers.url, data['request'])
        print(response.json())
        expected_response = {
            'COMMON_ENTITY_WITH_SUCH_FIELD_EXISTS': 'CommonEntityWithSuchFieldExists: AGENT ID =%s already exists' % existing_agentId}
        assert (response.status_code, response.json()) == (409, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя без login, fname, lname')
    def test_add_user_without_login_fname_lname(self, immutable_role, immutable_group_with_child):
        data = parse_request("post_users", {"$login": None,
                                           "$fname": None,
                                           "$lname": None,
                                           "$groupId": immutable_group_with_child['groupId'],
                                           "$roleId": immutable_role['roleId']})
        response = Client.post(TestUsers.url, data['request'])
        expected_response = {'ADM_VALIDATION_USER_LAST_NAME_LENGTH': 'LNAME length from 1 to 256',
                             'ADM_VALIDATION_USER_FIRST_NAME_LENGTH': 'FNAME length from 1 to 256',
                             'ADM_VALIDATION_USER_LOGIN_LENGTH': 'LOGIN length from 1 to 256'}
        assert (response.status_code, response.json()) == (400, expected_response)


    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя без roleId')
    def test_add_user_without_groupId_roleId(self, immutable_group_with_child):
        data = parse_request("post_users", {"$login": random_string(),
                                           "$fname": random_string(),
                                           "$lname": random_string(),
                                           "$groupId": immutable_group_with_child['groupId'],
                                           "$roleId": None})
        response = Client.post(TestUsers.url, data['request'])
        expected_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: ROLE by roleId=null not found'}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('функциональный тест')
    @allure.story('Создаем пользователя без groupId')
    def test_add_user_without_groupId(self, immutable_role):
        data = parse_request("post_users", {"$login": random_string(),
                                           "$fname": random_string(),
                                           "$lname": random_string(),
                                           "$groupId": None,
                                           "$roleId": immutable_role['roleId']})
        response = Client.post(TestUsers.url, data['request'])
        expected_response = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=null not found'}
        assert (response.status_code, response.json()) == (400, expected_response)