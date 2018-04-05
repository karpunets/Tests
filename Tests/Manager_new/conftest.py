import pytest
import random
from collections import deque
from bin.session import Client, rootGroupId


from bin.Make_requests_and_answers import parseRequest, random_string


@pytest.fixture(scope="function")
def group():
    data = parseRequest('post_group', {"$name": random_string(),
                                       "$parentGroupId": rootGroupId()})
    response = Client.post("groups", data['request'])
    yield response.json()
    Client.delete("groups", id=response.json()['groupId'])



@pytest.fixture(scope="module")
def immutable_user(immutable_group_with_child, immutable_role):
    data = parseRequest("post_users", {"$login":random_string(),
                                           "$fname":random_string(),
                                           "$lname":random_string(),
                                           "$groupId":immutable_group_with_child['groupId'],
                                           "$roleId":immutable_role['roleId'],
                                           "$agentId": random_string(),
                                           "$loginAD": random_string(),
                                           "$pname": random_string(),
                                           "$email": random_string()+'@.com.ua',
                                           "$phone": str(random.randint(11111, 99999999)),
                                           "$fax": random_string()
                                       })
    response = Client.post("users", data['request'])
    yield response.json()
    Client.delete("users", id=response.json()['userId'])



@pytest.fixture(scope="module")
def immutable_group_with_child():
    groupsId = deque([], maxlen=5)
    data = parseRequest('post_group', {"$name": random_string(),
                                       "$parentGroupId": rootGroupId()})
    responseParent = Client.post("groups", data['request'])
    groupsId.appendleft(responseParent.json()['groupId'])
    dataChild = parseRequest('post_group', {"$name": random_string(),
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
    data = parseRequest('post_roles', {"$name": random_string(),
                                       "$groupId": group['groupId']})
    response = Client.post(url, data['request'])
    yield response.json()
    Client.delete(url, id=response.json()['roleId'])


@pytest.fixture(scope="module")
def immutable_role(immutable_group_with_child):
    url = "roles"
    data = parseRequest('post_roles', {"$name": random_string(),
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