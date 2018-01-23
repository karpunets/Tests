import pytest, allure, json, requests, random
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import make_test_data, equal_schema, random_string
from Data.Test_data import ROOT_group_id, ROOT_user_id



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
@allure.feature('Позитивный тест')
@allure.story('Добавляем критерий')
def test_add_criteria(send_request, add_group, delete_group_and_criteria):
    group_id = next(add_group)['id']
    data = make_test_data('post_criteria', {'$name': random_string(),
                                       '$criteriagroupId': group_id,
                                       '$description':random_string()})
    response = send_request(URL.criteria, data['request'])
    instance = response.json()
    #Шаг для удаления критерия
    delete_group_and_criteria['criteriaId'].append(instance['id'])
    assert response.status_code == 200
    assert equal_schema(instance, data['schema'])
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий с уже существующим именем')
# def test_add_criteria_with_existing_name(send_request, add_criteria, delete_group_and_criteria):
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
#
#
@allure.feature('Позитивный тест')
@allure.story('Добавляем критерий без имени и описания')
def test_add_criteria_without_description_and_name(send_request, add_group):
    group_id = next(add_group)['id']
    data = make_test_data('post_criteria', {'$criteriagroupId': group_id})
    response = send_request(URL.criteria, data['request'])

    answer = {'QOS_TEMPLATE_CRITERIA_DESCRIPTION': 'DESCRIPTION length from 1 to 1024 characters. Criteria id=[null]',
              'QOS_TEMPLATE_CRITERIA_NAME': 'NAME length from 1 to 255 characters. Criteria id=[null]'}
    assert response.status_code == 400
    assert answer == response.json()

