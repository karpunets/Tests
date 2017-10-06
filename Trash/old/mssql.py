import pytest, allure, json, requests

import random







a = {
"identifier": 142017415,
"data": [{
"ACCOUNT_NUMBER": "ContractCode",
"ABONENT_FIO": "FIO",
"RESULT_DATE": "dateCreated",
"OPERATOR_LOGIN": "AgentName",
"SUCCESS": "SUCCESS",
"CAMPAIGN": "Campaign",
"OPERATOR_ID": "Operator_id",
"CALLBACK_USED": "Callback_used",
"CALL_STATUS":"call_status",
"CALL_RESULT":"result",
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

url = "http://172.22.2.63:8080/SCM-MSSQL-Connector/scmmssql/data"

headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}


for i in range(0,100):
    b = {
        "CAMPAIGN": "campaign%s"%i,
        "ACCOUNT_NUMBER": "accountNumber%s"%i,
        "ABONENT_FIO": "f",
        "RESULT_DATE": "2017-41-41 19:00",
        "OPERATOR_ID": "id%s"%i,
        "OPERATOR_LOGIN": "login%s"%i,
        "SUCCESS": "success%s"%i,
        "CALLBACK_USED": random.randint(0,2),
        "CALL_STATUS": "status%s"%i,
        "CALL_RESULT": "result%s"%i,
        "CALLS_MADE":random.randint(0,9999),
        "RESULT_DATE_END": "2017-41-41 19:00",
    }
    a['data'].append(b)

payload = json.dumps(a)

response = requests.post(url=url, data=payload, headers=headers)


print(response.json())
