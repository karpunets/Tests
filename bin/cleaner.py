import collections
from ast import literal_eval as make_tuple
from definition import DATA_DIR
from Data import identificators
from bin.helpers import get_url
from os import path
from definition import DATA_TO_CLEAN
import atexit


class Cleaner:

    def __init__(self):
        self._storage = collections.deque()
        self.file_path = DATA_TO_CLEAN
        atexit.register(self.write_to_file)

    @property
    def storage(self):
        return self._storage

    def write_to_file(self):
        if self.storage:
            with open(self.file_path, "w") as f:
                    for i in self.storage:
                        f.write(str(i))

    def add(self, url_name, response):
        rid_list = self.take_rid_list_from_response(response)
        for i in rid_list:
            self.storage.append((url_name, i))

    @staticmethod
    def take_rid_list_from_response(response):
        response = response.json()
        params_list = identificators.rid_params_map
        rid_list = [response[i] for i in params_list if i in response.keys() if isinstance(response[i], str)]
        return rid_list

    def remove(self, url_name, rid):
        url_with_rid = (url_name, rid)
        while url_with_rid in self.storage:
            self.storage.remove(url_with_rid)



# cleaner = Cleaner()



