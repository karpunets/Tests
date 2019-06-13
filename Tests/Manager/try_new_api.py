# -*- coding: utf-8 -*-

import allure
import pytest
import random

from bin.project import send_request
from bin.validator import equal_schema
from bin.api import root_group_id
from bin.common import random_string
from Data.URLs_MAP import Manager



@allure.feature('Функциональный тест')
@allure.story('Создаем группу')
def test_add_group():
    data = {"$name": random_string(),
            "$parentGroupId": root_group_id()}
    response = send_request.post(Manager.groups, data)
    assert equal_schema(response.json(), response.expected)
    assert response.status_code == 201