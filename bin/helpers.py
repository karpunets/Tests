import json
from urllib.parse import urljoin
from definition import PROPERTIES_DIR
from Data import URLs_MAP


def get_property(*args):
    f = open(PROPERTIES_DIR, encoding="utf-8").read()
    properties = json.loads(f)
    if len(args) != 0:
        return {key: properties[key] for key in args}
    else:
        return properties


def get_url(name, id=None):
    server = get_property("server")
    server_address = server['server']
    url = getattr(URLs_MAP, name)
    if "http" not in server_address:
        server_address = "http://" + server_address
    new_url = urljoin(server_address, url)
    if id is not None:
        new_url = new_url + "/"
        new_url = urljoin(new_url, id)
    return new_url


def make_user_group_roles(group_roles_obj):
    """
    :param group_roles_obj: {'groupId': roleId} :type roleId: str or list
    :return: [{'group': {'groupId': str}, 'roles': [{'roleId': str}], 'applyRolesRecursively': False}]
    """
    user_group_roles = list()
    for groupId in group_roles_obj:
        result = dict()
        roles = list()
        result['group'] = {"groupId": groupId}
        if isinstance(group_roles_obj[groupId], list):
            for roleId in group_roles_obj[groupId]:
                roles.append({'roleId': roleId})
        else:
            roles.append({'roleId': group_roles_obj[groupId]})
        result['roles'] = roles
        result["applyRolesRecursively"] = False
        user_group_roles.append(result)
    return user_group_roles
