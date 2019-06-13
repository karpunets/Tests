from cerberus import Validator


def equal_schema(response, schema):
    v = Validator()
    result = v.validate(response, schema)

    return result


a = {'name': 'dJRS4XW', 'cid': 25961, 'groupId': 'b7281473-07ac-4c78-a537-116a7e1040f1', 'children': []}
b = {'name': {'allowed': ['dJRS4XW']}, 'groupId': {'type': 'string'}, 'cid': {'type': 'number'}, 'children': {'type': 'list'}}


print(equal_schema(a,b))

