import json, re, random, string, pytest


def random_string():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(3,10)))

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
    json_file = re.sub(r'(\"\$[\w]+\")', 'null', json_file)
    json_file = json.loads(json_file)
    return {'request':json_file['request'], 'schema':json_file['schema']} if default==False else json_file


def equal_schema(response, schema, assert_keys_quantity=True):
    # Переменная для сбора ошибок
    not_equal = []
    #Мапа для преобразований json обьектов в python
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
                if type(schema[key]) == dict and 'type' in schema[key].keys() and len(schema[key]) == 1:
                    # Тип не совпадаем, пишем ошибку
                    if type(val) != default_types[schema[key]['type']]:
                        not_equal.append(
                            "{{{0}:{1}}} type of value is not equal to schema type({1})!={2}".format(key, val,
                                                                                                     schema[key][
                                                                                                         'type']))
                    # Подменяем значение в данных, для более коректного отображения в отчетах Allure
                    response[key] = {'type': default_types[type(val)]}
                # Если список, проходимся по елементам в списке с применением рекурсии
                elif type(val) == list:
                    for param in val:
                        equal(param, schema[key][val.index(param)])
                # Если тип значения - обьект, так же применяем рекурсию
                elif type(val) == dict:
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
                    not_equal.append('There is no key "{0}" in response keys {1}, but it exist in schema'.format(key, list(response.keys())))
        else:
            equal(response, schema)

    # Если есть ошибки, делаем асерт, для удобства отображения в отчетах
    if assert_keys_quantity == True and len(response) == len(schema) or assert_keys_quantity == False:
        equal(response, schema)
    else:
        s = lambda: "more" if len(response) > len(schema) else "less"
        not_equal.append("Number of keys in  response %s than number of keys in schema"%s())
        find_differences(response, schema)
    assert response == schema,(not_equal)
    return True
