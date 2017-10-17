import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _
from Data.Test_data import random_name

@allure.feature('Позитивный тест')
@allure.story('Добавляем новую групу')
def test_add_group(send_request, delete_group):
    payload = json.dumps({"groups":[{"id":2}],"name":random_name()})
    response = send_request(URL.criteria_group, payload)
    group_id = response.json()['id']
    delete_group.append[group_id]
    assert response.status_code == 200


@allure.feature('Позитивный тест')
@allure.story('Добавляем новую групу с существующим именем')
def test_add_group_with_existing_name(send_request, add_group):
    existing_name = add_group['name']
    payload = json.dumps({"groups":[{"id":2}],"name":existing_name})
    response = send_request(URL.criteria_group, payload)
    answer = {"QOS_ENTITY_WITH_SUCH_FIELD_EXISTS":"QoSEntityWithSuchFieldExists: NAME"}
    assert response.status_code == 500
    assert response.json() == answer