#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем критерий без ID групы критериев (criteriaGroupID)')
#
# def test_add_criteria_without_criteria_group(send_request):
#     data = make_test_data('post_criteria', {'$name': random_string(),
#                                        '$description': random_string(),
#                                             "$criteriagroupId":None})
#     response = send_request(URL.criteria, data['request'])
#     print(response.json())
#     answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': "QOSRequestValidationException: CriteriaGroup can't be empty"}
#     assert response.status_code == 500
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
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем criteriagroup с неизвестным id')
#
# def test_edit_criteria_group_with_unknown_id(send_request):
#     randomId = random.randint(1,9999)
#     data = make_test_data('put_criteria_group', {'$name': random_string(),
#                                            '$criteriaGroupId':randomId,
#                                            '$groupId':ROOT_group_id})
#     response = send_request(URL.criteria_group, data['request'], method = "PUT")
#     expect_answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': 'QOSRequestValidationException: CriteriaGroup with id does not exist'}
#     assert response.status_code == 500
#     assert response.json() == expect_answer
#
#
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
# def test_edit_criteria_group_name_on_existing(add_group, send_request):
#     existing_name = next(add_group)['name']
#     group_id = next(add_group)['id']
#     data = make_test_data('put_criteria_group', {'$name': existing_name,
#                                            '$criteriaGroupId':group_id,
#                                            '$groupId':ROOT_group_id})
#     response = send_request(URL.criteria_group, data['request'], method = "PUT")
#     print(response.json())
#     answer = {'QOS_ENTITY_WITH_SUCH_FIELD_EXISTS': 'QoSEntityWithSuchFieldExists: NAME'}
#     assert response.status_code == 500
#     assert response.json() == answer
#
#
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
# @allure.story('Редактируем критерий на уже существующее имя и description')
# def test_edit_criteria_on_existing_name_and_description(send_request, add_criteria):
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
#
#
#
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
#
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
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем criteriaGroupId критерия на другую(уже существующую)')
# def test_edit_criteria_on_existing_criteriaGroup(send_request, add_group, add_criteria):
#     criteria_group_id_without_criteria = next(add_group)['id']
#     criteria_for_edit = next(add_criteria)
#     data = make_test_data('put_criteria', {'$criteriaId': criteria_for_edit['id'],
#                                            '$name': random_string(),
#                                            '$criteriaGroupId': criteria_group_id_without_criteria,
#                                            '$description': random_string()})
#     response = send_request(URL.criteria, data['request'], method="PUT")
#     print(response.json())
#     answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': "QOSRequestValidationException: Criteria group can't be changed"}
#     assert response.status_code == 500
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем criteriaGroupId критерия на не существующую или пустую')
# def test_edit_criteria_on_unknown_or_empty_criteriaGroup(send_request, add_criteria):
#     criteria_for_edit = next(add_criteria)
#     data = make_test_data('put_criteria', {'$criteriaId': criteria_for_edit['id'],
#                                            '$name': random_string(),
#                                            '$criteriaGroupId': None,
#                                            '$description': random_string()})
#     response = send_request(URL.criteria, data['request'], method="PUT")
#     print(response.json())
#     answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': "QOSRequestValidationException: Criteria group can't be changed"}
#     assert response.status_code == 500
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем групы без параметров')
# def test_get_criteria_group_without_params(send_request, add_group):
#     group = next(add_group)
#     print("group", group)
#     response = send_request(URL.criteria_group, method="GET")
#     print("response", response.json())
#     assert response.status_code == 200
#     assert group in response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем групы по id')
# def test_get_criteria_group_by_id(send_request, add_group):
#     criteria_group = next(add_group)
#     response = send_request(url=URL.criteria_group, params={'id':criteria_group['id']}, method="GET")
#     print("response", response.json())
#     assert response.status_code == 200
#     assert response.json() == criteria_group
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем групы по не известному id')
# def test_get_criteria_group_by_unknown_id(send_request):
#     randomId = random.randint(2,99999)
#     response = send_request(url=URL.criteria_group, params={'id':randomId}, method="GET")
#     print("response", response.json())
#     expect_answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': 'QOSRequestValidationException: CriteriaGroup with id does not exist'}
#     assert response.status_code == 500
#     assert response.json() == expect_answer
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем criteria_group по id')
# def test_delete_criteria_group_by_id(send_request, add_group):
#     criteria_group_id = next(add_group)['id']
#     response = send_request(url=URL.criteria_group, params={'id':criteria_group_id}, method="DELETE")
#     print("response", response.json())
#     assert response.status_code == 200
#     assert response.json() == criteria_group_id
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем criteria_group по id')
#
# def test_delete_criteria_group_by_id(send_request):
#     random_criteria_group_id = random.randint(1,9999)
#     response = send_request(url=URL.criteria_group, params={'id':random_criteria_group_id}, method="DELETE")
#     expect_answer = {'nu such criteria group with id'}
#     assert response.status_code == 500
#     assert response.json() == expect_answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем criteria_group z id==null')
# def test_delete_criteria_group_by_id(send_request):
#     response = send_request(url=URL.criteria_group, method="DELETE")
#     print(response.json())
#     expect_answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': 'QOSRequestValidationException: Param id is required'}
#     assert response.status_code == 500
#     assert response.json() == expect_answer
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем все criteria')
# def test_get_criteria(send_request):
#     response = send_request(url=URL.criteria, method="GET")
#     print(response.json())
#     expect_answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': 'QOSRequestValidationException: Param id is required'}
#     assert response.status_code == 500
#     assert response.json() == expect_answer
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем criteria by id')
# def test_get_criteria_by_id(send_request, add_criteria):
#     criteria_for_test = next(add_criteria)
#     response = send_request(url=URL.criteria, params = {'id':criteria_for_test['id']}, method="GET")
#     print(response.json())
#     assert response.status_code == 200
#     assert response.json() == criteria_for_test
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем criteria by id')
# def test_get_criteria_by_unknown_id(send_request):
#     criteria_for_test = random.randint(1,9999)
#     response = send_request(url=URL.criteria, params = {'id':criteria_for_test}, method="GET")
#     #Присылает ничего
#     assert response.status_code == 500
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем criteria by id')
# def test_delete_criteria_by_id(send_request, add_criteria):
#     criteria_for_test = next(add_criteria)
#     response = send_request(url=URL.criteria, params = {'id':criteria_for_test['id']}, method="GET")
#     #Присылает ничего
#     assert response.status_code == 200
#     assert response.json() == criteria_for_test
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем criteria с неизвестным id')
# def test_delete_criteria_by_unknown_id(send_request):
#     criteria_for_test = random.randint(1,999)
#     response = send_request(url=URL.criteria, params = {'id':criteria_for_test}, method="GET")
#     expect_answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': 'QOSRequestValidationException: Template criteria with id=%d not fount'%criteria_for_test}
#     print(response.json())
#     assert response.status_code == 500
#     assert response.json() == expect_answer
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем criteria без id')
# def test_delete_criteria_without_id(send_request):
#     response = send_request(url=URL.criteria, method="GET")
#     print(response.json())
#     expect_answer = {'QOS_REQUEST_VALIDATION_EXCEPTION': 'QOSRequestValidationException: Param id is required'}
#     assert response.status_code == 500
#     assert response.json() == expect_answer



