import allure, pytest
from bin.session import Client, rootGroupId


from bin.Make_requests_and_answers import parseRequest, equal_schema, random_string


@pytest.fixture(scope="function")
def group():
    data = parseRequest('post_group', {"$name":random_string(),
                                "$parentGroupId":rootGroupId()})
    response = Client.post("groups", data['request'])
    yield response.json()
    Client.delete("groups", id=response.json()['groupId'])

@pytest.fixture(scope="function")
def deleteGroup():
    groupIdList = []
    yield groupIdList
    for id in groupIdList:
        Client.delete('groups', id=id)