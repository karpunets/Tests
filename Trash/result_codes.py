import pytest, allure, json, requests
import Data.URLs_MAP as URL

from Data.Make_requests_and_answers import JSON_generator as _
from Data.Users import make_50_users_for_get_user_list as take_user_list

headers ={'content-type': "application/json;charset=UTF-8",
           'authorization': "Basic cm9vdDpTbWlkbGUwOThhZG0h"}  # "Basic cm9vdDpTbWlkbGUwOThhZG0h

server = "http://172.22.2.63:8080"

url = "%s/SmiddleCampaignManager/cm/manager/get_result_code"%server
edit_url = "h%s/SmiddleCampaignManager/cm/manager/edit_result_variant"%server
get_campaign_url = "%s/SmiddleCampaignManager/cm/manager/get_campaign"%server

# campaignID = 66518604
# campaignCode = "O_Tele_Cross_2"




edit_list_call_result ={'Dialer has not yet attempted to contact that customer record': 'Dialer еще не пытался связаться с этим клиентом',
    'Error condition while dialing':'Состояние ошибки при наборе номера',
    'Number reported not in service by network':'Не в сети обслуживания',
    'No ringback from network when dial attempted':'Нет обратного вызова от сети при попытке набора',
    'Operator intercept returned from network when dial attempted':'При попытке дозвона опер-р получил возврат из ТФОП',
    'No dial tone when dialer port went off hook':'Нет гудка от сети при снятии трубки',
    'Number reported as invalid by the network':'Номер не действительный (Invalid)',
    'Customer phone did not answer':'Абонентский номер не отвечает', 'Customer phone was busy':'Номер абонента занят',
    'Customer answered and was connected to agent':'Абонент ответил и был соединен с операт-ом или IVR', 'Fax machine detected':'Обнаружен FAX',
    'Answering machine detected':'Обнаружен автоответчик',
    'Dialer stopped dialing customer due to lack of agents':'Dialer остановил попытку звонка к абоненту по причине нехватки операторов',
    'Customer requested callback':'Абонент запросил перезвон', 'Call was abandoned by the dialer due to lack of agents':'Звонок был остановлен - нехватка операторов',
                        'Failed to reserve agent for personal callback':'Не удалось зарезер-вать оператора для перс.отзвона',
                        'Agent has skipped or rejected a preview call or personal callback call':'Агент проп./отклонил вызов (Preview/перс.перезвон)',
                        'Agent has skipped or rejected a preview call with the close option':'Агент проп./отклонил вызов (Preview +опц. Закрыт.)',
                        'Customer has been abandoned to an IVR':'Абонент был потерян на IVR',
                        'Customer dropped call within configured abandoned time':'Абонент был потерян согласно сконфиг-ному времени',
                        'Mostly used with TDM switches - network answering machine, such as a network voicemail':'Обычно исп-ся с TDM: сетевой автоответчик.',
                        'Number successfully contacted but wrong number':'С абонентом соединились, но номер оказался ошиб.',
                        'Number successfully contacted but reached the wrong person':'С абон-том соединились, но персона оказалась ошиб.',
                        'Dialer has flushed this record due to a change in the skillgroup, the campaign, or some other parameter':'Запись пропущена-изменения в скиллгруппе /кампании',
                        'The number was on the do not call list':'Номер в "стоп листе", по которым нельзя звонить',
                        'Network disconnected while alerting':'Телефонная сеть отключена в момент звонка',
                        'Low Energy or Dead Air call detected by CPA':'Низк. громк. или плох. слышимость, обнаруж-ая СРА',
                        'SIP message received from dialer is not supported by voice gateway.':'Получ. SIP сооб-е, не поддерживается голос. шлюзом',
                        'SIP message received from dialer is not authorized by voice gateway':'Получ. SIP сооб-е, не авторизовано голос. шлюзом',
                        'Invalid sip message sent by dialer to voice gateway':'Недопуст.сообщ-ие, отпр-е dialer на голосовой шлюз'}


edit_list_callstatus ={'active':'Активен',
                       'agentNotAvailable':'Нет агента',
                       'agentRejected':'Отклонено агентом',
                       'callbackRequested':'общий перезвон',
                       'closed':'закрыт',
                       'maxAttemptsReached':'макс кол-во попыток',
                       'pending':'ожидание',
                       'personalCallbackRequested':'персональный перезвон',
                       'retry':'Повтор',
                       'unknown':'Неизвестно'}


get_campaign_json = {}

def get_campaign():
    payload = json.dumps(get_campaign_json)
    # Запрос на добавление пользователя
    response = requests.post(url=get_campaign_url, data=payload, headers=headers)
    return response.json()



campaign_list = get_campaign()


for campaign in campaign_list:

    if campaign['code'] != 'TELE':
        if campaign['code'] != 'CCallBack':

            edit_call_result = {"campaignCode":campaign['code'], "resultCode": "CD_callResult", "resultVariant":{"id":None, "value": "Абонент был потерян на IVR", "forInit":False}}
            edit_call_status = {"campaignCode":campaign['code'], "resultCode": "CD_callStatus", "resultVariant":{"id":None, "value": "Абонент был потерян на IVR", "forInit":False}}
            campaign ={"campaignId": campaign['id']}




            def get_result_codes():
                payload = json.dumps(campaign)
                # Запрос на добавление пользователя
                response = requests.post(url=url, data=payload, headers=headers)
                return response.json()


            a = get_result_codes()

            #print(a)

            for i in a:
                if i['code']=='CD_callResult':
                    for k in i['resultVariants']:
                        for j in edit_list_call_result:
                            if j == k['value']:
                                edit_call_result["resultVariant"] = k
                                edit_call_result["resultVariant"]['value'] = edit_list_call_result[j]
                                payload = json.dumps(edit_call_result)
                                response = requests.post(url=edit_url, data=payload, headers=headers)




            b = get_result_codes()
            for p in b:
                if p['code']=='CD_callStatus':
                    for k in p['resultVariants']:
                        for j in edit_list_callstatus:
                            if j == k['value']:
                                edit_call_status["resultVariant"] = k
                                edit_call_status["resultVariant"]['value'] = edit_list_callstatus[j]
                                payload = json.dumps(edit_call_status)
                                response = requests.post(url=edit_url, data=payload, headers=headers)