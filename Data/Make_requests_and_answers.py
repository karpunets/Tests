from Data.Requests_default_map import defaul_request
from Data.Response_default_map import defaul_response


class JSON_generator(object):
    def generate_JSON(JSON_request, kwargs):

        for i in kwargs.items():
            # Проверка есть ли нужное значение в основном теле запроса
            if i[0] in JSON_request:
                JSON_request[i[0]] = kwargs[i[0]]
            # Если не в основном, ищем во вложенных списка/словарях
            else:
                # Ищем значение во вложенных словарях
                for j in JSON_request:
                    # Проверяем, если ответ идет в списке
                    if type(JSON_request[j]) == list:
                        JSON_generator.generate_JSON(JSON_request[j][0], {i[0]: i[1]})
                    # Ищем вложенные словари
                    if type(JSON_request[j]) == dict:
                        # Проделываем все то же с вложенным словарем
                        JSON_generator.generate_JSON(JSON_request[j], {i[0]: i[1]})
        return JSON_request

    def get_JSON_request(request_name, **kwargs):
        data = kwargs
        request = defaul_request(request_name)
        return JSON_generator.generate_JSON(request, data)

    def get_JSON_response(response_name, **kwargs):
        data = kwargs
        request = defaul_response(response_name)
        return JSON_generator.generate_JSON(request, data)

