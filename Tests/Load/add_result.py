import json, requests, random, string, time

from locust import HttpLocust, TaskSet, task


campaign_name = "qqwe"
campaign_id = 146093915

headers = {
    'content-type': "application/json;charset=UTF-8"}

result_codes = ['SUCCESS', 'CD_callResult', 'CD_callStatus', 'CD_callsMade', 'COMENT', 'OtkazValue', 'typeTV',
               'SabjectTV', 'Provider', 'ProviderOther', 'SpeedInet', 'CostService', 'QualityInet', 'PurposeInet',
               'ValuationService', 'UpgradeService', 'QualityTV', 'DeviceInet', 'TypeInet', 'RedialNumber',
               'RedialDate', 'Contact_phone', 'DateCall', 'AgentName', 'Type', 'Service', 'activityFeed',
               'resultKontact', 'OutboundContactTypeOfContact', 'workDate', 'completionDate', 'inquiryTime',
               'OutboundContactSubtotalConversa', 'Campaign', 'Operator_id', 'Callback_used']
code_date = ["RedialDate", "DateCall", "workDate", "completionDate"]
code_int = ['Callback_used', "CD_callsMade"]
f = open("C:\\Users\\Victor\\PycharmProjects\\Smiddle_API\\Tests\\Load\\qq.txt", 'r')
abonents = f.read().split()
f.close()

authorization = ('Root', 'Smidle098adm!')
date_now = lambda: round(time.time() * 1000)
random_string = lambda: ''.join(random.choice(string.ascii_letters + string.digits) for list in range(8))
add_result = {"campaignCode": 'test_111', "clientId": '5544226', "code": 'RESULT_DATE_END',
              "resultValue": '1508230681012', "resultPhone": None}
# f = open("C:\\Users\\Victor\\PycharmProjects\\Smiddle_API\\Trash\\agentids.txt", 'r')
# agentIDs = f.read().split()
# f.close()

server = "http://172.22.2.63:8080"
url = "%s/SmiddleCampaignManager/cm/result/add_result_async"%server
# url = "%s/www"%server
url_get_abonent_and_result = "%s/SmiddleCampaignManager/cm/manager/get_abonent_and_result"%server
# response = requests.post(url=url, data=json.dumps(add_result), headers=headers)
# print(response.cookies)

class UserBehavior(TaskSet):
    @task()
    def as_script(self):
        abonent = random.choice(abonents)
        add_result['clientId'] = str(abonent)
        for code in result_codes:
            if code in code_date:
                add_result['code'] = code
                add_result['resultValue'] = date_now()
            if code in code_int:
                add_result['code'] = code
                add_result['resultValue'] = str(random.randint(1,50))
            else:
                add_result['code'] = code
                add_result['resultValue'] = random_string()
            payload = json.dumps(add_result)
            response = self.client.post(url=url, data=payload, headers=headers)
            print(response.cookies)

    # @task()
    # def get_abonent_and_result(self):



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
