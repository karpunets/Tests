import pytest
from bin import req
from helpers.utils import root_group_id

from bin.common import parse_request, random_string


@pytest.fixture(scope='function')
def connector():
    url = "connectors"
    data = parse_request("post_connectors", {"$name": random_string(),
                                             "$url": "https://" + random_string(),
                                             "$groupId": root_group_id()})
    response = req.post(url, data['request'])
    connector = response.json()
    yield connector
    req.delete(url, id_to_url=connector['rid'])

