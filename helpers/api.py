from bin.project import send_request
from Data.URLs_MAP import mgr


def root_group_id():
    response = send_request.get(mgr.groups)
    if "ROOT" in response.json()[0]["name"]:
        return response.json()[0]["groupId"]


def root_role_id():
    response = send_request.get(mgr.roles)
    for role in response.json():
        if role['name'] == "ROOT":
            return role['roleId']


def get_role_id(role_name):
    response = send_request.get(mgr.roles)
    for role in response.json():
        if role['name'] == role_name:
            return role['roleId']
