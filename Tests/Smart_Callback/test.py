import pytest, allure, json, requests, random, os
import Data.URLs_MAP as URL
import Data.Test_data as get

from Data.Make_requests_and_answers import JSON_generator as _




url = 'http://172.22.2.63:8080/SmiddleSmartCallback/scb/contact'
authorization = ('bitbok', 'bitbok')

headers = {'content-type': "application/json;charset=UTF-8"}



def test_qq():
    for i in range(5):
        payload = json.dumps({
            "fName": "Victor19"+str(random.randint(0,999)),
            "lName": "Kliui191"+str(random.randint(0,999)),
            "pName": None,
            "description": None,
            "createdDate": 1501075611720,
            "phones": [{"phoneNumber": str(random.randint(1111111,9999999)), "phoneType": "MOBILE", "comment": None},
                       {"phoneNumber": str(random.randint(1111111,9999999)), "phoneType": "HOME", "comment": None},
                       {"phoneNumber": str(random.randint(1111111,9999999)), "phoneType": "WORK", "comment": None}]
        })
        response = requests.post(url=url, headers=headers, auth=authorization, data=payload)
        print(response.status_code)





# def test_qq():
#     params = {'page_number':'1','page_size':'100'}
#     response = requests.get(url=url, params=params, auth = authorization)
#     for i in response.json():
#         response = requests.delete(url=url, auth = authorization, params={'id':i['id']})
#         print(response.json())

