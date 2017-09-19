import json, requests

from locust import HttpLocust, TaskSet, task

headers = {'content-type': "application/json;charset=UTF-8",
           'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}
url = '/SmiddleAgentScripting/as/script_executor/script_start'
data = json.dumps(
    {"clientId": "2222", "ani": "1535", "agentId": "1", "scriptId": "1635", "campaignName": "O_TELE_CROSS_1"})


class UserBehavior(TaskSet):
    @task(1)
    def profile(self):
        response = self.client.post(url=url, data=data, headers=headers)
        print(response.status_code)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
