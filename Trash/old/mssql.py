import pytest, allure, json, requests

import random







a = {
"identifier": 142017415,
"data": [{
"ACCOUNT_NUMBER": "ContractCode",
"ABONENT_FIO": "FIO",
"RESULT_DATE": "10.10.2017 19:00",
"OPERATOR_LOGIN": "AgentName",
"SUCCESS": "SUCCESS",
"CAMPAIGN": "Campaign",
"OPERATOR_ID": "Operator_id",
"CALLBACK_USED": 0,
"CALL_STATUS":"call_status",
"CALL_RESULT":"result",
"CALLS_MADE":15,
"RESULT_DATE_END":"10.10.2017 19:00"

}]
}



# a = {
# "identifier": 116099818,
# "data": [{
# "CAMPAIGN": "campaign",
# "ACCOUNT_NUMBER": "ContractCode",
# "ABONENT_FIO": "fio",
# "RESULT_DATE": "2017-01-01 15:00",
# "OPERATOR_ID": "id",
# "OPERATOR_LOGIN": "login",
# "SUCCESS": "success",
# "CALLBACK_USED": 1}]
# }

url = "http://10.101.10.188:8080/scmmssql/data"

headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}


for i in range(0,105):
    b = {
        "CAMPAIGN": "campaign%s"%i,
        "ACCOUNT_NUMBER": "accountNumber%s"%i,
        "ABONENT_FIO": "FIO%s"%i,
        "RESULT_DATE": "10.10.2017 19:00",
        "OPERATOR_ID": "id%s"%i,
        "OPERATOR_LOGIN": "login%s"%i,
        "SUCCESS": "success%s"%i,
        "CALLBACK_USED": random.randint(0,2),
        "CALL_STATUS": "status%s"%i,
        "CALL_RESULT": "result%s"%i,
        "CALLS_MADE":random.randint(0,9999),
        "RESULT_DATE_END": "10.10.2017 19:00"
    }
    a['data'].append(b)

print(a)
payload = json.dumps(a)

response = requests.post(url=url, data=payload, headers=headers)

print(response.status_code)
print(response.json())
