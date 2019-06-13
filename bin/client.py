from requests.sessions import Session as Requests_session
from .authorization import get_auth_token_with_headers


# TODO: Перенести очистку данных в cleaner не используя Session
class Session(Requests_session):
    """
    Reinitialize requests.Session with Smiddle auth token.
    Иннициализация сессия проиходит в .bin.__init__
    Если отправить запрос с собственными headers, то будет использована новая(одноразовая) Сессия
    """

    def __init__(self):
        super(Session, self).__init__()
        self.headers = get_auth_token_with_headers()

    def choose_request_method(self, method, url, **kwargs):
        """
        Если headers переданы создам "одноразовую" сессию, в противном случае используем старую сессию
        Если headers переданы без X-Smiddle-Auth-Token то добавляем авторизацию
        :param method:
        :param url:
        :param id_to_url:
        :param kwargs:
        :return:
        """

        if "headers" not in kwargs:
            return self.request(method=method, url=url, **kwargs)
        elif "X-Smiddle-Auth-Token" not in kwargs['headers'].keys():
            new_headers = self.headers.copy()
            new_headers.update(kwargs['headers'])
            kwargs['headers'] = new_headers
        with Requests_session() as session:
            return session.request(method=method, url=url, **kwargs)

    def send_request(self, method, url, **kwargs):
        return self.choose_request_method(method=method, url=url,  **kwargs)

    # def get(self, url, id_to_url=None, **kwargs):
    #     return self.choose_request_method(method="GET", url=url, id_to_url=id_to_url, **kwargs)
    #
    # def post(self, url, json=None, id_to_url=None, **kwargs):
    #
    #     return self.choose_request_method(method="POST", url=url, json=json, id_to_url=id_to_url, **kwargs)
    #
    # def put(self, url, json=None, id_to_url=None, **kwargs):
    #     return self.choose_request_method(method="PUT", url=url, json=json, id_to_url=id_to_url, **kwargs)
    #
    # def delete(self, url, id_to_url=None, cleaner=False, **kwargs):
    #     return self.choose_request_method(method="DELETE", url=url, id_to_url=id_to_url, **kwargs)