@allure.feature('Позитивный тест')
@allure.story('Добавляем template')
def test_add_template(send_request, add_criteria, delete_template):
    criteriaId = next(add_criteria)['id']
    data = make_test_data("post_template", {"$supervisorId":ROOT_user_id,
                                     "$name":random_string(),
                                     "$version":str(random.randint(1,10)),
                                     "$description":random_string(),
                                     "$criteriaId":criteriaId,
                                     "$weight":random.randint(1,100),
                                     "$criteriaPosition":1,
                                     "$section_name":random_string(),
                                     "$approvalPolicy":"STANDARD",
                                     "$templateCriteriaPosition":1
                                     })
    response = send_request(URL.edit_template, data['request'])
    print(response.json())
    assert response.status_code == 200
    delete_template['templateId'] = response.json()['id']
    assert equal_schema(response.json(), data['schema'])


@allure.feature('Позитивный тест')
@allure.story('Добавляем template')
def test_add_template(send_request, add_criteria, delete_template):
    criteriaId = next(add_criteria)['id']
    data = make_test_data("post_template", {"$supervisorId":ROOT_user_id,
                                     "$name":random_string(),
                                     "$version":str(random.randint(1,10)),
                                     "$description":random_string(),
                                     "$criteriaId":criteriaId,
                                     "$weight":random.randint(1,100),
                                     "$criteriaPosition":1,
                                     "$section_name":random_string(),
                                     "$approvalPolicy":"STANDARD",
                                     "$templateCriteriaPosition":1
                                     })
    response = send_request(URL.edit_template, data['request'])
    assert response.status_code == 200
    delete_template['templateId'] = response.json()['id']
    assert equal_schema(response.json(), data['schema'])


@allure.feature('Позитивный тест')
@allure.story('Добавляем template без имени, версии, id критерии, названия секции')
def test_add_template_without_name_version_criteriaId_sectionName(send_request):
    data = make_test_data("post_template", { "$supervisorId":None,
                                             "$name":None,
                                             "$version":None,
                                             "$description":random_string(),
                                             "$criteriaId":None,
                                             "$weight":random.randint(1,100),
                                             "$criteriaPosition":1,
                                             "$section_name":None,
                                             "$approvalPolicy":"STANDARD",
                                             "$templateCriteriaPosition":1
                                             })
    response = send_request(URL.edit_template, data['request'])
    excepted_response = {'QOS_TEMPLATE_NAME': 'NAME length from 1 to 255 characters.',
                         'QOS_TEMPLATE_SUPERVISOR': 'SUPERVISOR must be specified or SUPERVISOR ID must be > 1.',
                         'QOS_TEMPLATE_QCCL_SECTION_NAME': 'SECTION NAME length from 1 to 255 character. In section name=[null]',
                         'QOS_TEMPLATE_QCCL_CRITERIA_EMPTY_CRITERIA': 'Template CRITERIA must be not empty or CRITERIA ID must be > 0. id=[null]',
                         'QOS_TEMPLATE_VERSION': 'VERSION length from 1 to 255 characters.'}
    assert response.status_code == 400
    assert excepted_response == response.json()


# @allure.feature('Позитивный тест')
# @allure.story('Добавляем template без имени, версии, id критерии, названия секции')
# @pytest.mark.xfail
# def test_add_template_without_weight_criteriaPosition_templateCriteria(send_request, add_criteria):
#     criteriaId = next(add_criteria)['id']
#     data = make_test_data("post_template", {"$supervisorId":ROOT_user_id,
#                                          "$name":random_string(),
#                                          "$version":str(random.randint(1,10)),
#                                          "$description":random_string(),
#                                          "$criteriaId":criteriaId,
#                                          "$weight":None,
#                                          "$criteriaPosition":None,
#                                          "$section_name":random_string(),
#                                          "$approvalPolicy":"STANDARD",
#                                          "$templateCriteriaPosition":None
#                                          })
#     response = send_request(URL.edit_template, data['request'])
#     print(response.status_code)
#     print(response.json())
#     excepted_response = {'QOS_TEMPLATE_NAME': 'NAME length from 1 to 255 characters.',
#                          'QOS_TEMPLATE_SUPERVISOR': 'SUPERVISOR must be specified or SUPERVISOR ID must be > 1.',
#                          'QOS_TEMPLATE_QCCL_SECTION_NAME': 'SECTION NAME length from 1 to 255 character. In section name=[null]',
#                          'QOS_TEMPLATE_QCCL_CRITERIA_EMPTY_CRITERIA': 'Template CRITERIA must be not empty or CRITERIA ID must be > 0. id=[null]',
#                          'QOS_TEMPLATE_VERSION': 'VERSION length from 1 to 255 characters.'}
#     assert response.status_code == 400
#     assert excepted_response == response.json()