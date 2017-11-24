import pytest, allure, json, requests, random


from Data.Make_requests_and_answers import make_test_data
from Data.Make_requests_and_answers import random_string
from Data.URLs_MAP import sesl_integration,sesl_mapfield, sesl_tag



@pytest.fixture(scope="function")
def add_one_integration(send_request):
    data = make_test_data('post_integration', data={'$name': random_string(),
                                                    '$url': random_string(),
                                                    '$login': random_string(),
                                                    '$password': None})
    response = send_request(url=sesl_integration, data=data['request'])
    yield response.json()
    send_request(method = "DELETE", url=sesl_integration, params={'id':response.json()['id']})




@pytest.fixture(scope="function")
def add_two_integrations(send_request):
    results = []
    for i in range(2):
        data = make_test_data('post_integration', data={'$name': random_string(),
                                                        '$url': random_string(),
                                                        '$login': random_string(),
                                                        '$password': None})
        response = send_request(url=sesl_integration, data=data['request'])
        results.append(response.json())
    yield iter(results)
    for result in results:
        send_request(method = "DELETE", url=sesl_integration, params={'id':result['id']})



@pytest.fixture(scope="function")
def add_two_maps(send_request, add_one_integration):
    exitsting_integration = add_one_integration
    result = []
    position = 1
    for i in range(2):
        data = make_test_data("post_mapfield", {"$databaseColumn":random_string(),
                                                        "$title":random_string(),
                                                        "$position":str(position),
                                                        "$integrationId":exitsting_integration['id']})
        position+=1
        response = send_request(sesl_mapfield, data['request'])
        result.append(response.json())
    yield iter(result)

@pytest.fixture(scope="function")
def add_one_map(send_request, add_one_integration):
    exitsting_integration = add_one_integration
    data = make_test_data("post_mapfield", {"$databaseColumn": random_string(),
                                            "$title": random_string(),
                                            "$position": 1,
                                            "$integrationId": exitsting_integration['id']})
    response = send_request(sesl_mapfield, data['request'])
    return response.json()

@pytest.fixture(scope="function")
def add_integration_with_password(send_request, clear_result):
    data = make_test_data('post_integration', data={'$name': random_string(),
                                                    '$url': random_string(),
                                                    '$login': random_string(),
                                                    '$password': random_string()})
    response = send_request(url=sesl_integration, data=data['request'])
    yield response.json()
    clear_result['url'], clear_result['id'] = sesl_integration, response.json()['id']


@pytest.fixture(scope="function")
def add_one_tag(send_request, add_one_integration):
    integrationId = add_one_integration['id']
    data = make_test_data("post_tag", {"$tag":random_string(),
                                       "$integrationId":integrationId,
                                       "$position": "1"})
    response = send_request(sesl_tag, data['request'])
    yield response.json()
    send_request(method = "DELETE", url = sesl_tag, params = {'id':response.json()['id']})



@pytest.fixture(scope="function")
def add_two_tags(send_request, add_one_integration):
    results = []
    position = 1
    for i in range(2):
        integrationId = add_one_integration['id']
        data = make_test_data("post_tag", {"$tag":random_string(),
                                           "$integrationId":integrationId,
                                           "$position": str(position)})
        response = send_request(sesl_tag, data['request'])
        position+=1
        results.append(response.json())
    yield iter(results)
    for result in results:
        send_request(method = "DELETE", url = sesl_tag, params = {'id':result['id']})