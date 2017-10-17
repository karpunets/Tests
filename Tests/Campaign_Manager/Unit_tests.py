import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _



class Tests_add_campaign_and_result_codes:
    @pytest.fixture(scope='function')
    def delete_result_code(request):
        result_codes_id = {}
        yield result_codes_id
        response = requests.delete(url=URL.remove_result_code, params=result_codes_id, headers=URL.headers)
        assert response.status_code == 200

    @pytest.fixture(scope='function')
    def add_delete_result_code(request):
        result_codes_id = {}
        yield result_codes_id
        response = requests.delete(url=URL.remove_result_code, params=result_codes_id, headers=URL.headers)
        assert response.status_code == 200

    @allure.feature('Негативный тест')
    @allure.story('Добавляем кампанию без груп')
    def test_add_campaign_without_any_groups(self, send_request):
        payload = _.get_JSON_request('add_campaign', **{'groups': None})
        response = send_request(url=URL.edit_campaign, data=payload)
        answer = {'SCM_VALIDATION_CAMPAIGN_GROUPS': 'Can not add or edit Campaign without any Group'}
        assert response.status_code == 400
        assert response.json() == answer

    # Нет валидации на не существующую группу
    @allure.feature('Негативный тест')
    @allure.story('Добавляем кампанию с не существующй групой')
    @pytest.mark.xfail
    def test_add_campaign_with_unknown_group(self, send_request):
        payload = _.get_JSON_request('add_campaign', **{'groups': [{"id": 99999999999}]})
        response = send_request(url=URL.edit_campaign, data=payload)
        answer = {'SCM_VALIDATION_CAMPAIGN_GROUPS': 'No such group'}
        print(response.json())
        assert response.status_code == 500
        assert response.json() == answer

    @allure.feature('Негативный тест')
    @allure.story('Добавляем кампанию с существующей скилгрупой')
    def test_add_campaign_with_existing_skillgroup(self, add_campaign, send_request):
        payload = _.get_JSON_request('add_campaign')
        response = send_request(url=URL.edit_campaign, data=payload)
        answer = {
            'SCM_DIALER_EXCEPTION': "DialerException: ApiException{errors=[\n{errorData='skillGroup', errorMessage='Each Skill Group can only be assigned to one Campaign.'}]}"}
        assert response.status_code == 500
        assert response.json() == answer

    @pytest.mark.xfail
    @allure.feature('Негативный тест')
    @allure.story('Добавляем кампанию с существующим кодом')
    def test_add_campaign_with_existing_code(self, add_campaign, send_request):
        campaign_code = add_campaign['code']
        payload = _.get_JSON_request('add_campaign', **{'code': campaign_code})
        response = send_request(url=URL.edit_campaign, data=payload)
        answer = {"SCM_ENTITY_WITH_SUCH_FIELD_EXISTS": "SCMEntityWithSuchFieldExists: CODE"}
        assert response.status_code == 500
        assert response.json() == answer

    @allure.feature('Негативный тест')
    @allure.story('Добавляем кампанию с удаленным кодом')
    def test_add_campaign_with_deleted_code(self, send_request):
        payload = _.get_JSON_request('add_campaign', **{'code': 'deleted_code'})
        response = send_request(url=URL.edit_campaign, data=payload)
        answer = "errorData='name', errorMessage='A deleted item exists with the specified value.  The names of deleted items cannot be reused unless they are permanently deleted via the Deleted Objects tool.'"
        assert response.status_code == 500
        assert answer in response.json()['SCM_DIALER_EXCEPTION']

    @allure.feature('Позитивный тест')
    @allure.story('Получаем список кампаний')
    def test_get_campaign(self, add_campaign, send_request):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        code = add_campaign['code']
        data = {}
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.get_campaign, data=data)
        answer = [
            {'id': campaign_id, 'code': code, 'name': 'auto_test_campaign', 'comment': 'auto_test', 'deleted': False,
             'groups': [{'id': 2}]}]
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Позитивный тест')
    @allure.story('Получаем result_code кампаний')
    def test_get_result_code(self, add_campaign, send_request):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        data = {"campaignId": campaign_id}
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.get_result_code, data=data)
        assert response.status_code == 200
        result = ['SUCCESS', "CD_callResult", "CD_callStatus", 'CD_callsMade']
        answer = []
        for i in response.json():
            answer.append(i['code'])
        assert answer == result

    @allure.feature('Негативный тест')
    @allure.story('Получаем result_code не существующей кампаний')
    @pytest.mark.xfail
    def test_get_result_code_for_unknown_company(self, add_campaign, send_request):
        # Подготавливаем данные в JSON для запроса
        data = {"campaignId": 999999999999999999}
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.get_result_code, data=data)
        print(response.text)
        assert response.status_code == 400

    @allure.feature('Позитивный тест')
    @allure.story('Добавляем код результата')
    @pytest.mark.parametrize('dataType', ['INTEGER', 'FLOAT', 'STRING', 'TEXT', 'DATE'])
    @pytest.mark.parametrize('code', [123123123, 1232.22, 'string'])
    def test_add_result_codes(self, add_campaign, send_request, delete_result_code, dataType, code):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']

        data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
                                                        "dataType": dataType,
                                                        'code': code})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.edit_result_code, data=data)
        result_code_id = response.json()['id']
        delete_result_code['id'] = result_code_id
        answer = _.get_JSON_response('add_result_code', **{'id': result_code_id,
                                                           'dataType': dataType,
                                                           'code': str(code)})
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем код результата с строкой 256 символов')
    @pytest.mark.parametrize('dataType', ['INTEGER', 'FLOAT', 'STRING', 'TEXT', 'DATE'])
    def test_add_result_codes_with_256(self, add_campaign, send_request, dataType):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
                                                        "dataType": dataType,
                                                        'code': "q" * 256,
                                                        'name': 'q' * 256})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.edit_result_code, data=data)
        answer = {"SCM_VALIDATION_OVERALL_NAME_LENGTH": "Name is to long, max length = 255 characters",
                  "SCM_VALIDATION_OVERALL_CODE_LENGTH": "Code is to long, max length = 255 characters"}
        assert response.status_code == 400
        assert answer == response.json()

    @allure.feature('Позитивный тест')
    @allure.story('Добавляем варианты значений для кодов результатов')
    @pytest.mark.parametrize(('dataType', 'value'),
                             [('INTEGER', 123321), ('FLOAT', 123.25), ('STRING', 'string'), ('TEXT', 'some_text'),
                              ('DATE', 132213123213)])
    def test_add_result_variants(self, add_campaign, send_request, delete_result_code, dataType, value):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        campaign_code = add_campaign['code']
        data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
                                                        "dataType": dataType})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.edit_result_code, data=data)
        result_code_id = response.json()['id']
        delete_result_code['id'] = result_code_id
        assert response.status_code == 200
        data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
                                                            "resultVariant": {"value": value, "forInit": False}})
        response = send_request(url=URL.edit_result_variant, data=data)
        assert response.status_code == 200

    @allure.feature('Негативный тест')
    @allure.story('Добавляем не валидные варианты значений для кодов результатов')
    @pytest.mark.parametrize(('dataType', 'value'),
                             [('INTEGER', "string"), ('FLOAT', "string"), ('DATE', "string")])
    def test_add_incorrect_result_variants(self, add_campaign, send_request, delete_result_code, dataType, value):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        campaign_code = add_campaign['code']
        data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
                                                        "dataType": dataType})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.edit_result_code, data=data)
        result_code_id = response.json()['id']
        delete_result_code['id'] = result_code_id
        assert response.status_code == 200
        data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
                                                            "resultVariant": {"value": value, "forInit": False}})
        response = send_request(url=URL.edit_result_variant, data=data)
        answer = {
            "SCM_EDIT_RESULT_VARIANT_EXCEPTION": "SCMEditResultVariantException: Wrong result variant format for dataType '%s'" % dataType}
        assert response.status_code == 500
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем варианты значений с однаковыми результатами')
    @pytest.mark.parametrize(('dataType', 'value'),
                             [('INTEGER', 123321), ('FLOAT', 123.25), ('STRING', 'string'), ('TEXT', 'some_text'),
                              ('DATE', 132213123213)])
    def test_add_result_variant_with_existing_variant(self, add_campaign, send_request, delete_result_code, dataType,
                                                      value):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        campaign_code = add_campaign['code']
        data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
                                                        "dataType": dataType})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.edit_result_code, data=data)
        result_code_id = response.json()['id']
        delete_result_code['id'] = result_code_id
        assert response.status_code == 200
        data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
                                                            "resultVariant": {"value": value, "forInit": False}})
        response = send_request(url=URL.edit_result_variant, data=data)
        assert response.status_code == 200
        data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
                                                            "resultVariant": {"value": value, "forInit": False}})
        response = send_request(url=URL.edit_result_variant, data=data)
        answer = {
            'SCM_ENTITY_WITH_SUCH_FIELD_EXISTS': 'SCMEntityWithSuchFieldExists: ResultVariant with such field exists: VALUE'}
        assert response.status_code == 500
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем 2 значения forInit=True')
    @pytest.mark.parametrize(('dataType', 'value'),
                             [('INTEGER', 123321), ('FLOAT', 123.25), ('STRING', 'string'), ('TEXT', 'some_text'),
                              ('DATE', 132213123213)])
    def test_add_result_variant_withforInit_true(self, add_campaign, send_request, delete_result_code, dataType, value):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        campaign_code = add_campaign['code']
        data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
                                                        "dataType": dataType})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.edit_result_code, data=data)
        result_code_id = response.json()['id']
        delete_result_code['id'] = result_code_id
        assert response.status_code == 200
        data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
                                                            "resultVariant": {"value": value, "forInit": True}})
        response = send_request(url=URL.edit_result_variant, data=data)
        assert response.status_code == 200
        data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
                                                            "resultVariant": {"value": 99999999, "forInit": True}})
        response = send_request(url=URL.edit_result_variant, data=data)
        answer = {
            "SCM_EDIT_RESULT_VARIANT_EXCEPTION": "SCMEditResultVariantException: Unable to add forInit result variant='99999999' because forInit result variant already exists"}
        assert response.status_code == 500
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем варианты значения для кодов результатов с неизвесным "resultCode"')
    @pytest.mark.parametrize(('dataType', 'value'), [('STRING', 'string')])
    def test_add_result_variants_with_unknown_resultCode(self, add_campaign, send_request, delete_result_code, dataType,
                                                         value):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        campaign_code = add_campaign['code']
        data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
                                                        "dataType": dataType})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.edit_result_code, data=data)
        result_code_id = response.json()['id']
        delete_result_code['id'] = result_code_id
        assert response.status_code == 200
        data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
                                                            "resultCode": "UNKNOWN_result_code",
                                                            "resultVariant": {"value": value, "forInit": False}})
        response = send_request(url=URL.edit_result_variant, data=data)
        answer = {
            'SCM_REQUESTED_RESOURCE_NOT_FOUND': "SCMRequestedResourceNotFoundException: Unable to find result code 'UNKNOWN_result_code' for campaign '%s'" % campaign_code}
        assert response.status_code == 500
        assert response.json() == answer

    @allure.feature('Негативный тест')
    @allure.story('Пытаемся удалить стандартные значения кодов результатов(от дайлера)')
    @pytest.mark.parametrize('dialer_result_code', ['CD_callStatus', 'CD_callMade', 'CD_callResult'])
    def test_delete_dialer_results(self, add_campaign, send_request, dialer_result_code):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        data = {"campaignId": campaign_id}
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.get_result_code, data=data)
        assert response.status_code == 200
        for i in response.json():
            if i['code'] == dialer_result_code:
                response = requests.delete(url=URL.remove_result_code, params={'id': i['id']}, headers=URL.headers)
                answer = {
                    "SCM_DELETE_RESULT_CODE_EXCEPTION": "SCMDeleteResultCodeException: Unable to delete CISCO dialer result code '%s'" % dialer_result_code}
                assert response.status_code == 500
                assert response.json() == answer

    @allure.feature('Негативный тест')
    @allure.story('Пытаемся удалить стандартные варианты значений кодов результатов(от дайлера)')
    @pytest.mark.parametrize('dialer_result_code', ['CD_callStatus', 'CD_callResult'])
    def test_delete_dialer_results_variants(self, add_campaign, send_request, dialer_result_code):
        # Подготавливаем данные в JSON для запроса
        campaign_id, campaign_code = add_campaign['id'], add_campaign['code']
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.get_result_code, data={"campaignId": campaign_id})
        assert response.status_code == 200
        for i in response.json():
            if i['code'] == dialer_result_code:
                for j in i['resultVariants']:
                    params = {'id': j['id'], 'campaignCode': campaign_code, 'resultCode': dialer_result_code}
                    response = requests.delete(url=URL.remove_result_variant, params=params, headers=URL.headers)
                    answer = {
                        "SCM_DELETE_RESULT_VARIANT_EXCEPTION": "SCMDeleteResultVariantException: Unable to delete CISCO dialer result variant for result code '%s'" % dialer_result_code}
                    assert response.status_code == 500
                    assert response.json() == answer


