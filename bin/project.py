import atexit
import json
import re
from os import path
from bin.client import Session
from bin.cleaner import Cleaner
from ast import literal_eval as make_tuple
from definition import DATA_TO_CLEAN, SCHEMAS_DIR
from Data.URLs_MAP import Manager
from .helpers import get_url


class Project:

    def __init__(self):
        self.session = Session()
        self.cleaner = Cleaner()
        self.set_up_clean()
        atexit.register(self.tear_down_clean)

    def send(self, method, url, id_to_url, **kwargs):
        if method in ("GET", "DELETE"):
            json = {}
            request_response = self.replace(self._path_to_schema(url, method), json)

        else:
            request_response = self.replace(self._path_to_schema(url, method), kwargs['json'])
            kwargs['json'] = request_response['data']
        url = get_url(url, id_to_url)
        response = self.session.send_request(method, url, **kwargs)
        response.schema_of_expected_response = request_response['schema']
        return response

    def post(self, url, json=None, id_to_url=None, **kwargs):
        response = self.send(url, json, id_to_url, **kwargs)
        self.cleaner.add(url, response)
        return response

    def get(self, url, id_to_url=None, **kwargs):
        return self.send(url, json=None, id_to_url=id_to_url, **kwargs)

    def put(self, url, id_to_url=None, json=None, **kwargs):
        return self.send(url, json, id_to_url, **kwargs)

    def delete(self, url, id_to_url=None, cleaner=False, **kwargs):
        if not cleaner:
            self.cleaner.remove(url, id_to_url)
        return self.send(url, id_to_url, **kwargs)

    @staticmethod
    def _path_to_schema(url, method_name):
        file_name = method_name.lower() + "_" + url.path.split('.')[1] + ".json"
        schema_abs_path = path.join(url.path.split('.')[0], file_name)
        schema_full_path = path.join(SCHEMAS_DIR, schema_abs_path)
        return schema_full_path

    # def _get_expected_response(self, url, method_name, data):
    #     schema_path = self._path_to_schema(url, method_name)
    #     result = self.replace(schema_path, data)
    #
    #     return "response"

    def set_up_clean(self):
        """
        Очищает "заваленные" тесты с прошлого запуска
        :return:
        """
        with open(DATA_TO_CLEAN, "r") as f:
            for i in f.readlines():
                rid_url = make_tuple(i)
                self.session.delete(url=rid_url[0], id_to_url=rid_url[1], cleaner=True)

    def tear_down_clean(self):
        """
        Очищает все тестовые данные за данную сессию
        :return:
        """
        for i in self.cleaner.storage_copy:
            self.session.delete(url=i[0], id_to_url=i[1])

    @staticmethod
    def replace(json_path, data):
        with open(json_path, encoding="utf8") as f:
            json_file = f.read()
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


request = Project()

