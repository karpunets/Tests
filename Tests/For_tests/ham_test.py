import pytest,allure






def assert_equal(a,schema):
     not_equal = []
     for (key, val) in  a.items():
          if (key,val) not in schema.items() and key in schema.keys():
               if type(schema[key]) == dict and 'type' in schema[key].keys():
                    print('qq')
          elif (key,val) not in schema.items() and key not in schema.keys():
               not_equal.append("No such {'%s':'%s'} in scema"%(key,val))
     assert len(not_equal) == 0,(not_equal)



@allure.feature('Позитивный тест')
@allure.story('test_assert_equal')
def test_assert():
     a = {"fname": "asdsad", "lname": "lname", "pname": "sadsad", "phone": "12321321", "fax": "qwewqe", "login": "qwe",
          "password": "sads", "loginAD": "sadsad", "agentId": "123213", "scMode": "0", "unmappedCalls": False,
          "enabled": True, "deleted": False, "dateCreate": 1508847939631, "groups": [{"id": 2}], "roles": [{"id": 3}]}

     b = {"id": 217997526, "agentId": "123213", "login": "qwe", "loginAD": "sadsad", "lname": "sadsad",
          "fname": "asdsad",
          "pname": "sadsad", "email": None, "phone": "12321321", "fax": "qwewqe", "locale": None,
          "dateCreate": 1508847939631, "scMode": 0, "unmappedCalls": False, "enabled": True, "deleted": False,
          "groups": [{"id": 2, "name": "ROOT"}], "roles": [{"id": 3, "name": "ROOT"}], "userGroupRoles": None}

     schema = {"fname": {'type': str}, "1lname": "lname", "pname": "sadsad", "phone": "12321321", "fax": "qwewqe",
               "login": "qwe",
               "password": "sads", "loginAD": "sadsad", "agentId": "123213", "scMode": "0", "unmappedCalls": False,
               "enabled": True, "deleted": False, "dateCreate": 1508847939631, "groups": [{"id": 2}],
               "roles": [{"id": 3}]}
     assert_equal(a,schema)