class TestMapping:
    # Получаем списко фиксированных полей для маппинга
    @pytest.fixture(scope='module')
    def fixed_fields(self):
        # Словарь для добавления Ufieldov
        result = {'INTEGER': [], 'FLOAT': [], 'STRING': [], 'TEXT': []}
        response = requests.get(URL.get_fixed_fields, headers=URL.headers)
        for i in response.json():
            if i['dataType'] in result.keys():
                result[i['dataType']].append(i['field'])
        return result

    @pytest.fixture(scope='function')
    def add_map_field(self, add_campaign, fixed_fields, send_request, clear_result):
        fieldAbonent = random.choice(fixed_fields["STRING"])
        campaign_id = add_campaign['id']
        maps_json = []
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "fieldAbonent": fieldAbonent,
                                                      "campaign": {"id": campaign_id}})
        response = send_request(url=URL.map_field, data=data)
        assert response.status_code == 200
        maps_json.append(response.json())
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "phoneNumber": True,
                                                      "phoneType": "MOBILE",
                                                      "campaign": {"id": campaign_id}})
        response = send_request(url=URL.map_field, data=data)
        assert response.status_code == 200
        maps_json.append(response.json())
        yield maps_json
        print(maps_json)
        try:
            clear_result['url'], clear_result['id'] = URL.delete_mapfield, (maps_json[0]['id'], maps_json[1]['id'])
        except IndexError:
            pass

    @allure.feature('Позитивный тест')
    @allure.story('Добавляем мапинг полей(не телефоны)')
    @pytest.mark.parametrize('dataType', ['INTEGER', 'FLOAT', 'STRING', 'TEXT'])
    def test_add_map_fields(self, add_campaign, send_request, dataType, fixed_fields, clear_result):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        # SAMPLE
        fieldAbonent = random.choice(fixed_fields[dataType])
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "dataType": dataType,
                                                      "fieldAbonent": fieldAbonent,
                                                      "forExport": True,
                                                      "forFilter": True,
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        mapfield_id = response.json()['id']
        answer = _.get_JSON_response('add_map_field', **{'id': mapfield_id,
                                                         "name": "Mapping_test",
                                                         "fieldImport": "Mapping_test",
                                                         "dataType": dataType,
                                                         "fieldAbonent": fieldAbonent,
                                                         "forExport": True,
                                                         "forFilter": True,
                                                         "campaign": {"id": campaign_id}})
        clear_result['url'], clear_result['id'] = URL.delete_mapfield, mapfield_id
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Позитивный тест')
    @allure.story('Добавляем мапинг полей для поля phone=True')
    @pytest.mark.parametrize('phoneType', ['HOUSE', 'MOBILE', 'WORK'])
    def test_add_map_fields_phone(self, add_campaign, send_request, phoneType, clear_result):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "phoneNumber": True,
                                                      "phoneType": phoneType,
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        mapfield_id = response.json()['id']
        # Формируем ответ, который должен быть
        answer = _.get_JSON_response('add_map_field', **{'id': mapfield_id,
                                                         "name": "Mapping_test",
                                                         "fieldImport": "Mapping_test",
                                                         "phoneNumber": True,
                                                         "phoneType": phoneType,
                                                         "campaign": {"id": campaign_id}})
        # Удаляем добавленные ранее данные
        clear_result['url'], clear_result['id'] = URL.delete_mapfield, mapfield_id
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем мапинг полей без имени и поля импорта')
    def test_add_map_fields_without_name_and_fieldImport(self, add_campaign, send_request):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        data = _.get_JSON_request('add_map_field', **{
            "dataType": 'STRING',
            "fieldAbonent": "ClientID",
            "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        answer = {"SCM_VALIDATION_OVERALL_NAME": "Name is empty",
                  "SCM_VALIDATION_FIELD_MAP_IMPORT_FIELD": "fieldImport is empty"}

        assert response.status_code == 400
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем 2 раза один и тот же fieldAbonent')
    def test_add_map_field_with_existing_fieldAbonent(self, add_campaign, send_request, fixed_fields, clear_result):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        fieldAbonent = random.choice(fixed_fields["STRING"])
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "dataType": "STRING",
                                                      "fieldAbonent": fieldAbonent,
                                                      "forExport": True,
                                                      "forFilter": True,
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        mapfield_id = response.json()['id']
        clear_result['url'], clear_result['id'] = URL.delete_mapfield, mapfield_id
        assert response.status_code == 200

        # Отправляем запрос на создание мафилда с ClientID
        response = send_request(url=URL.map_field, data=data)
        answer = {
            "SCM_FIELD_MAPPING_EXCEPTION": "SCMFieldMappingException: Field map=%s already exists for campaignId=%s" % (
                fieldAbonent, campaign_id)}
        assert response.status_code == 500
        assert answer == response.json()

    @allure.feature('Позитивный тест')
    @allure.story('Добавляем 2 раза мапинг полей с одинаковыми полями fieldImport и name')
    def test_add_map_fields_with_existing_name_and_fieldImport(self, add_campaign, send_request, fixed_fields,
                                                               clear_result):
        # Подготавливаем данные в JSON для запроса
        dataType = "STRING"
        campaign_id = add_campaign['id']
        fieldAbonents = random.sample(fixed_fields[dataType], 2)
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "dataType": dataType,
                                                      "fieldAbonent": fieldAbonents[0],
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        assert response.status_code == 200
        mapfield_id_1 = response.json()['id']
        other_fieldAbonent = random.choice(fixed_fields[dataType])
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "dataType": dataType,
                                                      "fieldAbonent": fieldAbonents[1],
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        mapfield_id_2 = response.json()['id']
        answer = _.get_JSON_response('add_map_field', **{'id': mapfield_id_2,
                                                         "name": "Mapping_test",
                                                         "fieldImport": "Mapping_test",
                                                         "dataType": dataType,
                                                         "fieldAbonent": fieldAbonents[1],
                                                         "campaign": {"id": campaign_id}})
        clear_result['url'], clear_result['id'] = URL.delete_mapfield, (mapfield_id_1, mapfield_id_2)
        assert response.status_code == 200
        assert answer == response.json()

    # Не должно пропускать "forExport": True,"forFilter": True,"fieldAbonent":Ufield
    @allure.feature('Негативный тест')
    @allure.story('Добавляем 2 раза мапинг полей с одинаковыми полями fieldImport и name')
    @pytest.mark.xfail
    def test_add_map_field_with_fieldAbonent_forExport_forFilter_for_phones(self, add_campaign, send_request,
                                                                            fixed_fields):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        fieldAbonent = random.choice(fixed_fields["STRING"])
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "dataType": "STRING",
                                                      "fieldAbonent": fieldAbonent,
                                                      "forExport": True,
                                                      "forFilter": True,
                                                      "phoneNumber": True,
                                                      "phoneType": "HOUSE",
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        print(response.json())
        assert response.status_code == 500

    # Неудобочитаемая ошибка
    @allure.feature('Негативный тест')
    @allure.story('Добавляем не корекктный phoneType')
    @pytest.mark.xfail
    def test_add_map_field_with_incorrect_phoneType(self, add_campaign, send_request):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']

        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "dataType": "STRING",
                                                      "phoneNumber": True,
                                                      "phoneType": "Incorrect_type",
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        print(response.json())
        assert response.status_code == 400

    @allure.feature('Негативный тест')
    @allure.story('Добавляем мапинг полей с неправильным dataType для fieldAbonent')
    @pytest.mark.parametrize('dataType', ['INTEGER', 'FLOAT', 'STRING', 'TEXT'])
    def test_add_map_field_with_incorrect_dataType_for_fieldAbonent(self, add_campaign, send_request, fixed_fields,
                                                                    dataType):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        fieldAbonent = random.choice(fixed_fields[dataType])
        dataType_values = ['INTEGER', 'FLOAT', 'STRING', 'TEXT']
        # Удаляем корректное значение dataType для конкретного fieldAbonent
        dataType_values.remove(dataType)
        # Выбираем рандомное значение из оставшихся елементов
        incorrect_dataType = random.choice(dataType_values)
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "dataType": incorrect_dataType,
                                                      "fieldAbonent": fieldAbonent,
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        answer = {
            "SCM_FIELD_MAPPING_EXCEPTION": "SCMFieldMappingException: Incorrect mapping for=%s correct type=%s" % (
                fieldAbonent, dataType)}
        assert response.status_code == 500
        assert response.json() == answer

    # Не должно давать добавлять  phoneType для phoneNumber = False
    @allure.feature('Негативный тест')
    @allure.story('Добавляем мапинг полей(не телефоны) phoneType')
    @pytest.mark.xfail
    def test_add_map_fields_with_phoneType(self, add_campaign, send_request, dataType, fixed_fields, clear_result):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        fieldAbonent = random.choice(fixed_fields["STRING"])
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "phoneType": "MOBILE",
                                                      "dataType": dataType,
                                                      "fieldAbonent": fieldAbonent,
                                                      "campaign": {"id": campaign_id}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        mapfield_id = response.json()['id']
        clear_result['url'], clear_result['id'] = URL.delete_mapfield, mapfield_id
        assert response.status_code == 500

    @allure.feature('Негативный тест')
    @allure.story('Добавляем мапинг полей с не существующим campaignID')
    def test_add_map_fields_with_wrong_campaignID(self, add_campaign, send_request, fixed_fields):
        # Подготавливаем данные в JSON для запроса
        fieldAbonent = random.choice(fixed_fields["STRING"])
        data = _.get_JSON_request('add_map_field', **{"name": "Mapping_test",
                                                      "fieldImport": "Mapping_test",
                                                      "dataType": "STRING",
                                                      "fieldAbonent": fieldAbonent,
                                                      "campaign": {"id": 9999999999999999}})
        # Делаем запрос и получаем ответ
        response = send_request(url=URL.map_field, data=data)
        assert response.status_code == 500

    @allure.feature('Позитивный тест')
    @allure.story('Удаляем маппинг полей')
    def test_delete_map_fields(self, add_campaign, add_map_field):

        mapfield_id_no_phone, mapfield_id_phone = add_map_field[0]['id'], add_map_field[1]['id']
        add_map_field.pop(1), add_map_field.pop(0)
        response_no_phone = requests.delete(url=URL.delete_mapfield, params={'id': mapfield_id_no_phone},
                                            headers=URL.headers)
        response_phone = requests.delete(url=URL.delete_mapfield, params={'id': mapfield_id_phone}, headers=URL.headers)
        assert response_no_phone.status_code, response_phone.status_code == 200

    @allure.feature('Позитивный тест')
    @allure.story('Редактируем в маппинге(не телефон) след поля: "name", "fieldImport", "forExport", "forFilter"')
    def test_edit_map_fields(self, add_campaign, send_request, add_map_field):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        data = _.generate_JSON(add_map_field[0], {"name": "eddited_map_field",
                                                  "fieldImport": "eddited_map_field",
                                                  "forExport": True,
                                                  "forFilter": True,
                                                  })
        data['campaign'] = {"id": campaign_id}
        response = send_request(url=URL.map_field, data=data)
        assert response.status_code == 200
        assert response.json()['name'] and response.json()["fieldImport"] == "eddited_map_field"
        assert response.json()["forExport"] and response.json()["forFilter"] == True

    # Не существует такой кампании
    @allure.feature('Негативный тест')
    @allure.story('Удаляем маппинг не существующих полей')
    @pytest.mark.xfail
    def test_delete_map_fields_with_unknown_id(self, add_campaign):
        response = requests.delete(url=URL.delete_mapfield, params={'id': 99999999999}, headers=URL.headers)
        assert response.status_code == 500
        print(response.json())


        # Нужно дописать такие же тесты как и на добавление пользователей после фикса багов в валидации с телефонами
