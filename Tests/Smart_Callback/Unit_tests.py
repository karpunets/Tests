import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _


@pytest.mark.usefixtures('clear_credentials', 'credential', 'clear_routes')
class Test_Routes:

    @allure.feature('Позитивный тест')
    @allure.story('Добавляем новый роут с валидными данными')
    def test_add_route(self, make_request, clear_result):
        url = URL.fixed_routes
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"internalNumber": "1111",
                                                  "externalNumber": "0666816657"})
        # Делаем запрос и получаем ответ
        response = make_request(url, data)
        route_id = response.json()['id']
        answer = _.get_JSON_response('add_route', **{'id': route_id,
                                                     "internalNumber": "1111",
                                                     "externalNumber": "0666816657"})
        clear_result['url'], clear_result['id'] = url, route_id
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый роут с не существующим internalNumber')
    def test_add_route_with_unknown_internalNumber(self, make_request):
        url = URL.fixed_routes
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"internalNumber": "9999999999",
                                                  "externalNumber": "0666816657"})
        # Делаем запрос и получаем ответ
        response = make_request(url, data)
        answer = {'SCB_CALL_NOT_FOUND_EXCEPTION': 'RouteNotFoundException: Unable to find monitoring number=9999999999'}
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый роут с существующим externalNumber')
    def test_add_route_with_existing_externalNumber(self, add_route, make_request):
        url = URL.fixed_routes
        exist_phone = add_route['externalNumber']
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"internalNumber": "1111",
                                                  "externalNumber": exist_phone})
        # Делаем запрос и получаем ответ
        response = make_request(url, data)
        answer = {'SCB_CALL_CREATE_EXCEPTION': 'RouteCreateException: Unable to add new route cause route for this external number already exist.'}
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Позитивный тест')
    @allure.story('Удаляем существующий роут')
    def test_delete_route(self, add_route, make_request):
        url = URL.fixed_routes
        params = {'id':add_route['id']}
        # Делаем запрос и получаем ответ
        response = make_request(url, method = 'DELETE', params = params)
        answer = add_route['id']
        assert response.status_code == 200
        assert answer == response.json()

    @allure.feature('Негативный тест')
    @allure.story('Удаляем не существующий роут')
    def test_delete_route_with_unknown_id(self, make_request):
        url = URL.fixed_routes
        # Делаем запрос и получаем ответ
        response = make_request(url, method = 'DELETE',  params = {'id':999999999})
        answer = {'SCB_CALL_NOT_FOUND_EXCEPTION': 'RouteNotFoundException: Unable to find fixed route with id=999999999'}
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Позитивный тест')
    @allure.story('Обновляем ранее созданный роут')
    def test_put_route_internalNumber_externalNumber_callDate(self, add_route, make_request):
        url = URL.fixed_routes
        # Делаем запрос и получаем ответ
        data = _.generate_JSON(add_route, {"internalNumber": "1111",
                                           "externalNumber": "0666666666",
                                           "callDate": 1500292769604})
        response = make_request(url,  data, method = "PUT")
        answer = _.generate_JSON(add_route, {"internalNumber": "1111",
                                             "externalNumber": "0666666666"})
        assert response.status_code == 200
        assert answer == response.json()


    @allure.feature('Позитивный тест')
    @allure.story('Получаем информацию по роуту')
    def test_get_route(self, add_route, make_request):
        url = URL.fixed_routes
        # Делаем запрос и получаем ответ
        data =  {"internalNumber": "1022","page_size":10,"page_number":1}
        response = make_request(url, method = "GET",  params=data)
        answer = _.get_JSON_response('get_route', **add_route)
        assert response.status_code == 200
        assert answer == response.json()


    @allure.feature('Негативный тест')
    @allure.story('Получаем информацию по роуту (проверяем пагинацию) "page_size"=0,"page_number"0')
    def test_get_route_with_invalid_pagination(self, add_route, make_request):
        url = URL.fixed_routes
        # Делаем запрос и получаем ответ
        data =  {"internalNumber": "1022","page_size":0,"page_number":0}
        response = make_request(url, method = "GET",  params=data)
        answer = {"SCB_REQUEST_VALIDATION_EXCEPTION": "SCBRequestValidationException: Page size and page number can't be less then 1!"}
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Негативный тест')
    @allure.story('Получаем информацию по роуту с неизвестным номером агента')
    def test_get_route_with_unknown_agnetnumber(self, add_route, make_request):
        url = URL.fixed_routes
        # Делаем запрос и получаем ответ
        data =  {"internalNumber": "9379996","page_size":10,"page_number":1}
        response = make_request(url, method = "GET",  params=data)
        answer = []
        assert response.status_code == 200
        assert answer == response.json()['data']


    @allure.feature('Негативный тест')
    @allure.story('Обновляем роут с неизвесным ID')
    def test_put_route_with_unknown_id(self, add_route, make_request):
        url = URL.fixed_routes
        copy_add_route = add_route.copy()
        # Делаем запрос и получаем ответ
        data = _.generate_JSON(copy_add_route, {"id": 999999999,
                                           "externalNumber": "0666666666"})
        response = make_request(url,data,  method = "PUT")
        answer = {'SCB_CALL_NOT_FOUND_EXCEPTION': 'RouteNotFoundException: Unable to find fixed route with id=999999999'}
        assert response.status_code == 500
        assert answer == response.json()


    @allure.feature('Негативный тест')
    @allure.story('Редактируем externalNumber на уже существующий')
    def test_put_route_externalNumber_internalNumber_on_existing(self,add_route, make_request, clear_result):
        url = URL.fixed_routes
        # Подготавливаем данные в JSON для запроса
        data = _.get_JSON_request('add_route', **{"internalNumber": "1111",
                                                  "externalNumber": "0666816659"})
        # Делаем запрос и получаем ответ
        response = make_request(url, data)
        assert response.status_code == 200
        route_id = response.json()['id']
        #Добавляем ИД для очистки результата
        clear_result['id'].append(route_id)
        # Изменяем созданный перед тестом fixed_routes(internalNumber and externalNumber)на существующий(тот что в созданный в тесте)
        data = _.generate_JSON(add_route, {"internalNumber": "1111",
                                           "externalNumber": "0666816659"})
        response = make_request(url, data , method="PUT")
        answer = {'SCB_CALL_UPDATE_EXCEPTION': 'RouteUpdateException: Unable to update fixed route. Fixed route with such external number already exist'}
        assert response.status_code == 500
        assert answer == response.json()


