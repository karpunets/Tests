import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _

headers = {
    'content-type': "application/json;charset=UTF-8",
    'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h"  "Basic cm9vdDpyb290"

url_calls = "http://172.22.2.63:8080/SmiddleRecording/rec/reporter/calls"
url_empty_result = "http://172.22.2.63:8080/SmiddleQualityService/qos/result/build_empty_result"
url_edit_result = "http://172.22.2.63:8080/SmiddleQualityService/qos/result/edit_result"
url_result_approve = "http://172.22.2.63:8080/SmiddleQualityService/qos/result/result_approve"


data_calls = json.dumps({"dateFrom":1503608400000,"showUnmappedCalls":False,"pagination":{"page_number":"1","page_size":10,"sortedField":"dateStart","order":"ASC"}})
data_empty_result = {"templateId":141389096,"userId":2,"callIds":[141385835]}

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


for j in calls_id:
    count = 0
    data_empty_result["callIds"] = [j[0]]
    data_empty_result["userId"] = j[1]
    response_empty_res = requests.post(url_empty_result, data = json.dumps(data_empty_result), headers=headers)
    response_empty_res = response_empty_res.json()
    for sections in response_empty_res['sectionContainers']:
        for criterias in sections["criteriaList"]:
            criterias["score"] = 80
            count+=1
    response_edit_result = requests.post(url_edit_result, data = json.dumps(response_empty_res), headers=headers)
    print("result", response_edit_result.status_code)
    file.write(str(response_edit_result.json()['id'])+"\n")

file.close()


with open("template_ids.txt", "r") as file:
    id_to_approve = file.read().split()

for i in id_to_approve:
    response = requests.post(url_result_approve, data=json.dumps({"resultId":i}), headers=headers)
    print("approve", response.status_code)

file.close()