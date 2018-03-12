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
    users = []
    for i in range(2):
        data = parse('post_users', {'$name':random_string(),
                                    '$email':random_string(),
                                    '$userType':"DEVICE"})
        response = send_request(URL.svc_users, data['request'])
        users.append(response.json())
    yield iter(users)
    for user in users:
        send_request(method = "DELETE", url=URL.svc_users, params = {'id':user['id']})

@pytest.fixture(scope="function")
def get_cms_user(send_request):
    user_data = None
    params = {"page_number":1,"page_size":100,"order":"ASC","sortedField":"name"}
    response = send_request(URL.svc_users, method="GET", params=params)
    for user in response.json()['data']:
        if user["userType"] == "CMS_USER":
            user_data = user
    return user_data

@pytest.fixture(scope="function")
def get_deleted_cms_user(send_request):
    params = {"page_number": 1, "page_size": 100, "order": "ASC", "sortedField": "name"}
    data = {"type": "CMS_USER", "value": ""}
    response = send_request(url=URL.svc_users_search, data=data, params=params)
    cms_user = random.choice(response.json()['data'])
    send_request(URL.svc_users, method="DELETE", params = {'id':cms_user['id']})
    yield cms_user
    send_request(url=URL.svc_users_sync, data={})