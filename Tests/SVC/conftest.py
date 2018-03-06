import pytest
import random
import string
import time

import Data.URLs_MAP as URL
from bin.Make_requests_and_answers import parse
from bin.Make_requests_and_answers import random_string


@pytest.fixture(scope="function")
def delete_user(send_request):
    ids = []
    yield ids
    for id in ids:
        send_request(method = "DELETE", url = URL.svc_users, params = {"id":id})


@pytest.fixture(scope="function")
def add_user(send_request):
    data = parse('post_users', {'$name':random_string(),
                                '$email':random_string(),
                                '$userType':"DEVICE"})
    response = send_request(URL.svc_users, data['request'])
    user_id = response.json()['id']
    yield user_id
    send_request(method = "DELETE", url=URL.svc_users, params = {'id':user_id})