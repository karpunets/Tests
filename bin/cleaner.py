import collections
from Data import identificators
from definition import DATA_TO_CLEAN
import atexit


# TODO: записывать в json файл, ссылку на файл для очистки. Файл генерировать с данными новый, где в названии указывать
# дату\сервер? И очищать после чистки
class Cleaner:

    def __init__(self):
        self._storage = collections.deque()
        self.file_path = DATA_TO_CLEAN
        atexit.register(self.write_to_file)

    @property
    def storage(self):
        return self._storage

    @property
    def storage_copy(self):
        return list(self._storage)

    def write_to_file(self):
        if self._storage:
            with open(self.file_path, "w") as f:
                for i in self._storage:
                    f.write(str(i)+"\n")

    def add(self, url_name, response):
        rid_list = self.take_rid_list_from_response(response)
        for i in rid_list:
            self._storage.appendleft((url_name, i))

    @staticmethod
    def take_rid_list_from_response(response):
        response = response.json()
        params_list = identificators.rid_params_map
        rid_list = [response[i] for i in params_list if i in response.keys() if isinstance(response[i], str)]
        return rid_list

    def remove(self, url_name, rid):
        url_with_rid = (url_name, rid)
        while url_with_rid in self._storage:
            self._storage.remove(url_with_rid)
