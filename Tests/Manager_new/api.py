import allure, pytest
from bin.session import Client


from bin.Make_requests_and_answers import parse, equal_schema, random_string


@allure.feature('Функциональный тест')
@allure.story('Получаем все группы')
def test_get_groups():
    response = Client.get("groups")
    print(response.json())
    assert response.status_code == 200 and "ROOT" in response.json()[0]['name']



