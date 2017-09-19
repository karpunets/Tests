import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _


def test_add_questioner(make_request, pre_setup):
    IDs = pre_setup
    new_random = random.sample(set(IDs), 3)
    payload = json.dumps({"name": "for_CA_test",
                          "templateId": 141383199,
                          "url": "http://172.22.2.36:9080/qualityout",
                          "active": True,
                          "mentor": 68,
                          "group": 2,
                          "criterias": [{
                              "criteriaAnswers": [{"phoneButton": 1,
                                                   "result": 20},
                                                  {"phoneButton": 2,
                                                   "result": 40},
                                                  {"phoneButton": 3,
                                                   "result": 60},
                                                  {"phoneButton": 4,
                                                   "result": 80},
                                                  {"phoneButton": 5,
                                                   "result": 100}
                                                  ],
                              "qosCriteriaId": new_random[0],
                              "questionNumber": 1},
                              {
                                  "qosCriteriaId": new_random[1],
                                  "questionNumber": 2,
                                  "criteriaAnswers": [{"phoneButton": 1,
                                                       "result": 5},
                                                      {"phoneButton": 2,
                                                       "result": 15},
                                                      {"phoneButton": 3,
                                                       "result": 30},
                                                      {"phoneButton": 4,
                                                       "result": 99},
                                                      {"phoneButton": 5,
                                                       "result": 100}
                                                      ]},
                              {
                                  "qosCriteriaId": new_random[2],
                                  "questionNumber": 3,
                                  "criteriaAnswers": [{"phoneButton": 1,
                                                       "result": 100},
                                                      {"phoneButton": 2,
                                                       "result": 0}]
                              }]})
    print(payload_questioner)
    response = requests.post(url, headers=headers, data=payload_questioner)
    print('QUESTIONER', response.json())
    return response.json()['id']


random.randint()
