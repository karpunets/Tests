import json, re, pytest, random, string


def random_string():
    random_name = lambda: ''.join(random.choice(string.ascii_letters + string.digits) for list in range(random.randint(1,30)))
    random_string = random_name()
    return random_string

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


def equal_schema(instance, schema, assert_keys_quantity=True):
    # Переменная для сбора ошибок
    not_equal = []
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
    def helper(instance, schema):
        for (key, val) in instance.items():
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
                    instance[key] = {'type': default_types[type(val)]}
                elif type(val) == list:
                    for param in val:
                        helper(param, schema[key][val.index(param)])
                elif type(val) == dict:
                    helper(instance[key], schema[key])
                else:
                    not_equal.append(
                        "Value {{{0}:{1}}} not match schemas value {{{0}:{2}}}".format(key, val, schema[key]))
            elif (key, val) not in schema.items() and key not in schema.keys():
                not_equal.append("The key '%s' where no found in schema" % key)

    # Если есть ошибки, делаем асерт, для удобства отображения в отчетах
    if assert_keys_quantity == True and len(instance) == len(schema):
        helper(instance, schema)
    else:
        not_equal.append("Length of instance != length of schema")

    assert instance == schema,(not_equal)
    return True
