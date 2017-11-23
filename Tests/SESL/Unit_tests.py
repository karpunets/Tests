import pytest, allure, json, requests, random


from Data.Make_requests_and_answers import make_test_data
from Data.Make_requests_and_answers import equal_schema
from Data.Make_requests_and_answers import random_string
from Data.URLs_MAP import sesl_integration,sesl_mapfield, sesl_tag


@allure.feature('SESL')
@allure.story('Добавляем интеграцию')
def test_add_integration(send_request, clear_result):
    data = make_test_data('post_integration', data={'$name':random_string(),
                                             '$url':random_string(),
                                             '$login':random_string(),
                                             '$password':random_string()})
    response = send_request(url = sesl_integration, data=data['request'])
    print(response.json())
    assert response.status_code == 200
    assert equal_schema(response.json(),data['schema'])
    clear_result['url'], clear_result['id'] = sesl_integration, response.json()['id']


@allure.feature('SESL')
@allure.story('Добавляем интеграцию с пустыми значениями')
def test_add_integration_without_data(send_request):
    data = make_test_data('post_integration', data={'$name':None,
                                             '$url':None,
                                             '$login':None,
                                             '$password':None})
    response = send_request(url = sesl_integration, data=data['request'])
    answer = {'SESL_VALIDATION_INTEGRATION_URL_EMPTY': 'Integration URL is empty',
              'SESL_VALIDATION_INTEGRATION_NAME_EMPTY': 'Integration name is empty'}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('SESL')
@allure.story('Редактируем интегратор')
def test_edit_integration(send_request, add_one_integration):
    integrationId = add_one_integration['id']
    data = make_test_data('put_integration', data={'$integrationId':integrationId,
                                             '$name':random_string(),
                                             '$url':random_string(),
                                             '$login':random_string(),
                                             '$password':random_string()})
    response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
    assert response.status_code == 200
    assert equal_schema(response.json(),data['schema'])



@allure.feature('SESL')
@allure.story('Добавляем интеграцию с существующим именем')
def test_add_integration_with_existing_name(send_request, add_one_integration):
    existing_name = add_one_integration['name']
    data = make_test_data('post_integration', data={'$name':existing_name,
                                             '$url':random_string(),
                                             '$login':random_string(),
                                             '$password':random_string()})
    response = send_request(url = sesl_integration, data=data['request'])
    answer = {'SESL_VALIDATION_INTEGRATION_NAME_UNIQUE': 'Integration name already exists'}
    assert response.status_code == 400
    assert answer == response.json()


@allure.feature('SESL')
@allure.story('Редактируем интеграцию на уже существующее имя')
def test_edit_integration_on_existing_name(send_request, add_two_integrations):
    integration = next(add_two_integrations)
    existing_name = next(add_two_integrations)['name']
    data = make_test_data('put_integration', data={'$integrationId':integration['id'],
                                             '$name':existing_name,
                                             '$url':integration['url'],
                                             '$login':random_string(),
                                             '$password':random_string()})
    response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
    answer = {'SESL_VALIDATION_INTEGRATION_NAME_UNIQUE': 'Integration name already exists'}
    assert response.status_code == 400
    assert answer == response.json()


@allure.feature('SESL')
@allure.story('Редактируем интегратор на пустые значения')
def test_edit_integration_on_empty_fields(send_request, add_one_integration):
    integration = add_one_integration
    data = make_test_data('put_integration', data={'$integrationId':integration['id'],
                                             '$name':None,
                                             '$url':None,
                                             '$login':None,
                                             '$password':None})
    response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
    answer = {'SESL_VALIDATION_INTEGRATION_URL_EMPTY': 'Integration URL is empty',
              'SESL_VALIDATION_INTEGRATION_NAME_EMPTY': 'Integration name is empty'}
    assert response.status_code == 400
    assert answer == response.json()


