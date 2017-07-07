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
    yield campaign_id
    response = requests.delete(url=URL.delete_campaign, data = campaign_id)




class Test_add_campaign:


    @allure.feature('Позитивный тест')
    @allure.story('Получаем список кампаний')
    def test_get_campaign(self, make_request, add_campaign):
        # Подготавливаем данные в JSON для запроса
        data = {}
        # Делаем запрос и получаем ответ
        response = make_request(url=URL.get_campaign, data=data)
        print(response.json())

        assert response.status_code == 200
        # assert answer == response.json()