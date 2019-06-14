import pytest
import random
from bin.project import send_request
from bin.api import root_group_id
from bin.helpers import make_user_group_roles
from bin.api import get_role_id
from bin.common import random_string
from Data.URLs_MAP import Manager
#
#
# @pytest.fixture(scope="function")
# def group():
#     data = parse_request('post_group', {"$name": random_string(),
#                                         "$parentGroupId": root_group_id()})
#     response = send_request.post("groups", data['request'])
#
#     yield response.json()
#     send_request.delete("groups", id_to_url=response.json()['groupId'])
#
#
# @pytest.fixture(scope="function")
# def user(userGroupRoles, immutable_role):
#     data = parse_request("post_users", {"$login": random_string(),
#                                         "$fname": random_string(),
#                                         "$lname": random_string(),
#                                         "$roleId": immutable_role['roleId'],
#                                         "$agentId": random_string(),
#                                         "$ADlogin": random_string(),
#                                         "$pname": random_string(),
#                                         "$email": random_string() + '@.com.ua',
#                                         "$phone": str(random.randint(11111, 99999999)),
#                                         "$fax": random_string(),
#                                         "$userGroupRoles": userGroupRoles
#                                         })
#     response = send_request.post("users", data['request'])
#     user = response.json()
#     user['dateCreate'] = round(user['dateCreate']/1000) * 1000
#     yield user
#     send_request.delete("users", id_to_url=response.json()['userId'])
#
#
@pytest.fixture(scope="module")
def immutable_user(userGroupRoles, immutable_role):
    data = {"$login": random_string(),
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
            }
    response = send_request.post(Manager.users, data)
    user = response.json()
    user['dateCreate'] = round(user['dateCreate']/1000) * 1000
    yield user
    send_request.delete("users", id_to_url=response.json()['userId'])
#
#
#
# @pytest.fixture(scope="function")
# def role(group):
#     url = "roles"
#     data = parse_request('post_roles', {"$name": random_string(),
#                                         "$groupId": group['groupId']})
#     response = send_request.post(url, data['request'])
#     yield response.json()
#     send_request.delete(url, id_to_url=response.json()['roleId'])
#
#
@pytest.fixture(scope="module")
def immutable_role(immutable_group_with_child):
    data = {"$name": random_string(),
            "$groupId": immutable_group_with_child['groupId']}
    response = send_request.post(Manager.roles, data)
    yield response.json()
    send_request.delete(Manager.roles, id_to_url=response.json()['roleId'])


@pytest.fixture(scope='module')
def immutable_deleted_user(immutable_role, userGroupRoles):
    data = {"$login": random_string(),
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
            }
    data['request']['deleted'] = True
    response = send_request.post(Manager.users, data)
    user = response.json()
    user['dateCreate'] = round(user['dateCreate']/1000) * 1000
    return user
#
#
#
@pytest.fixture(scope="module")
def userGroupRoles(immutable_role, immutable_group_with_child):
    return make_user_group_roles({immutable_group_with_child['groupId']: immutable_role['roleId']})
#
#
# @pytest.fixture(scope="function")
# def add_user_with_role(request):
#
#     def _user(role_name=None, enabled=True):
#         role_name = "ROOT" if role_name is None else role_name
#         role_id = get_role_id(role_name)
#         user_group_and_role = make_user_group_roles({root_group_id():role_id})
#         data = parse_request("post_users", {"$login": random_string(),
#                                             "$fname": random_string(),
#                                             "$lname": random_string(),
#                                             "$password": "qwerty",
#                                             "$roleId": role_id,
#                                             "$agentId": random_string(),
#                                             "$ADlogin": random_string(),
#                                             "$pname": random_string(),
#                                             "$email": random_string() + '@.com.ua',
#                                             "$phone": str(random.randint(11111, 99999999)),
#                                             "$fax": random_string(),
#                                             "$userGroupRoles": user_group_and_role
#                                             })
#         data['request']['enabled'] = enabled
#         response = send_request.post("users", data['request'])
#         print(response.json())
#         user = response.json()
#         user['dateCreate'] = round(user['dateCreate'] / 1000) * 1000
#
#         def fin():
#             send_request.delete("users", id_to_url=user['userId'])
#         request.addfinalizer(fin)
#         return user
#     return _user
