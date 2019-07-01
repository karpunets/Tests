from cerberus import Validator


def equal_schema(response, schema):
    v = Validator()
    result = v.validate(response, schema)
    if not result:
        print("RESPONSE", response)
        print("schema", schema)
        print("ERROR", v.errors)
    return result