@allure.feature('SESL')
@allure.story('Редактируем интегратор не передавая integrationId')
def test_edit_integration_with_null_integrationId(send_request):
    data = make_test_data('put_integration', data={'$integrationId':None,
                                             '$name':random_string(),
                                             '$url':random_string(),
                                             '$login':random_string(),
                                             '$password':random_string()})
    response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
    answer = {'SESL_REQUEST_VALIDATION_EXCEPTION': 'SESLRequestValidationException: Integration id must not be empty'}
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('SESL')
@allure.story('Редактируем интегратор с не извсным integrationId')
def test_edit_integration_with_unknown_integrationId(send_request):
    randomId = random.randint(1,9999999)
    data = make_test_data('put_integration', data={'$integrationId':randomId,
                                             '$name':random_string(),
                                             '$url':random_string(),
                                             '$login':random_string(),
                                             '$password':random_string()})
    response = send_request(url = sesl_integration, data=data['request'], method = "PUT")
    answer = {'SESL_INTEGRATION_NOT_FOUND_EXCEPTION': 'SESLIntegrationNotFoundException: Unable to find integration with id=%d'%randomId}
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('SESL')
@allure.story('Получаем интегратор по имени')
def test_get_interation_by_integration_name(send_request, add_one_integration):
    existing_integration = add_one_integration
    params = {'name':existing_integration['name']}
    response = send_request(url = sesl_integration, params = params, method = "GET")
    assert response.status_code == 200
    assert existing_integration == response.json()


@allure.feature('SESL')
@allure.story('Получаем интегратор по ID')
def test_get_interation_by_integration_id(send_request, add_one_integration):
    existing_integration = add_one_integration
    params = {'id':existing_integration['id']}
    response = send_request(url = sesl_integration, params = params, method = "GET")
    assert response.status_code == 200
    assert existing_integration == response.json()


@allure.feature('SESL')
@allure.story('Получаем интегратор не передавая параметр')
def test_get_interation_without_sending_params(send_request, add_two_integrations):
    existing_integration_profile_1, existing_integration_profile_2 = next(add_two_integrations), next(add_two_integrations)
    response = send_request(url = sesl_integration,  method = "GET")
    assert response.status_code == 200
    assert existing_integration_profile_1 and existing_integration_profile_2 in response.json()


@allure.feature('SESL')
@allure.story('Получаем интегратор по неизвестному ID')
def test_get_interation_by_unknown_integration_id(send_request):
    randomId = random.randint(1,999999)
    params = {'id':randomId}
    response = send_request(url = sesl_integration, params = params, method = "GET")
    answer = {'SESL_INTEGRATION_NOT_FOUND_EXCEPTION': 'SESLIntegrationNotFoundException: Unable to find integration with id=%d'%randomId}
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('SESL')
@allure.story('Получаем интегратор по неизвестному имени')
def test_get_interation_by_unknown_integration_name(send_request):
    randomName = random_string()
    params = {'name':randomName}
    response = send_request(url = sesl_integration, params = params, method = "GET")
    answer = {'SESL_INTEGRATION_NOT_FOUND_EXCEPTION': 'SESLIntegrationNotFoundException: Unable to find integration with name=%s'%randomName}
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('SESL')
@allure.story('Удаляем интегратор')
def test_delete_interation_by_id(send_request, add_one_integration):
    existing_integration_id = add_one_integration['id']
    params = {'id':existing_integration_id}
    response = send_request(url = sesl_integration, params = params, method = "DELETE")
    assert response.status_code == 200
    assert response.json() == existing_integration_id


@allure.feature('SESL')
@allure.story('Удаляем интегратор с неизвестным ID')
def test_delete_interation_by_unknown_integration_id(send_request):
    randomId = random.randint(1,99999999)
    params = {'id':randomId}
    response = send_request(url = sesl_integration, params = params, method = "DELETE")
    answer = {'SESL_INTEGRATION_NOT_FOUND_EXCEPTION': 'SESLIntegrationNotFoundException: Unable to find integration with id=%d'%randomId}
    assert response.status_code == 500
    assert response.json() == answer


@allure.feature('SESL')
@allure.story('Добавляем маппинг с коректными параметрами')
def test_add_mapping(send_request, add_one_integration):
    exitsting_integration = add_one_integration
    data = make_test_data("post_mapfield", {"$databaseColumn":random_string(),
                                                    "$title":random_string(),
                                                    "$position":1,
                                                    "$integrationId":exitsting_integration['id']})
    response = send_request(sesl_mapfield, data['request'])
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])


