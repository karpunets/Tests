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

@pytest.fixture(scope='function')
def delete_result_code():
    result_codes_id = {}
    yield result_codes_id
    response = requests.delete(url=URL.remove_result_code, params = result_codes_id, headers = URL.headers)
    assert response.status_code == 200


class Tests_add_campaign_settings:

    @allure.feature('Позитивный тест')
    @allure.story('Получаем список кампаний')
    def test_get_campaign(self,  add_campaign, make_request):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        code = add_campaign['code']
        data = {}
        # Делаем запрос и получаем ответ
        response = make_request(url=URL.get_campaign, data=data)
        answer = [{'id': campaign_id, 'code': code, 'name': 'auto_test_campaign', 'comment': 'auto_test', 'deleted': False, 'groups': [{'id': 2}]}]
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Позитивный тест')
    @allure.story('Получаем result_code кампаний')
    def test_get_result_code(self, add_campaign, make_request):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']
        data = {"campaignId":campaign_id}
        # Делаем запрос и получаем ответ
        response = make_request(url=URL.get_result_code, data=data)
        assert response.status_code == 200
        result = ['SUCCESS', "CD_callResult", "CD_callStatus", 'CD_callsMade']
        answer = []
        for i in response.json():
            answer.append(i['code'])
        assert answer == result

    @allure.feature('Негативный тест')
    @allure.story('Получаем result_code не существующей кампаний')
    @pytest.mark.xfail
    def test_get_result_code_for_unknown_company(self, add_campaign, make_request):
        # Подготавливаем данные в JSON для запроса
        data = {"campaignId": 999999999999999999}
        # Делаем запрос и получаем ответ
        response = make_request(url=URL.get_result_code, data=data)
        print(response.text)
        assert response.status_code == 400

    @allure.feature('Позитивный тест')
    @allure.story('Добавляем код результата')
    @pytest.mark.parametrize(('dataType', 'code'), [('INTEGER', 123123123), ('FLOAT', 1232.22), ('STRING', 'string'), ('TEXT', 'texttexttext'), ('DATE', '123123132132')])
    def test_add_result_codes(self, add_campaign, make_request, delete_result_code, dataType, code):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']

        data = _.get_JSON_request('add_result_code',**{"campaign":{"id":campaign_id},
                                                  "dataType": dataType,
                                                       'code': code})
        # Делаем запрос и получаем ответ
        response = make_request(url=URL.edit_result_code, data=data)
        result_code_id = response.json()['id']
        delete_result_code['id']=result_code_id
        answer = _.get_JSON_response('add_result_code', **{'id':result_code_id,
                                                           'dataType':dataType,
                                                           'code':str(code)})
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем код результата')
    @pytest.mark.parametrize(('dataType', 'code'), [('INTEGER', 123123123), ('FLOAT', 1232.22), ('STRING', 'string'),
                                                    ('TEXT', 'texttexttext'), ('DATE', '123123132132')])
    def test_add_invalid_result_codes(self, add_campaign, make_request, delete_result_code, dataType, code):
        # Подготавливаем данные в JSON для запроса
        campaign_id = add_campaign['id']

        data = _.get_JSON_request('add_result_code', **{"campaign": {"id": campaign_id},
                                                        "dataType": dataType,
                                                        'code': code})
        # Делаем запрос и получаем ответ
        response = make_request(url=URL.edit_result_code, data=data)
        result_code_id = response.json()['id']
        delete_result_code['id'] = result_code_id
        answer = _.get_JSON_response('add_result_code', **{'id': result_code_id,
                                                           'dataType': dataType,
                                                           'code': str(code)})
        assert response.status_code == 200
        assert answer == response.json()
