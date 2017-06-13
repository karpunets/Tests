import pytest, allure, json, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator as _
from Data.Users import make_50_users_for_get_user_list as take_user_list

headers = headers = {'content-type': "application/json;charset=UTF-8"}

user_list = {'1':{'fieldContract':'description','fieldImport':'COMENT'},
             '2':{'fieldContract':'contractCode','fieldImport':'ContractCode'},
             '3':{'fieldContract':'OutboundContactTypeOfContact','fieldImport':'OtkazValue'},
             '4':{'fieldContract':'nameRespondent','fieldImport':'FIO'},
             '5':{'fieldContract':'typeInet','fieldImport':'TypeInet'},
             '6':{'fieldContract':'availabilityPC','fieldImport':'DeviceInet'},
             '7':{'fieldContract':'provider','fieldImport':'Provider'},
             '8':{'fieldContract':'mainInet','fieldImport':'QualityInet'},
             '9':{'fieldContract':'currentSpeed','fieldImport':'SpeedInet'},
             '10':{'fieldContract':'costServices','fieldImport':'CostService'},
             '11':{'fieldContract':'estimateQuality','fieldImport':'ValuationService'},
             '12':{'fieldContract':'typeTV','fieldImport':'typeTV'},
             '13':{'fieldContract':'subjects','fieldImport':'SabjectTV'},
             '14':{'fieldContract':'mainTV','fieldImport':'QualityTV'},
             '15':{'fieldContract':'inetPurpose','fieldImport':'PurposeInet'},
             '16':{'fieldContract':'improveTvInet','fieldImport':'UpgradeService'},
             '17':{'fieldContract':'DateCall','fieldImport':'DateCall'},
             '18':{'fieldContract':'newTel','fieldImport':'Contact_phone'},
'19':{'fieldContract':'callBackTime','fieldImport':'RedialDate'},
'20':{'fieldContract':'authorID','fieldImport':'Smiddle Login'}}



url = "http://172.22.2.63:8080/SmiddleCampaignManager/cm/sd/contract/fieldmap"

def setup_get_user_list():
    for i in user_list:
        payload = json.dumps(user_list[i])
        # Запрос на добавление пользователя
        response = requests.post(url=url, data = payload, headers = headers)
        # Записываем ID добавленных пользователей
        print(response.text)


setup_get_user_list()