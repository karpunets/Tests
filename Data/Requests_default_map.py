def defaul_request(request_name):

    list_of_default_requests = {
        'get_user_list':{"fName":None,"lName":None,"pName":None,"roleId":None,"groupId":None,"login":None,"adLogin":None,"agentId":None,
                         "showDeletedOnly":False,"phone":None,"pagination":{"page_number":"1","page_size":"10","sortedField":"login","order":"ASC"}},

    'add_user':{"fname":None,"lname":None,"pname":None,"email":None,"phone":None,"fax":None,"login":None,"password":None,
                "loginAD":None,"agentId":None,"scMode":"0","unmappedCalls":False,"enabled":True,"deleted":False,
                "dateCreate":1494845540000,"groups":[{"id":2}],"roles":[{"id":3}]},
    'add_group':{"name":None,"parent":{"id":2}},
    'delete_user': {"userId": None},
    'edit_user':{"id":None,"fname":None,"lname":None,"pname":None,"email":None,"phone":None,
                 "fax":None,"login":None,"password":None,"loginAD":None,"agentId":None,"scMode":"0","unmappedCalls":False,
                 "enabled":True,"deleted":False,"dateCreate":1494845540000,"groups":[{"id":2}],"roles":[{"id":3}]},
    "delete_group": {"groupId":None},
    "edit_group": {"id":None,"name":None,"parent":{"id":2}},
        'add_role':{"name":None,"roleTemplateId":None,"group":{"id":2}},
        'edit_role':{"id":None,"name":None,"group":{"id":2}},
        'delete_role':{"roleId":None},
        'add_role_access':{'roleId':None, 'access':None},
        'delete_role_access': {'roleId':None, 'access':None},
        'Manager_logs':{"moduleName":"Settings Controller","messageParams":["message"],"types":["SYSTEM"],"action":"get_menu_for_role",
                "dateFrom":1495462096000,"dateTo":1495721296000}
    }

    return list_of_default_requests[request_name]

