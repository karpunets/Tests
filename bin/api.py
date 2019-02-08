import json
import requests
from .helpers import get_property, get_url
from .session import Session

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
