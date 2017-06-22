import pytest, allure, json, requests
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _


@allure.feature('Позитивный тест')
@allure.story('Получаем логи')
def test_get_logs(make_request):
    name ="Manager_logs"
    data = _.get_JSON_request(name)
    response = make_request(url=URL.Manager_logs, data = data)
    assert response.status_code == 200
