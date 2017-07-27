import pytest, allure, json, requests

import random




a = {
"identifier": 116099818,
"data": [{
"CAMPAIGN": "campaign",
"ACCOUNT_NUMBER": "accountNumber",
"ABONENT_FIO": "fio",
"RESULT_DATE": "2017-01-01 15:00",
"OPERATOR_ID": "id",
"OPERATOR_LOGIN": "login",
"SUCCESS": "success",
"CALLBACK_USED": 1}]
}

url = "http://172.22.2.63:8080/SCM-MSSQL-Connector/scmmssql/data"

headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}


for i in range(0,100):
    b = {
        "CAMPAIGN": "campaign%s"%i,
        "ACCOUNT_NUMBER": "accountNumber%s"%i,
        "ABONENT_FIO": "f",
        "RESULT_DATE": "2017-41-41 9999:00",
        "OPERATOR_ID": "id%s"%i,
        "OPERATOR_LOGIN": "login%s"%i,
        "SUCCESS": "success%s"%i,
        "CALLBACK_USED": random.randint(0,2)}
    a['data'].append(b)

payload = json.dumps(a)

response = requests.post(url=url, data=payload, headers=headers)


print(response.json())