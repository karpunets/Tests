import json
from urllib.parse import urljoin
from definition import PROPERTIES_DIR
from Data import URLs_MAP


def getProperty(*args):
    f = open(PROPERTIES_DIR, encoding="utf-8").read()
    properties = json.loads(f)
    if len(args) != 0:
        return {key:properties[key] for key in args}
    else:
        return  properties


def getUrl(name, id=None):
    server = getProperty("server")
    server_addr = server['server']
    url = getattr(URLs_MAP, name)
    if "http" not in server_addr:
        server_addr = "http://" + server_addr
    new_url = urljoin(server_addr, url)
    if id is not None:
        new_url = urljoin(new_url, id)
    return new_url


