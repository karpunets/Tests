import random, string, time


def random_name():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3,10)))

def date_now():
    return round(time.time() * 1000)


ROOT_group_id = 2
ROOT_user_id = 68

# MANAGER(ADM)
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
add_user_existing = {"fname": "add_user_fName_existing",
                     "password": "add_user_password_existing",
                     "lname": "add_user_lName_existing",
                     "pname": "add_user_pName_existing",
                     "email": "add_user_existing@smiddle.com",
                     "fax": "add_user_fax_existing",
                     "agentId": "add_user_agentId_existing",
                     "login": "add_user_login_existing",
                     "loginAD": "add_user_loginAD_existing",
                     "phone": "6668164444"
                     }
add_user_deleted_existing = {"fname": "add_user_fName_deleted_existing",
                             "password": "add_user_password_deleted_existing",
                             "lname": "add_user_lName_deleted_existing",
                             "pname": "add_user_pName_deleted_existing",
                             "email": "add_user_deleted_existing@smiddle.com",
                             "fax": "add_user_fax_deleted_existing",
                             "agentId": "add_user_agentId_deleted_existing",
                             "login": "add_user_login_deleted_existing",
                             "loginAD": "add_user_loginAD_deleted_existing",
                             "phone": "6668165555",
                             "deleted": True
                             }
add_role = {"name": "editing_role",
            "roleTemplateId": None,
            "group": {"id": 2}}

# SMART CALLBACK
manifest = {
    "Build-OS": None,
    "Build-Time": None,
    "Build-Commit": None,
    "Project-Name": None,
    "Build-Java": None,
    "Build-By": None,
    "Project-Version": None
}
licenses = {
    "licenses": None,
    "licenseBeginDate": None,
    "licenseElapseDate": None,
    "licenseToModule": None,
    "licensedToCompany": None
}
add_contact = {"fName": "Autotest_fName",
               "lName": "Autotest_lName",
               "pName": "Autotest_pName",
               "description": "Autotest_description",
               "phones": [{"phoneNumber": "06668166550", "phoneType": "MOBILE", "comment": None},
                          {"phoneNumber": "0525731628", "phoneType": "HOME", "comment": None},
                          {"phoneNumber": "0443775578", "phoneType": "WORK", "comment": None}]}
credentials = {
    "cti": "172.22.2.12",
    "user": "CallBackUser",
    "password": "C1scoC1sco",
    "active": True}
