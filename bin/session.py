import requests, json


class Authorization(object):
    def __init__(self, principal, credential):
        self.principal = principal
        self.credential = credential

    def token(self):
        headers = {"Content-Type":"application/json"}
        response = requests.post()


class Client(object):


    session = requests.Session()
    headers = {'content-type': "application/json;charset=UTF-8"}
    auth = ("Root", "Smidle098adm!")



    # @staticmethod
    # def getInstance():
    #     if (Client.s == None):
    #         Client.s = Client("http://172.22.2.66:8080/SmiddleQualityService/qos/report/metadata", params={})
    #     return Client.s
    #
    # def __init__(self, url, params, data):
    #     requests.request()
    #     self.session = requests.Session()
    #     self.headers = {'content-type': "application/json;charset=UTF-8"}
    #     self.auth = ("Root", "Smidle098adm!")
    #     self.url = url
    #     self.params = params
    #     self.data = json.dumps(data)


    def get(url, params):
        return Client.session.get(url=url, params=params, headers = Client.headers)

    def post(self):
        return self.session.post(url=self.url, params=self.params, headers=self.headers)

    def put(self):
        return self.session.put(url=self.url, params=self.params, data=self.data, headers=self.headers)

    def delete(self):
        return self.session.delete(url=self.url, params=self.params, data=self.data, headers=self.headers)


par = Client("http://172.22.2.66:8080/SmiddleQualityService/qos/report/metadata", params={})
print(par.get())