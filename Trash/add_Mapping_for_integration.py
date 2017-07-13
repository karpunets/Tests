import json, requests


headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}

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



settings_id = 148962447
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
             '19':{"settings":{"id":settings_id},'fieldContract':'callBackTime','fieldImport':'RedialDate'},
             '20':{"settings":{"id":settings_id},'fieldContract':'service', 'fieldImport':'Service'},
             '21':{"settings":{"id":settings_id},'fieldContract':'type','fieldImport':'Type'},
             '22': {"settings": {"id": settings_id}, 'fieldContract': 'activityFeed', 'fieldImport': 'ActivityFeed'},
             '23': {"settings": {"id": settings_id}, 'fieldContract': 'resultKontact', 'fieldImport': 'ResultKontact'},
             '24': {"settings": {"id": settings_id}, 'fieldContract': 'authorID', 'fieldImport': 'SmiddleLogin'}
             }



url = "http://10.10.27.32:8080/SmiddleCampaignManager/cm/integration/contract/fieldmap"

def setup_get_user_list():
    for i in user_list:
        payload = json.dumps(user_list[i])
        # Запрос на добавление пользователя
        response = requests.post(url=url, data = payload, headers = headers)
        # Записываем ID добавленных пользователей
        print(response.text)
        print(response.status_code)


setup_get_user_list()