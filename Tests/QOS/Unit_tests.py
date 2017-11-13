import pytest, allure, json, requests, random
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import make_test_data, equal_schema, random_string
from Data.Test_data import ROOT_group_id



# @allure.feature('Позитивный тест')
# @allure.story('Добавляем новую групу')
# def test_add_group(send_request, delete_group_and_criteria):
#     data = make_test_data('post_criteria_group', {'$name':random_string()})
#     response = send_request(URL.criteria_group, data['request'])
#     instance = response.json()
#     delete_group_and_criteria['criteriaGroupId'].append(instance['id'])
#     assert response.status_code == 200
#     assert equal_schema(instance, data['schema'])
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем новую групу с существующим именем')
# def test_add_group_with_existing_name(send_request, add_group):
#     existing_group_name = next(add_group)['name']
#     data = make_test_data('post_criteria_group', {'$name': existing_group_name})
#     response = send_request(URL.criteria_group, data['request'])
#     answer = {"QOS_ENTITY_WITH_SUCH_FIELD_EXISTS":"QoSEntityWithSuchFieldExists: NAME"}
#     assert response.status_code == 500
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем новую групу без имени')
# def test_add_group_without_name(send_request):
#     data = make_test_data('post_criteria_group', {'$name': None})
#     response = send_request(URL.criteria_group, data['request'])
#     answer = {'QOS_TEMPLATE_CRITERIA_GROUP_NAME': 'NAME length from 1 to 255 characters.'}
#     assert response.status_code == 400
#     assert response.json() == answer
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий')
# def test_add_criteria(send_request, add_group, delete_group_and_criteria):
#     group_id = next(add_group)['id']
#     data = make_test_data('post_criteria', {'$name': random_string(),
#                                        '$criteriagroupId': group_id,
#                                        '$description':random_string()})
#     response = send_request(URL.criteria, data['request'])
#     instance = response.json()
#     #Шаг для удаления критерия
#     delete_group_and_criteria['criteriaId'].append(instance['id'])
#     assert response.status_code == 200
#     assert equal_schema(instance, data['schema'])

# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий с уже существующим именем')
# def test_add_criteria_with_existing_name(send_request, add_group, add_criteria, delete_group_and_criteria):
#     existing_criteria = next(add_criteria)
#     data = make_test_data('post_criteria', {'$name': existing_criteria['name'],
#                                        '$criteriagroupId': existing_criteria['criteriaGroup']['id'],
#                                        '$description':random_string()})
#     response = send_request(URL.criteria, data['request'])
#     instance = response.json()
#     #Шаг для удаления критерия
#     delete_group_and_criteria['criteriaId'].append(instance['id'])
#     assert response.status_code == 200
#     assert equal_schema(instance, data['schema'])


# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий без имени и описания')
# def test_add_criteria_without_description_and_name(send_request, add_group):
#     group_id = next(add_group)['id']
#     data = make_test_data('post_criteria', {'$criteriagroupId': group_id})
#     response = send_request(URL.criteria, data['request'])
#     #Шаг для удаления критерия
#     answer = {'QOS_TEMPLATE_CRITERIA_DESCRIPTION': 'DESCRIPTION length from 1 to 1024 characters. Сriteria id=[null]',
#               'QOS_TEMPLATE_CRITERIA_NAME': 'NAME length from 1 to 255 characters. Сriteria id=[null]'}
#     assert response.status_code == 400
#     assert answer == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий без ID групы критериев (criteriaGroupID)')
# @pytest.mark.xfail
# def test_add_criteria_without_criteria_group(send_request):
#     data = make_test_data('post_criteria', {'$name': random_string(),
#                                        '$description': random_string(),
#                                             "$criteriagroupId":None})
#     response = send_request(URL.criteria, data['request'])
#     print(response.json())
#     answer = {'QOS_TEMPLATE_CRITERIA_CRITERIAGROUP': 'Criteriagroup is empty'}
#     assert response.status_code == 400
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий с не верным ID групы критериев (criteriaGroupID)')
# def test_add_criteria_with_incorrect_criteria_group(send_request):
#     random_id = random.randint(0, 9999999999)
#     data = make_test_data('post_criteria', {'$name': random_string(),
#                                        '$description': random_string(),
#                                        '$criteriagroupId': random_id})
#     response = send_request(URL.criteria, data['request'])
#     answer = {
#         'DATA_ACCESS_ENTITY_NOT_FOUND_EXCEPTION': 'javax.persistence.EntityNotFoundException: Unable to find ua.com.smiddle.SmiddleQualityService.core.model.TemplateCriteriaGroup with id %s' %
#                                                   random_id}
#     assert response.status_code == 500
#     assert response.json() == answer
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем имя группы')
# def test_edit_criteria_group(add_group, send_request):
#     group_id = next(add_group)['id']
#     data = make_test_data('put_criteria_group', {'$name': random_string(),
#                                            '$criteriaGroupId':group_id,
#                                            '$groupId':ROOT_group_id})
#     response = send_request(URL.criteria_group, data['request'], method = "PUT")
#     instance = response.json()
#     assert response.status_code == 200
#     assert equal_schema(instance, data['schema'])
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем имя группы на пустое')
# def test_edit_criteria_group_name_on_empty(add_group, send_request):
#     group_id = next(add_group)['id']
#     data = make_test_data('put_criteria_group', {'$name': None,
#                                            '$criteriaGroupId':group_id,
#                                            '$groupId':ROOT_group_id})
#     response = send_request(URL.criteria_group, data['request'], method = "PUT")
#     answer = {'QOS_TEMPLATE_CRITERIA_GROUP_NAME': 'NAME length from 1 to 255 characters.'}
#     assert response.status_code == 400
#     assert answer == response.json()
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем имя группы на уже существующее')
# @pytest.mark.xfail
# def test_edit_criteria_group_name_on_existing(add_group, send_request):
#     existing_name = next(add_group)['name']
#     group_id = next(add_group)['id']
#     data = make_test_data('put_criteria_group', {'$name': existing_name,
#                                            '$criteriaGroupId':group_id,
#                                            '$groupId':ROOT_group_id})
#     response = send_request(URL.criteria_group, data['request'], method = "PUT")
#     answer = {'QOS_TEMPLATE_CRITERIA_GROUP_NAME': 'NAME of criteria is already exist.'}
#     assert response.status_code == 500
#     assert response.json() == answer
#


