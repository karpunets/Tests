import requests, json, string, random
from Data.URLs_MAP import headers

random_name = lambda: ''.join(random.choice(string.ascii_letters + string.digits) for list in range(8))

# url = "http://172.22.2.63:8080/SmiddleManager/adm/management/add_user"
# a=  {"fname":"name","lname":"sec_name","email":"mail@mail.ru","phone":"0666816545","login":"login","password":"password","agentId":"agent_id","scMode":"0","unmappedCalls":False,"enabled":True,"deleted":False,"dateCreate":1506422851338,"groups":[{"id":2}],"roles":[{"id":3}]}



# user_to_delete = open("user_ids.txt", "w")
# agent_ids = open("agent_ids.txt", "w")
# for i in range (0,100):
#     a['login'] = random_name()
#     a['agentId'] = random.randint(999,99999999)
#     a['phone'] = random.randint(999,99999999)
#     payload = json.dumps(a)
#     response = requests.post(url=url, data=payload, headers=headers)
#     print(response.status_code)
#     agent_ids.write(str(response.json()['agentId']) + "\n")
#     user_to_delete.write(str(response.json()['id']) + "\n")
# user_to_delete.close()
# agent_ids.close()

# url_delete = "http://172.22.2.63:8080/SmiddleManager/adm/management/delete_user"
#
#
# with open("user_ids.txt", "r") as file:
#     id_to_delete = file.read().split()
#
# for i in id_to_delete:
#     response = requests.post(url=url_delete, data=json.dumps({"userId": i}), headers=headers)
#     print(response.status_code)

url = "http://172.22.2.63:8080/SmiddleManager/adm/management/get_user_list"
payload = json.dumps({"roleId":"3","showDeletedOnly":False,"pagination":{"page_number":"1","page_size":"100","sortedField":"login","order":"ASC"}})
response = requests.post(url=url, data=payload, headers=headers)
agent_ids = open("agentids.txt", "w")
for i in response.json()['data']:
    agent_ids.write(str(i['agentId']) + "\n")
agent_ids.close()