import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _
from Data.Test_data import random_name


def test_add_group(make_request, delete_group):
    payload = json.dumps({"groups":[{"id":2}],"name":random_name})
    response = make_request(URL.criteria_group, payload)
    assert response.status_code == 200
