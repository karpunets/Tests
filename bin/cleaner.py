import collections
from ast import literal_eval as make_tuple
from definition import DATA_DIR
from Data import identificators
from .helpers import get_url
from os import path



class Cleaner:

    def __init__(self):
        self.storage = collections.deque()
        self.file = open(path.join(DATA_DIR, "data_to_clean.txt"), "r+")
        self.clear_db()

    def __del__(self):
        self.write_to_file()

    def write_to_file(self):
        with self.file as f:
            for i in self.storage:
                f.write(str(i))

    def add_for_clean(self, url_name, response):
        rid_url = self.normalize(url_name, response)
        self.storage.append(rid_url)

    @staticmethod
    def normalize(url_name, response):
        response = response.json()
        params_list = identificators.ids_list
        ident = {param:response[param] for param in params_list if param in response.keys()}
        if len(ident.keys()) > 1:
            for key in ident.keys():
                rid = ident[key] if url_name.startswith(key) else None
        else:
            rid =list(ident.values())[0]
        url = get_url(url_name)
        return (rid, url)

    def success_deleted(self, rid):
        print('DELETED', rid)
        self.storage.remove(rid)

    def clear_db(self):

        for i in self.file.readlines():
            rid_url = make_tuple(i)
            self.delete(url=rid_url[1], id_to_url=rid_url[0])







