import pytest, allure, json, requests, random


from Data.Make_requests_and_answers import make_test_data
from Data.Make_requests_and_answers import equal_schema
from Data.Make_requests_and_answers import random_string
from Data.URLs_MAP import sesl_integration,sesl_mapfield



@pytest.fixture(scope="function")
def add_integration(send_request, clear_result):
    results = []
    for i in range(2):
        data = make_test_data('post_integration', data={'$name': random_string(),
                                                        '$url': random_string(),
                                                        '$login': random_string(),
                                                        '$password': random_string(),
                                                        '$position': 1})
        response = send_request(url=sesl_integration, data=data['request'])
        results.append(response.json())

    yield iter(results)
    clear_result['url'] = sesl_integration
    clear_result['id'] = [results[0]['id'], results[1]['id']]

@pytest.fixture(scope="function")
def add_mapping(send_request, add_integration):
    exitsting_integration = next(add_integration)
    result = []
    for i in range(2):
        data = make_test_data("post_mapfield", {"$databaseColumn":random_string(),
                                                        "$title":random_string(),
                                                        "$position":1,
                                                        "$integrationId":exitsting_integration['id']})
        response = send_request(sesl_mapfield, data['request'])
        result.append(response.json())
    yield iter(result)