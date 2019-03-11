import atexit
from requests.sessions import Session as Requests_session
from ast import literal_eval as make_tuple
from .cleaner import Cleaner
from .helpers import get_url
from .authorization import get_auth_token_with_headers
from definition import DATA_TO_CLEAN


class Session(Requests_session):
    """
    Reinitialize requests.Session with Smiddle auth token.
    Иннициализация сессия проиходит в .bin.__init__
    Если отправить запрос с собственными headers, то будет использована новая(одноразовая) Сессия


    Осуществляет очистку тестовых данных после тестового прогона, также осуществляет удаленние тестовых данных с
    предыдущего тестового прогона, если они не были удалены
    """

    def __init__(self):
        super(Session, self).__init__()
        self.headers = get_auth_token_with_headers()
        self.set_up_clean()
        self.cleaner = Cleaner()
        atexit.register(self.tear_down_clean)

    def choose_request_method(self, method, url, id_to_url, **kwargs):
        """
        Если headers переданы создам "одноразовую" сессию, в противном случае используем старую сессию
        :param method:
        :param url:
        :param id_to_url:
        :param kwargs:
        :return:
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
        self.cleaner.add(url, response)
        return response

    def put(self, url, json=None, id_to_url=None, **kwargs):
        return self.choose_request_method(method="PUT", url=url, json=json, id_to_url=id_to_url, **kwargs)

    def delete(self, url, id_to_url=None, cleaner=False, **kwargs):
        if not cleaner:
            self.cleaner.remove(url, id_to_url)
        return self.choose_request_method(method="DELETE", url=url, id_to_url=id_to_url, **kwargs)

    def set_up_clean(self):
        """
        Очищает "заваленные" тесты с прошлого запуска
        :return:
        """
        with open(DATA_TO_CLEAN, "r") as f:
            for i in f.readlines():
                rid_url = make_tuple(i)
                self.delete(url=rid_url[0], id_to_url=rid_url[1], cleaner=True)

    def tear_down_clean(self):
        """
        Очищает все тестовые данные за данную сессию
        :return:
        """
        for i in self.cleaner.storage_copy:
            self.delete(url=i[0], id_to_url=i[1])


send_request = Session()
