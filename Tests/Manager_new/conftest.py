import allure, pytest
from bin.session import Client


from bin.Make_requests_and_answers import parse, equal_schema, random_string


@pytest.fixture(scope="function")
def add_group():
    a=1