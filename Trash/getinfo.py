import requests, json

url = "http://172.22.2.63:8080/SmiddleRecording/rec/crm/getInfo"
headers = {'content-type': "application/json;charset=UTF-8"}
payload = json.dumps({"crmCallId":"qq"})

response = requests.post(data=payload, url=url, headers=headers)

print(response.json())