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
        "edit_group": {"id":None,"name":None,"children":[],"cid":None}
                                }

    return list_of_default_requests[response_name]