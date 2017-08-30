import pytest, allure, json, requests, random
import Data.URLs_MAP as URL
from Data.Make_requests_and_answers import JSON_generator as _
import re




# a = open('JSON_files/test.json').read()
#
# b ={"$homephone":"21652"}
#
# for key, val in iter(b.items()):
#     a = a.replace(key, val)
# a = json.dumps(a)
# print(a)

b ={"$homephone": None}
z = _.make_data('test', b)
print(z)