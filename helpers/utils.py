import json
from urllib.parse import urljoin
from definition import SETTINGS


def get_property(*args):
    with open(SETTINGS, encoding="utf-8") as f:
        prop_file = f.read()
    properties = json.loads(prop_file)
    if args:
        return {key: properties[key] for key in args}
    return properties


def get_url(url, id=None):
    server = get_property("server")
    server_address = server['server']
    if "http" not in server_address:
        server_address = "http://" + server_address
    new_url = urljoin(server_address, str(url))
    if id is not None:
        new_url = urljoin(new_url + "/", id)
    return new_url


def make_user_group_roles(group_roles_obj):
    """
    :param group_roles_obj: {'groupId': roleId} :type roleId: str or list
    :return: [{'group': {'groupId': str}, 'roles': [{'roleId': str}], 'applyRolesRecursively': False}]
    """
    user_group_roles = list()
    for i in group_roles_obj:
        result = dict()
        result['group'] = {"groupId": i}
        if isinstance(group_roles_obj[i], list):
            roles = [{'roleId': groupId} for groupId in group_roles_obj[i]]
        else:
            roles = [{'roleId': group_roles_obj[i]}]
        result['roles'] = roles
        result["applyRolesRecursively"] = False
        user_group_roles.append(result)
    return user_group_roles

