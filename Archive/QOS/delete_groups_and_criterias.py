import requests, json

url = "http://172.22.2.66:8080/SmiddleQualityService/qos/template/criteria_group"
url_delete_criteria = "http://172.22.2.66:8080/SmiddleQualityService/qos/template/criteria"
url_delete_criteria_group = "http://172.22.2.66:8080/SmiddleQualityService/qos/template/delete_criteria_group"
headers = {
    'content-type': "application/json;charset=UTF-8",
    'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}

response_get = requests.get(url=url, headers=headers)


for i in response_get.json():
    for j in i['criteriaList']:
        response = requests.delete(url_delete_criteria, params = {'id':j['id']}, headers=headers)
        print(response.status_code)
    payload = json.dumps({"criteriaGroupId": i['id']})
    response = requests.post(url_delete_criteria_group, data=payload, headers=headers)
    print(response.status_code)