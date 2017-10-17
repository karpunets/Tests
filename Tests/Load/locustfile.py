import json, requests, random

from locust import HttpLocust, TaskSet, task


campaign_name = "qqwe"
campaign_id = 146093915

headers = {
    'content-type': "application/json;charset=UTF-8",
    'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}
f = open("C:\\Users\\Victor\\PycharmProjects\\Smiddle_API\\Trash\\qq.txt", 'r')
abonents = f.read().split()
f.close()
add_excel_params = {"campaignId":"%s"%campaign_id,"batchId":146312506}
excel_url = "http://172.22.2.63:8080/SmiddleCampaignManager/cm/manager/import_excel"
authorization = ('Root', 'Smidle098adm!')

add_excel_params_2 = {"campaignId":"%s"%campaign_id,"batchId":146094116}

f = open("C:\\Users\\Victor\\PycharmProjects\\Smiddle_API\\Trash\\agentids.txt", 'r')
agentIDs = f.read().split()
f.close()


class UserBehavior(TaskSet):
    @task(50)
    def as_script(self):
        agent_id = random.choice(agentIDs)
        url_script_start = "http://172.22.2.63:8080/SmiddleAgentScripting/as/script_executor/script_start"
        url_next = "http://172.22.2.63:8080/SmiddleAgentScripting/as/script_executor/script_next"

        data_start = {"clientId": "2620631", "ani": "1115", "agentId": "%s"%agent_id, "scriptId": "1635",
                      "campaignName": "%s"%campaign_name}
        data_next_1 = {"scriptId": "1635", "agentId": "%s"%agent_id, "campaignName": "%s"%campaign_name, "comment": None,
                       "variables": [{"variableId": "1", "data": "Раскрытие потребностей"}]}
        data_next_2 = {"scriptId": "1635", "agentId": "%s"%agent_id, "campaignName": "%s"%campaign_name, "comment": None,
                       "variables": [{"variableId": "1", "data": "Проводной"},
                                     {"variableId": "2", "data": "Кабельное ТВ"}]}
        data_next_3 = {"scriptId": "1635", "agentId": "%s"%agent_id, "campaignName": "%s"%campaign_name, "comment": None,
                       "variables": [{"variableId": "4", "data": ""}, {"variableId": "1", "data": "Детские"},
                                     {"variableId": "2", "data": "Стоимость"},
                                     {"variableId": "3", "data": "Укртелеком"},
                                     {"variableId": "7", "data": "До 60 Мбит"}, {"variableId": "6", "data": "Работа"},
                                     {"variableId": "5", "data": "Стабильность сигнала"},
                                     {"variableId": "8", "data": "До 120 грн"}, {"variableId": "9", "data": "2"},
                                     {"variableId": "10", "data": "Скорость выше"}]}
        data_next_4 = {"scriptId": "1635", "agentId": "%s"%agent_id, "campaignName": "%s"%campaign_name, "comment": None,
                       "variables": [{"variableId": "1", "data": "Оформление заявки"}]}
        # data_next_4 = {"scriptId":"1635","agentId":"Agent11","campaignName":"12345","comment":None,"variables":[{"variableId":"1","data":"Отказ от заявки"}]}
        # data_next_5 = {"scriptId":"1635","agentId":"Agent11","campaignName":"12345","comment":None,"variables":[{"variableId":"1","data":"Уже является пользователем услуг от компании 'Воля'"}]}
        # data_next_5 = {"scriptId":"1635","agentId":"Agent11","campaignName":"12345","comment":None,"variables":[{"variableId":"1","data":"Нет ПК/ нет ТВ"}]}
        data_next_finish = {"scriptId": "1635", "agentId": "%s"%agent_id, "campaignName": "%s"%campaign_name, "comment": None,
                            "variables": []}
        steps = [data_next_1, data_next_2, data_next_3, data_next_4]
        data_start['clientId'] = random.choice(abonents)
        data_start['ani'] = random.randint(1, 99999999)
        payload_start = json.dumps(data_start)
        response = self.client.post(url=url_script_start, data=payload_start, headers=headers)
        for step_data in steps:
            self.client.post(url_next, data=json.dumps(step_data), headers=headers)
        self.client.post(url_next, data=json.dumps(data_next_finish), headers=headers)


    # @task(35)
    # def add_excel(self):
    #     files = {'file': open('C:\\Users\\Victor\\PycharmProjects\\Smiddle_API\\Trash\\for_load.xlsx', 'rb')}
    #     self.client.post(excel_url, params=add_excel_params, files=files, auth=authorization)
    #
    # @task(3)
    # def add_excel(self):
    #     files = {'file': open('C:\\Users\\Victor\\PycharmProjects\\Smiddle_API\\Trash\\for_load_1.xlsx', 'rb')}
    #     self.client.post(excel_url, params=add_excel_params_2, files=files, auth=authorization)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
