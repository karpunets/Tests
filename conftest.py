import pytest
import os
from collections import deque
from helpers.api import root_group_id
from bin.common import random_string
from bin.project import send_request
from Data.URLs_MAP import mgr
from definition import ROOT_DIR



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


def pytest_sessionfinish(session):
    try:
        file_dir = os.environ['test_results_dir']
    except KeyError:
        file_dir = ROOT_DIR
    print("__________________________DIRECTORY file_dir", file_dir)
    print(os.environ)
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    with open(os.path.join(file_dir, "test_results.txt"), 'w') as f:
        if 'failed' in reporter.stats:
            f.write("FAILED: {}\n".format(len(reporter.stats['failed'])))
        else:
            f.write("FAILED: 0\n")
        if 'passed' in reporter.stats:
            f.write("PASSED: {}\n".format(len(reporter.stats['passed'])))
        else:
            f.write("PASSED: 0\n")


