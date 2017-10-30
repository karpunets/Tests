import allure


def assert_equal(instance, schema, assert_keys_quantity = True ):
    # Переменная для сбора ошибок
    not_equal = []
    # Подпрограмма для использования рекурсии
    def helper(instance, schema):
        for (key, val) in instance.items():
            # Если пара (ключ:значение), не совпадает, но ключ существует в схеме
            if (key, val) not in schema.items() and key in schema.keys():
                # Если в схеме указана проверка на тип
                if type(schema[key]) == dict and 'type' in schema[key].keys() and len(schema[key]) == 1:
                    # Тип не совпадаем, пишем ошибку
                    if type(val) != schema[key]['type']:
                        not_equal.append(
                            "{{{0}:{1}}} type of value is not equal to schema type({1})!={2}".format(key, val, schema[key]['type']))
                    #Подменяем значение в данных, для более коректного отображения в отчетах Allure
                    instance[key] = {'type': type(val)}
                elif type(val) == list:
                    for param in val:
                        helper(param, schema[key][val.index(param)])
                elif type(val) == dict:
                    helper(instance[key], schema[key])
                else:
                    not_equal.append(
                        "Value {{{0}:{1}}} not match schemas value {{{0}:{2}}}".format(key, val, schema[key]))
            elif (key, val) not in schema.items() and key not in schema.keys():
                not_equal.append("The key '%s' where no found in schema" % key)
    # Если есть ошибки, делаем асерт, для удобства отображения в отчетах
    if assert_keys_quantity == True and len(instance) == len(schema):
        helper(instance, schema)
    else:
        not_equal.append("Lenght of instance != leng of schema")
    if len(not_equal) > 0:
        assert instance == schema, (not_equal)
    else:
        return True

@allure.feature('Позитивный тест')
@allure.story('test_assert_equal')
def test_assert():
    a = {"fname": "asdss", "lname": "lname", "pname": "sadsd", "phone": "12321321", "fax": "qwewqe", "login": "qwe",
         "password": "sads", "loginAD": "sadsad", "agentId": "123213", "scMode": 0, "unmappedCalls": False,
         "enabled": True, "deleted": False, "dateCreate": 1508847939631, "groups": {"id": 2, "name": "ROOT1",'vv':{'qq':3, 21:{'z':'finish'}}},
         "roles": [{"id": 3, "name": "ROOT"}]}
    #
    # b = {"id": 217997526, "agentId": "123213", "login": "qwe", "loginAD": "sadsad", "lname": "sadsad",
    #      "fname": "asdsad",
    #      "pname": "sadsad", "email": None, "phone": "12321321", "fax": "qwewqe", "locale": None,
    #      "dateCreate": 1508847939631, "scMode": 0, "unmappedCalls": False, "enabled": True, "deleted": False,
    #      "groups": [{"id": 2, "name": "ROOT"}], "roles": [{"id": 3, "name": "ROOT"}], "userGroupRoles": None}

    schema = {"fname": {'type': str}, "lname": "lname", "pname": "sadsad", "phone": "12321321", "fax": "qwewqe",
              "login": "qwe",
              "password": "sads", "loginAD": "sadsad", "agentId": "123213", "scMode": 0, "unmappedCalls": False,
              "enabled": True, "deleted": False, "dateCreate": 1508847939631, "groups": {"id": 2, "name": "ROOT1",'vv':{'qq':3, 21:{'z':'finish'}}},
              "roles": [{"id": 3, "name": "ROOT"}]}

    assert_equal(a, schema)
