import pytest, allure, json, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator as _
from Data.Test_data import make_50_users_for_get_user_list as take_user_list

headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}

url = "http://172.22.2.63:8080/SmiddleCampaignManager/cm/integration/contract/fieldmap"

def setup_get_user_list():
    # Запрос на добавление пользователя
    response = requests.get(url=url,  headers=headers)
    # Записываем ID добавленных пользователей
    return response.json()


a = setup_get_user_list()

id_list = []
for i in a:
    id_list.append(i['id'])


print(id_list)
def delete_mapping(id_list):
    for id in id_list:
        new_url = "http://172.22.2.63:8080/SmiddleCampaignManager/cm/integration/contract/fieldmap?id=%s"%id
        response = requests.delete(url=new_url, headers=headers)
        print(response.text)


delete_mapping(id_list)
