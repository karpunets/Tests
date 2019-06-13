import atexit
import json
import re
from os import path
from bin.client import Session
from bin.cleaner import Cleaner
from ast import literal_eval as make_tuple
from definition import DATA_TO_CLEAN, SCHEMAS_DIR
from .helpers import get_url


class Project:

    def __init__(self):
        self.session = Session()
        self.cleaner = Cleaner()
        self.set_up_clean()
        # atexit.register(self.tear_down_clean)

    def send(self, method, url, id_to_url, **kwargs):
        if method in ("GET", "DELETE"):
            json = {}
            request_response = self.replace(self._path_to_schema(url, method), json)

        else:
            request_response = self.replace(self._path_to_schema(url, method), kwargs['json'])
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

    @staticmethod
    def _path_to_schema(url, method_name):
        file_name = method_name.lower() + "_" + url.path.split('.')[1] + ".json"
        schema_abs_path = path.join(url.path.split('.')[0], file_name)
        schema_full_path = path.join(SCHEMAS_DIR, schema_abs_path)
        return schema_full_path

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

    @staticmethod
    def get_file_data(file_path):
        try:
            with open(file_path, encoding="utf8") as f:
                return f.read()
        except FileNotFoundError:
            return str({"request": {}, "schema": {}})

    def replace(self, json_path, data=None):
        json_file = self.get_file_data(file_path=json_path)
        if data:
            for key, val in iter(data.items()):
                if key.startswith("$"):
                    if isinstance(val, (int, dict, list)):
                        key = '"%s"' % key
                        val = str(val)
                    if val is None:
                        key = '"%s"' % key
                        val = "null"
                    json_file = json_file.replace(key, val)
        json_file = json_file.replace("'", '"').replace("False", 'false').replace("True", 'true')
        # Вместо не переданных параметров подставляем null
        result = re.sub(r'(\"?\$[\w]+\"?)', 'null', json_file)
        result = json.loads(result)
        return result


send_request = Project()