@pytest.mark.usefixtures('clear_credentials', 'credential')
class Test_Settings:

    @pytest.fixture(scope="function")
    def get_settings(self, make_request):
        response = make_request(URL.scb_settings, method="GET")
        assert response.status_code == 200
        yield response.json()

        #Востанавливаем настройки которые были до теста
        response = make_request(URL.scb_settings, method="PUT", data = response.json())
        assert response.status_code == 200

    @allure.feature('Позитивный тест')
    @allure.story('Получаем манифест')
    def test_manifest(self, make_request):
        response = make_request(URL.scb_manifest, method = "GET")
        answer = _.get_JSON_response('manifest')
        assert response.status_code == 200
        assert response.json().keys()== answer.keys()


    @allure.feature('Позитивный тест')
    @allure.story('Получаем информацию о лицензиях')
    def test_licenses(self, make_request):
        response = make_request(URL.scb_licenses, method = "GET")
        answer = _.get_JSON_response('licenses')
        assert response.status_code == 200
        assert response.json().keys()== answer.keys()


    @allure.feature('Позитивный тест')
    @allure.story('Получаем информацию о количестве лицензий')
    def test_count(self, make_request):
        response = make_request(URL.scb_count, method = "GET",)
        assert response.status_code == 200


    @allure.feature('Позитивный тест')
    @allure.story('Получаем настройки')
    def test_settings(self, make_request):
        response = make_request(URL.scb_settings, method="GET")
        answer = _.get_JSON_response('scb_settings')
        assert response.status_code == 200
        assert answer.keys() == response.json().keys()


    @allure.feature('Позитивный тест')
    @allure.story('Изменяем настройки')
    @pytest.mark.parametrize("debugLevel, logLength",[(1,100), (2,500), (3, 900)])
    @pytest.mark.parametrize("monitoring, smartLabel, routing", [(True, True, True), (False, False, False)])
    def test_edit_settings(self,get_settings, make_request, debugLevel, logLength,monitoring,smartLabel,routing):
        data = _.generate_JSON(get_settings, {"debugLevel": debugLevel,
                                                     "logLength": logLength,
                                                     "monitoring": monitoring,
                                                     "smartLabel": smartLabel,
                                                     "routing": routing})
        response = make_request( URL.scb_settings, data, method="PUT")
        answer = data
        assert response.status_code == 200
        assert response.json() == answer


    @allure.feature('Негативный тест')
    @allure.story('Изменяем настройки с не существующим id')
    def test_edit_settings_with_unknown_id(self,get_settings, make_request):
        unknown_id = int(get_settings['id']) + 1
        data = _.generate_JSON(get_settings, {"id": unknown_id,
                                                   "debugLevel": 3,
                                                   "logLength": 300,
                                                   "monitoring": True,
                                                   "smartLabel": True,
                                                   "routing": True})
        response = make_request(URL.scb_settings, data, method="PUT")
        answer = {'SCB_REQUEST_VALIDATION_EXCEPTION': 'SCBRequestValidationException: Incorrect settings id!'}
        assert response.status_code == 500
        assert response.json() == answer


