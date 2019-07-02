from bin.project_config import cfg
from urllib.parse import urljoin


def get_url(url, id=None):
    host = cfg.host
    if "http" not in host:
        host = "http://" + host
    new_url = urljoin(host, str(url))
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

