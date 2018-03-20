import requests, json
from bin.helpers import getProperty, getUrl


def get_token():
    headers = {"Content-Type": "application/json"}
    payload = getProperty("principal", "credential")
    response = requests.post(url=getUrl("token"), data=json.dumps(payload), headers=headers)
    return response.json()



class Client(object):


    def update_headers(session):
        headers = {'content-type': "application/json;charset=UTF-8"}
        auth_token = get_token()
        headers[auth_token['name']] = auth_token['token']
        session.headers = headers


    def get(url, params=None, id=None):
        return Client.session.get(url=getUrl(url, id), params=params)

    def post(url, data=None, params=None):
        return Client.session.post(url=getUrl(url), params=params, data=json.dumps(data))

    def put(url, data=None, params=None, id=None):
        return Client.session.put(url=getUrl(url, id), params=params, data=json.dumps(data))

    def delete(url, data=None, params=None, id=None):
        return Client.session.delete(url=getUrl(url, id), params=params, data=json.dumps(data))

    session = requests.Session()
    update_headers(session)


