import pytest
from collections import deque
from helpers.api import root_group_id
from bin.common import random_string
from bin.project import send_request
from Data.URLs_MAP import Manager


@pytest.fixture(scope="module")
def immutable_group_with_child():
    """
    :return: {}
    """
    groups_id = deque([], maxlen=5)
    data = {"$name": random_string(),
            "$parentGroupId": root_group_id()}
    response_parent = send_request.post(Manager.groups, data)
    groups_id.appendleft(response_parent.json()['groupId'])
    data_child = {"$name": random_string(),
                  "$parentGroupId": groups_id[0]}
    response_child = send_request.post(Manager.groups, data_child)
    response = send_request.get(Manager.groups, id_to_url=groups_id[0])
    groups_id.appendleft(response_child.json()['groupId'])
    yield response.json()
    for i in groups_id:
        send_request.delete(Manager.groups, id_to_url=i)


def pytest_addoption(parser):
    # parser.addoption("--env", action="store", default=QA_ENV,
    #                  help=f"Possible environment values: {ALL_ENVS}")
    parser.addoption("--host", action="store", default=None,
                     help=f"If is not set QA host will be taken as default")



@pytest.fixture(scope="session")
def environment(request):
    option = request.config.getoption("--host")
    if not option or option.upper():
        raise EnvironmentError("Specified environment is invalid. Use --help for more information")

