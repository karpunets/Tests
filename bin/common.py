import json, re, random, string, codecs, os, time
from types import DynamicClassAttribute
from definition import ROOT_DIR
from enum import Enum


class MyEnum(Enum):

    def __str__(self):
        return str(self.value)

    @DynamicClassAttribute
    def path(self):
        """Class path"""
        return "%s.%s" % (self.__class__.__name__, self._name_)







# TODO: Избавится от файла, перенести в сессии или helpers
# TODO: Нужно придумать, как сделать проверку по тому, отбрабатывает ли запрос без токена

def random_string():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3, 10)))


def date_now():
    return round(time.time() * 1000)





# Получаем и преобразуем JSON файл, согласно переданным параметрам
# TODO: Вынести в helpers добавить возможность добавлять ключи, которые не начинаются с символа $
def parse_request(json_name, data={}):
    # Определяем откуда брать json файл
    if "/" not in json_name:
        path = 'Test_data/%s.json' % json_name
    else:
        path = os.path.normpath(os.path.join(ROOT_DIR, json_name + ".json"))
    json_file = open(path, encoding="utf8").read()

    # Доп. ф-ция для использования рекурсии
    # TODO: Вынести replace в helpers, rename on replace_string_on

    def replace(json_file, data):
        if len(data) > 0:
            for key, val in iter(data.items()):
                try:
                    if isinstance(val, (int, dict)):
                        # Для того, чтобы подставить int число в строку
                        if '"%s"' % key in json_file:
                            key = '"%s"' % key
                        val = str(val)
                    if isinstance(val, list):
                        key = '"%s"' % key
                        val = "%s" % val
                    json_file = json_file.replace(key, val)
                # Возникает если передать None(null)
                except TypeError:
                    continue
        # Для преобразования методом json.loads должны быть везде двойные кавычки
        json_file = json_file.replace("'", '"')
        json_file = json_file.replace("False", 'false')
        json_file = json_file.replace("True", 'true')
        return json_file

    result = replace(json_file, data)
    # Вместо не переданных параметров подставляем null
    result = re.sub(r'(\"?\$[\w]+\"?)', 'null', result)
    result = json.loads(result)
    return result


# TODO: Продумать как обьеденить со стандартным assert для илспользования multiassert
def equal_schema(response, schema, assert_keys_quantity=True):
    # Переменная для сбора ошибок
    not_equal = []
    # Мапа для преобразований json обьектов в python
    default_types = {'string': str,
                     'number': int,
                     'null': None,
                     'object': dict,
                     'boolean': bool,
                     'array': list,
                     str: 'string',
                     int: 'number',
                     dict: 'object',
                     bool: 'boolean',
                     list: 'array'
                     }

    # Подпрограмма для использования рекурсии
    def equal(response, schema):
        for (key, val) in response.items():
            # Если пара (ключ:значение), не совпадает, но ключ существует в схеме
            if (key, val) not in schema.items() and key in schema.keys():
                # Если в схеме указана проверка на тип
                if isinstance(schema[key], dict) and 'type' in schema[key].keys() and len(schema[key]) == 1:
                    # Тип не совпадаем, пишем ошибку
                    if not isinstance(val, default_types[schema[key]['type']]):
                        not_equal.append(
                            "{{{0}:{1}}} type of value is not equal to schema type({1})!={2}".format(key, val,
                                                                                                     schema[key][
                                                                                                         'type']))
                    # Подменяем значение в данных, для более коректного отображения в отчетах Allure
                    response[key] = {'type': default_types[type(val)]}
                # Если список, проходимся по елементам в списке с применением рекурсии
                elif isinstance(val, list):
                    for param in val:
                        equal(param, schema[key][val.index(param)])
                # Если тип значения - обьект, так же применяем рекурсию
                elif isinstance(val, dict):
                    equal(response[key], schema[key])
                else:
                    not_equal.append(
                        "Value {{{0}:{1}}} not match schemas value {{{0}:{2}}}".format(key, val, schema[key]))
            elif (key, val) not in schema.items() and key not in schema.keys():
                not_equal.append("{{{0}:{1}}} the key '{0}' were not found in schema".format(key, val))

    def find_differences(response, schema):
        if len(schema) > len(response):
            for key in schema:
                if key not in response.keys():
                    not_equal.append('There is no key "{0}" in response keys {1}, but it exist in schema'.format(key,list(response.keys())))
        else:
            equal(response, schema)

    # Если есть ошибки, делаем асерт, для удобства отображения в отчетах
    if assert_keys_quantity == True and len(response) == len(schema) or assert_keys_quantity == False:
        equal(response, schema)
    else:
        s = lambda: "more" if len(response) > len(schema) else "less"
        not_equal.append("Number of keys in  response %s than number of keys in schema" % s())
        find_differences(response, schema)
    assert response == schema, (not_equal)
    return True


def convert_to_utf_8(fileName):
    csv_file = "Test_data/%s.csv" % fileName
    f = codecs.open(csv_file, 'r', 'cp1251')
    u = f.read()  # now the contents have been transformed to a Unicode string
    new_file_path = csv_file + "_converted.csv"
    out = codecs.open(new_file_path, 'w', 'utf-8')
    out.write(u)  # and now the contents have been output as UTF-8
    out.close()
    return new_file_path
