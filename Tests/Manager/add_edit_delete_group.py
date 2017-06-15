import pytest, allure, json, requests
import Data.URLs_MAP as URL
import Data.Users as get

from Data.Make_requests_and_answers import JSON_generator as _

@pytest.fixture(scope="function")
def delete_group(make_request):
    group_id = {}
    yield group_id
    for i in group_id:
        response = make_request(url = URL.delete_group, data = {'groupId':group_id[i]})
        assert response.status_code == 200


@pytest.fixture(scope = "function")
def add_group(make_request):
    data = _.get_JSON_request("add_group", **{"name":"test_edit_group"})
    response = make_request(url=URL.add_group, data=data)
    assert response.status_code == 200
    group_id = response.json()['id']
    return group_id



@allure.feature('Позитивный тест')
@allure.story('Добавляем новую групу под ROOT')
def test_add_Root_group(make_request,delete_group):
    name ="add_group"
    url = URL.add_group
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"name":"test_add_group"})
    # Делаем запрос и получаем ответ
    response = make_request(url=url, data=data)
    group_id = response.json()['id']
    # Данные которые должны быть в ответе
    answer ={"name":"test_add_group"}
    delete_group["id"] = group_id
    assert response.status_code == 200
    for i in answer:
        assert answer[i]== response.json()[i]


@allure.feature('Позитивный тест')
@allure.story('Редактируем название группы')
def test_edit_group(add_group, make_request, delete_group):
    name ="edit_group"
    url = URL.edit_group
    group_id = add_group
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"id":group_id, "name":"test_edited_group"})
    # Делаем запрос и получаем ответ
    response = make_request(url=url, data=data)
    answer ={"id":group_id, "name":"test_edited_group"}
    delete_group['id'] = group_id
    assert response.status_code == 200
    for i in answer:
        assert answer[i]== response.json()[i]

@allure.feature('Позитивный тест')
@allure.story('Удаляем группу')
def test_delete_group(add_group, make_request):
    url = URL.delete_group
    group_id = add_group
    # Делаем запрос и получаем ответ
    response = make_request(url=url, data={"groupId": group_id})
    assert response.status_code == 200
    assert response.json() == True