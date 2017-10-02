import pytest, json, requests

headers = {'content-type': "application/json;charset=UTF-8",
           'authorization': "Basic di5rbGl1aTp1Zmtmcm5icmY="}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h

server = "http://172.22.8.103:8080"

campaign_code = "qwrasd"
campaign_id = 868159

# url = "%s/SmiddleCampaignManager/cm/manager/get_result_code"%server
# get_campaign_url = "%s/SmiddleCampaignManager/cm/manager/get_campaign"%server
# edit_result_code_url = '%s/SmiddleCampaignManager/cm/manager/edit_result_code'%server
# get_result_code_url = '%s/SmiddleCampaignManager/cm/manager/get_result_code'%server
# edit_result_variant = '%s/SmiddleCampaignManager/cm/manager/edit_result_variant'%server

# add_result = [  {'name':'Campaign', 'comment': 'Campaign_code for MSSQL',"dataType":"STRING"},
#                 {'name':'Operator_id' , 'comment': 'Agent_id for MSSQL',"dataType":"STRING"},
#                 {'name':'Callback_used' , 'comment': 'Callback_used for MSSQL' ,"dataType":"INTEGER"}
#                 ]


url = "%s/SmiddleCampaignManager/cm/manager/resultcode" % server
get_campaign_url = "%s/SmiddleCampaignManager/cm/uccx/campaign" % server
result_code_url = "%s/SmiddleCampaignManager/cm/manager/resultcode" % server
fields = "%s/SmiddleCampaignManager/cm/settings/fields"%server

# Считывем результаты с файла
with open('JSON_files/result_codes.json', encoding="utf8") as data_file:
    add_result = json.load(data_file)

add_mapfield_json = {"order": "1", "forExport": None, "forFilter": None, "phoneNumber": None, "enabled": None,
                     "deleted": None, "name": "123", "fieldImport": "123", "dataType": "STRING",
                     "fieldAbonent": "ClientID", "campaign": {"id": campaign_id}}
edit_result_code = {"campaign": {"id": None}, "fieldOrder": None, "name": None, "code": None, "dataType": "STRING",
                    "comment": "comm", "forExport": False, "forFilter": False}


def get_campaign():
    # Запрос на добавление пользователя
    response = requests.get(url=get_campaign_url, headers=headers)
    return response.json()


# Для одной кампании
campaign_list = [{id: campaign_id, "code": campaign_code, "name": "qqweqqwr", "comment": "11231", "deleted": False,
                  "groups": [{id: 2}]}]
#Для всех кампаний
campaign_list = get_campaign()

for i in campaign_list:

    response = requests.get(url=result_code_url, params={"code": campaign_code}, headers=headers)

    field_order_list = []
    for k in response.json():
        field_order_list.append(int(k['fieldOrder']))

    max_field_order = max(field_order_list)

    for j in add_result:
        max_field_order += 1
        edit_result_code["fieldOrder"] = max_field_order
        edit_result_code["comment"] = j["comment"]
        edit_result_code["name"] = j['name']
        edit_result_code["code"] = j['name']
        edit_result_code["dataType"] = j["dataType"]
        edit_result_code['forExport'] = j['forExport']
        edit_result_code['forFilter'] = j['forFilter']
        # #Для всех кампаний
        # edit_result_code["campaign"] = {"id":i['id']}
        # #Для одной кампании
        edit_result_code["campaign"] = {"id": campaign_id}
        print(edit_result_code)
        payload = json.dumps(edit_result_code)
        response = requests.post(url=result_code_url, data=payload, headers=headers)
        print(response.status_code, response.json())


def add_mapping():
    with open('JSON_files/mapfields.json', encoding="utf8") as data_file:
        add_mapfield = json.load(data_file)
    for field in add_mapfield:
        for j in field:
            print(j)
            if j != 'id':
                add_mapfield_json[j] = field[j]
        payload = json.dumps(add_mapfield_json)
        response = requests.post(fields, data=payload, headers=headers)
        print(response.status_code)
add_mapping()

            # for j in campaign_list:
            #     payload = json.dumps({"campaignCode":j['code'], "resultCode":"inquiryTime","resultVariant":{"value":"27316628","forInit":True}})
            #     response = requests.post(url=edit_result_variant, data=payload, headers=headers)
            #     print(response.status_code, response.json())
            #     payload = json.dumps({"campaignCode":j['code'],"resultCode":"activityFeed","resultVariant":{"value":"1","forInit":True}})
            #     response = requests.post(url=edit_result_variant, data=payload, headers=headers)
            #     print(response.status_code, response.json())
