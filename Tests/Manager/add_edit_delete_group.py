import allure
import pytest

import Data.URLs_MAP as URL
from bin.Make_requests_and_answers import JSON_generator as _


@pytest.fixture(scope="function")
def delete_group(send_request):
    group_id = {}
    yield group_id
    sorted_group = sorted(group_id.keys())
    for i in sorted_group:
        response = send_request(url=URL.delete_group, data={'groupId': group_id[i]})
        assert response.status_code == 200


@pytest.fixture(scope="function")
def add_group(send_request):
    data = _.get_JSON_request("add_group", **{"name": "test_edit_group"})
    response = send_request(url=URL.add_group, data=data)
    assert response.status_code == 200
    group_id = response.json()['id']
    return group_id


@allure.feature('Позитивный тест')
@allure.story('Добавляем новую групу под ROOT')
def test_add_Root_group(send_request, delete_group):
    name = "add_group"
    url = URL.add_group
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"name": "test_add_group"})
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data=data)
    group_id = response.json()['id']
    # Данные которые должны быть в ответе
    answer = {"name": "test_add_group"}
    delete_group["id"] = group_id
    assert response.status_code == 200
    for i in answer:
        assert answer[i] == response.json()[i]


@allure.feature('Позитивный тест')
@allure.story('Редактируем название группы')
def test_edit_group(add_group, send_request, delete_group):
    name = "edit_group"
    url = URL.edit_group
    group_id = add_group
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"id": group_id, "name": "test_edited_group"})
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data=data)
    answer = {"id": group_id, "name": "test_edited_group"}
    delete_group['id'] = group_id
    assert response.status_code == 200
    for i in answer:
        assert answer[i] == response.json()[i]


@allure.feature('Позитивный тест')
@allure.story('Удаляем группу')
def test_delete_group(add_group, send_request):
    url = URL.delete_group
    group_id = add_group
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data={"groupId": group_id})
    assert response.status_code == 200
    assert response.json() == True


@allure.feature('Негативный тест')
@allure.story('Добавляем новую групу под ROOT с названием < 3 символов')
def test_add_Root_group_less_3_symbols(send_request):
    name = "add_group"
    url = URL.add_group
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"name": "ab"})
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data=data)
    answer = {"ADM_VALIDATION_GROUP_NAME_LENGTH": "NAME length from 3 to 256"}
    assert response.status_code == 400
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Добавляем новую групу под не существующую')
def test_add_under_unknown_parent_group(send_request):
    name = "add_group"
    url = URL.add_group
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"name": "unspecified_group", "parent": {"id": 0}})
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data=data)
    answer = {"ADM_VALIDATION_GROUP_PARENT_EMPTY": "PARENT GROUP ID not specified"}
    assert response.status_code == 400
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Добавляем новую групу name=null')
def test_add_name_is_null(send_request):
    name = "add_group"
    url = URL.add_group
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"name": None})
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data=data)
    answer = {"ADM_VALIDATION_GROUP_NAME": "NAME not specified"}
    assert response.status_code == 400
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Удаляем ROOT группу')
@pytest.mark.xfail
def test_delete_ROOT_group(send_request):
    url = URL.delete_group
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data={"groupId": 2})
    assert response.status_code == 500
    assert response.json() == True


@allure.feature('Позитивный тест')
@allure.story('Редактируем название ROOT группы')
@pytest.mark.xfail
def test_edit_ROOT_group(send_request):
    name = "edit_group"
    url = URL.edit_group
    # Подготавливаем данные в JSON для запроса
    data = _.get_JSON_request(name, **{"id": 2, "name": "edit_ROOT_group", "parent": {}})
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data=data)
    answer = {"1": "Can'edit ROOT group"}
    assert response.status_code == 500
    assert answer == response.json()


@allure.feature('Негативный тест')
@allure.story('Удаляем группу, у которой есть child')
@pytest.mark.xfail
def test_delete_group_with_child(send_request, delete_group):
    name = "add_group"
    url = URL.add_group
    # Подготавливаем данные в JSON для добавления группы под рутом
    data = _.get_JSON_request(name, **{"name": "test_add_group_1"})
    # Делаем запрос и получаем ответ
    response = send_request(url=url, data=data)
    group_id_1 = response.json()['id']
    # Добавляем ИД для удаления после теста
    delete_group["id_2"] = group_id_1
    # Подготавливаем данные в JSON для добавления группы под только что созданную группу
    data = _.get_JSON_request(name, **{"name": "test_add_group_2", "parent": {"id": group_id_1}})
    response = send_request(url=url, data=data)
    group_id_2 = response.json()['id']
    # Добавляем ИД для удаления после теста
    delete_group["id_1"] = group_id_2
    # Пробуем удалить группу с child
    response = send_request(url=URL.delete_group, data={"groupId": group_id_1})
    answer = {}
    assert response.status_code == 500
    assert answer == response.json()
