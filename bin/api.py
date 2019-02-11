from bin import _request


def root_group_id():
    response = _request.get('groups')
    if "ROOT" in response.json()[0]["name"]:
        return response.json()[0]["groupId"]


def root_role_id():
    response = _request.get('roles')
    for role in response.json():
        if role['name'] == "ROOT":
            return role['roleId']


def get_role_id(role_name):
    response = _request.get('roles')
    for role in response.json():
        if role['name'] == role_name:
            return role['roleId']
