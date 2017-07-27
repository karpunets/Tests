def toPostman(a):
    a = str(a)
    a = a.replace("'", "\"")
    a = a.replace('None', 'null')
    a = a.replace('False', 'false')
    a = a.replace('True', 'true')
    return a


send_value = {'fName': 'Victor1', 'lName': 'Kliui1', 'pName': None, 'description': None, 'phones': [{'phoneNumber': '06668166551', 'phoneType': 'MOBILE', 'comment': None}, {'phoneNumber': '0525731628', 'phoneType': 'HOME', 'comment': None}, {'phoneNumber': '0443775578', 'phoneType': 'WORK', 'comment': None}]}
print(toPostman(send_value))
