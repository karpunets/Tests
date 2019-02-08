import requests
import json
from requests.sessions import Session as Requests_session
from bin.helpers import get_property, get_url
# from .api import get_token


def get_token(*args):
    headers = {"Content-Type": "application/json"}
    if len(args) == 0:
        payload = get_property("principal", "credential")
    else:
        payload = {"principal": args[0], "credential": args[1]}
    response = requests.post(url=get_url("token"), data=json.dumps(payload), headers=headers)
    return response.json()


def get_headers_with_credentials(principial, credential):
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    auth_token = get_token(principial, credential)
    headers[auth_token['name']] = auth_token['token']
    return headers


def root_group_id():
    response = Session.get('groups')
    if "ROOT" in response.json()[0]["name"]:
        return response.json()[0]["groupId"]


def root_role_id():
    response = Session.get('roles')
    for role in response.json():
        if role['name'] == "ROOT":
            return role['roleId']


def get_role_id(role_name):
    response = Session.get('roles')
    for role in response.json():
        if role['name'] == role_name:
            return role['roleId']


class Session(Requests_session):

    def __init__(self):
        super(Session, self).__init__()
        headers = {'content-type': "application/json;charset=UTF-8"}
        auth_token = get_token()
        headers[auth_token['name']] = auth_token['token']
        self.headers = headers

    def choose_request_method(self, method, url, **kwargs):
        if "headers" not in kwargs:
            return self.request(method=method, url=url, **kwargs)
        else:
            with Requests_session() as session:
                return session.request(method=method, url=url, **kwargs)

    def get(self, url, id=None, **kwargs):
        url = get_url(url, id)
        return self.choose_request_method(method="GET", url=url, **kwargs)

    def post(self, url, id=None, **kwargs):
        url = get_url(url, id)
        return self.choose_request_method(method="POST", url=url, **kwargs)

    def put(self, url, id=None, **kwargs):
        url = get_url(url, id)
        return self.choose_request_method(method="PUT", url=url, **kwargs)

    def delete(self, url, id=None, **kwargs):
        url = get_url(url, id)
        return self.choose_request_method(method="DELETE", url=url, **kwargs)



# class Client(object):
#
#     def __init__(self):
#         self.session = requests.Session()
#         headers = {'content-type': "application/json;charset=UTF-8"}
#         auth_token = get_token()
#         headers[auth_token['name']] = auth_token['token']
#         self.session.headers = headers
#
#
#     # def update_headers(session):
#     #     headers = {'content-type': "application/json;charset=UTF-8"}
#     #     auth_token = get_token()
#     #     headers[auth_token['name']] = auth_token['token']
#     #     session.headers = headers
#
#     def get(self, url, params=None, id=None, headers=None):
#         if headers is None:
#             response = self.session.get(url=get_url(url, id), params=params)
#         else:
#             response = requests.get(url=get_url(url, id), params=params, headers=headers)
#         return response
#
#     def post(url, data=None, params=None, headers=None):
#         if headers is None:
#             response = Client.session.post(url=get_url(url), params=params, data=json.dumps(data))
#         else:
#             response = requests.post(url=get_url(url), params=params, data=json.dumps(data), headers=headers)
#         return response
#
#     def put(url, data=None, params=None, id=None, headers=None):
#         if headers is None:
#             response = Client.session.put(url=get_url(url, id), params=params, data=json.dumps(data))
#         else:
#             response = requests.put(url=get_url(url, id), params=params, data=json.dumps(data), headers=headers)
#         return response
#
#     def delete(url, data=None, params=None, id=None, headers=None):
#         if headers is None:
#             response = Client.session.delete(url=get_url(url, id), params=params, data=json.dumps(data))
#         else:
#             response = requests.delete(url=get_url(url, id), params=params, data=json.dumps(data), headers=headers)
#         return response

    # session = requests.Session()
    # update_headers(session)


#
# print(requests.get(url=get_url("groups")))
# print("qq")
# print(Client.get(url = "groups"))
