import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.URLs_MAP import headers


server = "http://172.22.2.63:8080"

url = "%s/SmiddleQualityService/qos/template/criteria_group"%server
url_delete_criteria = "%s/SmiddleQualityService/qos/template/criteria"%server
url_delete_group = "%s/SmiddleQualityService/qos/template/delete_criteria_group"%server

response_criterias_and_groups = requests.get(url, headers=headers)


for group in response_criterias_and_groups.json():
    for criteria in group['criteriaList']:
        response = requests.delete(url_delete_criteria, params = {"id":criteria['id']}, headers=headers)
        print(response.status_code)
    response = requests.post(url_delete_group, data=json.dumps({"criteriaGroupId":group['id']}), headers=headers)
    print(response.status_code)


