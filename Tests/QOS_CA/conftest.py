import json, pytest, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator as _
import Data.Test_data as get


@pytest.fixture(scope="module")
def pre_setup(make_request):
    criteria_names = _.make_data('criteria_names')
    group_and_criteria_id = {}
    for criteria_groups in criteria_names:
        payload = json.dumps({"groups": [{"id": 2}], "name": criteria_groups})
        response = make_request(url=URL.criteria_group, data=payload)
        criteria_group_id  = response.json()['id']
        group_and_criteria_id[criteria_group_id] = []
        for names in criteria_names[criteria_groups]:
            criteria_data = json.dumps({"name": names[0], "description": names[1], "criteriaGroup": {"id": response.json()['id']}})
            response_criteria = make_request(url=URL.criteria, data=criteria_data)
            group_and_criteria_id[criteria_group_id].append(response_criteria.json()['id'])
    yield group_and_criteria_id
    for group in group_and_criteria_id:
        for criteria in group:
            data = json.dumps({'id':criteria})
            make_request(URL.criteria, method='DELETE', params = data)
        data = {"criteriaGroupId":group}
        make_request(URL.delete_criteria_group, data)


# @pytest.fixture(scope="function")
# def add_questioner():
#     IDs = get_template()
#     new_random = random.sample(set(IDs), 3)
#     payload_questioner = json.dumps({"name": "for_CA_test",
#                             "templateId": 141383199,
#                             "url": "http://172.22.2.36:9080/qualityout",
#                             "active": True,
#                             "mentor": 68,
#                             "group": 2,
#                             "criterias": [ {
#                                             "criteriaAnswers": [{"phoneButton": 1,
#                                                                  "result": 20},
#                                                                 {"phoneButton": 2,
#                                                                  "result": 40},
#                                                                 {"phoneButton": 3,
#                                                                  "result": 60},
#                                                                 {"phoneButton": 4,
#                                                                  "result": 80},
#                                                                 {"phoneButton": 5,
#                                                                  "result": 100}
#                                                                 ],
#                                             "qosCriteriaId": new_random[0],
#                                             "questionNumber": 1},
#                                             {
#                                             "qosCriteriaId": new_random[1],
#                                             "questionNumber": 2,
#                                             "criteriaAnswers": [{"phoneButton": 1,
#                                                                   "result": 5},
#                                                                  {"phoneButton": 2,
#                                                                   "result": 15},
#                                                                  {"phoneButton": 3,
#                                                                   "result": 30},
#                                                                  {"phoneButton": 4,
#                                                                   "result": 99},
#                                                                  {"phoneButton": 5,
#                                                                   "result": 100}
#                                                                  ]},
#                                             {
#                                             "qosCriteriaId": new_random[2],
#                                             "questionNumber": 3,
#                                             "criteriaAnswers": [{"phoneButton": 1,
#                                                                  "result": 100},
#                                                                 {"phoneButton": 2,
#                                                                  "result": 0}]
#                                             }]})
#     print(payload_questioner)
#     response = requests.post(url,headers=headers, data=payload_questioner)
#     print('QUESTIONER', response.json())
#     return response.json()['id']
