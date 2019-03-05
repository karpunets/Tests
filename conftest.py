import pytest
from collections import deque
from bin.api import root_group_id
from bin.common import parse_request, random_string
from bin.client import send_request


@pytest.fixture(scope="function")
def clear_data(request):
    url = getattr(request.cls, "url")
    group_id_list = []
    yield group_id_list
    for id_to_delete in group_id_list:
        send_request.delete(url, id_to_url=id_to_delete)


@pytest.fixture(scope="module")
def immutable_group_with_child():
    """
    :return: {}
    """
    groups_id = deque([], maxlen=5)
    data = parse_request('Tests/Manager/Test_data/post_group', {"$name": random_string(),
                                        "$parentGroupId": root_group_id()})
    response_parent = send_request.post("groups", data['request'])
    groups_id.appendleft(response_parent.json()['groupId'])
    data_child = parse_request('Tests/Manager/Test_data/post_group', {"$name": random_string(),
                                             "$parentGroupId": groups_id[0]})
    response_child = send_request.post("groups", data_child['request'])
    response = send_request.get("groups", id_to_url=groups_id[0])
    print(response.json())
    groups_id.appendleft(response_child.json()['groupId'])
    yield response.json()
    for id in groups_id:
        send_request.delete("groups", id_to_url=id)


@pytest.fixture(scope="module")
def teardown_clear():
    return