@allure.feature('SESL')
@allure.story('Добавляем маппинг с пустыми полями')
def test_add_mapping_with_empty_fields(send_request, add_one_integration):
    exitsting_integration = add_one_integration
    data = make_test_data("post_mapfield", {"$databaseColumn":None,
                                                    "$title":None,
                                                    "$position":None,
                                                    "$integrationId":exitsting_integration['id']})
    response = send_request(sesl_mapfield, data['request'])
    answer = {'SESL_VALIDATION_MAP_FIELD_DATABASE_COLUMN_EMPTY': 'Map field database column is empty',
              'SESL_VALIDATION_MAP_FIELD_TITLE_EMPTY': 'Map field title is empty',
              'SESL_VALIDATION_MAP_FIELD_POSITION_EMPTY': 'Map field position is empty'}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('SESL')
@allure.story('Добавляем маппинг с неизвестным|null integrationId')
def test_add_mapping_with_unknown_integrationId(send_request):
    data = make_test_data("post_mapfield", {"$databaseColumn":random_string(),
                                                    "$title":random_string(),
                                                    "$position":random.randint(3,999),
                                                    "$integrationId":random.randint(1,999999)})
    response = send_request(sesl_mapfield, data['request'])
    answer = {'SESL_VALIDATION_MAP_FIELD_INTEGRATION_NOT_EXISTS': 'Map field integration not exists'}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('SESL')
@allure.story('Добавляем маппинг, проверяем правильность присвоения к integration профилю')
def test_add_mapping_check_integration_response(send_request, add_one_integration):
    exitsting_integration = add_one_integration
    data = make_test_data("post_mapfield", {"$databaseColumn":random_string(),
                                                    "$title":random_string(),
                                                    "$position":random.randint(3,999),
                                                    "$integrationId":exitsting_integration['id']})
    response = send_request(sesl_mapfield, data['request'])
    assert response.status_code == 200
    assert response.json()['integration'] == exitsting_integration


@allure.feature('SESL')
@allure.story('Добавляем маппинг с уже существующими параметрами')
def test_add_mapping_with_existing_title_position_databaseColumn(send_request, add_one_map):
    existing_mapping = add_one_map
    data = make_test_data("post_mapfield", {"$databaseColumn":existing_mapping['databaseColumn'],
                                                    "$title":existing_mapping['title'],
                                                    "$position":existing_mapping['position'],
                                                    "$integrationId":existing_mapping['integration']['id']})
    response = send_request(sesl_mapfield, data['request'])

    answer = {'SESL_VALIDATION_MAP_FIELD_TITLE_UNIQUE': 'Map field title for such integration already exists',
              'SESL_VALIDATION_MAP_FIELD_DATABASE_COLUMN_UNIQUE': 'Map field database column for such integration already exists',
              'SESL_VALIDATION_MAP_FIELD_POSITION_UNIQUE': 'Map field position for such integration already exists'}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('SESL')
@allure.story('Изменяем маппинг на валидные данные')
def test_edit_mapping(send_request, add_one_map):
    existing_mapping = add_one_map
    data = make_test_data("put_mapfield", {"$databaseColumn":random_string(),
                                            "$mapfieldId":existing_mapping['id'],
                                            "$title":random_string(),
                                            "$position":random.randint(3,999)})
    response = send_request(sesl_mapfield, data['request'], method = "PUT")
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])

@allure.feature('SESL')
@allure.story('Изменяем маппинг на пустые значения')
def test_edit_mapping_on_empty_values(send_request, add_one_map):
    existing_mapping = add_one_map
    data = make_test_data("put_mapfield", { "$mapfieldId":existing_mapping['id'],
                                            "$databaseColumn":None,
                                            "$title":None,
                                            "$position":None})
    response = send_request(sesl_mapfield, data['request'], method = "PUT")

    answer = {'SESL_VALIDATION_MAP_FIELD_DATABASE_COLUMN_EMPTY': 'Map field database column is empty',
              'SESL_VALIDATION_MAP_FIELD_TITLE_EMPTY': 'Map field title is empty',
              'SESL_VALIDATION_MAP_FIELD_POSITION_EMPTY': 'Map field position is empty'}
    assert response.status_code == 400
    assert response.json() == answer