@pytest.mark.usefixtures('clear_credentials', "clear_contact", 'credential')
class Test_Contact():

    @allure.feature('Позитивный тест')
    @allure.story('Добавляем новый контакт в справочник с валидными данными')
    @pytest.mark.parametrize('phoneType',['MOBILE', 'HOME', 'WORK'])
    def test_add_contact_with_valide_data(self, make_request, clear_result, phoneType):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": "Victor1",
                                                        "lName": "Kliui1",
                                                        "description": "bitbok1",
                                                        "phoneNumber": "06668166551",
                                                        "phoneType": phoneType } )
        response = make_request(url, data=payload)
        clear_result['url'], clear_result['id'] = url, response.json()['id']
        assert response.status_code == 200


    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый контакт в справочник с пустыми ФИО')
    def test_add_contact_with_fName_lName_is_None(self, make_request):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": None,
                                                        "lName": None,
                                                        "phoneNumber": "06668166551",
                                                        "phoneType": "MOBILE" } )
        response = make_request(url, data=payload)
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
        response = make_request(url, data=payload)
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
        response = make_request(url, data=payload)
        assert response.status_code == 400



    @allure.feature('Негативный тест')
    @allure.story('Добавляем новый контакт в справочник без phones"')
    def test_add_contact_without_phones(self, make_request, clear_result):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": "Victor1",
                                                        "lName": "Kliui1",
                                                        "phones":None})
        response = make_request(url, data=payload)
        answer = []
        clear_result['url'], clear_result['id'] = url, response.json()['id']
        assert response.status_code == 200
        assert response.json()['phones'] == answer


    @allure.feature('Позитивный тест')
    @allure.story('Добавляем новый контакт в справочник с несколькими телефонами')
    def test_add_contact_with_many_phones(self, make_request, clear_result):
        url = URL.scb_contact
        payload = _.get_JSON_request('add_contact', **{"fName": "Victor1",
                                                        "lName": "Kliui1",
                                                        "phones":[{ "phoneNumber": "06668166551","phoneType": "MOBILE","comment": None},
                                                                  {"phoneNumber": "0525731628","phoneType": "HOME","comment": None},
                                                                  {"phoneNumber": "0443775578","phoneType": "WORK","comment": None}]})
        response = make_request(url, data=payload)
        clear_result['url'], clear_result['id'] = url, response.json()['id']
        assert response.status_code == 200
        # Количество телефонов добавленных = кол-ву телефонов переданных
        assert len(response.json()['phones']) == len(payload['phones'])


    @allure.feature('Позитивный тест')
    @allure.story('Получаем контакты из справочника')
    def test_get_contact(self, make_request, add_contact):
        url = URL.scb_contact
        response = make_request(url, method = "GET")
        answer = [add_contact]
        assert response.status_code == 200
        assert response.json() == answer


    @allure.feature('Позитивный тест')
    @allure.story('Удаляем контакт')
    def test_delete_contact(self, make_request, add_contact):
        url = URL.scb_contact
        contact_id = add_contact['id']
        response = make_request(url, method = "DELETE",  params = {'id':contact_id})
        answer = contact_id
        assert response.status_code == 200
        assert response.json() == answer


    @allure.feature('Негативный тест')
    @allure.story('Удаляем не существующий контакт(с неизвестным id)')
    def test_delete_contact_with_unknown_id(self, make_request):
        url = URL.scb_contact
        response = make_request(url, method = "DELETE",  params = {'id':999999999})
        answer = {'SCB_CONTACT_NOT_FOUND_EXCEPTION': 'ContactNotFoundException: Unable to find contact with id=999999999'}
        assert response.status_code == 500
        assert response.json() == answer


    @allure.feature('Позитивный тест')
    @allure.story('Редактируем контакт в справочнике с валидными данными')
    @pytest.mark.parametrize('phoneType',['MOBILE', 'HOME', 'WORK'])
    def test_edit_contact_with_valide_data(self, make_request, add_contact, phoneType):
        url = URL.scb_contact
        payload = _.generate_JSON(add_contact, {"fName": "Victor1",
                                                "lName": "Kliui1",
                                                'pName': "Yurich",
                                                "description": "bitbok1",
                                                "phoneNumber": "0666816651",
                                                "phoneType": phoneType,
                                                'comment':'comment'} )
        response = make_request(url, method = "PUT",  data=payload)
        answer = payload
        assert response.status_code == 200
        assert response.json() == answer


    @allure.feature('Негативный тест')
    @allure.story('Редактируем контакт в справочнике с пустыми ФИО и номером телефона')
    def test_edit_contact_with_FIO_and_phoneNumber_is_null(self, make_request, add_contact):
        url = URL.scb_contact
        payload = _.generate_JSON(add_contact, {"fName": None,
                                                "lName": None,
                                                "phoneNumber": None,
                                                "phoneType": "MOBILE"} )
        response = make_request(url, method = "PUT",  data=payload)
        answer = {'SCB_VALIDATION_CONTACT_FIRST_NAME_EMPTY': 'Contact first name is empty',
                  'SCB_VALIDATION_CONTACT_LAST_NAME_EMPTY': 'Contact last name is empty',
                  'SCB_VALIDATION_PHONE_NUMBER': 'Phone number is empty'}
        assert response.status_code == 400
        assert response.json() == answer


    @allure.feature('Негативный тест')
    @allure.story('Редактируем контакт в справочнике с неизвесным contact id')
    def test_edit_contact_with_unknown_id(self, make_request, add_contact):
        url = URL.scb_contact
        payload = _.generate_JSON(add_contact, {'id': 999999999})
        response = make_request(url, method = "PUT",  data=payload)
        answer = {'SCB_CONTACT_NOT_FOUND_EXCEPTION': 'ContactNotFoundException: Unable to find contact with id=999999999'}
        assert response.status_code == 500
        assert response.json() == answer


    @allure.feature('Негативный тест')
    @allure.story('Редактируем телефон контакта в справочнике с неизвесным id телефона')
    def test_edit_contact_phone_with_unknown_phone_id(self, make_request, add_contact):
        url = URL.scb_contact
        #Изменяем id телефона
        add_contact['phones'][0]['id'] = 999999999
        response = make_request(url, method = "PUT",  data=add_contact)
        assert response.status_code == 500


    @allure.feature('Негативный тест')
    @allure.story('Редактируем контакт в справочнике с phones = null')
    def test_edit_contact_with_phone_us_null(self, make_request, add_contact):
        url = URL.scb_contact
        payload = _.generate_JSON(add_contact, {'phones':None})
        response = make_request( url, method = "PUT", data=payload)
        answer = []
        assert response.status_code == 200
        assert response.json()['phones'] == answer

