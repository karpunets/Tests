def toPostman(a):
    a = str(a)
    a = a.replace("'", "\"")
    a = a.replace('None', 'null')
    a = a.replace('False', 'false')
    a = a.replace('True', 'true')
    return a


send_value = {'fName': 'get_userlist_fName_one', 'lName': 'get_userlist_lName_one', 'pName': 'get_userlist_pName_one', 'roleId': None, 'groupId': None, 'login': None, 'adLogin': None, 'agentId': None, 'showDeletedOnly': False, 'phone': None, 'pagination': {'page_number': '1', 'page_size': '10', 'sortedField': 'login', 'order': 'ASC'}}

print(toPostman(send_value))
