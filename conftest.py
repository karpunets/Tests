import pytest
from collections import deque
from helpers.api import root_group_id
from bin.common import random_string
from bin.project import send_request
from Data.URLs_MAP import mgr
from bin.project_config import cfg
from definition import LAST_TEST_RESULTS



def pytest_sessionfinish(session, exitstatus):
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    with open(LAST_TEST_RESULTS, 'w') as f:
        if 'failed' in reporter.stats:
            f.write("FAILED: {}\n".format(len(reporter.stats['failed'])))
        else:
            f.write("FAILED: 0\n")
        if 'passed' in reporter.stats:
            f.write("PASSED: {}\n".format(len(reporter.stats['passed'])))
        else:
            f.write("PASSED: 0\n")




@pytest.fixture(scope="module")
def immutable_group_with_child():
    """
    :return: {}
    """
    groups_id = deque([], maxlen=5)
    data = {"$name": random_string(),
            "$parentGroupId": root_group_id()}
    response_parent = send_request.post(mgr.groups, data)
    groups_id.appendleft(response_parent.json()['groupId'])
    data_child = {"$name": random_string(),
                  "$parentGroupId": groups_id[0]}
    response_child = send_request.post(mgr.groups, data_child)
    response = send_request.get(mgr.groups, id_to_url=groups_id[0])
    groups_id.appendleft(response_child.json()['groupId'])
    yield response.json()
    for i in groups_id:
        send_request.delete(mgr.groups, id_to_url=i)


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
    print("OPTION", option)
    return cfg.set_host(option)


# @pytest.fixture(scope="session")
# def add_to_config(enviroment):
#     return cfg.set_host(enviroment)