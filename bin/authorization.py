import requests
from bin.helpers import get_property, get_url
from Data.URLs_MAP import AuthServer

def get_auth_token_with_headers(*args):
    """
    :param args: str Login and str Password
    :return: {"Content-Type": "application/json;charset=UTF-8",
              "X-Smiddle-Auth-Token": str: token}
    """
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    if not args:
        payload = get_property("principal", "credential")
    else:
        payload = {"principal": args[0], "credential": args[1]}
    response = requests.post(url=get_url(AuthServer.token), json=payload, headers=headers)
    assert response.status_code == 200, "AUTH SERVER PROBLEM, response_code = %d" % response.status_code
    headers[response.json()['name']] = response.json()['token']
    return headers
