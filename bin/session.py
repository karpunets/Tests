import requests
from requests.sessions import Session as Requests_session
from bin.helpers import get_property, get_url


def get_auth_token_with_headers(*args):
    """
    :param args: str Login and str Password
    :return: {"Content-Type": "application/json;charset=UTF-8",
              "X-Smiddle-Auth-Token: str: token}
    """
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    if len(args) == 0:
        payload = get_property("principal", "credential")
    else:
        payload = {"principal": args[0], "credential": args[1]}
    response = requests.post(url=get_url("token"), json=payload, headers=headers)
    assert response.status_code == 200, "AUTH SERVER PROBLEM, response_code = %d" % response.status_code
    headers[response.json()['name']] = response.json()['token']
    return headers


class Session(Requests_session):
    """
    Reinitialize requests.Session with Smiddle auth token.
    Иннициализация сессия проиходит в .bin.__init__
    Если отправить запрос с собственными headers, то будет использована новая(одноразовая) Сессия
    """

    def __init__(self):
        super(Session, self).__init__()
        self.headers = get_auth_token_with_headers()

    def choose_request_method(self, method, url, id_to_url, **kwargs):
        """
        :param method:
        :param url:
        :param id_to_url:
        :param kwargs:
        :return:
                    Если headers переданы создам "одноразовую" сессию, в противном случае используем старую сессию
        """
        url = get_url(url, id_to_url)
        if "headers" not in kwargs:
            return self.request(method=method, url=url, **kwargs)
        else:
            with Requests_session() as session:
                return session.request(method=method, url=url, **kwargs)

    def get(self, url, id_to_url=None, **kwargs):
        return self.choose_request_method(method="GET", url=url, id_to_url=id_to_url, **kwargs)

    def post(self, url, json=None, id_to_url=None, **kwargs):
        return self.choose_request_method(method="POST", url=url, json=json, id_to_url=id_to_url, **kwargs)

    def put(self, url, json=None, id_to_url=None, **kwargs):
        return self.choose_request_method(method="PUT", url=url, json=json, id_to_url=id_to_url, **kwargs)

    def delete(self, url, id_to_url=None, **kwargs):
        return self.choose_request_method(method="DELETE", url=url, id_to_url=id_to_url, **kwargs)


get_auth_token_with_headers()
