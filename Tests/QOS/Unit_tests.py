import pytest, allure, json, requests, random
import Data.URLs_MAP as URL

from Data.Test_data import random_name
from Data.Make_requests_and_answers import make_test_data
from Data.Make_requests_and_answers import equal_schema


@allure.feature('Позитивный тест')
@allure.story('Добавляем новую групу')
def test_add_group(send_request, delete_group):
    data = make_test_data('add_group', {'$name':random_name()})
    response = send_request(URL.criteria_group, data['request'])
    print(data['request'])
    print(response.json())
    instance = response.json()
    delete_group['id'] = instance['id']
    assert equal_schema(instance, data['schema'])
    assert response.status_code == 200


@allure.feature('Позитивный тест')
@allure.story('Добавляем новую групу с существующим именем')
def test_add_group_with_existing_name(send_request, add_group):
    existing_name = add_group['name']
    payload = {"groups":[{"id":2}],"name":existing_name}
    response = send_request(URL.criteria_group, payload)
    answer = {"QOS_ENTITY_WITH_SUCH_FIELD_EXISTS":"QoSEntityWithSuchFieldExists: NAME"}
    assert response.status_code == 500
    assert response.json() == answer




