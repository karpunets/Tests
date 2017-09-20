import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _


url_delete_result = "http://172.22.8.102:8080/SmiddleQualityService/qos/result/delete_result"
headers = {
    'content-type': "application/json;charset=UTF-8",
    'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h"  "Basic cm9vdDpyb290"


with open("template_ids.txt", "r") as file:
    id_to_delete = file.read().split()

# url_get_ids = "http://172.22.2.63:8080/SmiddleQualityService/qos/result/get_result_list"
# response = requests.post(url_get_ids,data = json.dumps({}), headers=headers, params = {'page_number':1, "page_size":9999})


for i in id_to_delete:
    response = requests.post(url_delete_result, data = json.dumps({'resultId':i}), headers=headers)
    print(response.status_code)
    print(response.json())

file.close()