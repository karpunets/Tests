import pytest, allure, json, requests
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _

@pytest.fixture(scope="function")
def delete_role(make_request):
    role_id = {}
    yield role_id
    for id in role_id:
        response = make_request(url=URL.delete_role, data={'roleId': role_id[id]})
        assert response.status_code == 200

@pytest.fixture(scope='function')
def add_role(make_request):
    data = get.add_role
    response = make_request(url=URL.add_role, data=data)
    assert response.status_code==200
    role_id = response.json()['id']
    return role_id


@allure.feature('Позитивный тест')
@allure.story('Добавляем новую роль')
def test_add_new_role(make_request, delete_role):
    name ="add_role"
    data = _.get_JSON_request(name, **{'name':'test_add_role'})
    response = make_request(url=URL.add_role, data = data)
    role_id = response.json()['id']
    delete_role['role_id'] = role_id
    answer = _.get_JSON_response(name,**{"id":role_id,
                                         'name':'test_add_role'})
    assert response.status_code == 200
    assert response.json() == answer

@allure.feature('Позитивный тест')
@allure.story('Удаляем новую роль')
@pytest.mark.xfail
def test_delete_new_role(add_role, make_request):
    name ="delete_role"
    role_id = add_role
    data = {'roleId':role_id}
    response = make_request(url=URL.delete_role, data = data)
    assert response.status_code == 200
    assert response.json() == True


@allure.feature('Позитивный тест')
@allure.story('Редактируем новую роль')
def test_edit_new_role(add_role, make_request, delete_role):
    name ="edit_role"
    role_id = add_role
    data = _.get_JSON_request(name, **{'id':role_id,
                              'name':'edited_role'})
    response = make_request(url=URL.edit_role, data = data)
    answer = _.get_JSON_response(name,**{"id":role_id,
                                         'name':'edited_role'})
    delete_role['role_id'] = role_id
    assert response.status_code == 200
    assert response.json() == answer



