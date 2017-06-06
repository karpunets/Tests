def defaul_request(request_name):

    list_of_default_requests = {
        'get_user_list':{"fName":None,"lName":None,"pName":None,"roleId":None,"groupId":None,"login":None,"adLogin":None,"agentId":None,
                         "showDeletedOnly":False,"phone":None,"pagination":{"page_number":"1","page_size":"10","sortedField":"login","order":"ASC"}},

    'add_user':{"fname": None, "lname": None, "pname": None, "phone": None, "login": None,
                                "password": None, "loginAD": None, "agentId": None, "scMode": "0", "unmappedCalls": False,
                                "enabled": True, "deleted": False, "dateCreate": 1494845540000, "groups": [{"id": 2}], "roles": [{"id": 3}]},

    'delete_user': {"userId": None},
    'edit_user':{"id":None,"fname":None,"lname":None,"pname":None,"email":None,"phone":None,
                 "fax":None,"login":None,"password":None,"loginAD":None,"agentId":None,"scMode":"0","unmappedCalls":False,
                 "enabled":True,"deleted":False,"dateCreate":1494845540000,"groups":[{"id":2}],"roles":[{"id":3}]}
                               }

    return list_of_default_requests[request_name]