@allure.feature('SESL')
@allure.story('Изменяем маппинг с неизвестным\пустым ID')
def test_edit_mapping_with_unknown_id(send_request):
    randomId= random.randint(1,999999)
    data = make_test_data("put_mapfield", { "$mapfieldId":randomId,
                                            "$databaseColumn":random_string(),
                                            "$title":random_string(),
                                            "$position":random.randint(3,999)})
    response = send_request(sesl_mapfield, data['request'], method = "PUT")

    answer = {'SESL_VALIDATION_MAP_FIELD_NOT_EXISTS': 'Map field not exists'}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('SESL')
@allure.story('Изменяем маппинг на существующие данные')
def test_edit_mapping_on_already_exist_fields(send_request, add_two_maps):
    existing_mapping = next(add_two_maps)
    to_change_mapping = next(add_two_maps)
    data = make_test_data("put_mapfield", {"$databaseColumn":existing_mapping['databaseColumn'],
                                            "$mapfieldId":to_change_mapping['id'],
                                            "$title":existing_mapping['title'],
                                            "$position":existing_mapping['position']})
    response = send_request(sesl_mapfield, data['request'], method = "PUT")

    answer = {'SESL_VALIDATION_MAP_FIELD_TITLE_UNIQUE': 'Map field title for such integration already exists',
              'SESL_VALIDATION_MAP_FIELD_DATABASE_COLUMN_UNIQUE': 'Map field database column for such integration already exists',
              'SESL_VALIDATION_MAP_FIELD_POSITION_UNIQUE': 'Map field position for such integration already exists'}
    assert response.status_code == 400
    assert response.json() == answer

@allure.feature('SESL')
@allure.story('Получаем маппинг по ID')
def test_get_mapping_by_id(send_request, add_one_map):
    existing_mapping = add_one_map
    params = {'id':existing_mapping['id']}
    response = send_request(sesl_mapfield, params=params, method = "GET")
    assert response.status_code == 200
    assert response.json() == existing_mapping


@allure.feature('SESL')
@allure.story('Получаем маппинг по ID')
def test_get_mapping_by_id(send_request, add_one_map):
    existing_mapping = add_one_map
    params = {'id':existing_mapping['id']}
    response = send_request(sesl_mapfield, params=params, method = "GET")
    assert response.status_code == 200
    assert response.json() == existing_mapping


@allure.feature('SESL')
@allure.story('Получаем маппинг по integrationId')
def test_get_mapping_by_integrationId(send_request, add_two_maps):
    existing_mapping_1 = next(add_two_maps)
    existing_mapping_2 = next(add_two_maps)
    integrationId = existing_mapping_1['integration']['id']
    params = {'integrationId':integrationId}
    response = send_request(sesl_mapfield, params=params, method = "GET")
    assert response.status_code == 200
    assert existing_mapping_1 and existing_mapping_2 in response.json()


@allure.feature('SESL')
@allure.story('Удаляем маппинг по Id')
def test_delete_mapping_by_id(send_request, add_one_map):
    existing_mapping = add_one_map
    mappingId = existing_mapping['id']
    params = {'id':mappingId}
    response = send_request(sesl_mapfield, params=params, method = "DELETE")
    assert response.status_code == 200
    assert response.json() == mappingId


@allure.feature('SESL')
@allure.story('Удаляем маппинг по неизвестному Id')
def test_delete_mapping_by_unknown_id(send_request):
    randomId = random.randint(1,9999999)
    params = {'id':randomId}
    response = send_request(sesl_mapfield, params=params, method = "DELETE")
    answer = {'SESL_MAP_FIELD_NOT_FOUND_EXCEPTION': 'SESLMapFieldNotFoundException: Unable to find map field with id=%d'%randomId}
    assert response.status_code == 500
    assert response.json() == answer



@allure.feature('SESL')
@allure.story('Получаем маппинг без параметров')
def test_get_mapping_without_params(send_request):
    response = send_request(sesl_mapfield,  method = "GET")
    answer = {'SESL_MAP_FIELD_NOT_FOUND_EXCEPTION': 'SESLMapFieldNotFoundException: Id or integrationId must not be empty'}
    assert response.status_code == 500
    assert response.json() == answer