@pytest.mark.usefixtures('clear_credentials')
class Test_Credential:


    @allure.feature('Позитивный тест')
    @allure.story('Добавляем credential с валидными данными')
    def test_add_credentials_with_valide_data(self, make_request, clear_result):
        url = URL.scb_credentials
        credential = get.credentials
        response = make_request(url, data=credential)
        credential_id = response.json()['id']
        credential['id'] = credential_id
        clear_result['url'], clear_result['id'] = url, credential_id
        assert response.status_code == 200
        assert response.json() == credential


    @allure.feature('Позитивный тест')
    @allure.story('Удаляем credential с валидными данными')
    def test_delete_credentials_with_valide_id(self, make_request, add_credential):
        url = URL.scb_credentials
        credential_id = {'id': add_credential['id']}
        response = make_request(url, method = 'DELETE',  params=credential_id)
        assert response.status_code == 200
        assert response.json() == credential_id['id']


    @allure.feature('Негативный тест')
    @allure.story('Удаляем credential с не валидными данными')
    def test_delete_credentials_with_unknown_id(self, make_request, add_credential):
        url = URL.scb_credentials
        credential_id = {'id':int(add_credential['id'])+999}
        response = make_request(url, method = 'DELETE',  params=credential_id)
        answer = {"SCB_CREDENTIALS_NOT_FOUND_EXCEPTION": "CredentialsNotFoundException: Unable to find credential with id=%s"%credential_id['id']}
        assert response.status_code == 500
        assert response.json() == answer
