import json
import re
from os import path
from definition import SCHEMAS_DIR


class Parser:

    def replace_on(self, url, method, data):
        return self.replace(self._path_to_json(url, method), data)

    @staticmethod
    def _path_to_json(url, method_name):
        file_name = method_name.lower() + "_" + url.path.split('.')[1] + ".json"
        schema_abs_path = path.join(url.path.split('.')[0], file_name)
        schema_full_path = path.join(SCHEMAS_DIR, schema_abs_path)
        return schema_full_path

    @staticmethod
    def get_file_data(file_path):
        try:
            with open(file_path, encoding="utf8") as f:
                return f.read()
        except FileNotFoundError:
            return str({"request": {}, "schema": {}})

    @staticmethod
    def replace_default_values(json_file):
        result = json.loads(json_file)
        for key,val in result['request'].items():
            if isinstance(val, dict) and ("default", "value") == tuple(val.keys()):
                if isinstance(val['value'], str):
                    if val['value'].startswith('$'):
                        result['request'][key] = val['default']
                        result['schema'][key]["allowed"] = [val['default']]
                    else:
                        result['request'][key] = val['value']
                else:
                    result['request'][key] = val['value']
        result = json.loads(re.sub(r'(\"?\$[\w]+\"?)', 'null', json.dumps(result)))
        return result

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
        return self.replace_default_values(json_file)


json_schema = Parser()

