import json
from urllib.parse import urljoin
from definition import PROPERTIES_DIR
from Data import URLs_MAP

class Property:
    def get(*args):
        f = open(PROPERTIES_DIR, encoding="utf-8").read()
        properties = json.loads(f)
        if len(args) != 0:
            return {key:properties[key] for key in args}
        else:
            return  properties




class URL:
    def get(name):
        server = Property.get("server")
        server_addr = server['server']
        url = getattr(URLs_MAP, name)
        if "http" not in server_addr:
            server_addr ="http://" + server_addr
        new_url = urljoin(server_addr, url)
        return new_url


print(URL.get("get_user_list"))