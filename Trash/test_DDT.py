import pytest, allure


from Data.Make_requests_and_answers import make_test_data, equal_schema
from Data.Make_requests_and_answers import get_from_csv



@allure.feature('Позитивный тест')
@allure.story('Добавляем критерий')
@pytest.mark.parametrize("role, name, method, schema_name, URL, payload, params, status_code, expect_response",get_from_csv("xls_from_radion"))
def test_add_criteria(send_request, add_group, delete_group_and_criteria, role, name, method, schema_name, URL, payload, params, status_code, expect_response):
    if "$from_fixture" in payload["$criteriaGroupId"]:
        group_id = next(add_group)['id']
        payload["$criteriaGroupId"] = group_id
    payload["$errors"] = expect_response
    data = make_test_data(schema_name, payload)
    print("data", data)
    response = send_request(method=method, url=URL, payload=data['request'], params=params)
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
