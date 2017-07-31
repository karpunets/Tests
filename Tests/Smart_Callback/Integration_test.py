import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _


def test_add_route_with_credential(make_request, credential, clear_result):
    url = URL.route
    data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
                                              "clientPhone": "0666816111"})
    response = make_request(url=url, data=data)
    clear_result['id'], clear_result['url'] = response.json()['id'], url
    assert response.status_code == 200