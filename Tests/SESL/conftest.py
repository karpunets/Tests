import pytest

from Data.URLs_MAP import sesl_integration, sesl_mapfield, sesl_tag
from bin.Make_requests_and_answers import parse_request
from bin.Make_requests_and_answers import random_string


@pytest.fixture(scope="function")
def add_one_integration(send_request):
    data = parse_request('integration', method ="POST", data={'$name': random_string(),
                                                    '$url': random_string(),
                                                    '$login': random_string(),
                                                    '$password': None})
    response = send_request(url=sesl_integration, data=data['request_body'])
    to_return = response.json()
    to_return['integrationId'] = response.json()['id']
    yield to_return
    send_request(method = "DELETE", url=sesl_integration, params={'id':response.json()['id']})




@pytest.fixture(scope="function")
def add_two_integrations(send_request):
    results = []
    for i in range(2):
        data = parse_request('integration', method ="POST", data={'$name': random_string(),
                                                        '$url': random_string(),
                                                        '$login': random_string(),
                                                        '$password': None})
        response = send_request(url=sesl_integration, data=data['request_body'])
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
        data = parse_request("mapfield", method ="POST", data = {"$databaseColumn":random_string(),
                                                        "$title":random_string(),
                                                        "$position":str(position),
                                                        "$integrationId":exitsting_integration['id']})
        position+=1
        response = send_request(sesl_mapfield, data['request_body'])
        result.append(response.json())
    yield iter(result)

@pytest.fixture(scope="function")
def add_one_map(send_request, add_one_integration):
    exitsting_integration = add_one_integration
    data = parse_request("mapfield", method="POST", data = {"$databaseColumn": random_string(),
                                            "$title": random_string(),
                                            "$position": 1,
                                            "$integrationId": exitsting_integration['id']})
    response = send_request(sesl_mapfield, data['request_body'])
    return response.json()

@pytest.fixture(scope="function")
def add_integration_with_password(send_request, clear_result):
    data = parse_request('integration', data={'$name': random_string(),
                                                    '$url': random_string(),
                                                    '$login': random_string(),
                                                    '$password': random_string()})
    response = send_request(url=sesl_integration, data=data['request_body'])
    yield response.json()
    clear_result['url'], clear_result['id'] = sesl_integration, response.json()['id']


@pytest.fixture(scope="function")
def add_one_tag(send_request, add_one_integration):
    integrationId = add_one_integration['id']
    data = parse_request("tag", method ="POST", data={"$tag":random_string(),
                                       "$integrationId":integrationId,
                                       "$position": "1"})
    response = send_request(sesl_tag, data['request_body'])
    yield response.json()
    send_request(method = "DELETE", url = sesl_tag, params = {'id':response.json()['id']})



@pytest.fixture(scope="function")
def add_two_tags(send_request, add_one_integration):
    results = []
    position = 1
    for i in range(2):
        integrationId = add_one_integration['id']
        data = parse_request("tag", {"$tag":random_string(),
                                           "$integrationId":integrationId,
                                           "$position": str(position)})
        response = send_request(sesl_tag, data['request_body'])
        position+=1
        results.append(response.json())
    yield iter(results)
    for result in results:
        send_request(method = "DELETE", url = sesl_tag, params = {'id':result['id']})