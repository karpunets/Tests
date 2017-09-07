import json, requests, random


url_script_start = "http://172.22.2.63:8080/SmiddleAgentScripting/as/script_executor/script_start"
url_next = "http://172.22.2.63:8080/SmiddleAgentScripting/as/script_executor/script_next"

url_get_abonent = "http://172.22.2.63:8080/SmiddleCampaignManager/cm/manager/get_abonent"


data_start = {"clientId":"2620631","ani":"1115","agentId":"Agent11","scriptId":"1635","campaignName":"123"}
data_next_1 = {"scriptId":"1635","agentId":"Agent11","campaignName":"123","comment":None,"variables":[{"variableId":"1","data":"Раскрытие потребностей"}]}
data_next_2 = {"scriptId":"1635","agentId":"Agent11","campaignName":"123","comment":None,"variables":[{"variableId":"1","data":"Проводной"},{"variableId":"2","data":"Кабельное ТВ"}]}
data_next_3 = {"scriptId":"1635","agentId":"Agent11","campaignName":"123","comment":None,"variables":[{"variableId":"4","data":""},{"variableId":"1","data":"Детские"},{"variableId":"2","data":"Стоимость"},{"variableId":"3","data":"Укртелеком"},{"variableId":"7","data":"До 60 Мбит"},{"variableId":"6","data":"Работа"},{"variableId":"5","data":"Стабильность сигнала"},{"variableId":"8","data":"До 120 грн"},{"variableId":"9","data":"2"},{"variableId":"10","data":"Скорость выше"}]}
data_next_4 = {"scriptId":"1635","agentId":"Agent11","campaignName":"123","comment":None,"variables":[{"variableId":"1","data":"Оформление заявки"}]}
data_next_finish = {"scriptId":"1635","agentId":"Agent11","campaignName":"123","comment":None,"variables":[]}


def script(client_id, ani):

    s = requests.session()
    params = {"clientId":str(client_id),"ani":str(ani),"agentId":"Agent11","scriptId":1635,"campaignName":123}
    headers = {'content-type': "application/json;charset=UTF-8"}
    s.headers.update(headers)
    steps = [data_next_1, data_next_2, data_next_3, data_next_4]
    data_start['clientId'] = client_id
    data_start['ani'] = ani
    payload_start = json.dumps(data_start)
    response = s.post(url = url_script_start, data=payload_start)
    for step_data in steps:
        response = s.post(url_next, data=json.dumps(step_data))
        print("step", response.status_code)
    response_finish = s.post(url_next, data=json.dumps(data_next_finish))
    print('finish', response_finish.status_code)


f = open("qq.txt", 'r')
abonents = f.read().split()
f.close()
count = 0
for i in abonents:
    script(i, random.randint(1,99999999))
    count+=1
    print(count)
