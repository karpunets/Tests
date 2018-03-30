# -*- coding: utf-8 -*-

import allure
import pytest
from bin.session import Client
from bin.session import rootGroupId
from bin.session import getHeadersForUser
from bin.Make_requests_and_answers import parseRequest, equal_schema, random_string


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
        data = parseRequest("post_group", {"$name": random_string(),
                                           "$parentGroupId": rootGroupId()})
        response = Client.post(TestGroups.url, data['request'])
        idToDelete = "qq"
        clear_data.append(response.json()['groupId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201
#
    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу без имени')
    def test_addGroup_without_name(self):
        data = parseRequest("post_group", {"$name": None,
                                           "$parentGroupId": rootGroupId()})
        response = Client.post(TestGroups.url, data['request'])
        exceptedResponse = {'ADM_VALIDATION_GROUP_NAME': 'NAME not specified'}
        assert (response.status_code, response.json()) == (400, exceptedResponse)

    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу без parentGroupId')
    def test_addGroup_without_group(self):
        data = parseRequest("post_group", {"$name": random_string(),
                                           "$parentGroupId": None})
        response = Client.post(TestGroups.url, data['request'])
        exceptedResponse = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=null not found'}
        assert (response.status_code, response.json()) == (400, exceptedResponse)

    @allure.feature('Проверка валидации')
    @allure.story('Создаем группу с неизвестным parendGroupId')
    def test_addGroup_with_unknown_parentGroupId(self):
        randonGroupId = random_string()
        data = parseRequest("post_group", {"$name": random_string(),
                                           "$parentGroupId": randonGroupId
                                           })
        response = Client.post(TestGroups.url, data['request'])
        expectedResponse = {
            'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % randonGroupId}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональный тест')
    @allure.story('Создаем группу с сущесвующим именем')
    def test_addGroup_with_existing_name(self, imutableGroupWithChild, clear_data):
        existinGroupName = imutableGroupWithChild['name']
        data = parseRequest("post_group", {"$name": existinGroupName,
                                           "$parentGroupId": rootGroupId()})
        response = Client.post(TestGroups.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['groupId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу')
    def test_edit_group(self, group):
        data = parseRequest("put_group", {"$name": random_string(),
                                          "$groupId": group['groupId']})
        response = Client.put(TestGroups.url, data=data['request'], id=group['groupId'])
        assert response.status_code == 200 and equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу на пустое имя')
    def test_edit_group_on_empty_name(self, group):
        data = parseRequest("put_group", {"$name": None,
                                          "$groupId": group['groupId']})
        response = Client.put(TestGroups.url, data=data['request'], id=group['groupId'])
        print(response.json())
        expectedResponse = {'ADM_VALIDATION_GROUP_NAME': 'NAME not specified'}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем группу с неизвестным groupId')
    def test_edit_group_with_unknown_groupId(self, group):
        unknownGroupId = random_string()
        data = parseRequest("put_group", {"$name": random_string(),
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
    def test_delete_group_with_child(self, imutableGroupWithChild):
        groupId = imutableGroupWithChild['groupId']
        response = Client.delete(TestGroups.url, id=groupId)
        expectedResponse = {'COMMON_NOT_ALLOWED_OPERATION': 'CommonNotAllowedOperationException: This group has got children. Kill them first... If you dare...'}
        assert (response.status_code, response.json()) == (400, expectedResponse)


class TestRoles():
    # TODO: добавить интеграционный тест, в котором в пользователя будет назначина группа, ниже RootChild
    # TODO: добавить тест, в котором пользователь будет находится в двух RootChild

    url = "roles"

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с первым child от рута')
    def test_add_role_with_first_root_child(self, imutableGroupWithChild, clear_data):
        data = parseRequest('post_roles', {"$name":random_string(),
                                            "$groupId":imutableGroupWithChild['groupId']})
        response = Client.post(TestRoles.url, data['request'])
        clear_data.append(response.json()['roleId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль')
    def test_add_role_without_name(self, imutableGroupWithChild):
        data = parseRequest('post_roles', {"$name": None,
                                           "$groupId": imutableGroupWithChild['groupId']})
        response = Client.post(TestRoles.url, data['request'])
        expectedResponse = {'ADM_VALIDATION_ROLE_NAME': 'NAME not specified'}
        assert (response.status_code, response.json()) == (400, expectedResponse)

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с root групой')
    def test_add_role_with_root_group(self, clear_data):
        data = parseRequest('post_roles', {"$name":random_string(),
                                            "$groupId":rootGroupId()})
        response = Client.post(TestRoles.url, data['request'])
        clear_data.append(response.json()['roleId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201


    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль вторым по вложености child')
    def test_add_role_with_second_child(self, imutableGroupWithChild, clear_data):
        childGroupId = imutableGroupWithChild['children'][0]['groupId']
        data = parseRequest('post_roles', {"$name": random_string(),
                                           "$groupId": childGroupId})
        response = Client.post(TestRoles.url, data['request'])
        print(childGroupId, response.json())
        clear_data.append(response.json()['roleId'])
        assert (response.status_code, response.json()['group']['groupId']) == (201, imutableGroupWithChild['groupId'])

    # Не правильный текст валидации
    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль без группы')
    @pytest.mark.xfail
    def test_add_role_without_group(self):
        data = parseRequest('post_roles', {"$name":random_string(),
                                            "$groupId":None})
        response = Client.post(TestRoles.url, data['request'])
        print(response.json())
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

    # Имя роли должно быть уникальным только для компании
    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль с сущесвующим именем')
    @pytest.mark.xfail
    def test_add_role_with_existing_name(self, imutableGroupWithChild, clear_data, role):
        existingName = role['name']
        data = parseRequest('post_roles', {"$name":existingName,
                                            "$groupId":imutableGroupWithChild['groupId']})
        response = Client.post(TestRoles.url, data['request'])
        print(response.json())
        clear_data.append(response.json()['roleId'])
        assert equal_schema(response.json(), data['schema']) and response.status_code == 201

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
        expectedResponse = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: ROLE by roleId=%s not found'%unknownRoleId}
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
        expectedResponse = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: ROLE by roleId=%s not found'%unknownRoleId}
        assert (response.status_code, response.json()) == (400, expectedResponse)
