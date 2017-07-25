import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _


# class Test_Routes:
#
#     @pytest.fixture(scope="function")
#     def add_route(self, make_request, clear_result):
#         url = URL.route
#         # Подготавливаем данные в JSON для запроса
#         data = _.get_JSON_request('add_route', **{"agentNumber": "1022",
#                                                   "clientPhone": "0666816655"})
#         # Делаем запрос и получаем ответ
#         response = make_request(url=url, data=data)
#         assert response.status_code == 200
#         route_response = response.json()
#         clear_result['id'] = []
#         yield route_response
#         clear_result['url']= url
#         clear_result['id'].append(route_response['id'])
#
#
#
#     @allure.feature('Позитивный тест')
#     @allure.story('Добавляем новый роут с валидными данными')
#     def test_add_route(self, make_request, clear_result):
#         url = URL.route
#         # Подготавливаем данные в JSON для запроса
#         data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
#                                                   "clientPhone": "0666816657"})
#         # Делаем запрос и получаем ответ
#         response = make_request(url=url, data=data)
#         route_id = response.json()['id']
#         answer = _.get_JSON_response('add_route', **{'id': route_id,
#                                                      "agentNumber": "1111",
#                                                      "clientPhone": "0666816657"})
#         clear_result['url'], clear_result['id'] = url, route_id
#         assert response.status_code == 200
#         assert answer == response.json()
#
#     @allure.feature('Негативный тест')
#     @allure.story('Добавляем новый роут с не существующим agentNumber')
#     def test_add_route_with_unknown_agentNumber(self, make_request):
#         url = URL.route
#         # Подготавливаем данные в JSON для запроса
#         data = _.get_JSON_request('add_route', **{"agentNumber": "9999999999",
#                                                   "clientPhone": "0666816657"})
#         # Делаем запрос и получаем ответ
#         response = make_request(url=url, data=data)
#         answer = {'SCB_VALIDATION_CALL_AGENT_NUMBER_LENGTH': 'Call agent number length must be = 4'}
#         assert response.status_code == 400
#         assert answer == response.json()
#
#
#     @allure.feature('Негативный тест')
#     @allure.story('Добавляем новый роут с существующим clientPhone')
#     def test_add_route_with_existing_clientPhone(self, add_route, make_request):
#         url = URL.route
#         exist_phone = add_route['clientPhone']
#         # Подготавливаем данные в JSON для запроса
#         data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
#                                                   "clientPhone": exist_phone})
#         # Делаем запрос и получаем ответ
#         response = make_request(url=url, data=data)
#         answer = {'SCB_CALL_CREATE_EXCEPTION': 'CallCreateException: Unable to add new route cause route for this client number already exist.'}
#         assert response.status_code == 500
#         assert answer == response.json()
#
#
#     @allure.feature('Позитивный тест')
#     @allure.story('Удаляем существующий роут')
#     def test_delete_route(self, add_route):
#         url = URL.route
#         params = {'id':add_route['id']}
#         # Делаем запрос и получаем ответ
#         response = requests.delete(url=url, params = params, headers = URL.headers)
#         answer = add_route['id']
#         assert response.status_code == 200
#         assert answer == response.json()
#
#     @allure.feature('Негативный тест')
#     @allure.story('Удаляем не существующий роут')
#     def test_delete_route_with_unknown_id(self):
#         url = URL.route
#         # Делаем запрос и получаем ответ
#         response = requests.delete(url=url, params = {'id':999999999}, headers = URL.headers)
#         answer = {"SCB_CALL_NOT_FOUND_EXCEPTION": "CallNotFoundException: Unable to find call with id=999999999"}
#         assert response.status_code == 500
#         assert answer == response.json()
#
#
#     @allure.feature('Позитивный тест')
#     @allure.story('Обновляем ранее созданный роут')
#     def test_put_route_agentNumber_clientPhone_callDate(self, add_route, make_request):
#         url = URL.route
#         # Делаем запрос и получаем ответ
#         data = _.generate_JSON(add_route, {"agentNumber": "1111",
#                                            "clientPhone": "0666666666",
#                                            "callDate": 1500292769604})
#         response = make_request(method = "PUT", url=url, data=data)
#         answer = _.generate_JSON(add_route, {"agentNumber": "1111",
#                                              "clientPhone": "0666666666"})
#         assert response.status_code == 200
#         assert answer == response.json()
#
#
#     @allure.feature('Негативный тест')
#     @allure.story('Обновляем роут с неизвесным ID')
#     def test_put_route_with_unknown_id(self, add_route, make_request):
#         url = URL.route
#         copy_add_route = add_route.copy()
#         # Делаем запрос и получаем ответ
#         data = _.generate_JSON(copy_add_route, {"id": 999999999,
#                                            "clientPhone": "0666666666"})
#         response = make_request(method = "PUT", url=url, data=data)
#         answer = {"SCB_CALL_NOT_FOUND_EXCEPTION": "CallNotFoundException: Unable to find call with id=999999999"}
#         assert response.status_code == 500
#         assert answer == response.json()
#
#
#     @allure.feature('Негативный тест')
#     @allure.story('Редактируем clientPhone на уже существующий')
#     def test_put_route_clientPhone_agentNumber_on_existing(self,add_route, make_request, clear_result):
#         url = URL.route
#         # Подготавливаем данные в JSON для запроса
#         data = _.get_JSON_request('add_route', **{"agentNumber": "1111",
#                                                   "clientPhone": "0666816659"})
#         # Делаем запрос и получаем ответ
#         response = make_request(url=url, data=data)
#         assert response.status_code == 200
#         route_id = response.json()['id']
#         #Добавляем ИД для очистки результата
#         clear_result['id'].append(route_id)
#         # Изменяем созданный перед тестом route(agentNumber and clientPhone)на существующий(тот что в созданный в тесте)
#         data = _.generate_JSON(add_route, {"agentNumber": "1111",
#                                            "clientPhone": "0666816659"})
#         response = make_request(method="PUT", url=url, data=data)
#         answer = {"SCB_CALL_UPDATE_EXCEPTION": "CallUpdateException: Unable to update call. Call with such client number already exist"}
#         assert response.status_code == 500
#         assert answer == response.json()
#
#
# class Test_Settings:
#
#     @pytest.fixture(scope="function")
#     def get_settings(self, make_request):
#         response = make_request(method="GET", url=URL.scb_settings)
#         assert response.status_code == 200
#         yield response.json()
#
#         #Востанавливаем настройки которые были до теста
#         response = make_request(method="PUT", data = response.json(), url=URL.scb_settings)
#         assert response.status_code == 200
#
#     @allure.feature('Позитивный тест')
#     @allure.story('Получаем манифест')
#     def test_manifest(self, make_request):
#         response = make_request(method = "GET", url=URL.scb_manifest)
#         answer = _.get_JSON_response('scb_manifest')
#         assert response.status_code == 200
#         assert response.json().keys()== answer.keys()
#
#
#     @allure.feature('Позитивный тест')
#     @allure.story('Получаем информацию о лицензиях')
#     def test_licenses(self, make_request):
#         response = make_request(method = "GET", url=URL.scb_licenses)
#         answer = _.get_JSON_response('scb_licenses')
#         assert response.status_code == 200
#         assert response.json().keys()== answer.keys()
#
#
#     @allure.feature('Позитивный тест')
#     @allure.story('Получаем информацию о количестве лицензий')
#     def test_count(self, make_request):
#         response = make_request(method = "GET", url=URL.scb_count)
#         assert response.status_code == 200
#
#
#     @allure.feature('Позитивный тест')
#     @allure.story('Получаем настройки')
#     def test_settings(self, make_request):
#         response = make_request(method="GET", url=URL.scb_settings)
#         answer = _.get_JSON_response('scb_settings')
#         assert response.status_code == 200
#         assert response.json().keys() == answer.keys()
#
#
#     @allure.feature('Позитивный тест')
#     @allure.story('Изменяем настройки')
#     @pytest.mark.parametrize("debugLevel, logLength",[(1,100), (2,500), (3, 900)])
#     @pytest.mark.parametrize("monitoring, smartLabel, routing", [(True, True, True), (False, False, False)])
#     def test_edit_settings(self,get_settings, make_request, debugLevel, logLength,monitoring,smartLabel,routing):
#         data = _.generate_JSON(get_settings, {"debugLevel": debugLevel,
#                                                      "logLength": logLength,
#                                                      "monitoring": monitoring,
#                                                      "smartLabel": smartLabel,
#                                                      "routing": routing})
#         response = make_request(method="PUT", url=URL.scb_settings, data=data)
#         answer = data
#         assert response.status_code == 200
#         assert response.json() == answer
#
#
#     @allure.feature('Негативный тест')
#     @allure.story('Изменяем настройки с не существующим id')
#     def test_edit_settings_with_unknown_id(self,get_settings, make_request):
#         unknown_id = int(get_settings['id']) + 1
#         data = _.generate_JSON(get_settings, {"id": unknown_id,
#                                                    "debugLevel": 3,
#                                                    "logLength": 300,
#                                                    "monitoring": True,
#                                                    "smartLabel": True,
#                                                    "routing": True})
#         response = make_request(method="PUT", url=URL.scb_settings, data=data)
#         answer = {'SCB_REQUEST_VALIDATION_EXCEPTION': 'SCBRequestValidationException: Incorrect settings id!'}
#         assert response.status_code == 500
#         assert response.json() == answer


