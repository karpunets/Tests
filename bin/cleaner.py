import collections
from ast import literal_eval as make_tuple
from definition import DATA_DIR
from Data import identificators
from bin.helpers import get_url
from os import path


class Cleaner:

    def __init__(self):
        self.storage = collections.deque()
        self.file_path = path.join(DATA_DIR, "data_to_clean.txt")
        # self.clean()

    def __del__(self):
        self.write_to_file()

    def write_to_file(self):
        with open(self.file_path, "w") as f:
            for i in self.storage:
                f.write(str(i))

    def add(self, url_name, response):
        rid_list = self.take_rid_list_from_response(response)
        url = get_url(url_name)
        for i in rid_list:
            self.storage.append((url, i))

    @staticmethod
    def take_rid_list_from_response(response):
        response = response.json()
        params_list = identificators.rid_params_map
        rid_list = [response[i] for i in params_list if i in response.keys() if isinstance(response[i], str)]
        # rid_list = {param: response[param] for param in params_list if param in response.keys()}
        # if len(ident.keys()) > 1:
        #     for i in ident:
        #         rid = ident[i] if url_name.startswith(i) else None
        # else:
        #     rid = list(ident.values())[0]
        # url = get_url(url_name)
        return rid_list

    def remove(self, url_name, rid):
        url = get_url(url_name)
        url_with_rid = (url, rid)
        while url_with_rid in self.storage:
            self.storage.remove(url_with_rid)

    # def clean(self):
    #     for i in self.file.readlines():
    #         rid_url = make_tuple(i)
    #         for j in rid_url[0]:
    #             print(j, "hello")
    #             # self.delete(url=rid_url[1], id_to_url=j)







