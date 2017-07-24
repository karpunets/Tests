import string, random


root_group_id = 2
scb_settings_id = 2797954




def random_code():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))


def defaul_request(request_name):
    list_of_default_requests = {
        'get_user_list':{"fName":None,"lName":None,"pName":None,"roleId":None,"groupId":None,"login":None,"adLogin":None,"agentId":None,
                         "showDeletedOnly":False,"phone":None,"pagination":{"page_number":"1","page_size":"10","sortedField":"login","order":"ASC"}},

    'add_user':{"fname":None,"lname":None,"pname":None,"email":None,"phone":None,"fax":None,"login":None,"password":None,
                "loginAD":None,"agentId":None,"scMode":"0","unmappedCalls":False,"enabled":True,"deleted":False,
                "dateCreate":1494845540000,"groups":[{"id":root_group_id}],"roles":[{"id":3}]},
    'add_group':{"name":None,"parent":{"id":root_group_id}},
    'delete_user': {"userId": None},
    'edit_user':{"id":None,"fname":None,"lname":None,"pname":None,"email":None,"phone":None,
                 "fax":None,"login":None,"password":None,"loginAD":None,"agentId":None,"scMode":"0","unmappedCalls":False,
                 "enabled":True,"deleted":False,"dateCreate":1494845540000,"groups":[{"id":root_group_id}],"roles":[{"id":3}]},
    "delete_group": {"groupId":None},
    "edit_group": {"id":None,"name":None,"parent":{"id":root_group_id}},
        'add_role':{"name":None,"roleTemplateId":None,"group":{"id":root_group_id}},
        'edit_role':{"id":None,"name":None,"group":{"id":root_group_id}},
        'delete_role':{"roleId":None},
        'add_role_access':{'roleId':None, 'access':None},
        'delete_role_access': {'roleId':None, 'access':None},
        'Manager_logs':{"moduleName":"Settings Controller","messageParams":["message"],"types":["SYSTEM"],"action":"get_menu_for_role",
                "dateFrom":1495462096000,"dateTo":1495721296000},
        'Manager_settings': {"id":1,"debugLevel":"1","logLength":"200"},
        'test_domain':{"domainName":"smidle.lab","ldapServerIp":"172.22.2.11","serviceUser":"Administrator","perPage":'10',"serviceUserPassword":"Smidle098adm!","description":"smidle.lab"},
        'add_campaign':{"campaign":{"code":random_code(),"name":"auto_test_campaign","comment":"auto_test","groups":[{"id":root_group_id}]},
                        "skillGroups":[{"refURL":"/unifiedconfig/config/skillgroup/5019","changeStamp":0,"agentCount":2,
                                        "agents":[{"refURL":"/unifiedconfig/config/agent/5060","name":None},{"refURL":"/unifiedconfig/config/agent/5063","name":None}],
                                        "agentsAdded":None,"agentsRemoved":None, "bucketInterval":None,"correlationId":None,"department":None,"description":None,"markDeletable":None,
                                        "mediaRoutingDomain":{"refURL":"/unifiedconfig/config/mediaroutingdomain/1","name":"Cisco_Voice"},"name":"test1",
                                        "peripheral":{"refURL":None,"changeStamp":None,"id":5000,"name":"PIM_CUCM"},"peripheralNumber":5020,"selectedAgentCount":None,
                                        "serviceLevelThreshold":None,"serviceLevelType":None}],
                        "timeZone":{"refURL":"/unifiedconfig/config/timezone/Dateline%20Standard%20Time","changeStamp":None,"bias":720,
                                    "displayName":"(UTC-12:00) International Date Line West","dstName":"Dateline Daylight Time","dstObserved":False,
                                    "name":"Dateline Standard Time","stdName":"Dateline Standard Time"},
                        "dialingMode":"INBOUND",
                        "dialedNumber":"123213"},
        'add_result_code':{"campaign":{"id":119696173},"fieldOrder":"4","name":"123","code":"123","dataType":"STRING","forExport":True,"forFilter":True},
        'edit_result_variant': {"campaignCode":None,"resultCode":"123","resultVariant":{"value":"q","forInit":True}},
        'add_map_field':{'id':None, "order":"1","forExport":False,"forFilter":False,"phoneNumber":False, "phoneType":None, "enabled":True,"deleted":False,"name":None,
                         "fieldImport":None,"dataType":"STRING","fieldAbonent":None,"campaign":{"id":None}},
        #Smart_Callback
        'add_route':{"agentNumber": None, "clientPhone": None, "callDate": 1500292769604},
        'scb_settings':{"id": scb_settings_id,"debugLevel": 2,"logLength": 200,"monitoring": True,"smartLabel": True, "routing": True}
    }

    return list_of_default_requests[request_name]



