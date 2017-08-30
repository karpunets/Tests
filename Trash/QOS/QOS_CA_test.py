import json, requests, random

authorization = ('Root', 'Smidle098adm!')
headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}
server = "http://172.22.2.63:8080"
url = "%s/SmiddleQualityService_CA/qos/ca/questioner"%server
criteria_url = "%s/SmiddleQualityService/qos/template/criteria_group"%server
filter_url = "%s/SmiddleQualityService_CA/qos/ca/questioner/filter"%server
abonent_url = "%s/SmiddleQualityService_CA/qos/ca/questioner/filter/phone/import"%server
agent_url = "%s/SmiddleQualityService_CA/qos/ca/questioner/filter/agent"%server
template_url = "%s/SmiddleQualityService/qos/template/get_template"%server

def delete_questioner():
    get_response = requests.get(url=url, headers=headers)
    for i in get_response.json():
        delete_response = requests.delete(url, headers=headers, params = {'id':i['id']})
        print(delete_response.status_code)
        print(delete_response.json())



def get_template():
    template_id = 141383199
    payload = json.dumps({"templateId":template_id})
    template_criteria_id = []
    response = requests.post(url=template_url, data=payload, headers=headers)
    for i in response.json()['templateSections']:
        for j in i['templateCriterias']:
            template_criteria_id.append(j['id'])
    return template_criteria_id




def add_questioner():
    IDs = get_template()
    new_random = random.sample(set(IDs), 3)
    payload_questioner = json.dumps({"name": "for_CA_test",
                            "templateId": 141383199,
                            "url": "http://172.22.2.36:9080/qualityout",
                            "active": True,
                            "mentor": 68,
                            "group": 2,
                            "criterias": [ {
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
    response = requests.post(url,headers=headers, data=payload_questioner)
    print('QUESTIONER', response.json())
    return response.json()['id']

def add_filter():
    id = add_questioner()
    payload = json.dumps({"durationFrom": 1,
                                 "durationTo": 15,
                                 "callDirection": "DIRECTION_OUT",
                                 "questioner": {
                                     "id": id}})
    response = requests.post(url=filter_url, data=payload, headers=headers)
    print(response.json())
    print('FILTER', response.json()['id'])
    return response.json()['id']


filter_id =add_filter()


def add_phones():
    files = {'file':open('phones.xlsx', 'rb')}
    response = requests.post(abonent_url,  params = {'filterId':filter_id}, files=files, auth = authorization)
    print(response.status_code)
    print(response.json())


def add_agent():
    agent_ids = [139687208, 139973039]
    for id in agent_ids:
        payload = json.dumps( {
                            "agent": {"id": id},
                            "filter": {"id": filter_id}})
        response = requests.post(agent_url, data=payload, headers=headers)
        print(response.status_code)
        print(response.json())

def delete_agents():
    response_get = requests.get(url=agent_url, headers=headers)
    for i in response_get.json():
        response = requests.delete(agent_url, headers=headers, params = {'id':i['id']})
        print(response.status_code)
        print(response.json())


add_agent()
add_phones()

# delete_agents()
# delete_questioner()