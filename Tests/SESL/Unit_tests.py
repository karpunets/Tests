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


# @allure.feature('Позитивный тест')
# @allure.story('Добавляем интеграцию с существующим именем')
# @pytest.mark.xfail
# def test_add_integration_with_existing_name(send_request, clear_result, add_integration):
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