import json

with open('JSON_files/mapfields.json', encoding="utf8") as data_file:
    add_result = json.load(data_file)

for i in add_result:
    print(i)