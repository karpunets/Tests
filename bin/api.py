from bin.session import req


def root_group_id():
    response = req.get('groups')
    if "ROOT" in response.json()[0]["name"]:
        return response.json()[0]["groupId"]


def root_role_id():
    response = req.get('roles')
    for role in response.json():
        if role['name'] == "ROOT":
            return role['roleId']


def get_role_id(role_name):
    response = req.get('roles')
    for role in response.json():
        if role['name'] == role_name:
            return role['roleId']
