import json, requests


headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}

server = "http://172.22.2.63:8080"

# user_list = {
#              '2':{'fieldContract':'contractCode','fieldImport':'ContractCode'},
#              '3':{'fieldContract':'OutboundContactTypeOfContact','fieldImport':'OtkazValue'},
#              '4':{'fieldContract':'nameRespondent','fieldImport':'FIO'},
#              '5':{'fieldContract':'typeInet','fieldImport':'TypeInet'},
#              '6':{'fieldContract':'availabilityPC','fieldImport':'DeviceInet'},
#              '7':{'fieldContract':'provider','fieldImport':'Provider'},
#              '8':{'fieldContract':'mainInet','fieldImport':'QualityInet'},
#              '9':{'fieldContract':'currentSpeed','fieldImport':'SpeedInet'},
#              '10':{'fieldContract':'costServices','fieldImport':'CostService'},
#              '11':{'fieldContract':'estimateQuality','fieldImport':'ValuationService'},
#              '12':{'fieldContract':'typeTV','fieldImport':'typeTV'},
#              '13':{'fieldContract':'subjects','fieldImport':'SabjectTV'},
#              '14':{'fieldContract':'mainTV','fieldImport':'QualityTV'},
#              '15':{'fieldContract':'inetPurpose','fieldImport':'PurposeInet'},
#              '16':{'fieldContract':'improveTvInet','fieldImport':'UpgradeService'},
#              '17':{'fieldContract':'DateCall','fieldImport':'DateCall'},
#              '18':{'fieldContract':'newTel','fieldImport':'Contact_phone'},
#              '19':{'fieldContract':'callBackTime','fieldImport':'RedialDate'},
#              '20':{'fieldContract':'service', 'fieldImport':'service'},
#              '21':{'fieldContract':'type','fieldImport':'type'}}
#              #'22':{'fieldContract':'authorID','fieldImport':'Smiddle Login'}



settings_id = 139967687
user_list = {
             '2':{"settings":{"id":settings_id},'fieldContract':'contractCode','fieldImport':'ContractCode'},
             '3':{"settings":{"id":settings_id},'fieldContract':'OutboundContactTypeOfContact','fieldImport':'OutboundContactTypeOfContact'},
             '4':{"settings":{"id":settings_id},'fieldContract':'nameRespondent','fieldImport':'FIO'},
             '5':{"settings":{"id":settings_id},'fieldContract':'typeInet','fieldImport':'TypeInet'},
             '6':{"settings":{"id":settings_id},'fieldContract':'availabilityPC','fieldImport':'DeviceInet'},
             '7':{"settings":{"id":settings_id},'fieldContract':'provider','fieldImport':'Provider'},
             '8':{"settings":{"id":settings_id},'fieldContract':'mainInet','fieldImport':'QualityInet'},
             '9':{"settings":{"id":settings_id},'fieldContract':'currentSpeed','fieldImport':'SpeedInet'},
             '10':{"settings":{"id":settings_id},'fieldContract':'costServices','fieldImport':'CostService'},
             '11':{"settings":{"id":settings_id},'fieldContract':'estimateQuality','fieldImport':'ValuationService'},
             '12':{"settings":{"id":settings_id},'fieldContract':'typeTV','fieldImport':'typeTV'},
             '13':{"settings":{"id":settings_id},'fieldContract':'subjects','fieldImport':'SabjectTV'},
             '14':{"settings":{"id":settings_id},'fieldContract':'mainTV','fieldImport':'QualityTV'},
             '15':{"settings":{"id":settings_id},'fieldContract':'inetPurpose','fieldImport':'PurposeInet'},
             '16':{"settings":{"id":settings_id},'fieldContract':'improveTvInet','fieldImport':'UpgradeService'},
             '17':{"settings":{"id":settings_id},'fieldContract':'DateCall','fieldImport':'DateCall'},
             '18':{"settings":{"id":settings_id},'fieldContract':'newTel','fieldImport':'Contact_phone'},
             '20':{"settings":{"id":settings_id},'fieldContract':'service', 'fieldImport':'Service'},
             '21':{"settings":{"id":settings_id},'fieldContract':'type','fieldImport':'Type'},
             '22': {"settings": {"id": settings_id}, 'fieldContract': 'activityFeed', 'fieldImport': 'ActivityFeed'},
             '23': {"settings": {"id": settings_id}, 'fieldContract': 'resultKontact', 'fieldImport': 'ResultKontact'},
             '24': {"settings": {"id": settings_id}, 'fieldContract': 'authorID', 'fieldImport': 'SmiddleLogin'},
            '25': {"settings": {"id": settings_id}, 'fieldContract': 'OutboundContactSubtotalConversa', 'fieldImport': 'OutboundContactSubtotalConversa'},
            '26': {"settings": {"id": settings_id}, 'fieldContract': 'description', 'fieldImport': 'OfferName'},
            '27': {"settings": {"id": settings_id}, 'fieldContract': 'workDate', 'fieldImport': 'workDate'},
            '28': {"settings": {"id": settings_id}, 'fieldContract': 'completionDate', 'fieldImport': 'completionDate'},
            '29': {"settings": {"id": settings_id}, 'fieldContract': 'inquiryTime', 'fieldImport': 'inquiryTime'}}


outbound = {'Бросили трубку во время презентации':'6',	'Дорого (оборудование, доп. точки)':'49',
            'Дорого (текущие условия дешевле, не готов платить за лучшее качество услуг).':'50',
            'Заявка уже в работе':'9',	'Контракт с другим провайдером (проплачен наперед другой провайдер/контакт)':'51',
            'Не конкурентное предложение':'10',	'Нет ПК/ нет ТВ':'11',	'Нет технической возможности':'57',
            'Номер не принадлежит клиенту':'52',
            'Отказ от общения':'13',	'Пожилые люди':'14',	'Абонент вне зоны покрытия':'48',
            'Пользовались услугой - негативный опыт/не довольны качеством':'16',
            'Посмотрю на сайте/сам обращусь в компанию':'17',
            'Просьба больше не беспокоить (добавить в черный список) ':'19',
            'Уже является пользователем услуг от компании "Воля"':'21',
            'Уже звонили в этом месяце/с этим предложением':'7',
            'Юр. Лицо':'46'}


data = {"id":None,"settings":{"id":settings_id},"fieldMap":{"id":None},"scmValue":"original","contractValue":"zamena"}


url = "%s/SmiddleCampaignManager/cm/integration/contract/fieldmap"%server

def setup_get_user_list():
    for i in user_list:
        payload = json.dumps(user_list[i])
        # Запрос на добавление пользователя
        response = requests.post(url=url, data = payload, headers = headers)
        # Записываем ID добавленных пользователей
        if response.json()['fieldContract'] == 'OutboundContactSubtotalConversa':
            fieldmap_id = response.json()['id']
    return fieldmap_id

fieldmap_id = setup_get_user_list()

def add_outbound():
    url ='%s/SmiddleCampaignManager/cm/integration/contract/valmapping'%server
    for i in outbound:
        payload = json.dumps({"id":None,"settings":{"id":settings_id},"fieldMap":{"id":fieldmap_id},"scmValue":i,"contractValue":outbound[i]})
        response = requests.post(url=url, data=payload, headers=headers)
        print(response.status_code)

add_outbound()