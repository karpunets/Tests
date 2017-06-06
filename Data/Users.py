from Data.Make_requests_and_answers import JSON_generator
import Data.Requests_default_map as get

one_user_get_userlist = {"fname": "get_userlist_fName_one",
                     "password": "get_userlist_password_one",
                    "lname": "get_userlist_lName_one",
                    "pname": "get_userlist_pName_one",
                    "agentId": "get_userlist_agentId_one",
                    "login":"get_userlist_login_one",
                    "loginAD":"get_userlist_loginAD_one",
                    "phone":"666816321"
                     }
edit_user = {"fname": "edit_user_fName_one",
                     "password": "edit_user_password_one",
                    "lname": "edit_user_lName_one",
                    "pname": "edit_user_pName_one",
                     "email": "edit_user@smiddle.com",
                     "fax":"edit_user_fax",
                    "agentId": "edit_user_agentId_one",
                    "login":"edit_user_login_one",
                    "loginAD":"edit_user_loginAD_one",
                    "phone":"666816322"
                     }



def get_user_list_Nusers(users_count):

    user_list = {}
    for i in range(1, users_count+1):

        data = {"fname": "get_userlist_fName_%s" % i,
                "lname": "get_userlist_lName_%s"%i,
                "pname": "get_userlist_pName_%s"%i,
                "phone": "%s"%i,
                "login": "get_userlist_login_%s"%i,
                "password": "get_userlist_password_%s"%i,
                "loginAD": "get_userlist_loginAD_%s"%i,
                "agentId": "get_userlist_agentId_%s"%i,
                "scMode": "0",
                "unmappedCalls": False,
                "enabled": True,
                "deleted": False,
                "dateCreate": 1494845539570,
                "groups": [{"id": 2}],
                "roles": [{"id": 3}]}
        request = get.defaul_request('add_user')
        data = JSON_generator.generate_JSON(request, data)
        user_list["Pagination_user_%s"%i] = data
    return user_list


#print(get_user_list_users(50))