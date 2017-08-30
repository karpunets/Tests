import json, pytest, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator as _
import Data.Test_data as get


@pytest.fixture(scope="module")
def pre_setup(make_request):
    criteria_names = _.make_data('criteria_names')
    group_id = []
    names_id = []
    for criteria_groups in criteria_names:
        payload = json.dumps({"groups": [{"id": 2}], "name": criteria_groups})
        response = make_request(url=URL.criteria_group, data=payload)
        group_id.append(response.json()['id'])
        for names in criteria_names[criteria_groups]:
            criteria_data = json.dumps({"name": names[0], "description": names[1], "criteriaGroup": {"id": response.json()['id']}})
            response_criteria = make_request(url=URL.criteria, data=criteria_data)
            names_id.append(response_criteria.json()['id'])
    yield 


@pytest.fixture(scope="function")
def add_questioner(make_request):
    