@allure.feature('SESL')
@allure.story('Получаем маппинг по не правильному ID')
def test_get_mapping_by_unknown_id(send_request):
    randomId = random.randint(1,999999)
    params = {'id':randomId}
    response = send_request(sesl_mapfield, params=params, method = "GET")

    answer = {'SESL_MAP_FIELD_NOT_FOUND_EXCEPTION': 'SESLMapFieldNotFoundException: Unable to find map field with id=%d'%randomId}
    assert response.status_code == 500
    assert response.json() == answer


@allure.feature('SESL')
@allure.story('Получаем маппинг по не правильному integrationId')
def test_get_mapping_by_unknown_integrationId(send_request):
    randomIntegrationId = random.randint(1,999999)
    params = {'id':randomIntegrationId}
    response = send_request(sesl_mapfield, params=params, method = "GET")
    answer = {'SESL_MAP_FIELD_NOT_FOUND_EXCEPTION': 'SESLMapFieldNotFoundException: Unable to find map field with id=%d'%randomIntegrationId}
    assert response.json() == answer and response.status_code == 500

@allure.feature('SESL')
@allure.story('Получаем маппинг по не правильному integrationId')
def test_get_integration_check_password(send_request, add_integration_with_password):
    integration_id = add_integration_with_password['id']
    params = {'id':integration_id}
    response = send_request(url=sesl_integration, params=params, method="GET")
    assert response.json()['password'] == None and response.status_code == 200


@allure.feature('SESL')
@allure.story('Добавляем тег')
def test_add_tag(send_request, add_one_integration, clear_result):
    integrationId = add_one_integration['id']
    data = make_test_data("post_tag", {"$tag":random_string(),
                                       "$position":random.randint(3,99),
                                       "$integrationId":integrationId})
    response = send_request(sesl_tag, data['request'])
    clear_result['url'], clear_result['id'] = sesl_tag, response.json()['id']
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])


@allure.feature('SESL')
@allure.story('Добавляем тег без интеграции')
@pytest.mark.xfail
def test_add_tag_without_integration(send_request,  clear_result):
    data = make_test_data("post_tag", {"$tag":random_string(),
                                       "$position": random.randint(3, 99)})
    response = send_request(sesl_tag, data['request'])
    print(response.json())
    clear_result['url'], clear_result['id'] = sesl_tag, response.json()['id']
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])


@allure.feature('SESL')
@allure.story('Добавляем тег без поля tag')
def test_add_tag_without_tag_name(send_request, add_one_integration):
    integrationId = add_one_integration['id']
    data = make_test_data("post_tag", {"$integrationId":integrationId,
                                       "$position": random.randint(3, 99)})
    response = send_request(sesl_tag, data['request'])
    expected_answer = {'SESL_VALIDATION_INTEGRATION_TAG_TAG_EMPTY': 'Integration tag is empty'}
    assert response.status_code == 400
    assert response.json() == expected_answer


@allure.feature('SESL')
@allure.story('Добавляем тег с не верным integrationId')
@pytest.mark.xfail
def test_add_tag_with_unknown_integrationId(send_request):
    randomId = random.randint(1,99999)
    data = make_test_data("post_tag", {"$tag":random_string(),
                                       "$position": random.randint(3, 99),
                                       "$integrationId":randomId})
    response = send_request(sesl_tag, data['request'])
    print(response.json())
    expected_answer = {'DATA_ACCESS_ENTITY_NOT_FOUND_EXCEPTION': 'mosuch integrationID %d'%randomId}
    assert response.status_code == 500
    assert response.json() == expected_answer


@allure.feature('SESL')
@allure.story('Добавляем тег с несколькими интеграциями')
def test_add_tag_with_few_integrations(send_request, add_two_integrations, clear_result):
    first_integration = next(add_two_integrations)
    second_integration = next(add_two_integrations)
    data = make_test_data("post_tag", {"$tag":random_string(),
                                       "$position": 1,
                                       "$integrationId":first_integration['id']})
    #Добавляем еще одну интеграцию в список
    data['request']['positionIntegrations'].append({2:{'id':second_integration['id']}})
    response = send_request(sesl_tag, data['request'])
    response = response.json()
    clear_result['url'], clear_result['id'] = sesl_tag, response['id']
    assert response.status_code == 200
    assert first_integration in response['integrations'].values() and \
           second_integration in response['integrations'].values()


