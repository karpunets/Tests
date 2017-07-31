import json, pytest, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator as _
import Data.Test_data as get

headers = URL.headers


@pytest.fixture(scope='module')
def clear_contact(make_request):
    url = URL.scb_contact
    #Получаем все что есть в справочнику
    response = make_request(method = "GET", url=url)
    for i in response.json():
        to_delete = {'id': i['id']}
        make_request(method = 'DELETE', url=url, params=to_delete)

@pytest.fixture(scope='module')
def clear_routes(make_request):
    url = URL.route
    response = make_request(url = url, method = "GET", params = {'page_number':1, 'page_size':100})
    for i in response.json()['data']:
        to_delete = {"id":int(i['id'])}
        make_request(url=url, method="DELETE", params = to_delete )

@pytest.fixture(scope="class")
def credential(make_request):
    url = URL.scb_credentials
    credential = get.credentials
    response = make_request(url=url, data = credential)
    yield response.json()
    to_delete = {'id':response.json()['id']}
    make_request(method = 'DELETE', url=url, params = to_delete)

@pytest.fixture(scope="function")
def add_route(make_request, clear_result):
    url = URL.route
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request('add_route', **{"agentNumber": "1022",
                                              "clientPhone": "0666816655"})
    # Делаем запрос и получаем ответ
    response = make_request(url=url, data=data)
    assert response.status_code == 200
    route_response = response.json()
    clear_result['id'] = []
    yield route_response
    clear_result['url'] = url
    clear_result['id'].append(route_response['id'])

@pytest.fixture(scope="function")
def add_contact(make_request, clear_result):
    url = URL.scb_contact
    payload = _.get_JSON_request('add_contact', **get.add_contact)
    response = make_request(url=url, data=payload)
    assert response.status_code == 200
    yield response.json()
    clear_result['url'], clear_result['id'] = url, response.json()['id']


@pytest.fixture(scope='function')
def add_credential(make_request, clear_result):
        url = URL.scb_credentials
        credential = get.credentials
        response = make_request(url=url, data=credential)
        credential_id = response.json()['id']
        yield response.json()
        clear_result['url'], clear_result['id'] = url, credential_id