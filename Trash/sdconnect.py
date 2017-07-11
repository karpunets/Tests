import pytest, allure, json, requests

import random




a = {"identifier":115301820,
"count":1,
"total":1,
"data":[
	'''{
"city":"Бобринець",
"nameRespondent":"Клюй Віктор Юрійович",
"contractCode":"5566",
"OutboundContactTypeOfContact":None,
"typeTV":"Цифровое ТВ",
"subjects":"Детские; Развлекательные",
"provider":"Датагруп",
"currentSpeed":"До 100 Мбит",
"costServices":"До 150 грн",
"mainInet":"Стабильность сигнала; Цена",
"inetPurpose":"Работа; Игры в Интернете",
"estimateQuality":"6",
"improveTvInet":"Скорость выше; Больше интересных каналов; Стабильности сигнала",
"mainTV":"Качество изображения; Соотношение цены/качества",
"availabilityPC":"-", 
"typeInet":"Беспроводной", 
"callBackTime":None, 
"newTel":"066681115", 
"DateCall":"30.06.2017 07:57"}'''
]
}

url = "http://172.22.2.63:8080/ServiceDeskConnector/api/request"
headers = {'content-type': "application/json;charset=UTF-8",
                     'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}


payload = json.dumps(a)
print(a)
response = requests.post(url=url, data=payload, headers=headers)


print(response)