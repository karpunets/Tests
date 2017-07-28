import json, pytest, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator
from Data.Requests_default_map import defaul_request
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


