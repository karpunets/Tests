
a = {"fname": "asdsad", "lname":"lname", "pname": "sadsad", "phone": "12321321", "fax": "qwewqe", "login": "qwe",
     "password": "sads", "loginAD": "sadsad", "agentId": "123213", "scMode": "0", "unmappedCalls": False,
     "enabled": True, "deleted": False, "dateCreate": 1508847939631, "groups": [{"id": 2}], "roles": [{"id": 3}]}

b = {"id": 217997526, "agentId": "123213", "login": "qwe", "loginAD": "sadsad", "lname": "sadsad", "fname": "asdsad",
     "pname": "sadsad", "email": None, "phone": "12321321", "fax": "qwewqe", "locale": None,
     "dateCreate": 1508847939631, "scMode": 0, "unmappedCalls": False, "enabled": True, "deleted": False,
     "groups": [{"id": 2, "name": "ROOT"}], "roles": [{"id": 3, "name": "ROOT"}], "userGroupRoles": None}

schema = {"fname": {'type':str}, "lname":"lname", "pname": "sadsad", "phone": "12321321", "fax": "qwewqe", "login": "qwe",
     "password": "sads", "loginAD": "sadsad", "agentId": "123213", "scMode": "0", "unmappedCalls": False,
     "enabled": True, "deleted": False, "dateCreate": 1508847939631, "groups": [{"id": 2}], "roles": [{"id": 3}]}


a1 = [(key, val) for key,val in iter(a.items())]
schema1 = [(key, val) for key,val in iter(schema.items())]
print(sorted(a1))
print(sorted(schema1))

def assert_equal(a,schema):
     for (key, val) in  schema.items():
          if type(val) == dict and 'type' in val.keys():
               print(key,val)
          else:
               dosmth
