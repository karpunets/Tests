import pytest, allure, json, requests, random
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import make_test_data, equal_schema, random_string
from Data.Make_requests_and_answers import get_from_csv



@allure.feature('Позитивный тест')
@allure.story('Добавляем критерий')
@pytest.mark.parametrize("name, method, json_name, payload, status_code, expect_response",get_from_csv("csv_example"))
def test_add_criteria(send_request, add_group, delete_group_and_criteria, name, method, json_name, payload, status_code, expect_response):
    #TODO: реализовать возможность не передвать ID, зарезервировать слово "$from fixture"
    group_id = next(add_group)['id']
    payload["$criteriagroupId"] = group_id
    payload["$errors"] = expect_response
    data = make_test_data(json_name, payload)
    print("data", data)
    response = send_request(URL.criteria, data['request'])
    instance = response.json()
    #Шаг для удаления критерия
    try:
        delete_group_and_criteria['criteriaId'].append(instance['id'])
    except KeyError:
        pass
    assert response.status_code == status_code
    if status_code == 200 and expect_response == {}:
        assert equal_schema(instance, data['schema'])
    else:
        assert equal_schema(instance, data['errors'])
