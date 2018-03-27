import pytest
from collections import deque
from bin.session import Client, rootGroupId


from bin.Make_requests_and_answers import parseRequest, random_string


@pytest.fixture(scope="function")
def group():
    data = parseRequest('post_group', {"$name":random_string(),
                                "$parentGroupId":rootGroupId()})
    response = Client.post("groups", data['request'])
    yield response.json()
    Client.delete("groups", id=response.json()['groupId'])



@pytest.fixture(scope="module")
def imutableGroupWithChild():
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
def deleteRole():
    roleIdList = []
    yield roleIdList
    for id in roleIdList:
        Client.delete('roles', id=id)

@pytest.fixture(scope="function")
def deleteGroup():
    groupIdList = []
    yield groupIdList
    for id in groupIdList:
        Client.delete('groups', id=id)