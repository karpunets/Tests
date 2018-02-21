import requests, json


class Client(object):
    def __init__(self):
        self.session = requests.Session
        self.session.headers = {'content-type': "application/json;charset=UTF-8"}
        self.auth = ("Root", "Smidle098adm!")

    def get(self, req_url, req_params):
        return self.session.get(url=req_url, params=req_params)