@allure.feature('Validation')
@allure.story('Добавляем тег с существующим именем')
@pytest.mark.xfail
def test_add_tag_with_existing_name(send_request, add_one_tag):
    existingName = add_one_tag['tag']
    data = make_test_data("post_tag", {"$tag":existingName,
                                       "$position": random.randint(3, 99)})
    response = send_request(sesl_tag, data['request'])
    print(response.json())
    expected_answer = {"Name already exist"}
    assert response.status_code == 200
    assert response.json() == expected_answer


@allure.feature('SESL')
@allure.story('Добавляем тег с существующим integrationId')
def test_add_tag_with_existing_in_other_tag_integrationId(send_request, add_one_tag, clear_result):
    integrationId = add_one_tag['integrations'][0]['id']
    data = make_test_data("post_tag", {"$tag":random_string(),
                                       "$integrationId":integrationId,
                                       "$position": random.randint(3, 99)})
    response = send_request(sesl_tag, data['request'])
    clear_result['url'], clear_result['id'] = sesl_tag, response.json()['id']
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])


@allure.feature('SESL')
@allure.story('Добавляем тег с пустой позицией')
def test_add_tag_without_position(send_request, add_one_integration, clear_result):
    integrationId = add_one_integration['id']
    data = make_test_data("post_tag", {"$tag":random_string(),
                                       "$position":None,
                                       "$integrationId":integrationId})
    response = send_request(sesl_tag, data['request'])
    print(response.json())
    clear_result['url'], clear_result['id'] = sesl_tag, response.json()['id']
    assert response.status_code == 200
    assert equal_schema(response.json(), data['schema'])


@allure.feature('SESL')
@allure.story('Добавляем тег, ')
def test_add_two_tag_integrationId_which_already_exist_in_tag(send_request, add_one_integration, clear_result):
    integrationId = add_one_integration['id']
    data = make_test_data("post_tag", {"$tag":random_string(),
                                       "$position":None,
                                       "$integrationId":integrationId})
    data['request']['positionIntegrations'].append({2: {'id': integrationId}})
    response = send_request(sesl_tag, data['request'])
    print(response.json())
    clear_result['url'], clear_result['id'] = sesl_tag, response.json()['id']
    assert response.status_code == 400
    assert equal_schema(response.json(), data['schema'])

