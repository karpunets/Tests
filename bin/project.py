from bin.client import Session
from bin.cleaner import Cleaner
from ast import literal_eval as make_tuple
from definition import DATA_TO_CLEAN
from .helpers import get_url
from .json_parser import json_schema


class Project:

    def __init__(self):
        self.session = Session()
        self.cleaner = Cleaner()
        self.set_up_clean()
        self.json_schema = json_schema
        # atexit.register(self.tear_down_clean)

    def send(self, method, url, id_to_url, **kwargs):
        if method in ("GET", "DELETE"):
            json = {}
            request_response = self.json_schema.replace_on(url=url, method=method, data=json)
        else:
            request_response = self.json_schema.replace_on(url=url, method=method, data=kwargs['json'])
            kwargs['json'] = request_response['request']
        url = get_url(url, id_to_url)
        response = self.session.send_request(method, url, **kwargs)
        response.expected = request_response['schema']
        return response

    def post(self, url, json=None, id_to_url=None, **kwargs):
        response = self.send(method="POST", url=url, id_to_url=id_to_url, json=json, **kwargs)
        self.cleaner.add(get_url(url), response)
        return response

    def get(self, url, id_to_url=None, **kwargs):
        return self.send(method="GET", url=url, id_to_url=id_to_url, **kwargs)

    def put(self, url, json=None, id_to_url=None, **kwargs):
        return self.send(method="PUT", url=url, id_to_url=id_to_url, json=json, **kwargs)

    def delete(self, url, id_to_url=None, **kwargs):
        return self.send(method="DELETE", url=url, id_to_url=id_to_url, **kwargs)

    def set_up_clean(self):
        """
        Очищает тестовые данные с прошлого запуска
        :return:
        """
        with open(DATA_TO_CLEAN, "r") as f:
            for i in f.readlines():
                rid_url = make_tuple(i)
                self.session.send_request(method="DELETE", url=get_url(rid_url[0], rid_url[1]))


    def tear_down_clean(self):
        """
        Очищает все тестовые данные за данную сессию
        :return:
        """
        for i in self.cleaner.storage_copy:
            self.session.delete(url=i[0], id_to_url=i[1])


send_request = Project()
