import pytest, allure, json, requests, random, os
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _



@pytest.fixture(scope='function')
def create_txt_file():
    file = open("for_test.txt", "w+")
    for i in range(random.randint(1, 50)):
        file.write(str(random.randint(100, 999999999999)) + ',')
    file.close()
    yield  file.name
    os.remove("for_test.txt")

@pytest.fixture(scope='function')
def delete_results():
    prefix = {}
    yield prefix
    requests.delete(url=URL.proxy_prefix, headers = URL.headers, params = prefix)

# @allure.feature('Позитивный тест')
# @allure.story('Добавляем новый роут с валидными данными')
# def test_add_phones_with_prefix(self, make_request, delete_results):

# def test_qq(create_txt_file, delete_results):
#     prefix = '066'
#     files = {'file':open('for_test.txt', 'rb')}
#     params = {'prefix':prefix, 'default':False}
#     response = requests.post(url=URL.proxy_prefix,  params = params, files=files, auth = URL.authorization)
#     delete_results['prefix'] = prefix
#     print(response.status_code)
#     print(response.json())
#     assert response.status_code == 200


def test_get_licenses(make_request):
    url=URL.proxy_licenses
    response = make_request(method='GET', url=url)
    print(response.json())
    assert response.status_code == 200