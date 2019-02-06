from bin.session import client
from bin.session import Client
from bin.helpers import get_property, get_url


test = Client()
a = test.get(url = "groups")
print(test.get(url = "groups"))
print(a.json())