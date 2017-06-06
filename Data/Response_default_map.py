def defaul_response(response_name):

    delete_user = {"userId": None}
    list_of_default_requests = {
        'get_user_list':{"page_number":1,"page_size":10,"sortedField":"login","order":"ASC","row_count":1,"data":
                        [{"id":1,"agentId":None,"login":None,"loginAD":None,"lname":None,
                        "fname":None,"pname":None,"email":None,"phone":"999","fax":None,"locale":None,
                        "dateCreate":1494845539570,"scMode":0,"unmappedCalls":False,"enabled":True,"deleted":False,
                        "groups":[{"id":2,"name":"ROOT"}],"roles":[{"id":3,"name":"ROOT"}],"userGroupRoles":None}]},
        'add_user':None,
        'delete_user':{"userId": None}
                }

    return list_of_default_requests[response_name]