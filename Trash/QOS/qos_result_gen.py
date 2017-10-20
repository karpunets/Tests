import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _


headers = {
    'content-type': "application/json;charset=UTF-8",
    'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h"  "Basic cm9vdDpyb290" "Basic Yml0Ym9rOmJpdGJvaw=="

server = "http://172.22.2.66:8080"
##63
# template_id = 141389096
#66
template_id = 217927458
groups = [126018576]


url_calls = "%s/SmiddleRecording/rec/reporter/calls"%server
url_empty_result = "%s/SmiddleQualityService/qos/result/build_empty_result"%server
url_edit_result = "%s/SmiddleQualityService/qos/result/edit_result"%server
url_result_approve = "%s/SmiddleQualityService/qos/result/result_approve"%server


count_of_results = 66


for group in groups:
    data_calls = json.dumps({"dateFrom":1500325200000,"dateTo":1500379200000,"showUnmappedCalls":False,"pagination":{"page_number":"1","page_size":count_of_results,"sortedField":"dateStart","order":"ASC"}})

    # data_calls = json.dumps({"dateFrom": 1503498793000, "showUnmappedCalls": False, "pagination": {"page_number": "1", "page_size": count_of_results,
    #                                         "sortedField": "dateStart",
    #                                         "order": "ASC"}})
    data_empty_result = {"templateId": template_id, "userId": 2, "callIds": [141385835]}

    calls_id = []
    response_calls = requests.post(url_calls, data=data_calls, headers=headers)
    file = open("template_ids.txt", "w")
    for i in response_calls.json()['data']:
        id_and_userid = []
        id_and_userid.append(i['id'])
        for user in i["participants"]:
            if user['user'] != None:
                id_and_userid.append(user['user']['id'])
        calls_id.append(id_and_userid)

    estimate = 33
    for j in calls_id:
        count = 0
        data_empty_result["callIds"] = [j[0]]
        data_empty_result["userId"] = j[1]
        response_empty_res = requests.post(url_empty_result, data=json.dumps(data_empty_result), headers=headers)
        response_empty_res = response_empty_res.json()
        for sections in response_empty_res['sectionContainers']:
            for criterias in sections["criteriaList"]:
                # criterias["score"] = random.randint(0, 100)
                criterias["score"] = estimate
                count += 1
        response_edit_result = requests.post(url_edit_result, data=json.dumps(response_empty_res), headers=headers)
        print("result", response_edit_result.status_code)
        file.write(str(response_edit_result.json()['id']) + "\n")
        estimate += 1

    file.close()

    with open("template_ids.txt", "r") as file:
        id_to_approve = file.read().split()
    count = 1
    for i in id_to_approve:
        response = requests.post(url_result_approve, data=json.dumps({"resultId": i}), headers=headers)
        print("approve", response.status_code)
        count += 1
    print(count)

file.close()
