import pytest, allure, json, requests, random
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import make_test_data, equal_schema, random_string
from Data.Test_data import ROOT_group_id, ROOT_user_id
from Data.Make_requests_and_answers import get_from_csv



@allure.feature('Позитивный тест')
@allure.story('Добавляем критерий')
@pytest.mark.parametrize("name, method, json_name, payload, status_code, expect_response",get_from_csv("csv_example"))
def test_add_criteria(send_request, add_group, delete_group_and_criteria, name, method, json_name, payload, status_code, expect_response):
    group_id = next(add_group)['id']
    payload["$criteriagroupId"] = group_id
    data = make_test_data(json_name, payload)
    response = send_request(URL.criteria, data['request'])
    print(response.json())
    instance = response.json()
    #Шаг для удаления критерия
    try:
        delete_group_and_criteria['criteriaId'].append(instance['id'])
    except KeyError:
        pass

    assert response.status_code == status_code
    if status_code == 200:
        assert equal_schema(instance, data['schema'])
    else:
        assert response.json() == expect_response