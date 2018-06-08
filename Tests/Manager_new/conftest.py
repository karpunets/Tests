import pytest
import random
from collections import deque
from bin.session import Client, root_group_id
from bin.helpers import make_user_group_roles
from bin.session import get_role_id
from bin.Make_requests_and_answers import parse_request, random_string


@pytest.fixture(scope="function")
def group():
    data = parse_request('post_group', {"$name": random_string(),
                                        "$parentGroupId": root_group_id()})
    response = Client.post("groups", data['request'])
    yield response.json()
    Client.delete("groups", id=response.json()['groupId'])


@pytest.fixture(scope="function")
def user(userGroupRoles, immutable_role):
    data = parse_request("post_users", {"$login": random_string(),
                                        "$fname": random_string(),
                                        "$lname": random_string(),
                                        "$roleId": immutable_role['roleId'],
                                        "$agentId": random_string(),
                                        "$ADlogin": random_string(),
                                        "$pname": random_string(),
                                        "$email": random_string() + '@.com.ua',
                                        "$phone": str(random.randint(11111, 99999999)),
                                        "$fax": random_string(),
                                        "$userGroupRoles": userGroupRoles
                                        })
    response = Client.post("users", data['request'])
    user = response.json()
    user['dateCreate'] = round(user['dateCreate']/1000) * 1000
    yield user
    Client.delete("users", id=response.json()['userId'])


@pytest.fixture(scope="module")
def immutable_user(userGroupRoles, immutable_role):
    data = parse_request("post_users", {"$login": random_string(),
                                        "$fname": random_string(),
                                        "$lname": random_string(),
                                        "$roleId": immutable_role['roleId'],
                                        "$agentId": random_string(),
                                        "$ADlogin": random_string(),
                                        "$pname": random_string(),
                                        "$email": random_string() + '@.com.ua',
                                        "$phone": str(random.randint(11111, 99999999)),
                                        "$fax": random_string(),
                                        "$userGroupRoles": userGroupRoles
                                        })
    response = Client.post("users", data['request'])
    user = response.json()
    user['dateCreate'] = round(user['dateCreate']/1000) * 1000
    yield user
    Client.delete("users", id=response.json()['userId'])


@pytest.fixture(scope="module")
def immutable_group_with_child():
    groupsId = deque([], maxlen=5)
    data = parse_request('post_group', {"$name": random_string(),
                                        "$parentGroupId": root_group_id()})
    responseParent = Client.post("groups", data['request'])
    groupsId.appendleft(responseParent.json()['groupId'])
    dataChild = parse_request('post_group', {"$name": random_string(),
                                             "$parentGroupId": groupsId[0]})
    responseChild = Client.post("groups", dataChild['request'])
    response = Client.get("groups", id=groupsId[0])
    groupsId.appendleft(responseChild.json()['groupId'])
    yield response.json()
    for id in groupsId:
        Client.delete("groups", id=id)


@pytest.fixture(scope="function")
def role(group):
    url = "roles"
    data = parse_request('post_roles', {"$name": random_string(),
                                        "$groupId": group['groupId']})
    response = Client.post(url, data['request'])
    yield response.json()
    Client.delete(url, id=response.json()['roleId'])


@pytest.fixture(scope="module")
def immutable_role(immutable_group_with_child):
    url = "roles"
    data = parse_request('post_roles', {"$name": random_string(),
                                        "$groupId": immutable_group_with_child['groupId']})
    response = Client.post(url, data['request'])
    yield response.json()
    Client.delete(url, id=response.json()['roleId'])


@pytest.fixture(scope="function")
def clear_data(request):
    url = getattr(request.cls, "url")
    group_id_list = []
    yield group_id_list
    for id_to_delete in group_id_list:
        Client.delete(url, id=id_to_delete)


@pytest.fixture(scope='module')
def immutable_deleted_user(immutable_role, userGroupRoles):
    data = parse_request("post_users", {"$login": random_string(),
                                        "$fname": random_string(),
                                        "$lname": random_string(),
                                        "$roleId": immutable_role['roleId'],
                                        "$agentId": random_string(),
                                        "$ADlogin": random_string(),
                                        "$pname": random_string(),
                                        "$password": "qwerty",
                                        "$email": random_string() + '@.com.ua',
                                        "$phone": str(random.randint(11111, 99999999)),
                                        "$fax": random_string(),
                                        "$userGroupRoles": userGroupRoles
                                        })
    data['request']['deleted'] = True
    response = Client.post("users", data['request'])
    user = response.json()
    user['dateCreate'] = round(user['dateCreate']/1000) * 1000
    yield user
    Client.delete("users", id=response.json()['userId'])


@pytest.fixture(scope="module")
def userGroupRoles(immutable_role, immutable_group_with_child):
    return make_user_group_roles({immutable_group_with_child['groupId']: immutable_role['roleId']})


@pytest.fixture(scope="function")
def add_user_with_role(request):

    def _user(role_name=None, enabled=True):
        role_name = "ROOT" if role_name is None else role_name
        role_id = get_role_id(role_name)
        user_group_and_role = make_user_group_roles({root_group_id():role_id})
        data = parse_request("post_users", {"$login": random_string(),
                                            "$fname": random_string(),
                                            "$lname": random_string(),
                                            "$password": "qwerty",
                                            "$roleId": role_id,
                                            "$agentId": random_string(),
                                            "$ADlogin": random_string(),
                                            "$pname": random_string(),
                                            "$email": random_string() + '@.com.ua',
                                            "$phone": str(random.randint(11111, 99999999)),
                                            "$fax": random_string(),
                                            "$userGroupRoles": user_group_and_role
                                            })
        data['request']['enabled'] = enabled
        response = Client.post("users", data['request'])
        print(response.json())
        user = response.json()
        user['dateCreate'] = round(user['dateCreate'] / 1000) * 1000

        def fin():
            Client.delete("users", id=user['userId'])
        request.addfinalizer(fin)
        return user
    return _user
