# -*- coding: utf-8 -*-

import allure
import pytest
import random
from bin.session import Session
from bin.session import root_group_id, root_role_id
from bin.session import get_headers_with_credentials
from bin.helpers import make_user_group_roles
from bin.common import parse_request, equal_schema, random_string
from bin.helpers import get_property


class TestConnectors:
    url = "connectors"
    connectors_list = ['/CiscoSparkConnector', '/ECEConnector', '/EchoConnector', '/FacebookConnector',
                       '/TelegramConnector',
                       '/ViberConnector', '/WebConnector']

    # @allure.feature('Функциональный тест')
    # @allure.story('Создаем коннектор')
    # @pytest.mark.parametrize('connector_name', connectors_list)
    # def test_add_connectors(self, clear_data, connector_name):
    #     data = parse_request("post_connectors", {"$name": random_string(),
    #                                              "$url": get_property("server")['server'] + connector_name,
    #                                              "$groupId": root_group_id()})
    #     print(data)
    #     response = Client.post(TestConnectors.url, data['request'])
    #     print(response.json())
    #     assert response.status_code == 200
    #     clear_data.append(response.json()['rid'])
    #     assert equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор')
    def test_add_unknown_connector_with_not_ROOT_group(self, clear_data, immutable_group_with_child):
        group_id = immutable_group_with_child['groupId']
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": group_id})
        response = Session.post(TestConnectors.url, data['request'])
        print(response.json())
        assert response.status_code == 200
        clear_data.append(response.json()['rid'])
        assert equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор')
    def test_add_unknown_connector_with_ROOT_group(self, clear_data):
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": root_group_id()})
        response = Session.post(TestConnectors.url, data['request'])
        print(response.json())
        assert response.status_code == 200
        clear_data.append(response.json()['rid'])
        assert equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Получаем коннекторы')
    def test_get_connectors(self, connector):
        response = Session.get(TestConnectors.url)
        assert response.status_code == 200
        assert connector in response.json()

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с пустым именем')
    def test_add_connector_with_empty_name(self):
        data = parse_request("post_connectors", {"$name": None,
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": root_group_id()})
        response = Session.post(TestConnectors.url, data['request'])
        expected_result = {'SMC_VALIDATION_CONNECTOR_NAME': "Connector name mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_result)

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с пустым URL')
    @pytest.mark.xfail
    def test_add_connector_with_empty_url(self):
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": None,
                                                 "$groupId": root_group_id()})
        response = Session.post(TestConnectors.url, data['request'])
        print(response.json())
        expected_result = {'SMC_VALIDATION_CONNECTOR_URL': "Connector url mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_result)

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с пустой группой')
    @pytest.mark.xfail
    def test_add_connector_without_group(self):
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": None})
        response = Session.post(TestConnectors.url, data['request'])
        print(response.json())
        expected_result = {'SMC_VALIDATION_CONNECTOR_GROUP': "Connector group mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_result)

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с уже существующим именем')
    def test_add_connector_with_existing_name(self, clear_data, connector):
        existing_name = connector['name']
        data = parse_request("post_connectors", {"$name": existing_name,
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": root_group_id()})
        response = Session.post(TestConnectors.url, data['request'])
        print(response.json())
        assert response.status_code == 200
        clear_data.append(response.json()['rid'])
        assert equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с уже существующим URL')
    @pytest.mark.xfail
    def test_add_connector_with_existing_URL(self, connector):
        existing_url = connector['url']
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": existing_url,
                                                 "$groupId": root_group_id()})
        response = Session.post(TestConnectors.url, data['request'])
        print(response.json())
        expected_result = {'SMC_VALIDATION_CONNECTOR_URL_UNIQUE': "Connector url must be unique"}
        assert (response.status_code, response.json()) == (400, expected_result)

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем коннектор')
    def test_edit_connector(self, connector, immutable_group_with_child):
        group_id = immutable_group_with_child['groupId']
        data = parse_request("put_connectors", {"$rid": connector['rid'],
                                                "$name": random_string(),
                                                "$url": "http://" + random_string(),
                                                "$groupId": group_id
                                                })
        response = Session.put(TestConnectors.url, data['request'])
        print(response.json())
        assert response.status_code == 200
        assert equal_schema(response.json(), data['schema'])

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор имя - пустое')
    def test_edit_connector_without_name(self, connector):
        data = parse_request("put_connectors", {"$rid": connector['rid'],
                                                "$name": None,
                                                "$url": "http://" + random_string(),
                                                "$groupId": root_group_id()
                                                })
        response = Session.put(TestConnectors.url, data['request'])
        print(response.json())
        expected_response = {'SMC_VALIDATION_CONNECTOR_NAME': "Connector name mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем коннектор имя - пустое')
    def test_edit_connector_without_URL(self, connector):
        data = parse_request("put_connectors", {"$rid": connector['rid'],
                                                "$name": random_string(),
                                                "$url": None,
                                                "$groupId": root_group_id()
                                                })
        response = Session.put(TestConnectors.url, data['request'])
        print(response.json())
        expected_response = {'SMC_VALIDATION_CONNECTOR_URL': "Connector url mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем коннектор группа не указана')
    def test_edit_connector_without_group(self, connector):
        data = parse_request("put_connectors", {"$rid": connector['rid'],
                                                "$name": random_string(),
                                                "$url": "http://" + random_string(),
                                                "$groupId": None
                                                })
        response = Session.put(TestConnectors.url, data['request'])
        print(response.json())
        expected_response = {'SMC_VALIDATION_CONNECTOR_GROUP': "Connector group mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_response)

    @allure.feature('Функциональный тест')
    @allure.story('Редактируем коннектор группа не указана')
    def test_edit_connector_with_random_rid(self):
        random_rid = random_string()
        data = parse_request("put_connectors", {"$rid": random_rid,
                                                "$name": random_string(),
                                                "$url": "http://" + random_string(),
                                                "$groupId": root_group_id()
                                                })
        response = Session.put(TestConnectors.url, data['request'])
        print(response.json())
        expected_response = {'UNMAPPED_EXCEPTION': 'SMCRequestException: Connector with rid=%s not found' % random_rid}
        assert (response.status_code, response.json()) == (500, expected_response)

    @allure.feature('Функциональный тест')
    @allure.story('Удаляем коннектор')
    def test_delete_connector(self, connector):
        response = Session.delete(TestConnectors.url, id=connector['rid'])
        print(response.json())
        assert (response.status_code, response.json()) == (200, connector)

    @allure.feature('Функциональный тест')
    @allure.story('Удаляем коннектор с не правильным id')
    def test_delete_connector_with_unknown_id(self, connector):
        random_id = random_string()
        response = Session.delete(TestConnectors.url, id=random_id)
        expected_response = {'UNMAPPED_EXCEPTION': 'SMCRequestException: Connector with id=%s not found'%random_id}
        print(response.json())
        assert (response.status_code, response.json()) == (500, expected_response)


class TestAccounts:
    #TODO: Проверять пулы, связать аккаунт, потом удалить связанный акк
    url = "accounts"

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор')
    def test_add_unknown_connector_with_ROOT_group(self, clear_data):
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$connectorRid": "",
                                                 "$groupId": root_group_id(),
                                                 "$bindAccountRid": "",
                                                 "$connectorUrl": "",
                                                 "$botName": "",
                                                 "$authToken": ""
                                                 })
        response = Session.post(TestConnectors.url, data['request'])
        print(response.json())
        assert response.status_code == 200
        clear_data.append(response.json()['rid'])
        assert equal_schema(response.json(), data['schema'])


class TestTRUMClients:
    url = "clients"

