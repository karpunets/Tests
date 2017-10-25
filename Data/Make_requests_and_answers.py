import json, re, pytest, random, string

from Data.Requests_default_map import defaul_request
from Data.Response_default_map import defaul_response



random_name = lambda: ''.join(random.choice(string.ascii_letters + string.digits) for list in range(8))


# Получаем и преобразуем JSON файл, согласно переданным параметрам
def make_test_data(json_name, data= {}, default=False):
    # Определяем откуда брать json файл
    path = 'JSON_files/%s.json' % json_name
    if default == True:
        path = path.replace("JSON_files/", "JSON_files/default_data/")
    json_file = open(path, encoding="utf8").read()
    # Если передали параметры для изменения, заменяем их
    if len(data) > 0:
        for key, val in iter(data.items()):
            try:
                if type(val) == int:
                    key = '"%s"' % key
                    val = str(val)
                json_file = json_file.replace(key, val)
            # Возникает если передать None(null)
            except TypeError:
                continue
    # Вместо не переданных параметров подставляем null
    json_file = re.sub(r'(\$[\w]+)', "null", json_file)
    # Преобразуем в dict для удобства
    return json.loads(json_file)





