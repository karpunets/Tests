def defaul_response(response_name):

    list_of_default_requests = {
        'get_user_list':{"page_number":1,"page_size":10,"sortedField":"login","order":"ASC","row_count":1,"data":
                        [{"id":1,"agentId":None,"login":None,"loginAD":None,"lname":None,
                        "fname":None,"pname":None,"email":None,"phone":"999","fax":None,"locale":None,
                        "dateCreate":1494845540000,"scMode":0,"unmappedCalls":False,"enabled":True,"deleted":False,
                        "groups":[{"id":2,"name":"ROOT"}],"roles":[{"id":3,"name":"ROOT"}],"userGroupRoles":None}]},
        'add_user':{"id": 582848,"agentId": None,"login": None, "loginAD": None, "lname": None, "fname": None, "pname": None, "email": None,
                    "phone": None,"fax": None,"locale": None,"dateCreate": 1494845540000, "scMode": 0,
                    "unmappedCalls": False,"enabled": True,"deleted": False,"groups":
                    [{"id": 2,"name": "ROOT"}],"roles": [{"id": 3,"name": "ROOT"}],"userGroupRoles": None},
        'delete_user':{"userId": None},
        'edit_user': {'id': 19755723, 'agentId': None, 'login': None, 'loginAD':None,
                      'lname': None, 'fname': None, 'pname': None, 'email': None, 'phone': None,
                      'fax': None, 'locale': None, 'dateCreate': 1494845540000, 'scMode': 0, 'unmappedCalls': False,
                      'enabled': True, 'deleted': False, 'groups': [{'id': 2, 'name': 'ROOT'}],
                      'roles': [{'id': 3, 'name': 'ROOT'}], 'userGroupRoles': None},
        'add_group': {"id":731148,"name":"qqq","children":[],"cid":731148},
        'delete_group': True,
        "edit_group": {"id":None,"name":None,"children":[],"cid":None},
        'add_role':{"id":None,"name":None,"group":{"id":2,"name":"ROOT","cid":0},"tasks":None,"roleTemplateId":None, "system":False},
        'edit_role':{"id":1053592,"name":None,"group":{"id":2,"name":"ROOT","cid":0},"tasks":None,"roleTemplateId":None,"system":False},
        'delete_role':None,
        'add_role_access': {'roleId':None, 'access':None},
        'delete_role_access':None,
        'test_domain':{'id':None,"domainName":"smidle.lab","ldapServerIp":"172.22.2.11","serviceUser":"Administrator","perPage":10,"description":"smidle.lab"},
        'add_campaign':{"id":None,"code":None,"name":"auto_test_campaign","comment":"auto_test","deleted":False,"groups":[{"id":2}]},
        'add_result_code':{"id":None,"code":"123","forPhone":False,"name":"123","comment":None,"cdRes":False,"dataType":None,"forExport":True,
                           "forFilter":True,"fieldOrder":4,"deleted":False,"resultVariants":None},
        'add_map_field':{'id': None, 'name': None, 'fieldImport': None, 'fieldAbonent': None, 'dataType': 'STRING',
                         'phoneType': None, 'phoneNumber': False, 'enabled': True, 'deleted': False, 'forExport': False, 'forFilter': False, 'order': 1},
        #Smart_Callback
        'add_soft_route':{'id':None, "internalNumber": None, "externalNumber": None, "callDate": 1500292769604},
        'add_route': {'id':None, "internalNumber": None, "externalNumber": None},
        "manifest" : {"Build-OS": None,"Build-Time": None,"Build-Commit": None,"Project-Name": None,"Build-Java": None,"Build-By": None,"Project-Version": None},
        "licenses" : {"licenses": None,"licenseBeginDate": None,"licenseElapseDate": None,"licenseToModule": None,"licensedToCompany": None},
        "scb_settings":{"id": None,"debugLevel": None,"logLength": None,"monitoring": None, "smartLabel": None, "routing": None, "routeLifeTime": None, "routeClearingTime": None, "dynamicPeriod": None, 'defaultPeriod':None},
        "add_settings":{'id': None, 'fName': None, 'lName': None, 'pName': None, 'description': None, 'createdDate': None, 'phones': [{'id': None, 'phoneNumber': None, 'phoneType': None, 'comment': None}]},
        "get_route":{'page_number': 1, 'page_size': 10, 'sortedField': None, 'row_count': 1, 'order': None, 'data': [{'id': None, 'internalNumber': None, 'externalNumber': None}]}

            }

    return list_of_default_requests[response_name]