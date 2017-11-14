import pytest, allure, json, requests, random


from Data.Make_requests_and_answers import make_test_data
from Data.Make_requests_and_answers import equal_schema
from Data.Make_requests_and_answers import random_string
from Data.URLs_MAP import sesl_integration,sesl_mapfield


# @allure.feature('Позитивный тест')
# @allure.story('Добавляем интеграцию')
# def test_add_integration(send_request, clear_result):
#     data = make_test_data('post_integration', data={'$name':random_string(),
#                                              '$url':random_string(),
#                                              '$login':random_string(),
#                                              '$password':random_string(),
#                                              '$position':1})
#     response = send_request(url = sesl_integration, data=data['request'])
#     assert response.status_code == 200
#     assert equal_schema(response.json(),data['schema'])
#     clear_result['url'], clear_result['id'] = sesl_integration, response.json()['id']
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем интеграцию с пустыми значениями')
# @pytest.mark.xfail
# def test_add_integration_without_data(send_request, clear_result):
#     data = make_test_data('post_integration', data={'$name':None,
#                                              '$url':None,
#                                              '$login':None,
#                                              '$password':None,
#                                              '$position':None})
#     response = send_request(url = sesl_integration, data=data['request'])
#     print(response.json())
#     assert response.status_code == 200
#     assert equal_schema(response.json(),data['schema'])
#     clear_result['url'], clear_result['id'] = sesl_integration, response.json()['id']
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем интеграцию с не правильной позицией')
# @pytest.mark.xfail
# def test_add_integration_with_incorrect_position(send_request, clear_result):
#     data = make_test_data('post_integration', data={'$name':random_string(),
#                                              '$url':random_string(),
#                                              '$login':random_string(),
#                                              '$password':random_string(),
#                                              '$position':random.randint(2,10)})
#     response = send_request(url = sesl_integration, data=data['request'])
#     print(response.json())
#     clear_result['url'], clear_result['id'] = sesl_integration, response.json()['id']
#     assert response.status_code == 400
#     assert equal_schema(response.json(),data['schema'])
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем интегратор')
# def test_edit_integration(send_request, add_integration):
#     integrationId = next(add_integration)['id']
#     data = make_test_data('put_integration', data={'$integrationId':integrationId,
#                                              '$name':random_string(),
#                                              '$url':random_string(),
#                                              '$login':random_string(),
#                                              '$password':random_string(),
#                                              '$position':2})
#     response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
#     assert response.status_code == 200
#     assert equal_schema(response.json(),data['schema'])
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем интеграцию с существующей позицией')
# @pytest.mark.xfail
# def test_add_integration_with_existing_position(send_request, clear_result, add_integration):
#     existing_position = next(add_integration)['position']
#     data = make_test_data('post_integration', data={'$name':random_string(),
#                                              '$url':random_string(),
#                                              '$login':random_string(),
#                                              '$password':random_string(),
#                                              '$position':existing_position})
#     response = send_request(url = sesl_integration, data=data['request'])
#     clear_result['url'], clear_result['id'] = sesl_integration, response.json()['id']
#     answer = {'SESL_UNIQUE_VALUE_EXCEPTION': "SESLUniqueValueException: Integration with position %s already exists"%existing_position}
#     assert response.status_code == 400
#     assert answer == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем интеграцию с существующим именем')
# @pytest.mark.xfail
# def test_add_integration_with_existing_name(send_request, add_integration):
#     existing_name = next(add_integration)['name']
#     data = make_test_data('post_integration', data={'$name':existing_name,
#                                              '$url':random_string(),
#                                              '$login':random_string(),
#                                              '$password':random_string(),
#                                              '$position':random.randint(1,3)})
#     response = send_request(url = sesl_integration, data=data['request'])
#     print(response.json())
#     answer = {'SESL_UNIQUE_VALUE_EXCEPTION': "SESLUniqueValueException: Integration with name '%s' already exists"%existing_name}
#     assert response.status_code == 400
#     assert answer == response.json()
#
#
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем интегратор на уже существующее имя')
# @pytest.mark.xfail
# def test_edit_integration_on_existing_name(send_request, add_integration):
#     integration = next(add_integration)
#     existing_name = next(add_integration)['name']
#     data = make_test_data('put_integration', data={'$integrationId':integration['id'],
#                                              '$name':existing_name,
#                                              '$url':integration['url'],
#                                              '$login':random_string(),
#                                              '$password':random_string(),
#                                              '$position':1})
#     response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
#     answer = {'SESL_UNIQUE_VALUE_EXCEPTION': "SESLUniqueValueException: Integration with name '%s' already exists"%existing_name}
#     assert response.status_code == 400
#     assert answer == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем интегратор на пустые значения')
# @pytest.mark.xfail
# def test_edit_integration_on_empty_fields(send_request, add_integration):
#     integration = next(add_integration)
#     data = make_test_data('put_integration', data={'$integrationId':integration['id'],
#                                              '$name':None,
#                                              '$url':None,
#                                              '$login':None,
#                                              '$password':None,
#                                              '$position':None})
#     response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
#     answer = {'SESL_VALIDATION_INTEGRATION_URL_EMPTY': 'Integration URL is empty',
#               'SESL_VALIDATION_INTEGRATION_NAME_EMPTY': 'Integration name is empty',
#               'SESL_VALIDATION_INTEGRATION_POSITION_EMPTY': 'Integration position is empty'}
#     assert response.status_code == 400
#     assert answer == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем интегратор не передавая integrationId')
# def test_edit_integration_with_null_integrationId(send_request):
#     data = make_test_data('put_integration', data={'$integrationId':None,
#                                              '$name':random_string(),
#                                              '$url':random_string(),
#                                              '$login':random_string(),
#                                              '$password':random_string(),
#                                              '$position':1})
#     response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
#     answer = {'SESL_REQUEST_VALIDATION_EXCEPTION': 'SESLRequestValidationException: Integration id must not be empty'}
#     assert response.status_code == 500
#     assert answer == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Редактируем интегратор не передавая integrationId')
# def test_edit_integration_with_null_integrationId(send_request):
#     randomId = random.randint(1,9999999)
#     data = make_test_data('put_integration', data={'$integrationId':randomId,
#                                              '$name':random_string(),
#                                              '$url':random_string(),
#                                              '$login':random_string(),
#                                              '$password':random_string(),
#                                              '$position':1})
#     response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
#     answer = {'SESL_INTEGRATION_NOT_FOUND_EXCEPTION': 'SESLIntegrationNotFoundException: Unable to find integration with id=%d'%randomId}
#     assert response.status_code == 500
#     assert answer == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем интегратор по имени')
# def test_get_interation_by_integration_name(send_request, add_integration):
#     existing_integration = next(add_integration)
#     params = {'name':existing_integration['name']}
#     response = send_request(url = sesl_integration, params = params, method = "GET")
#     assert response.status_code == 200
#     assert existing_integration == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем интегратор по ID')
# def test_get_interation_by_integration_id(send_request, add_integration):
#     existing_integration = next(add_integration)
#     params = {'id':existing_integration['id']}
#     response = send_request(url = sesl_integration, params = params, method = "GET")
#     assert response.status_code == 200
#     assert existing_integration == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем интегратор не передавая параметр')
# def test_get_interation_without_sending_params(send_request, add_integration):
#     existing_integration_profile_1, existing_integration_profile_2 = next(add_integration), next(add_integration)
#     response = send_request(url = sesl_integration,  method = "GET")
#     assert response.status_code == 200
#     assert existing_integration_profile_1 and existing_integration_profile_2 in response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем интегратор по неизвестному ID')
# def test_get_interation_by_unknown_integration_id(send_request):
#     randomId = random.randint(1,999999)
#     params = {'id':randomId}
#     response = send_request(url = sesl_integration, params = params, method = "GET")
#     answer = {'SESL_INTEGRATION_NOT_FOUND_EXCEPTION': 'SESLIntegrationNotFoundException: Unable to find integration with id=%d'%randomId}
#     assert response.status_code == 500
#     assert answer == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Получаем интегратор по неизвестному имени')
# def test_get_interation_by_unknown_integration_name(send_request):
#     randomName = random_string()
#     params = {'name':randomName}
#     response = send_request(url = sesl_integration, params = params, method = "GET")
#     answer = {'SESL_INTEGRATION_NOT_FOUND_EXCEPTION': 'SESLIntegrationNotFoundException: Unable to find integration with name=%s'%randomName}
#     assert response.status_code == 500
#     assert answer == response.json()
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем интегратор')
# def test_delete_interation_by_id(send_request, add_integration):
#     existing_integration_id = next(add_integration)['id']
#     params = {'id':existing_integration_id}
#     response = send_request(url = sesl_integration, params = params, method = "DELETE")
#     assert response.status_code == 200
#     assert response.json() == existing_integration_id
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Удаляем интегратор с неизвестным ID')
# def test_delete_interation_by_unknown_integration_id(send_request):
#     randomId = random.randint(1,99999999)
#     params = {'id':randomId}
#     response = send_request(url = sesl_integration, params = params, method = "DELETE")
#     answer = {'SESL_INTEGRATION_NOT_FOUND_EXCEPTION': 'SESLIntegrationNotFoundException: Unable to find integration with id=%d'%randomId}
#     assert response.status_code == 500
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем маппинг с коректными параметрами')
# def test_add_mapping(send_request, add_integration):
#     exitsting_integration = next(add_integration)
#     data = make_test_data("post_mapfield", {"$databaseColumn":random_string(),
#                                                     "$title":random_string(),
#                                                     "$position":1,
#                                                     "$integrationId":exitsting_integration['id']})
#     response = send_request(sesl_mapfield, data['request'])
#     assert response.status_code == 200
#     assert equal_schema(response.json(), data['schema'])
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем маппинг с пустыми полями')
# def test_add_mapping_with_empty_fields(send_request, add_integration):
#     exitsting_integration = next(add_integration)
#     data = make_test_data("post_mapfield", {"$databaseColumn":None,
#                                                     "$title":None,
#                                                     "$position":None,
#                                                     "$integrationId":exitsting_integration['id']})
#     response = send_request(sesl_mapfield, data['request'])
#     answer = {'SESL_VALIDATION_MAP_FIELD_DATABASE_COLUMN_EMPTY': 'Map field database column is empty',
#               'SESL_VALIDATION_MAP_FIELD_TITLE_EMPTY': 'Map field title is empty',
#               'SESL_VALIDATION_MAP_FIELD_POSITION_EMPTY': 'Map field position is empty'}
#     assert response.status_code == 400
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем маппинг с неизвестным|null integrationId')
# @pytest.mark.xfail
# def test_add_mapping_with_unknown_integrationId(send_request):
#     data = make_test_data("post_mapfield", {"$databaseColumn":random_string(),
#                                                     "$title":random_string(),
#                                                     "$position":1,
#                                                     "$integrationId":random.randint(1,999999)})
#     response = send_request(sesl_mapfield, data['request'])
#     answer = {'SESL_VALIDATION_INTEGRATION_ID': 'No such integration ID'}
#     assert response.status_code == 400
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем маппинг, проверяем правильность присвоения к integration профилю')
# def test_add_mapping_check_integration_response(send_request, add_integration):
#     exitsting_integration = next(add_integration)
#     data = make_test_data("post_mapfield", {"$databaseColumn":random_string(),
#                                                     "$title":random_string(),
#                                                     "$position":1,
#                                                     "$integrationId":exitsting_integration['id']})
#     response = send_request(sesl_mapfield, data['request'])
#     assert response.status_code == 200
#     assert response.json()['integration'] == exitsting_integration
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Добавляем маппинг с уже существующими параметрами')
# @pytest.mark.xfail
# def test_add_mapping_with_existing_title_position_databaseColumn(send_request, add_mapping):
#     existing_mapping = next(add_mapping)
#     data = make_test_data("post_mapfield", {"$databaseColumn":existing_mapping['databaseColumn'],
#                                                     "$title":existing_mapping['title'],
#                                                     "$position":existing_mapping['position'],
#                                                     "$integrationId":existing_mapping['integration']['id']})
#     response = send_request(sesl_mapfield, data['request'])
#     answer = {'SESL_VALIDATION_MAPPING': 'Fields with this title position databasecolumn already exist'}
#     assert response.status_code == 400
#     assert response.json() == answer
#
#
# @allure.feature('Позитивный тест')
# @allure.story('Изменяем маппинг на валидные данные')
# @pytest.mark.xfail
# def test_edit_mapping(send_request, add_mapping):
#     existing_mapping = next(add_mapping)
#     data = make_test_data("put_mapfield", {"$databaseColumn":random_string(),
#                                             "$mapfieldId":existing_mapping['id'],
#                                             "$title":random_string(),
#                                             "$position":5})
#     response = send_request(sesl_mapfield, data['request'], method = "PUT")
#     print(response.json())
#     answer = {'SESL_VALIDATION_MAPPING': 'Fields with this title position databasecolumn already exist'}
#     assert response.status_code == 400
#     assert response.json() == answer

