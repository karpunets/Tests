from Data.Make_requests_and_answers import JSON_generator
import Data.Requests_default_map as get

one_user_get_userlist = {"fname": "get_userlist_fName_one",
                "lname": "get_userlist_lName_one",
                "pname": "get_userlist_pName_one",
                "phone": "666816321",
                "login": "get_userlist_login_one",
                "password": "get_userlist_password_one",
                "loginAD": "get_userlist_loginAD_one",
                "agentId": "get_userlist_agentId_one",
                "scMode": "0",
                "unmappedCalls": False,
                "enabled": True,
                "deleted": False,
                "dateCreate": 1494845540000,
                "groups": [{"id": 2}],
                "roles": [{"id": 3}]}
deleted_user_get_user_list = {"fname": "get_userlist_fName_deleted",
                "lname": "get_userlist_lName_deleted",
                "pname": "get_userlist_pName_deleted",
                "phone": "6668163212",
                "login": "get_userlist_login_deleted",
                "password": "get_userlist_password_deleted",
                "loginAD": "get_userlist_loginAD_deleted",
                "agentId": "get_userlist_agentId_deleted",
                "scMode": "0",
                "unmappedCalls": False,
                "enabled": True,
                "deleted": True,
                "dateCreate": 1494845540000,
                "groups": [{"id": 2}],
                "roles": [{"id": 3}]}
edit_user = {"fname": "edit_user_fName_one",
             "password": "edit_user_password_one",
             "lname": "edit_user_lName_one",
             "pname": "edit_user_pName_one",
             "email": "edit_user@smiddle.com",
             "fax": "edit_user_fax",
             "agentId": "edit_user_agentId_one",
             "login": "edit_user_login_one",
             "loginAD": "edit_user_loginAD_one",
             "phone": "666816322"
             }
edit_user_deleted = {"fname": "edit_user_fName_deleted",
             "password": "edit_user_password_deleted",
             "lname": "edit_user_lName_deleted",
             "pname": "edit_user_pName_deleted",
             "email": "edit_user@smiddle.com",
             "fax": "edit_user_fax_deleted",
             "agentId": "edit_user_agentId_deleted",
             "login": "edit_user_login_deleted",
             "loginAD": "edit_user_loginAD_deleted",
             "phone": "666816323",
            "deleted": True
             }
edit_user_existing = {"fname": "edit_user_fName_existing",
             "password": "edit_user_password_existing",
             "lname": "edit_user_lName_existing",
             "pname": "edit_user_pName_existing",
             "email": "edit_user_existing@smiddle.com",
             "fax": "edit_user_fax_existing",
             "agentId": "edit_user_agentId_existing",
             "login": "edit_user_login_existing",
             "loginAD": "edit_user_loginAD_existing",
             "phone": "6668163333"
             }
edit_user_deleted_existing = {"fname": "edit_user_fName_deleted_existing",
             "password": "edit_user_password_deleted_existing",
             "lname": "edit_user_lName_deleted_existing",
             "pname": "edit_user_pName_deleted_existing",
             "email": "edit_user_deleted_existing@smiddle.com",
             "fax": "edit_user_fax_deleted_existing",
             "agentId": "edit_user_agentId_deleted_existing",
             "login": "edit_user_login_deleted_existing",
             "loginAD": "edit_user_loginAD_deleted_existing",
             "phone": "6668163333",
            "deleted": True
             }

def make_50_users_for_get_user_list():
    # Количество пользователей для теста
    users_count = 50
    user_list = {}
    # Создаем список JSONов для создания пользователей
    for i in range(1, users_count + 1):
        data = {"fname": "get_userlist_fName_%s" % i,
                "lname": "get_userlist_lName_%s" % i,
                "pname": "get_userlist_pName_%s" % i,
                "phone": "%s" % i,
                "login": "get_userlist_login_%s" % i,
                "password": "get_userlist_password_%s" % i,
                "loginAD": "get_userlist_loginAD_%s" % i,
                "agentId": "get_userlist_agentId_%s" % i,
                "scMode": "0",
                "unmappedCalls": False,
                "enabled": True,
                "deleted": False,
                "dateCreate": 1494845540000,
                "groups": [{"id": 2}],
                "roles": [{"id": 3}]}
        # Пол
        request = get.defaul_request('add_user')
        #
        data = JSON_generator.generate_JSON(request, data)
        #
        user_list["Pagination_user_%s" % i] = data
    #
    user_list['one_user_get_userlist'] = one_user_get_userlist
    user_list['deleted_user_get_user_list'] = deleted_user_get_user_list
    return user_list

