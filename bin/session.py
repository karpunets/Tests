import requests, json


class Authorization(object):
    def __init__(self, principal, credential):
        self.principal = principal
        self.credential = credential

    def token(self):
        headers = {"Content-Type":"application/json"}
        response = requests.post()


class Client(object):

    def __init__(self, url, params, data):
        self.session = requests.Session()
        self.headers = {'content-type': "application/json;charset=UTF-8"}
        self.auth = ("Root", "Smidle098adm!")
        self.url = url
        self.params = params
        self.data = json.dumps(data)


    def get(self):
        return self.session.get(url=self.url, params=self.params, headers = self.headers)

    def post(self):
        return self.session.post(url=self.url, params=self.params, headers=self.headers)

    def put(self):
        return self.session.put(url=self.url, params=self.params, data=self.data, headers=self.headers)

    def delete(self):
        return self.session.delete(url=self.url, params=self.params, data=self.data, headers=self.headers)


par = Client("http://172.22.2.66:8080/SmiddleQualityService/qos/report/metadata", params={})
print(par.get())