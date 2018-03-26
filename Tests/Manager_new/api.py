import allure
import pytest
from bin.session import Client
from bin.session import rootGroupId

from bin.Make_requests_and_answers import parseRequest, equal_schema, random_string


# class TestGroups():
#     url = "groups"
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Получаем все группы')
#     def test_get_groups(self):
#         response = Client.get(TestGroups.url)
#         assert response.status_code == 200 and "ROOT" in response.json()[0]['name']
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Получаем групу по ID')
#     def test_get_group_by_id(self, group):
#         response = Client.get(TestGroups.url, id=group['groupId'])
#         assert (response.status_code, response.json()) == (200, group)
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Проверяем есть ли ранеее созданная группа в списке полученных груп')
#     def test_get_group_bew_group_in_group_list(self, group):
#         response = Client.get(TestGroups.url)
#         rootChilderIds = [group['groupId'] for group in response.json()[0]['children']]
#         assert response.status_code == 200 and group['groupId'] in rootChilderIds
#
#     @allure.feature('Проверка валидации')
#     @allure.story('Получаем группу с неизвестным id')
#     def test_get_group_with_unknownId(self):
#         unknownId = random_string()
#         response = Client.get(TestGroups.url, id=unknownId)
#         exceptedResponse = {
#             'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % unknownId}
#         assert (response.status_code, response.json()) == (400, exceptedResponse)
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Создаем группу')
#     def test_addGroup(self, deleteGroup):
#         data = parseRequest("post_group", {"$name": random_string(),
#                                            "$parentGroupId": rootGroupId()})
#         response = Client.post(TestGroups.url, data['request'])
#         deleteGroup.append(response.json()['groupId'])
#         assert equal_schema(response.json(), data['schema']) and response.status_code == 201
#
#     @allure.feature('Проверка валидации')
#     @allure.story('Создаем группу без имени')
#     def test_addGroup_without_name(self):
#         data = parseRequest("post_group", {"$name": None,
#                                            "$parentGroupId": rootGroupId()})
#         response = Client.post(TestGroups.url, data['request'])
#         exceptedResponse = {'ADM_VALIDATION_GROUP_NAME': 'NAME not specified'}
#         assert (response.status_code, response.json()) == (400, exceptedResponse)
#
#     @allure.feature('Проверка валидации')
#     @allure.story('Создаем группу без parentGroupId')
#     def test_addGroup_without_group(self):
#         data = parseRequest("post_group", {"$name": random_string(),
#                                            "$parentGroupId": None})
#         response = Client.post(TestGroups.url, data['request'])
#         exceptedResponse = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=null not found'}
#         assert (response.status_code, response.json()) == (400, exceptedResponse)
#
#     @allure.feature('Проверка валидации')
#     @allure.story('Создаем группу с неизвестным parendGroupId')
#     def test_addGroup_with_unknown_parentGroupId(self):
#         randonGroupId = random_string()
#         data = parseRequest("post_group", {"$name": random_string(),
#                                            "$parentGroupId": randonGroupId
#                                            })
#         response = Client.post(TestGroups.url, data['request'])
#         expectedResponse = {
#             'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % randonGroupId}
#         assert (response.status_code, response.json()) == (400, expectedResponse)
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Создаем группу с сущесвующим именем')
#     def test_addGroup_with_existing_name(self, imutableGroupWithChild, deleteGroup):
#         existinGroupName = imutableGroupWithChild['name']
#         data = parseRequest("post_group", {"$name": existinGroupName,
#                                            "$parentGroupId": rootGroupId()})
#         response = Client.post(TestGroups.url, data['request'])
#         print(response.json())
#         deleteGroup.append(response.json()['groupId'])
#         assert equal_schema(response.json(), data['schema']) and response.status_code == 201
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Редактируем группу')
#     def test_edit_group(self, group):
#         data = parseRequest("put_group", {"$name": random_string(),
#                                           "$groupId": group['groupId']})
#         response = Client.put(TestGroups.url, data=data['request'], id=group['groupId'])
#         assert response.status_code == 200 and equal_schema(response.json(), data['schema'])
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Редактируем группу на пустое имя')
#     def test_edit_group_on_empty_name(self, group):
#         data = parseRequest("put_group", {"$name": None,
#                                           "$groupId": group['groupId']})
#         response = Client.put(TestGroups.url, data=data['request'], id=group['groupId'])
#         print(response.json())
#         expectedResponse = {'ADM_VALIDATION_GROUP_NAME': 'NAME not specified'}
#         assert (response.status_code, response.json()) == (400, expectedResponse)
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Редактируем группу с неизвестным groupId')
#     def test_edit_group_with_unknown_groupId(self, group):
#         unknownGroupId = random_string()
#         data = parseRequest("put_group", {"$name": random_string(),
#                                           "$groupId": group['groupId']})
#         response = Client.put(TestGroups.url, data=data['request'], id=unknownGroupId)
#         expectedResponse = {
#             'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % unknownGroupId}
#         assert (response.status_code, response.json()) == (400, expectedResponse)
#
#     @allure.feature('Функциональный тест')
#     @allure.story('Удаляем группу')
#     def test_delete_group(self, group):
#         response = Client.delete(TestGroups.url, id=group['groupId'])
#         assert (response.status_code, response.json()) == (200, group)
#
#     @allure.feature('Проверка валидации')
#     @allure.story('Удаляем группу с неизвестным id')
#     def test_delete_group_with_unknown_id(self):
#         unknownGroupId = random_string()
#         response = Client.delete(TestGroups.url, id=unknownGroupId)
#         expectedResponse = {
#             'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found' % unknownGroupId}
#         assert (response.status_code, response.json()) == (400, expectedResponse)
#
#     @allure.feature('Проверка валидации')
#     @allure.story('Удаляем группу у которой есть child')
#     def test_delete_group_with_child(self, imutableGroupWithChild):
#         groupId = imutableGroupWithChild['groupId']
#         response = Client.delete(TestGroups.url, id=groupId)
#         expectedResponse = {'COMMON_NOT_ALLOWED_OPERATION': 'CommonNotAllowedOperationException: This group has got children. Kill them first... If you dare...'}
#         assert (response.status_code, response.json()) == (400, expectedResponse)



class TestRoles():
    url  = "roles"

    # @allure.feature('Функциональний тест')
    # @allure.story('Создаем роль')
    # def test_add_role(self, imutableGroupWithChild, deleteRole):
    #     data = parseRequest('post_roles', {"$name":random_string(),
    #                                         "$groupId":imutableGroupWithChild['groupId']})
    #     response = Client.post(TestRoles.url, data['request'])
    #     deleteRole.append(response.json()['roleId'])
    #     print(data, response.json())
    #     assert equal_schema(response.json(), data['schema']) and response.status_code == 200

    @allure.feature('Функциональний тест')
    @allure.story('Создаем роль')
    def test_add_role_without_name(self, imutableGroupWithChild, deleteRole):
        data = parseRequest('post_roles', {"$name": None,
                                           "$groupId": imutableGroupWithChild['groupId']})
        response = Client.get("current_user", data['request'])
        print(response.json())
        # expectedResponse = {'ADM_VALIDATION_ROLE_NAME': 'NAME not specified'}
        # print(data, response.json())
        # assert equal_schema(response.json(), data['schema']) and response.status_code == 200