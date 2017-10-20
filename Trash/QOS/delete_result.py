import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _


server = "http://172.22.2.66:8080"

url_get_ids = "%s/SmiddleQualityService/qos/result/get_result_list"%server
url_delete_result = "%s/SmiddleQualityService/qos/result/delete_result"%server
headers = {
    'content-type': "application/json;charset=UTF-8",
    'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h"  "Basic cm9vdDpyb290"

#
# with open("template_ids.txt", "r") as file:
#     id_to_delete = file.read().split()


# for i in id_to_delete:
#     response = requests.post(url_delete_result, data = json.dumps({'resultId':i}), headers=headers)
#     print(response.status_code)
#     print(response.json())

# file.close()



response = requests.post(url_get_ids,data = json.dumps({}), headers=headers, params = {'page_number':1, "page_size":9999})


for i in response.json()['data']:
    response_1 = requests.post(url_delete_result, data = json.dumps({'resultId':i['id']}), headers=headers)
    print(response_1.status_code)
