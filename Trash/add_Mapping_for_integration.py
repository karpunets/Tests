import pytest, allure, json, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator as _
from Data.Test_data import make_50_users_for_get_user_list as take_user_list

headers = headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}

user_list = {
             '2':{"settings":{"id":115301820},'fieldContract':'contractCode','fieldImport':'ContractCode'},
             '3':{"settings":{"id":115301820},'fieldContract':'OutboundContactTypeOfContact','fieldImport':'OtkazValue'},
             '4':{"settings":{"id":115301820},'fieldContract':'nameRespondent','fieldImport':'FIO'},
             '5':{"settings":{"id":115301820},'fieldContract':'typeInet','fieldImport':'TypeInet'},
             '6':{"settings":{"id":115301820},'fieldContract':'availabilityPC','fieldImport':'DeviceInet'},
             '7':{"settings":{"id":115301820},'fieldContract':'provider','fieldImport':'Provider'},
             '8':{"settings":{"id":115301820},'fieldContract':'mainInet','fieldImport':'QualityInet'},
             '9':{"settings":{"id":115301820},'fieldContract':'currentSpeed','fieldImport':'SpeedInet'},
             '10':{"settings":{"id":115301820},'fieldContract':'costServices','fieldImport':'CostService'},
             '11':{"settings":{"id":115301820},'fieldContract':'estimateQuality','fieldImport':'ValuationService'},
             '12':{"settings":{"id":115301820},'fieldContract':'typeTV','fieldImport':'typeTV'},
             '13':{"settings":{"id":115301820},'fieldContract':'subjects','fieldImport':'SabjectTV'},
             '14':{"settings":{"id":115301820},'fieldContract':'mainTV','fieldImport':'QualityTV'},
             '15':{"settings":{"id":115301820},'fieldContract':'inetPurpose','fieldImport':'PurposeInet'},
             '16':{"settings":{"id":115301820},'fieldContract':'improveTvInet','fieldImport':'UpgradeService'},
             '17':{"settings":{"id":115301820},'fieldContract':'DateCall','fieldImport':'DateCall'},
             '18':{"settings":{"id":115301820},'fieldContract':'newTel','fieldImport':'Contact_phone'},
             '19':{"settings":{"id":115301820},'fieldContract':'callBackTime','fieldImport':'RedialDate'},
             '20':{"settings":{"id":115301820},'fieldContract':'service', 'fieldImport':'service'},
             '21':{"settings":{"id":115301820},'fieldContract':'type','fieldImport':'type'}}
             #'22':{"settings":{"id":115301820},'fieldContract':'authorID','fieldImport':'Smiddle Login'}



url = "http://172.22.2.63:8080/SmiddleCampaignManager/cm/integration/contract/fieldmap"

def setup_get_user_list():
    for i in user_list:
        payload = json.dumps(user_list[i])
        # Запрос на добавление пользователя
        response = requests.post(url=url, data = payload, headers = headers)
        # Записываем ID добавленных пользователей
        print(response.text)


setup_get_user_list()