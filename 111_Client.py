import json
import requests
from requests.sessions import Session
from bin.helpers import get_property, get_url



def get_token(*args):
    headers = {"Content-Type": "application/json"}
    if len(args) == 0:
        payload = get_property("principal", "credential")
    else:
        payload = {"principal": args[0], "credential": args[1]}
    response = requests.post(url=get_url("token"), data=json.dumps(payload), headers=headers)
    return response.json()


class Client(Session):

    def __init__(self):
        super(Client, self).__init__()
        headers = {'content-type': "application/json;charset=UTF-8"}
        auth_token = get_token()
        headers[auth_token['name']] = auth_token['token']
        self.headers = headers

    def choose_request_method(self, method, url, **kwargs):
        if "headers" not in kwargs:
            return self.request(method=method, url=url, **kwargs)
        else:
            with Session() as session:
                return session.request(method=method, url=url, **kwargs)


    def get(self, url, id=None, **kwargs):
        url = get_url(url, id)
        return self.choose_request_method(method="GET", url=url, **kwargs)

    # def post(url, data=None, params=None, headers=None):
    #     if headers is None:
    #         response = Client.session.post(url=get_url(url), params=params, data=json.dumps(data))
    #     else:
    #         response = requests.post(url=get_url(url), params=params, data=json.dumps(data), headers=headers)
    #     return response
    #
    # def put(url, data=None, params=None, id=None, headers=None):
    #     if headers is None:
    #         response = Client.session.put(url=get_url(url, id), params=params, data=json.dumps(data))
    #     else:
    #         response = requests.put(url=get_url(url, id), params=params, data=json.dumps(data), headers=headers)
    #     return response
    #
    # def delete(url, data=None, params=None, id=None, headers=None):
    #     if headers is None:
    #         response = Client.session.delete(url=get_url(url, id), params=params, data=json.dumps(data))
    #     else:
    #         response = requests.delete(url=get_url(url, id), params=params, data=json.dumps(data), headers=headers)
    #     return response

a = Client()

print(a.get(url = "groups", headers = {"X-Smiddle-Auth-Token":"efb6ad2c-6f1d-44d0-84ef-c064e36681b5"}))