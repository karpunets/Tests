import json, requests, random

authorization = ('Root', 'Smidle098adm!')
headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}
url = "http://172.22.2.63:8080/SmiddleQualityService_CA/qos/ca/questioner"
criteria_url = "http://172.22.2.63:8080/SmiddleQualityService/qos/template/criteria_group"
filter_url = "http://172.22.2.63:8080/SmiddleQualityService_CA/qos/ca/questioner/filter"
abonent_url = "http://172.22.2.63:8080/SmiddleQualityService_CA/qos/ca/questioner/filter/phone/import"
agent_url = "http://172.22.2.63:8080/SmiddleQualityService_CA/qos/ca/questioner/filter/agent"

def delete_questioner():
    get_response = requests.get(url=url, headers=headers)
    for i in get_response.json():
        delete_response = requests.delete(url, headers=headers, params = {'id':i['id']})
        print(delete_response.status_code)



def add_questioner():
    IDs = [140530159, 140530173, 140530183, 140530198, 140530213, 140530222, 140530234]
    criteriaList_id =[]
    for i in IDs:
        get_criteria_response = requests.get(criteria_url, headers=headers, params={'id':i})
        for j in get_criteria_response.json()['criteriaList']:
            criteriaList_id.append(j['id'])
    new_random = random.sample(set(criteriaList_id), 3)
    payload_questioner = json.dumps({  "name": "for_CA_test",
                            "templateId": 140571874,
                            "url": "http://172.22.2.36:9080/qualityout",
                            "active": True,
                            "mentor": 68,
                            "group": 2,
                            "criterias": [ {
                            "qosCriteriaId": new_random[0],
                            "questionNumber": 1}, {
                            "qosCriteriaId": new_random[1],
                            "questionNumber": 2}, {
                            "qosCriteriaId": new_random[2],
                            "questionNumber": 3}]})
    response = requests.post(url,headers=headers, data=payload_questioner)
    print('QUESTIONER', response.json()['id'])
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

filter_id =140572705


def add_phones():
    files = {'file':open('phones.xlsx', 'rb')}
    response = requests.post(abonent_url,  params = {'filterId':filter_id}, files=files, auth = authorization)
    print(response.status_code)



def add_agent():
    payload = json.dumps( {
                        "agent": {"id": 139973039},
                        "filter": {
                        "id": filter_id}})
    response = requests.post(agent_url, data=payload, headers=headers)
    print(response.status_code)
    print(response.json())

add_agent()