import allure


def assert_equal(a, schema):
    not_equal = []
    def helper(a, schema):
        for (key, val) in a.items():
            if (key, val) not in schema.items() and key in schema.keys():
                if type(schema[key]) == dict and 'type' in schema[key].keys() and len(schema[key]) == 1:
                    if type(val) != schema[key]['type']:
                        not_equal.append(
                            "{{{0}:{1}}} type of value is not equal to schema type({1})!={2}".format(key, val, schema[key]['type']))
                    a[key] = {'type': type(val)}
                elif type(val) == list:

                    for param in val:
                        helper(param, schema[key][val.index(param)])
                else:
                    not_equal.append(
                        "Value {{{0}:{1}}} not match schemas value {{{0}:{2}}}".format(key, val, schema[key]))
            elif (key, val) not in schema.items() and key not in schema.keys():
                not_equal.append("The key '%s' where no found in schema" % key)
    helper(a, schema)
    assert a == schema, (not_equal)


@allure.feature('Позитивный тест')
@allure.story('test_assert_equal')
def test_assert():
    a = {"fname": "asdss", "lname": "lname", "pname": "sadsad", "phone": "12321321", "fax": "qwewqe", "login": "qwe",
         "password": "sads", "loginAD": "sadsad", "agentId": "123213", "scMode": 0, "unmappedCalls": False,
         "enabled": True, "deleted": False, "dateCreate": 1508847939631, "groups": [{"id": 2, "name": "ROOT"}],
         "roles": [{"id": 3, "name": "ROOT"}]}
    #
    # b = {"id": 217997526, "agentId": "123213", "login": "qwe", "loginAD": "sadsad", "lname": "sadsad",
    #      "fname": "asdsad",
    #      "pname": "sadsad", "email": None, "phone": "12321321", "fax": "qwewqe", "locale": None,
    #      "dateCreate": 1508847939631, "scMode": 0, "unmappedCalls": False, "enabled": True, "deleted": False,
    #      "groups": [{"id": 2, "name": "ROOT"}], "roles": [{"id": 3, "name": "ROOT"}], "userGroupRoles": None}

    schema = {"fname": {'type': str}, "lname": "ln1ame", "pname": "sadsad", "phone": "12321321", "fax": "qwewqe",
              "login": "qwe",
              "password": "sads", "loginAD": "sadsad", "agentId": "123213", "scMode": 0, "unmappedCalls": False,
              "enabled": True, "deleted": False, "dateCreate": 1508847939631, "groups": [{"id": {'type': int}, "name": "ROOT"}],
              "roles": [{"id": 3, "name": "qq"}]}

    assert_equal(a, schema)