# @allure.feature('SESL')
# @allure.story('Редактируем тег')
# def test_edit_tag(send_request, add_one_tag):
#     exsist_tag = add_one_tag
#     data = make_test_data("put_tag", {"$id":exsist_tag['id'],
#                                       "$tag":random_string(),
#                                       "$integrationId":exsist_tag['integrations'][0]['id']})
#
#     response = send_request(sesl_tag, data['request'], method = "PUT")
#     assert response.status_code == 200
#     assert equal_schema(response.json(), data['schema'])
#
#
# @allure.feature('SESL')
# @allure.story('Редактируем тег, удаляем integrationId(передаем пустое)')
# @pytest.mark.xfail
# def test_edit_tag_integrationId_on_empty(send_request, add_one_tag):
#     exsist_tag = add_one_tag
#     data = make_test_data("put_tag", {"$id":exsist_tag['id'],
#                                       "$tag":random_string()})
#
#     response = send_request(sesl_tag, data['request'], method = "PUT")
#     print(response.json())
#     assert response.status_code == 200
#     assert equal_schema(response.json(), data['schema'])
#
#
# @allure.feature('SESL')
# @allure.story('Редактируем тег с пустым tag')
# def test_edit_tag_with_empty_tag(send_request, add_one_tag):
#     exsist_tag = add_one_tag
#     data = make_test_data("put_tag", {"$id":exsist_tag['id'],
#                                       "$tag":None,
#                                       "$integrationId":exsist_tag['integrations'][0]['id']})
#
#     response = send_request(sesl_tag, data['request'], method = "PUT")
#     exissting_answer = {'SESL_VALIDATION_INTEGRATION_TAG_TAG_EMPTY': 'Integration tag is empty'}
#     assert response.status_code == 400
#     assert response.json() == exissting_answer
#
#
# @allure.feature('SESL')
# @allure.story('Редактируем тег с неизвестным id')
# def test_edit_tag_with_unknown_tag_id(send_request, add_one_tag):
#     exsist_tag = add_one_tag
#     randomId = random.randint(1,99999)
#     data = make_test_data("put_tag", {"$id":randomId,
#                                       "$tag":random_string(),
#                                       "$integrationId":exsist_tag['integrations'][0]['id']})
#
#     response = send_request(sesl_tag, data['request'], method = "PUT")
#     exissting_answer = {'SESL_INTEGRATION_TAG_NOT_FOUND_EXCEPTION': 'SESLIntegrationTagNotFoundException: Unable to find integration tag with id=%d'%randomId}
#     assert response.status_code == 500
#     assert response.json() == exissting_answer
#
#
# @allure.feature('SESL')
# @allure.story('Редактируем тег на уже существующее имя')
# @pytest.mark.xfail
# def test_edit_tag_on_existitng_tag_name(send_request, add_two_tags):
#     exist_tag_name = next(add_two_tags)['tag']
#     exist_tag = next(add_two_tags)
#     data = make_test_data("put_tag", {"$id":exist_tag['id'],
#                                       "$tag":exist_tag_name,
#                                       "$integrationId":exist_tag['integrations'][0]['id']})
#     response = send_request(sesl_tag, data['request'], method = "PUT")
#     expect_answer = {'SESL_UNIQUE_VALUE_EXCEPTION': "SESLUniqueValueException: Tag '%s' already exists"%exist_tag_name}
#     assert response.status_code == 400
#     assert response.json() == expect_answer
#
#
# @allure.feature('SESL')
# @allure.story('Редактируем тег на integrationId, который уже есть в другом теге')
# def test_edit_tag_on_existitng_integrationId(send_request, add_two_tags):
#     exist_integratioId = next(add_two_tags)['integrations'][0]['id']
#     exist_tag = next(add_two_tags)
#     data = make_test_data("put_tag", {"$id":exist_tag['id'],
#                                       "$tag":random_string(),
#                                       "$integrationId":exist_integratioId})
#     response = send_request(sesl_tag, data['request'], method = "PUT")
#     assert response.status_code == 200
#     assert equal_schema(response.json(), data['schema'])
#
#
# @allure.feature('SESL')
# @allure.story('Получаем теги')
# def test_get_all_tags(send_request, add_two_tags):
#     exist_tag_1 = next(add_two_tags)
#     exist_tag_2 = next(add_two_tags)
#     response = send_request(sesl_tag, method = "GET")
#     assert response.status_code == 200
#     assert exist_tag_1 in response.json() and exist_tag_2 in response.json()
#
#
# @allure.feature('SESL')
# @allure.story('Получаем тег по id')
# def test_get_tag_by_id(send_request, add_one_tag):
#     exist_tag = add_one_tag
#     response = send_request(sesl_tag,params={'id':exist_tag['id']}, method = "GET")
#     assert response.status_code == 200
#     assert exist_tag == response.json()
#
#
# @allure.feature('SESL')
# @allure.story('Получаем тег по не известному id')
# def test_get_tag_by_unknown_id(send_request):
#     random_tagId = random.randint(1,999999)
#     response = send_request(sesl_tag,params={'id':random_tagId}, method = "GET")
#     expect_answer = {'SESL_INTEGRATION_TAG_NOT_FOUND_EXCEPTION': 'SESLIntegrationTagNotFoundException: Unable to find integration tag with id=%d'%random_tagId}
#     assert response.status_code == 500
#     assert response.json() == expect_answer
#
#
# @allure.feature('SESL')
# @allure.story('Удаляем тег по id')
# def test_delete_tag_by_id(send_request, add_one_tag):
#     exist_tagId = add_one_tag['id']
#     response = send_request(sesl_tag,params={'id':exist_tagId}, method = "DELETE")
#     assert response.status_code == 200
#     assert exist_tagId == response.json()
#
#
# @allure.feature('SESL')
# @allure.story('Удаляем тег по не извесному id')
# def test_delete_tag_by_unknown_id(send_request):
#     random_tagId = random.randint(1,99999)
#     response = send_request(sesl_tag,params={'id':random_tagId}, method = "DELETE")
#     expect_answer = {'SESL_INTEGRATION_TAG_NOT_FOUND_EXCEPTION': 'SESLIntegrationTagNotFoundException: Unable to find integration tag with id=%d'%random_tagId}
#     assert response.status_code == 500
#     assert response.json() == expect_answer