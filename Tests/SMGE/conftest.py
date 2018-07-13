import pytest
import random
from collections import deque
from bin.session import Client, root_group_id
from bin.helpers import make_user_group_roles
from bin.session import get_role_id
from bin.common import parse_request, random_string


@pytest.fixture(scope='function')
def connector():
    url = "connectors"
    data = parse_request("post_connectors", {"$name": random_string(),
                                             "$url": "https://" + random_string(),
                                             "$groupId": root_group_id()})
    response = Client.post(url, data['request'])
    connector = response.json()
    yield connector
    Client.delete(url, id=connector['rid'])