import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _


class Test_Routes:

    @pytest.fixture(scope="function")
    def add_route(self, make_request, clear_result):
        url = URL.route
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"agentNumber": "1155",
                                                  "clientPhone": "0666816655"})
        # Делаем запрос и получаем ответ
        response = make_request(url=url, data=data)
        assert response.status_code == 200
        route_response = response.json()['id']
        yield route_response
        clear_result['url'], clear_result['id'] = url, route_response['id']


    @allure.feature('Позитивный тест')
    @allure.story('Добавляем новый роут с валидными данными')
    def test_add_route(self, make_request, clear_result):
        url = URL.route
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
                                                  "clientPhone": "0666816657"})
        # Делаем запрос и получаем ответ
        response = make_request(url=url, data=data)
        route_id = response.json()['id']
        answer = _.get_JSON_response('add_route', **{'id': route_id,
                                                     "agentNumber": "1111",
                                                     "clientPhone": "0666816657"})
        clear_result['url'], clear_result['id'] = url, route_id
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый роут с не существующим agentNumber')
    @pytest.mark.xfail
    def test_add_route_with_unknown_agentNumber(self, make_request):
        url = URL.route
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"agentNumber": "9999999999",
                                                  "clientPhone": "0666816657"})
        # Делаем запрос и получаем ответ
        response = make_request(url=url, data=data)
        answer = ['No such agentNumber']
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый роут с существующим clientPhone')
    def test_add_route_with_existing_clientPhone(self, add_route, make_request):
        url = URL.route
        exist_phone = add_route['clientPhone']
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
                                                  "clientPhone": exist_phone})
        # Делаем запрос и получаем ответ
        response = make_request(url=url, data=data)
        answer = {"CALL_CREATE_EXCEPTION": "CallCreateException: Unable to add new route cause route for this client number already exist."}
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Позитивный тест')
    @allure.story('Удаляем существующий роут')
    def test_delete_route(self, add_route):
        url = URL.route
        params = {'id':add_route['id']}
        # Делаем запрос и получаем ответ
        response = requests.delete(url=url, params = params, headers = URL.headers)
        answer = add_route
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Удаляем не существующий роут')
    def test_delete_rout_with_unknown_id(self):
        url = URL.route
        # Делаем запрос и получаем ответ
        response = requests.delete(url=url, params = {'id':999999999}, headers = URL.headers)
        answer = {"CALL_NOT_FOUND_EXCEPTION": "CallNotFoundException: Unable to find call with id=999999999"}
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Позитивный тест')
    @allure.story('Обновляем ранее созданный роут')
    def test_put_route_agentNumber_clientPhone_callDate(self, add_route, make_request):
        url = URL.route
        # Делаем запрос и получаем ответ
        data = _.generate_JSON(add_route, {"agentNumber": "1111",
                                           "clientPhone": "0666666666",
                                           "callDate": 1500292769604})
        response = make_request(method = "PUT", url=url, data=data)
        answer = _.generate_JSON(add_route, {"agentNumber": "1111",
                                             "clientPhone": "0666666666"})
        assert response.status_code == 200
        assert answer == response.json()


    @allure.feature('Негативный тест')
    @allure.story('Обновляем роут с неизвесным ID')
    def test_put_rouet_with_unknown_id(self, add_route, make_request):
        url = URL.route
        # Делаем запрос и получаем ответ
        data = _.generate_JSON(add_route, {"id": 999999999,
                                           "clientPhone": "0666666666"})
        response = make_request(method = "PUT", url=url, data=data)
        answer = {"CALL_NOT_FOUND_EXCEPTION": "CallNotFoundException: Unable to find call with id=999999999"}
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Негативный тест')
    @allure.story('Редактируем clientPhone на уже существующий')
    def test_put_route_clientPhone_agentNumber_on_existing(self,add_route, make_request, clear_result):
        url = URL.route
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
                                                  "clientPhone": "0666816657"})
        # Делаем запрос и получаем ответ
        response = make_request(url=url, data=data)
        assert response.status_code == 200
        route_id = response.json()['id']
        clear_result['url'], clear_result['id'] = url, route_id
        # Изменяем созданный перед тестом route(agentNumber and clientPhone)на существующий(тот что в созданный в тесте)
        data = _.generate_JSON(add_route, {"agentNumber": "1111",
                                           "clientPhone": "0666816657"})
        response = make_request(method="PUT", url=url, data=data)
        answer = {"CALL_UPDATE_EXCEPTION": "CallUpdateException: Unable to edit agentNumber, clientPhone cause they are already exist."}
        assert response.status_code == 500
        assert answer == response.json()


class Test_Settings:


    @allure.feature('Позитивный тест')
    @allure.story('Получаем манифест')
    def test_manifest(self, make_request):
        response = make_request(method = "GET", url=URL.scb_manifest)
        answer = _.get_JSON_response('scb_manifest')
        assert response.status_code == 200
        assert response.json().keys()== answer.keys()


    @allure.feature('Позитивный тест')
    @allure.story('Получаем информацию о лицензиях')
    def test_licenses(self, make_request):
        response = make_request(method = "GET", url=URL.scb_licenses)
        answer = _.get_JSON_response('scb_licenses')
        assert response.status_code == 200
        assert response.json().keys()== answer.keys()


    @allure.feature('Позитивный тест')
    @allure.story('Получаем информацию о количестве лицензий')
    def test_count(self, make_request):
        response = make_request(method = "GET", url=URL.scb_count)
        assert response.status_code == 200


    @allure.feature('Позитивный тест')
    @allure.story('Получаем настройки')
    def test_settings(self, make_request):
        response = make_request(method="GET", url=URL.scb_settings)
        answer = _.get_JSON_response('scb_settings')
        assert response.status_code == 200
        assert response.json().keys() == answer.keys()
