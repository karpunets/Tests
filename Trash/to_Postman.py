def toPostman(a):
    a = str(a)
    a = a.replace("'", "\"")
    a = a.replace('None', 'null')
    a = a.replace('False', 'false')
    a = a.replace('True', 'true')
    return a


send_value = {'fname': 'add_user_fName_one', 'lname': 'add_user_lName_one', 'pname': 'add_user_pName_one', 'phone': '666816000', 'login': 'add_user_login_one', 'password': 'add_user_password_one', 'loginAD': 'add_user_loginAD_one', 'agentId': 'add_user_agentId_one', 'scMode': '0', 'unmappedCalls': False, 'enabled': True, 'deleted': False, 'dateCreate': 1494845540000, 'groups': [{'id': 2}], 'roles': [{'id': 3}]}

print(toPostman(send_value))
