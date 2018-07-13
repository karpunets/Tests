# -*- coding: utf-8 -*-

import allure
import pytest
import random
from bin.session import Client
from bin.session import root_group_id, root_role_id
from bin.session import get_headers_with_credentials
from bin.helpers import make_user_group_roles
from bin.common import parse_request, equal_schema, random_string
from bin.helpers import get_property


class TestConnectors:


    url = "connectors"
    connectors_list = ['/CiscoSparkConnector', '/ECEConnector', '/EchoConnector', '/FacebookConnector', '/TelegramConnector',
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
    def test_add_unknown_connector(self, clear_data):
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": root_group_id()})
        response = Client.post(TestConnectors.url, data['request'])
        print(response.json())
        assert response.status_code == 200
        clear_data.append(response.json()['rid'])
        assert equal_schema(response.json(), data['schema'])


    @allure.feature('Функциональный тест')
    @allure.story('Получаем коннекторы')
    def test_get_connectors(self, connector):
        response = Client.get(TestConnectors.url)
        assert response.status_code == 200
        assert connector in response.json()

    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с пустым именем')
    def test_add_connector_with_empty_name(self):
        data = parse_request("post_connectors", {"$name": None,
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": root_group_id()})
        response = Client.post(TestConnectors.url, data['request'])
        expected_result = {'SMC_VALIDATION_CONNECTOR_NAME': "Connector name mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_result)


    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с пустым URL')
    @pytest.mark.xfail
    def test_add_connector_with_empty_url(self):
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": None,
                                                 "$groupId": root_group_id()})
        response = Client.post(TestConnectors.url, data['request'])
        print(response.json())
        expected_result = {'SMC_VALIDATION_CONNECTOR_NAME': "Connector URL mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_result)


    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с пустой группой')
    @pytest.mark.xfail
    def test_add_connector_without_group(self):
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": None})
        response = Client.post(TestConnectors.url, data['request'])
        print(response.json())
        expected_result = {'SMC_VALIDATION_CONNECTOR_NAME': "Connector group mustn't be empty"}
        assert (response.status_code, response.json()) == (400, expected_result)


    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с уже существующим именем')
    def test_add_connector_with_existing_name(self, clear_data, connector):
        existing_name = connector['name']
        data = parse_request("post_connectors", {"$name": existing_name,
                                                 "$url": "http://" + random_string(),
                                                 "$groupId": root_group_id()})
        response = Client.post(TestConnectors.url, data['request'])
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
        response = Client.post(TestConnectors.url, data['request'])
        print(response.json())
        expected_result = {'SMC_VALIDATION_CONNECTOR_URL_UNIQUE': "Connector url must be unique"}
        assert (response.status_code, response.json()) == (400, expected_result)


    @allure.feature('Функциональный тест')
    @allure.story('Создаем коннектор с уже существующим URL')
    @pytest.mark.xfail
    def test_add_connector_with_existing_URL__1(self):
        data = parse_request("post_connectors", {"$name": random_string(),
                                                 "$url": random_string(),
                                                 "$groupId": root_group_id(),
                                                 "$enabled" : True})
        response = Client.post(TestConnectors.url, data['request'])
        print(response.json())
        expected_result = {'SMC_VALIDATION_CONNECTOR_URL_UNIQUE': "Connector url must be unique"}
        assert (response.status_code, response.json()) == (400, expected_result)



