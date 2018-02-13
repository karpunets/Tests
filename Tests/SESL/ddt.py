import pytest, allure


from Data.Make_requests_and_answers import make_test_data, equal_schema
from Data.Make_requests_and_answers import get_from_csv



@allure.feature('Позитивный тест')
@allure.story('Добавляем критерий')
@pytest.mark.parametrize("role, name, method, schema_name, URL, payload, params, status_code, expect_response",get_from_csv("xls_from_radion"))
def test_add_criteria(send_request, add_one_integration, add_one_map, add_one_tag, role, name, method, schema_name, URL, payload, params, status_code, expect_response):
    payload["$errors"] = expect_response
    fixture = {"add_one_integration":add_one_integration,
               "add_one_map":add_one_map,
               "add_one_tag":add_one_tag}
    data = make_test_data(json_name= schema_name, method=method, data = payload, params=params, fixture_params=fixture["add_one_"+schema_name])
    print("DATA", data)
    response = send_request(method=method, url=URL, data=data['request_body'], params=params)
    print(response.json())
    instance = response.json()
    #Шаг для удаления критерия
    assert response.status_code == status_code
    if status_code == 200 and expect_response == {}:
        assert equal_schema(instance, data['schema'])
    else:
        assert instance == data['errors']
