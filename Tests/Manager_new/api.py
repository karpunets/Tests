import allure
import pytest
from bin.session import Client
from bin.session import rootGroupId

from bin.Make_requests_and_answers import parseRequest, equal_schema, random_string


# @allure.feature('Функциональный тест')
# @allure.story('Получаем все группы')
# def test_get_groups():
#     response = Client.get("groups")
#     assert response.status_code == 200 and "ROOT" in response.json()[0]['name']
#
# @allure.feature('Функциональный тест')
# @allure.story('Получаем групу по ID')
# def test_get_group_by_id(group):
#     response = Client.get("groups", id=group['groupId'])
#     assert (response.status_code, response.json()) == (200, group)
#
#
# @allure.feature('Функциональный тест')
# @allure.story('Проверяем есть ли ранеее созданная группа в списке полученных груп')
# def test_get_group_bew_group_in_group_list(group):
#     response = Client.get("groups")
#     rootChilderIds = [group['groupId'] for group in response.json()[0]['children']]
#     assert response.status_code == 200 and group['groupId'] in rootChilderIds
#
#
# @allure.feature('Проверка валидации')
# @allure.story('Получаем группу с неизвестным id')
# def test_get_group_with_unknownId():
#     unknownId = random_string()
#     response = Client.get("groups", id=unknownId)
#     exceptedResponse = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found'%unknownId}
#     assert (response.status_code, response.json()) == (400, exceptedResponse)
#
# @allure.feature('Функциональный тест')
# @allure.story('Создаем группу')
# def test_addGroup(deleteGroup):
#     data = parseRequest("post_group",{"$name":random_string(),
#                                       "$parentGroupId":rootGroupId()})
#     response = Client.post("groups", data['request'])
#     deleteGroup.append(response.json()['groupId'])
#     assert equal_schema(response.json(), data['schema']) and response.status_code == 201
#
# @allure.feature('Проверка валидации')
# @allure.story('Создаем группу без имени')
# def test_addGroup_without_name():
#     data = parseRequest("post_group",{"$name":None,
#                                       "$parentGroupId":rootGroupId()})
#     response = Client.post("groups", data['request'])
#     exceptedResponse = {'ADM_VALIDATION_GROUP_NAME': 'NAME not specified'}
#     assert (response.status_code, response.json()) == (400, exceptedResponse)
#
# @allure.feature('Проверка валидации')
# @allure.story('Создаем группу без parentGroupId')
# def test_addGroup_without_name():
#     data = parseRequest("post_group",{"$name":random_string(),
#                                       "$parentGroupId":None})
#     response = Client.post("groups", data['request'])
#     exceptedResponse = {'ADM_VALIDATION_GROUP_PARENT_EMPTY': 'PARENT GROUP ID not specified'}
#     assert (response.status_code, response.json()) == (400, exceptedResponse)


# @allure.feature('Проверка валидации')
# @allure.story('Создаем группу с неизвестным parendGroupId')
# def test_addGroup_with_unknown_parentGroupId():
#     randonGroupId = random_string()
#     data = parseRequest("post_group", {"$name":random_string(),
#                                       "$parentGroupId":randonGroupId
#                                       })
#     response = Client.post("groups", data['request'])
#     expectedResponse = {'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found'%randonGroupId}
#     assert (response.status_code, response.json()) == (400, expectedResponse)

# @allure.feature('Функциональный тест')
# @allure.story('Создаем группу')
# def test_addGroup(imutableGroup, deleteGroup):
#     existinGroupName = imutableGroup['name']
#     data = parseRequest("post_group",{"$name":existinGroupName,
#                                       "$parentGroupId":rootGroupId()})
#     response = Client.post("groups", data['request'])
#     print(response.json())
#     deleteGroup.append(response.json()['groupId'])
#     assert equal_schema(response.json(), data['schema']) and response.status_code == 201

# @allure.feature('Функциональный тест')
# @allure.story('Редактируем группу')
# @pytest.mark.xfail
# def test_edit_group(group, imutableGroup):
#     newParentGroupId = imutableGroup['groupId']
#     data = parseRequest("put_group",{ "$name":random_string()})
#     print(data)
#     response = Client.put("groups", data = data['request'], id = group['groupId'])
#     print(response.json())
#     assert equal_schema(response.json(), data['schema']) and response.status_code == 200


# @allure.feature('Функциональный тест')
# @allure.story('Удаляем группу')
# def test_delete_group(group):
#     response = Client.delete("groups", id=group['groupId'])
#     assert (response.status_code, response.json()) == (200, group)


# @allure.feature('Проверка валидации')
# @allure.story('Удаляем группу с неизвестным id')
# def test_delete_group_with_unknown_id():
#     unknownGroupId = random_string()
#     response = Client.delete("groups", id=unknownGroupId)
#     expectedResponse  ={'COMMON_REQUESTED_RESOURCES_NOT_FOUND': 'CommonRequestedResourcesNotFound: GROUP by groupId=%s not found'%unknownGroupId}
#     assert (response.status_code, response.json()) == (400, expectedResponse)

# @allure.feature('Проверка валидации')
# @allure.story('Удаляем группу у которой есть child')
# def test_delete_group_with_child(imutableGroupWithChild):
#     groupId = imutableGroupWithChild['groupId']
#     response = Client.delete("groups", id=groupId)
#     print(response.json())
#     assert (response.status_code, response.json()) == (400, "cant delete users with child")

