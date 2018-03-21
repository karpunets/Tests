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
# @pytest.mark.xfail
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

@allure.feature('Функциональный тест')
@allure.story('Создаем группу')
def test_addGroup(deleteGroup):
    data = parseRequest("post_group",{"$name":random_string(),
                                      "parentGroupId":rootGroupId()})
    response = Client.post("groups", data)
