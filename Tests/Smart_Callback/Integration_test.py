import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _


@allure.feature('Позитивный тест')
@allure.story('Добавляем новый роут с credentials')
def test_add_route_with_credential(make_request, credential, clear_result):
    url = URL.route
    data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
                                              "clientPhone": "0666816111"})
    response = make_request(url=url, data=data)
    route_id = response.json()['id']
    answer = _.get_JSON_response('add_route', **{'id': route_id,
                                                 "agentNumber": "1111",
                                                 "clientPhone": "0666816111"})
    clear_result['url'], clear_result['id'] = url, route_id
    assert response.status_code == 200
    assert answer == response.json()
    clear_result['id'], clear_result['url'] = response.json()['id'], url


@allure.feature('Негативный тест')
@allure.story('Добавляем новый роут без credentials')
@pytest.mark.xfail
def test_add_route_without_credentials(make_request):
    url = URL.route
    data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
                                              "clientPhone": "0666816111"})
    response = make_request(url=url, data=data)
    assert response.json() == 500

