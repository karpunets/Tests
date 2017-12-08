def toPostman(a):
    a = str(a)
    a = a.replace("'", "\"")
    a = a.replace('None', 'null')
    a = a.replace('False', 'false')
    a = a.replace('True', 'true')
    return a


send_value = {'dateCreate': 1512048684805, 'supervisor': {'id': 68}, 'name': 'VsywRA8D', 'version': 895, 'description': 'CM3y', 'approvalPolicy': None, 'groups': [{'id': 2}], 'templateSections': [{'templateCriterias': [{'templateCriteria': {'id': 218035101}, 'weight': 82, 'position': 1}], 'name': 'KP4f7t', 'position': 1}]}
print(toPostman(send_value))
