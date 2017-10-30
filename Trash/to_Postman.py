def toPostman(a):
    a = str(a)
    a = a.replace("'", "\"")
    a = a.replace('None', 'null')
    a = a.replace('False', 'false')
    a = a.replace('True', 'true')
    return a


send_value = {'id': 218001699, 'name': 'mGfbRUfl', 'groups': [{'id': 2, 'name': 'ROOT', 'cid': 0}], 'criteriaList': None}
print(toPostman(send_value))