class Test_Contact:

    # @pytest.fixture(scope="function")
    # def add_contact(self, make_request, clear_result):
    #     url = URL.scb_contact
    #     payload = _.get_JSON_request('add_contact', get.add_contact)
    #     response = make_request(url = url, data=payload)
    #     assert response.status_code == 200
    #     yield response.json()
    #     clear_result['url'], clear_result['id'] = url, response.json()['id']
    #
    #
    # @allure.feature('Позитивный тест')
    # @allure.story('Добавляем новый контакт в справочник с валидными данными')
    # @pytest.mark.parametrize('phoneType',['MOBILE', 'HOME', 'WORK'])
    # def test_add_contact_with_valide_data(self, make_request, clear_result, phoneType):
    #     url = URL.scb_contact
    #     payload = _.get_JSON_request('add_contact', **{"fName": "Victor1",
    #                                                     "lName": "Kliui1",
    #                                                     "description": "bitbok1",
    #                                                     "phoneNumber": "06668166551",
    #                                                     "phoneType": phoneType } )
    #     response = make_request(url=url, data=payload)
    #     clear_result['url'], clear_result['id'] = url, response.json()['id']
    #     assert response.status_code == 200
    #     print("TEST", response.json()['id'])



    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый контакт в справочник с пустыми ФИО')
    def test_add_contact_with_fName_lName_is_None(self, make_request):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": None,
                                                        "lName": None,
                                                        "phoneNumber": "06668166551",
                                                        "phoneType": "MOBILE" } )
        response = make_request(url=url, data=payload)
        answer = {"SCB_VALIDATION_CONTACT_FIRST_NAME_EMPTY": "Contact first name is empty",
                  "SCB_VALIDATION_CONTACT_LAST_NAME_EMPTY": "Contact last name is empty"}
        assert response.status_code == 400
        assert response.json() == answer


    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый контакт в справочник с пустым phoneNumber')
    def test_add_contact_with_phoneNumber_is_null(self, make_request):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": "Victor1",
                                                        "lName": "Kliui1",
                                                        "phoneNumber": None,
                                                        "phoneType": "MOBILE" } )
        response = make_request(url=url, data=payload)
        answer = {'SCB_VALIDATION_PHONE_NUMBER': 'Phone number is empty'}
        assert response.status_code == 400
        assert response.json() == answer


    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый контакт в справочник с не верным "phoneType"')
    def test_add_contact_with_incorrect_phoneType(self, make_request):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": "Victor1",
                                                        "lName": "Kliui1",
                                                        "phoneNumber": None,
                                                        "phoneType": "HOUSE"})
        response = make_request(url=url, data=payload)
        assert response.status_code == 400



    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый контакт в справочник без phones"')
    def test_add_contact_without_phones(self, make_request):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": "Victor1",
                                                        "lName": "Kliui1",
                                                        "phones":None})
        response = make_request(url=url, data=payload)
        print(response.json())
        answer = {"SCB_VALIDATION_CONTACT_FIRST_NAME_EMPTY": "Phones is empty"}
        assert response.status_code == 200
        # assert response.json() == answer


    @allure.feature('Поизитивный тест')
    @allure.story('Добавляем новый контакт в справочник с несколькими телефонами')
    def test_add_contact_with_many_phones(self, make_request):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": "Victor1",
                                                        "lName": "Kliui1",
                                                        "phones":[{ "phoneNumber": "06668166551","phoneType": "MOBILE","comment": None},
                                                                  {"phoneNumber": "0525731628","phoneType": "HOME","comment": None},
                                                                  {"phoneNumber": "0443775578","phoneType": "WORK","comment": None}]})
        response = make_request(url=url, data=payload)
        assert response.status_code == 200
        # Количество телефонов добавленных = кол-ву телефонов переданных
        assert len(response.json()['phones']) == len(payload['phones'])
        print(response.json())
