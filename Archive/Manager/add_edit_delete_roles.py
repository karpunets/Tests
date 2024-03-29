import Data.Test_data as get
import allure
import pytest

import Data.URLs_MAP as URL
from bin.common import JSON_generator as _


@pytest.fixture(scope="function")
def delete_role(send_request):
    role_id = {}
    yield role_id
    for id in role_id:
        response = send_request(url=URL.delete_role, data={'roleId': role_id[id]})
        assert response.status_code == 200


@pytest.fixture(scope='function')
def add_role(send_request):
    data = get.add_role
    response = send_request(url=URL.add_role, data=data)
    assert response.status_code==200
    role_id = response.json()['id']
    return role_id


@allure.feature('Позитивный тест')
@allure.story('Добавляем новую роль')
def test_add_new_role(send_request, delete_role):
    name ="add_role"
    data = _.get_JSON_request(name, **{'name':'test_add_role'})
    response = send_request(url=URL.add_role, data = data)
    role_id = response.json()['id']
    delete_role['role_id'] = role_id
    answer = _.get_JSON_response(name,**{"id":role_id,
                                         'name':'test_add_role'})
    assert response.status_code == 200
    assert response.json() == answer


@allure.feature('Позитивный тест')
@allure.story('Удаляем новую роль')
@pytest.mark.xfail
def test_delete_new_role(add_role, send_request):
    role_id = add_role
    data = {'roleId':role_id}
    response = send_request(url=URL.delete_role, data = data)
    assert response.status_code == 200
    assert response.json() == True


@allure.feature('Позитивный тест')
@allure.story('Редактируем новую роль')
def test_edit_new_role(add_role, send_request, delete_role):
    name ="edit_role"
    role_id = add_role
    data = _.get_JSON_request(name, **{'id':role_id,
                              'name':'edited_role'})
    response = send_request(url=URL.edit_role, data = data)
    answer = _.get_JSON_response(name,**{"id":role_id,
                                         'name':'edited_role'})
    delete_role['role_id'] = role_id
    assert response.status_code == 200
    assert response.json() == answer


@allure.feature('Негативный тест')
@allure.story('Добавляем новую роль с названием < 3 символов')
@pytest.mark.xfail
def test_add_new_role_with_2_symbols(send_request):
    name ="add_role"
    data = _.get_JSON_request(name, **{'name':'12'})
    response = send_request(url=URL.add_role, data = data)

    answer = {"ADM_VALIDATION_ROLE_NAME_LENGTH":"NAME length must be from 3 to 256"}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('Негативный тест')
@allure.story('Добавляем новую роль без группы')
def test_add_new_role_without_group(send_request):
    name ="add_role"
    data = _.get_JSON_request(name, **{'name':'test_add_role',
                                       "group": {}})
    response = send_request(url=URL.add_role, data = data)

    answer = {"ADM_VALIDATION_ROLE_GROUP_EMPTY": "GROUP not specified for not system role"}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('Негативный тест')
@allure.story('Редактируем системную рольь')
@pytest.mark.xfail
def test_edit_system_role(send_request):
    name ="edit_role"
    root_id = 3
    data = _.get_JSON_request(name, **{'id':root_id,
                              'name':'edited_role'})
    response = send_request(url=URL.edit_role, data = data)
    answer ={"COMMON_INVALID_SYSTEM_ROLE_OPARATION":"CommonInvalidSystemRoleOperation: System role can't be edited"}
    assert response.status_code == 400
    assert response.json() == answer


@allure.feature('Негативный тест')
@allure.story('Удаляем системную роль')
def test_delete_system_role(send_request):
    root_id = 3
    data = {'roleId':root_id}
    response = send_request(url=URL.delete_role, data = data)
    answer = {"COMMON_INVALID_SYSTEM_ROLE_OPARATION": "CommonInvalidSystemRoleOperation: System role can't be deleted"}
    assert response.status_code == 500
    assert response.json() == answer


@allure.feature('Позитивный тест')
@allure.story('Добавляем новую роль и копируем настройки с Root роли')
@pytest.mark.xfail
def test_add_new_role_with_root_settings(send_request, delete_role):
    name ="add_role"
    data = _.get_JSON_request(name, **{'name':'test_add_role',
                                       "roleTemplateId": 3})
    response = send_request(url=URL.add_role, data = data)
    role_id = response.json()['id']
    delete_role['role_id'] = role_id
    answer = _.get_JSON_response(name,**{"id":role_id,
                                         'name':'test_add_role',
                                         "roleTemplateId": 3})
    assert response.status_code == 200
    assert response.json() == answer


@allure.feature('Позитивный тест')
@allure.story('Добавляем новую роль и даем Root access и удаляем')
def test_add_delete_role_access(add_role, send_request, delete_role):
    role_id = add_role
    data = _.get_JSON_request("add_role_access", **{'roleId':role_id,
                                                    "access": 3})
    response = send_request(url=URL.add_role_access, data = data)
    delete_role['role_id'] = role_id
    answer ={'roleId':role_id, "access": 3}
    assert response.status_code == 200
    assert response.json() == answer
    data = _.get_JSON_request("delete_role_access", **{'roleId': role_id,
                                                    "access": 3})
    response = send_request(url=URL.delete_role_access, data=data)
    assert response.status_code == 200
    assert response.json() == True


@allure.feature('Негативный тест')
@allure.story('Добавляем новую роль и даем не правильный access и role_id')
@pytest.mark.xfail
def test_add_role_access_wrong_IDs(send_request):
    name = "add_role_access"
    data = _.get_JSON_request(name, **{'roleId':99999999999999,
                                       "access": 33333333333333})
    response = send_request(url=URL.add_role, data = data)

    answer ={"COMMON_DISALLOWED_IDS_EXCEPTION": "CommonDisallowedIDsException: Prohibited IDs"}
    assert response.status_code == 500
    assert response.json() == answer


@allure.feature('Негативный тест')
@allure.story('Удаляем access в не существующей role_id и access')
@pytest.mark.xfail
def test_add_role_access_wrong_IDs(send_request):
    name = "delete_role_access"
    data = _.get_JSON_request(name, **{'roleId':99999999999999,
                                       "access": 33333333333333})
    response = send_request(url=URL.add_role, data = data)

    answer ={"COMMON_DISALLOWED_IDS_EXCEPTION": "CommonDisallowedIDsException: Prohibited IDs"}
    assert response.status_code == 500
    assert response.json() == answer


@allure.feature('Позитивный тест')
@allure.story('Для новой роли по очереди задаем значения прав ролей')
def test_edit_new_role_tasks(add_role, send_request, delete_role):
    role_id = add_role
    delete_role['role_id'] = role_id
    response = send_request(url=URL.get_task_list, data={"roleId": role_id})
    task_list = response.json()
    print(len(task_list['tasks']))
    assert len(task_list['tasks']) == 154
    for i in task_list['tasks']:
        i['value'] = 1
        response = send_request(url=URL.set_tasks_to_role, data=task_list)
        assert response.status_code == 200
