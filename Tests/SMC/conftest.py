import pytest
import random
from collections import deque
from bin import req
from bin.api import  root_group_id

from bin.common import parse_request, random_string
import pymysql as db

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

