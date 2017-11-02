import pytest, allure, json, requests, random
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import make_test_data, equal_schema, random_string
from Data.Test_data import ROOT_group_id

# @allure.feature('Позитивный тест')
# @allure.story('Добавляем новую групу')
# def test_add_group(send_request, delete_group_and_criteria):
#     data = make_test_data('add_group', {'$name':random_string()})
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
#     existing_group_name = add_group['name']
#     data = make_test_data('add_group', {'$name': existing_group_name})
#     response = send_request(URL.criteria_group, data['request'])
#     answer = {"QOS_ENTITY_WITH_SUCH_FIELD_EXISTS":"QoSEntityWithSuchFieldExists: NAME"}
#     assert response.status_code == 500
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем новую групу без имени')
# def test_add_group_without_name(send_request):
#     data = make_test_data('add_group', {'$name': None})
#     response = send_request(URL.criteria_group, data['request'])
#     answer = {'QOS_TEMPLATE_CRITERIA_GROUP_NAME': 'NAME length from 1 to 255 characters.'}
#     assert response.status_code == 400
#     assert response.json() == answer


#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий')
# def test_add_criteria(send_request, add_group, delete_group_and_criteria):
#     group_id = add_group['id']
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
#     group_id = add_group['id']
#     existing_criteria_name = add_criteria['name']
#     data = make_test_data('post_criteria', {'$name': existing_criteria_name,
#                                        '$criteriagroupId': group_id,
#                                        '$description':random_string()})
#     response = send_request(URL.criteria, data['request'])
#     instance = response.json()
#     print(instance)
#     #Шаг для удаления критерия
#     delete_group_and_criteria['criteriaId'].append(instance['id'])
#     assert response.status_code == 200
#     assert equal_schema(instance, data['schema'])
#
#
# #
# #
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий без имени и описания')
# def test_add_criteria_without_description_and_name(send_request, add_group):
#     group_id = add_group['id']
#     data = make_test_data('post_criteria', {'$criteriagroupId': group_id})
#     response = send_request(URL.criteria, data['request'])
#     #Шаг для удаления критерия
#     answer = {'QOS_TEMPLATE_CRITERIA_DESCRIPTION': 'DESCRIPTION length from 1 to 1024 characters. Сriteria id=[null]',
#               'QOS_TEMPLATE_CRITERIA_NAME': 'NAME length from 1 to 255 characters. Сriteria id=[null]'}
#     assert response.status_code == 400
#     assert answer == response.json()


# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий без ID групы критериев (criteriaGroupID)')
# @pytest.mark.xfail
# def test_add_criteria_without_criteria_group(send_request):
#     data = make_test_data('post_criteria', {'$name': random_string(),
#                                        '$description': random_string()})
#     response = send_request(URL.criteria, data['request'])
#     answer = {'QOS_TEMPLATE_CRITERIA_CRITERIAGROUP': 'Criteriagroup is empty'}
#     assert response.status_code == 400
#     assert response.json() == answer


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



# @allure.feature('Позитивный тест')
# @allure.story('Редактируем имя группы')
# def test_edit_criteria(add_group, send_request):
#     group_id = add_group['id']
#     data = make_test_data('put_criteria', {'$name': random_string(),
#                                            '$criteriaGroupId':group_id},
#                                           '$groupId':ROOT_group_id)
#     response = send_request(URL.criteria_group, data['request'], method = "PUT")
#     instance = response.json()
#     assert response.status_code == 200
#     assert equal_schema(instance, data['schema'])

# @allure.feature('Позитивный тест')
# @allure.story('Редактируем имя группы на пустое')
# def test_edit_criteria_name_on_empty(add_group, send_request):
#     group_id = add_group['id']
#     data = make_test_data('put_criteria', {'$name': None,
#                                            '$criteriaGroupId':group_id,
#                                            '$groupId':ROOT_group_id})
#     response = send_request(URL.criteria_group, data['request'], method = "PUT")
#     answer = {'QOS_TEMPLATE_CRITERIA_GROUP_NAME': 'NAME length from 1 to 255 characters.'}
#     assert response.status_code == 400
#     assert answer == response.json()



# @allure.feature('Позитивный тест')
# @allure.story('Редактируем имя группы на уже существующее')
# @pytest.mark.xfail
# def test_edit_criteria_name_on_existing(add_group, send_request, add_criteria):
#     existing_name = add_criteria['name']
#     group_id = add_group['id']
#     data = make_test_data('put_criteria', {'$name': existing_name,
#                                            '$criteriaGroupId':group_id,
#                                            '$groupId':ROOT_group_id})
#     response = send_request(URL.criteria_group, data['request'], method = "PUT")
#     print(response.status_code, response.json())
#     answer = {'QOS_TEMPLATE_CRITERIA_GROUP_NAME': 'NAME length from 1 to 255 characters.'}
#     assert response.status_code == 400
#     assert answer == response.json()