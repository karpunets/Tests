from requests.sessions import Session as Requests_session
from .cleaner import Cleaner
from .helpers import get_url
from .authorization import get_auth_token_with_headers


class Session(Requests_session):
    """
    Reinitialize requests.Session with Smiddle auth token.
    Иннициализация сессия проиходит в .bin.__init__
    Если отправить запрос с собственными headers, то будет использована новая(одноразовая) Сессия
    """

    def __init__(self):
        super(Session, self).__init__()
        self.headers = get_auth_token_with_headers()
        self.cleaner = Cleaner()

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
        response = self.choose_request_method(method="POST", url=url, json=json, id_to_url=id_to_url, **kwargs)
        self.cleaner.add_for_clean(url, response)
        return response

    def put(self, url, json=None, id_to_url=None, **kwargs):
        return self.choose_request_method(method="PUT", url=url, json=json, id_to_url=id_to_url, **kwargs)

    def delete(self, url, id_to_url=None, **kwargs):
        self.cleaner.success_deleted(id_to_url)
        return self.choose_request_method(method="DELETE", url=url, id_to_url=id_to_url, **kwargs)


req = Session()
