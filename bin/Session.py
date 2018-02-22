import requests, json


class Client:
    session = requests.Session
    session.headers = {'content-type': "application/json;charset=UTF-8"}
    session.auth = ("Root", "Smidle098adm!")

    def get(req_url, req_params):
        return session.get(url=req_url, params=req_params)





print(Client.get(req_url="http://172.22.2.66:8080/SmiddleQualityService/qos/report/metadata", req_params={}))