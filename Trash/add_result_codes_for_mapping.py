import pytest, json, requests


headers ={'content-type': "application/json;charset=UTF-8",
           'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h

server = "http://10.10.27.32:8080"

url = "%s/SmiddleCampaignManager/cm/manager/get_result_code"%server
get_campaign_url = "%s/SmiddleCampaignManager/cm/manager/get_campaign"%server
edit_result_code_url = '%s/SmiddleCampaignManager/cm/manager/edit_result_code'%server
get_result_code_url = '%s/SmiddleCampaignManager/cm/manager/get_result_code'%server

add_result = [  {'name':'Type', 'comment': 'Тип подключения'},
                {'name':'Service' , 'comment': 'Сервис'},
                {'name':'ActivityFeed' , 'comment': 'Канал активности'},
                {'name':'ResultKontact' , 'comment': 'Результат контакта'},
                {'name':'OutboundContactTypeOfContact' , 'comment': 'Направление активности'}
                ]



edit_result_code = {"campaign":{"id":None},"fieldOrder":None,"name":None,"code":None,"dataType":"STRING","comment":"comm","forExport":False,"forFilter":False}

get_campaign_json = {}

def get_campaign():
    payload = json.dumps(get_campaign_json)
    # Запрос на добавление пользователя
    response = requests.post(url=get_campaign_url, data=payload, headers=headers)
    return response.json()

campaign_list = get_campaign()

for i in campaign_list:
    payload = json.dumps({"campaignId":i['id']})
    response = requests.post(url=get_result_code_url, data=payload, headers=headers)

    field_order_list = []
    for k in response.json():
        field_order_list.append(int(k['fieldOrder']))

    max_field_order = max(field_order_list)

    for j in add_result:
        max_field_order +=1
        edit_result_code["fieldOrder"] = max_field_order
        edit_result_code["comment"] = j["comment"]
        edit_result_code["name"] = j['name']
        edit_result_code["code"] = j['name']
        edit_result_code["campaign"] = {"id":i['id']}
        print(edit_result_code)
        payload = json.dumps(edit_result_code)
        response = requests.post(url=edit_result_code_url, data=payload, headers=headers)
        print(response.status_code)
