import json, pytest, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator as _
import Data.Test_data as get

headers = URL.headers


@pytest.fixture(scope='module')
def clear_contact(send_request):
    url = URL.scb_contact
    #Получаем все что есть в справочнику
    response = send_request(method = "GET", url=url)
    for i in response.json():
        to_delete = {'id': i['id']}
        send_request(method = 'DELETE', url=url, params=to_delete)

@pytest.fixture(scope='module')
def clear_routes(send_request):
    url = URL.fixed_routes
    response = send_request(url = url, method = "GET", params = {'page_number':1, 'page_size':100})
    for i in response.json()['data']:
        to_delete = {"id":int(i['id'])}
        send_request(url=url, method="DELETE", params = to_delete )

@pytest.fixture(scope='class')
def clear_credentials(send_request):
    url = URL.scb_credentials
    response = send_request(url = url, method = "GET")
    for i in response.json():
        to_delete = {"id":int(i['id'])}
        send_request(url=url, method="DELETE", params = to_delete )

@pytest.fixture(scope="class")
def credential(send_request):
    url = URL.scb_credentials
    credential = get.credentials
    response = send_request(url=url, data = credential)
    yield response.json()
    to_delete = {'id':response.json()['id']}
    send_request(method = 'DELETE', url=url, params = to_delete)

@pytest.fixture(scope="function")
def add_route(send_request, clear_result):
    url = URL.fixed_routes
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request('add_route', **{"internalNumber": "1022",
                                              "externalNumber": "0666816655"})
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data=data)
    assert response.status_code == 200
    route_response = response.json()
    clear_result['id'] = []
    yield route_response
    clear_result['url'] = url
    clear_result['id'].append(route_response['id'])

@pytest.fixture(scope="function")
def add_contact(send_request, clear_result):
    url = URL.scb_contact
    payload = _.get_JSON_request('add_contact', **get.add_contact)
    response = send_request(url=url, data=payload)
    assert response.status_code == 200
    yield response.json()
    clear_result['url'], clear_result['id'] = url, response.json()['id']


@pytest.fixture(scope='function')
def add_credential(send_request, clear_result):
        url = URL.scb_credentials
        credential = get.credentials
        response = send_request(url=url, data=credential)
        credential_id = response.json()['id']
        yield response.json()
        clear_result['url'], clear_result['id'] = url, credential_id