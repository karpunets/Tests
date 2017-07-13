import pytest, allure, json, requests
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _


@pytest.fixture(scope='module')
def add_campaign(make_request):
    payload = _.get_JSON_request('add_campaign')
    response = make_request(url=URL.edit_campaign, data=payload)
    assert response.status_code == 200
    campaign_id = response.json()['id']
    yield response.json()
    response = requests.delete(url=URL.delete_campaign, params = {'id':campaign_id}, headers = URL.headers)
    assert response.status_code == 200


class Tests_add_campaign_settings:
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
    def test_add_campaign_without_any_groups(self, make_request):
        payload = _.get_JSON_request('add_campaign', **{'groups': None})
        response = make_request(url=URL.edit_campaign, data=payload)
        answer = {'SCM_VALIDATION_CAMPAIGN_GROUPS': 'Can not add or edit Campaign without any Group'}
        assert response.status_code == 400
        assert response.json() == answer

    #Нет валидации на не существующую группу
    @pytest.mark.xfail
    @allure.feature('Негативный тест')
    @allure.story('Добавляем кампанию с не существующй групой')
    def test_add_campaign_with_unknown_group(self, make_request):
        payload = _.get_JSON_request('add_campaign', **{'groups': [{"id":99999999999}]})
        response = make_request(url=URL.edit_campaign, data=payload)
        answer = {'SCM_VALIDATION_CAMPAIGN_GROUPS': 'No such group'}
        print(response.json())
        assert response.status_code == 500
        assert response.json() == answer



    # @allure.feature('Негативный тест')
    # @allure.story('Добавляем кампанию с существующей скилгрупой')
    # def test_add_campaign_with_existing_skillgroup(self, add_campaign, make_request):
    #     payload = _.get_JSON_request('add_campaign')
    #     response = make_request(url=URL.edit_campaign, data=payload)
    #     answer = {'SCM_DIALER_EXCEPTION': "DialerException: ApiException{errors=[\n{errorData='skillGroup', errorMessage='Each Skill Group can only be assigned to one Campaign.'}]}"}
    #     assert response.status_code == 500
    #     assert response.json() == answer
    #
    # @pytest.mark.xfail
    # @allure.feature('Негативный тест')
    # @allure.story('Добавляем кампанию с существующим кодом')
    # def test_add_campaign_with_existing_code(self, add_campaign, make_request):
    #     campaign_code = add_campaign['code']
    #     payload = _.get_JSON_request('add_campaign', **{'code':campaign_code})
    #     response = make_request(url=URL.edit_campaign, data=payload)
    #     answer = {"SCM_ENTITY_WITH_SUCH_FIELD_EXISTS":"SCMEntityWithSuchFieldExists: CODE"}
    #     assert response.status_code == 500
    #     assert response.json() == answer
    #
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Добавляем кампанию с удаленным кодом')
    # def test_add_campaign_with_deleted_code(self,  make_request):
    #     payload = _.get_JSON_request('add_campaign', **{'code': 'deleted_code'})
    #     response = make_request(url=URL.edit_campaign, data=payload)
    #     print(response.json())
    #     answer = "errorData='name', errorMessage='A deleted item exists with the specified value.  The names of deleted items cannot be reused unless they are permanently deleted via the Deleted Objects tool.'"
    #     assert response.status_code == 500
    #     assert answer in response.json()['SCM_DIALER_EXCEPTION']
    #
    #
    #
    # @allure.feature('Позитивный тест')
    # @allure.story('Получаем список кампаний')
    # def test_get_campaign(self,  add_campaign, make_request):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     code = add_campaign['code']
    #     data = {}
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.get_campaign, data=data)
    #     answer = [{'id': campaign_id, 'code': code, 'name': 'auto_test_campaign', 'comment': 'auto_test', 'deleted': False, 'groups': [{'id': 2}]}]
    #     assert response.status_code == 200
    #     assert answer == response.json()
    #
    # @allure.feature('Позитивный тест')
    # @allure.story('Получаем result_code кампаний')
    # def test_get_result_code(self, add_campaign, make_request):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     data = {"campaignId":campaign_id}
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.get_result_code, data=data)
    #     assert response.status_code == 200
    #     result = ['SUCCESS', "CD_callResult", "CD_callStatus", 'CD_callsMade']
    #     answer = []
    #     for i in response.json():
    #         answer.append(i['code'])
    #     assert answer == result
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Получаем result_code не существующей кампаний')
    # @pytest.mark.xfail
    # def test_get_result_code_for_unknown_company(self, add_campaign, make_request):
    #     # Подготавливаем данные в JSON для запроса
    #     data = {"campaignId": 999999999999999999}
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.get_result_code, data=data)
    #     print(response.text)
    #     assert response.status_code == 400
    #
    # @allure.feature('Позитивный тест')
    # @allure.story('Добавляем код результата')
    # @pytest.mark.parametrize('dataType', ['INTEGER', 'FLOAT', 'STRING', 'TEXT', 'DATE'])
    # @pytest.mark.parametrize('code', [ 123123123, 1232.22, 'string'])
    # def test_add_result_codes(self, add_campaign, make_request, delete_result_code, dataType, code):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #
    #     data = _.get_JSON_request('add_result_code',**{"campaign":{"id":campaign_id},
    #                                               "dataType": dataType,
    #                                                    'code': code})
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_result_code, data=data)
    #     result_code_id = response.json()['id']
    #     delete_result_code['id']=result_code_id
    #     answer = _.get_JSON_response('add_result_code', **{'id':result_code_id,
    #                                                        'dataType':dataType,
    #                                                        'code':str(code)})
    #     assert response.status_code == 200
    #     assert answer == response.json()
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Добавляем код результата с строкой 256 символов')
    # @pytest.mark.parametrize('dataType', ['INTEGER', 'FLOAT', 'STRING', 'TEXT', 'DATE'])
    # def test_add_result_codes_with_256(self, add_campaign, make_request,  dataType):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
    #                                                     "dataType": dataType,
    #                                                     'code': "q"*256,
    #                                                     'name':'q'*256})
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_result_code, data=data)
    #     answer ={ "SCM_VALIDATION_OVERALL_NAME_LENGTH": "Name is to long, max length = 255 characters",
    #               "SCM_VALIDATION_OVERALL_CODE_LENGTH": "Code is to long, max length = 255 characters"}
    #     assert response.status_code == 400
    #     assert answer == response.json()
    #
    #
    # @allure.feature('Позитивный тест')
    # @allure.story('Добавляем варианты значений для кодов результатов')
    # @pytest.mark.parametrize(('dataType','value'), [('INTEGER', 123321), ('FLOAT', 123.25), ('STRING','string'), ('TEXT', 'some_text'), ('DATE',132213123213)])
    # def test_add_result_variants(self, add_campaign, make_request, delete_result_code, dataType, value):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     campaign_code = add_campaign['code']
    #     data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
    #                                                     "dataType": dataType})
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_result_code, data=data)
    #     result_code_id = response.json()['id']
    #     delete_result_code['id'] = result_code_id
    #     assert response.status_code == 200
    #     data = _.get_JSON_request('edit_result_variant', **{"campaignCode":campaign_code,
    #                                                         "resultVariant":{"value":value,"forInit":False}})
    #     response = make_request(url=URL.edit_result_variant, data=data)
    #     assert response.status_code == 200
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Добавляем не валидные варианты значений для кодов результатов')
    # @pytest.mark.parametrize(('dataType', 'value'),
    #                          [('INTEGER', "string"), ('FLOAT', "string"), ('DATE', "string")])
    # def test_add_incorrect_result_variants(self, add_campaign, make_request, delete_result_code, dataType, value):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     campaign_code = add_campaign['code']
    #     data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
    #                                                     "dataType": dataType})
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_result_code, data=data)
    #     result_code_id = response.json()['id']
    #     delete_result_code['id'] = result_code_id
    #     assert response.status_code == 200
    #     data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
    #                                                         "resultVariant": {"value": value, "forInit": False}})
    #     response = make_request(url=URL.edit_result_variant, data=data)
    #     answer = {"SCM_EDIT_RESULT_VARIANT_EXCEPTION":"SCMEditResultVariantException: Wrong result variant format for dataType '%s'"%dataType}
    #     assert response.status_code == 500
    #     assert answer == response.json()
    #
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Добавляем варианты значений с однаковыми результатами')
    # @pytest.mark.parametrize(('dataType', 'value'),
    #                          [('INTEGER', 123321), ('FLOAT', 123.25), ('STRING', 'string'), ('TEXT', 'some_text'),
    #                           ('DATE', 132213123213)])
    # def test_add_result_variant_with_existing_variant(self, add_campaign, make_request, delete_result_code, dataType, value):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     campaign_code = add_campaign['code']
    #     data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
    #                                                     "dataType": dataType})
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_result_code, data=data)
    #     result_code_id = response.json()['id']
    #     delete_result_code['id'] = result_code_id
    #     assert response.status_code == 200
    #     data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
    #                                                         "resultVariant": {"value": value, "forInit": False}})
    #     response = make_request(url=URL.edit_result_variant, data=data)
    #     assert response.status_code == 200
    #     data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
    #                                                         "resultVariant": {"value": value, "forInit": False}})
    #     response = make_request(url=URL.edit_result_variant, data=data)
    #     answer = {'SCM_ENTITY_WITH_SUCH_FIELD_EXISTS': 'SCMEntityWithSuchFieldExists: ResultVariant with such field exists: VALUE'}
    #     assert response.status_code == 500
    #     assert answer == response.json()
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Добавляем 2 значения forInit=True')
    # @pytest.mark.parametrize(('dataType', 'value'),
    #                          [('INTEGER', 123321), ('FLOAT', 123.25), ('STRING', 'string'), ('TEXT', 'some_text'),
    #                           ('DATE', 132213123213)])
    # def test_add_result_variant_withforInit_true(self, add_campaign, make_request, delete_result_code, dataType, value):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     campaign_code = add_campaign['code']
    #     data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
    #                                                     "dataType": dataType})
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_result_code, data=data)
    #     result_code_id = response.json()['id']
    #     delete_result_code['id'] = result_code_id
    #     assert response.status_code == 200
    #     data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
    #                                                         "resultVariant": {"value": value, "forInit": True}})
    #     response = make_request(url=URL.edit_result_variant, data=data)
    #     assert response.status_code == 200
    #     data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
    #                                                         "resultVariant": {"value": 99999999, "forInit": True}})
    #     response = make_request(url=URL.edit_result_variant, data=data)
    #     answer = {
    #         "SCM_EDIT_RESULT_VARIANT_EXCEPTION": "SCMEditResultVariantException: Unable to add forInit result variant='99999999' because forInit result variant already exists"}
    #     assert response.status_code == 500
    #     assert answer == response.json()
    #
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Добавляем варианты значения для кодов результатов с неизвесным "resultCode"')
    # @pytest.mark.parametrize(('dataType', 'value'),[('STRING', 'string')])
    # def test_add_result_variants_with_unknown_resultCode(self, add_campaign, make_request, delete_result_code, dataType, value):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     campaign_code = add_campaign['code']
    #     data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
    #                                                     "dataType": dataType})
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.edit_result_code, data=data)
    #     result_code_id = response.json()['id']
    #     delete_result_code['id'] = result_code_id
    #     assert response.status_code == 200
    #     data = _.get_JSON_request('edit_result_variant', **{"campaignCode": campaign_code,
    #                                                         "resultCode":"UNKNOWN_result_code",
    #                                                         "resultVariant": {"value": value, "forInit": False}})
    #     response = make_request(url=URL.edit_result_variant, data=data)
    #     answer = {'SCM_REQUESTED_RESOURCE_NOT_FOUND': "SCMRequestedResourceNotFoundException: Unable to find result code 'UNKNOWN_result_code' for campaign '%s'"%campaign_code}
    #     assert response.status_code == 500
    #     assert response.json() == answer
    #
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Пытаемся удалить стандартные значения кодов результатов(от дайлера)')
    # @pytest.mark.parametrize('dialer_result_code', ['CD_callStatus', 'CD_callMade', 'CD_callResult'])
    # def test_delete_dialer_results(self, add_campaign, make_request, dialer_result_code):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id = add_campaign['id']
    #     data = {"campaignId": campaign_id}
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.get_result_code, data=data)
    #     assert response.status_code == 200
    #     for i in response.json():
    #         if i['code']== dialer_result_code:
    #             response = requests.delete(url=URL.remove_result_code, params = {'id':i['id']}, headers = URL.headers)
    #             answer  ={"SCM_DELETE_RESULT_CODE_EXCEPTION":"SCMDeleteResultCodeException: Unable to delete CISCO dialer result code '%s'"%dialer_result_code}
    #             assert response.status_code == 500
    #             assert response.json() == answer
    #
    #
    # @allure.feature('Негативный тест')
    # @allure.story('Пытаемся удалить стандартные варианты значений кодов результатов(от дайлера)')
    # @pytest.mark.parametrize('dialer_result_code', ['CD_callStatus', 'CD_callResult'])
    # def test_delete_dialer_results_variants(self, add_campaign, make_request, dialer_result_code):
    #     # Подготавливаем данные в JSON для запроса
    #     campaign_id, campaign_code = add_campaign['id'], add_campaign['code']
    #     # Делаем запрос и получаем ответ
    #     response = make_request(url=URL.get_result_code, data={"campaignId": campaign_id})
    #     assert response.status_code == 200
    #     for i in response.json():
    #         if i['code']== dialer_result_code:
    #                 for j in i['resultVariants']:
    #                     params = {'id':j['id'], 'campaignCode':campaign_code, 'resultCode':dialer_result_code}
    #                     response = requests.delete(url=URL.remove_result_variant, params = params, headers = URL.headers)
    #                     answer  ={"SCM_DELETE_RESULT_VARIANT_EXCEPTION":"SCMDeleteResultVariantException: Unable to delete CISCO dialer result variant for result code '%s'"%dialer_result_code}
    #                     assert response.status_code == 500
    #                     assert response.json() == answer
