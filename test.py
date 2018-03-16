import requests, json

headers ={"X-Smiddle-Auth-Token": "c1a000ad-f900-4140-a48b-812f5f5b3dc0", 'Content-Type': 'multipart/form-data'}
data = {"groups": [{"groupId": "7c4d48e9-7d6a-4184-ae3a-2889fa6f1cd4"}], "roles": [{"roleId": "b1fb18ba-874a-4180-bdd8-a7191496db26"}], "updateDuplicates": True}
req = "type=application/json"
files = {'file': ('Users_adm.xlsx', open('C:\\Users\\Victor\\PycharmProjects\\scripts\\Users_adm.xlsx', 'rb'))}
url = "http://10.100.70.11:8080/SmiddleManager/adm/management/import/users/excel "

# data = json.dumps(data)

response = requests.post(url=url, headers=headers, files = files)
print(response.status_code)
print(response.text)


# a = {'file': ('report.xls', open('C:\\Users\\Victor\\PycharmProjects\\scripts\\Users_adm.xlsx', 'rb'), 'multipart/form-data', {'request': data})}