# @allure.feature('Позитивный тест')
# @allure.story('Редактируем имя и описание критерия')
# def test_edit_criteria_name_and_description(send_request, add_criteria):
#     criteria_for_edit = next(add_criteria)
#     data = make_test_data('put_criteria', {'$criteriaId': criteria_for_edit['id'],
#                                         '$name': random_string(),
#                                        '$criteriaGroupId': criteria_for_edit['criteriaGroup']['id'],
#                                        '$description':random_string()})
#     response = send_request(URL.criteria, data['request'], method = "PUT")
#     instance = response.json()
#     assert response.status_code == 200
#     assert equal_schema(instance, data['schema'])
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем критерий на уже существующее имя')
# def test_edit_criteria_on_existing_name(send_request, add_criteria):
#     existing_criteria = next(add_criteria)
#     criteria_for_edit = next(add_criteria)
#     data = make_test_data('put_criteria', {'$criteriaId': criteria_for_edit['id'],
#                                         '$name': existing_criteria['name'],
#                                        '$criteriaGroupId': criteria_for_edit['criteriaGroup']['id'],
#                                        '$description':existing_criteria['description']})
#     response = send_request(URL.criteria, data['request'], method = "PUT")
#     instance = response.json()
#     assert response.status_code == 200
#     assert equal_schema(instance, data['schema'])



# @allure.feature('Позитивный тест')
# @allure.story('Редактируем критерий с не известным id')
# def test_edit_criteria_with_unknown_id(send_request, add_criteria):
#     unknown_criteria_id = random.randint(1,99999999)
#     criteria_for_edit = next(add_criteria)
#     data = make_test_data('put_criteria', {'$criteriaId': unknown_criteria_id,
#                                            '$name': random_string(),
#                                            '$criteriaGroupId': criteria_for_edit['criteriaGroup']['id'],
#                                            '$description':random_string()})
#
#     response = send_request(URL.criteria, data['request'], method = "PUT")
#     answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': 'QOSRequestValidationException: Criteria with id does not exist'}
#     assert response.status_code == 500
#     assert response.json() == answer

# @allure.feature('Позитивный тест')
# @allure.story('Редактируем имя критерия и описание на пустые')
# def test_edit_criteria_name_and_description_on_empty(send_request, add_criteria):
#     criteria_for_edit = next(add_criteria)
#     criteria_id = criteria_for_edit['id']
#     data = make_test_data('put_criteria', {'$criteriaId': criteria_id,
#                                            '$name': None,
#                                            '$criteriaGroupId': criteria_for_edit['criteriaGroup']['id'],
#                                            '$description': None})
#     response = send_request(URL.criteria, data['request'], method="PUT")
#     answer = {'QOS_TEMPLATE_CRITERIA_DESCRIPTION': 'DESCRIPTION length from 1 to 1024 characters. Сriteria id=[%s]'%str(criteria_id),
#               'QOS_TEMPLATE_CRITERIA_NAME': 'NAME length from 1 to 255 characters. Сriteria id=[%s]'%str(criteria_id)}
#     assert response.status_code == 400
#     assert response.json() == answer


# @allure.feature('Позитивный тест')
# @allure.story('Редактируем criteriaGroupId критерия на другую(уже существующую)')
# @pytest.mark.xfail
# def test_edit_criteria_on_existing_criteriaGroup(send_request, add_group, add_criteria):
#     criteria_group_id_without_criteria = next(add_group)['id']
#     criteria_for_edit = next(add_criteria)
#     data = make_test_data('put_criteria', {'$criteriaId': criteria_for_edit['id'],
#                                            '$name': random_string(),
#                                            '$criteriaGroupId': criteria_group_id_without_criteria,
#                                            '$description': random_string()})
#     response = send_request(URL.criteria, data['request'], method="PUT")
#     answer = {'QOS_TEMPLATE_CRITERIA_CRITERIAGROUPID': 'No such criteria id{criteria_id} in criteriaGroup {id}'}
#     assert response.status_code == 500
#     assert response.json() == answer


# @allure.feature('Позитивный тест')
# @allure.story('Редактируем criteriaGroupId критерия на не существующую или пустую')
# @pytest.mark.xfail
# def test_edit_criteria_on_unknown_or_empty_criteriaGroup(send_request, add_criteria):
#     criteria_for_edit = next(add_criteria)
#     data = make_test_data('put_criteria', {'$criteriaId': criteria_for_edit['id'],
#                                            '$name': random_string(),
#                                            '$criteriaGroupId': None,
#                                            '$description': random_string()})
#     response = send_request(URL.criteria, data['request'], method="PUT")
#     print(response.json())
#     answer = {'QOS_TEMPLATE_CRITERIA_CRITERIAGROUPID': 'No such criteriaGroup {id}'}
#     assert response.status_code == 500
#     assert response.json() == answer


@allure.feature('Позитивный тест')
@allure.story('Получаем групы')
@pytest.mark.xfail
def test_get_criteria_group_withou_criterias(send_request, add_group):
    group = next(add_group)
    response = send_request(URL.criteria_group, method="GET")
    assert response.status_code == 200
    assert group in response.json()