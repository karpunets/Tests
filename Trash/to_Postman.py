def toPostman(a):
    a = str(a)
    a = a.replace("'", "\"")
    a = a.replace('None', 'null')
    a = a.replace('False', 'false')
    a = a.replace('True', 'true')
    return a


send_value = {'contractCode': '50025704', 'type': '111323', 'service': '24850210', 'OutboundContactTypeOfContact': 'Отказ от общения', 'nameRespondent': 'Осадчик Геннадий Владимирович', 'typeInet': None, 'availabilityPC': None, 'provider': None, 'mainInet': None, 'currentSpeed': None, 'costServices': None, 'estimateQuality': None, 'typeTV': None, 'subjects': None, 'mainTV': None, 'DateCall': '08.06.2017 03:45', 'newTel': '0954292054', 'callBackTime': '19.06.2017 03:18'}
print(toPostman(send_value))
