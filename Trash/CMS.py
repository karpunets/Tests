import requests, json, ssl, websockets, asyncio, websocket


from websocket import create_connection

url_search_guest = "https://join.smiddle.com/api/v1/search-guest-conference"
url_guest_register = "https://join.smiddle.com/api/v1/guest-register"
url_login = "https://join.smiddle.com/api/v1/login"
url_streams = "https://join.smiddle.com/api/v1/streams"
s = requests.Session()

s.verify = False
# s.cert = "C:\\Users\\Victor\\PycharmProjects\\Smiddle_API\\Trash\\meetingserv.smidle.lab.crt"
request_body = {"numericId":"707077485","secret":"9FwKpDKuYFDCRlTouBvY_A","passcode":None}
stream_post_body = {"subscriptions":[]}
response_search = s.post(url_search_guest, data=json.dumps(request_body))
request_body["token"] = response_search.json()['token']
request_body["displayName"] = "bitbok"


response_guest_register = s.post(url_guest_register, data=json.dumps(request_body))
loginPassword = response_guest_register.json()

response_login = s.post(url_login, data=json.dumps(loginPassword))
save_cookie = response_login.cookies

s.cookies.update(response_login.cookies)
s.headers.update({"CSRF-Token":response_login.cookies.values()[1]})



response_streams_get = s.get(url_streams)

response_streams_post  = s.post(url_streams, data=json.dumps(stream_post_body))
print(response_streams_post.json())

websocket_url = "wss://join.smiddle.com/api/v1/streams/{0}/updates".format(response_streams_post.json()['id'])

# print(websocket_url)
# ctx=ssl.create_default_context(ssl.PROTOCOL_SSLv23)
# ctx.load_cert_chain("C:\\Users\\Victor\\PycharmProjects\\Smiddle_API\\Trash\\meetingserv.smidle.lab.pem")


# async def hello():
#
#     async with websockets.connect(websocket_url,  ssl=ssl.SSLContext(ssl.PROTOCOL_SSLv23)) as websocket:
#
#         greeting = await websocket.recv()
#         print(greeting)
#
# asyncio.get_event_loop().run_until_complete(hello())


#
# ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.PROTOCOL_SSLv23})
# ws.connect(websocket_url)
#
# # ws = create_connection(websocket_url,  ssl=ssl.SSLContext(ssl.PROTOCOL_SSLv23))
# result =  ws.recv()
# print("Received '%s'" % result)
# ws.close()


# cook = {}
# for i in save_cookie.items():
#     cook[i[0]] = i[1]
# print(cook)
cook = ""
cnt  =0
save_cookie.
for i in save_cookie.items():
    cook += i[0] + "=" + i[1]+ ";"
cook.strip(";")

ws = websocket.create_connection(websocket_url, sslopt={"cert_reqs":  ssl.CERT_NONE}, cookie = cook, headers = {"Sec-WebSocket-Protocol":response_login.cookies.values()[1],"Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits", "Sec-WebSocket-Version":13, "Sec-WebSocket-Key":"HnJQeJtPAN8n+amqKVD6Mg=="})
count = 0
print(ws.headers)
while count <10:
    result = ws.headers
    print("Received '%s'" % result)
    count += 1
ws.close()