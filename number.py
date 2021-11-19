#!/usr/bin/env python3

# api_id= 9054139
# api_hash= 67016da318f1c1bf80454b8487678c77


from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

chats  = []
last_date = None 
chunk_size = 200
groups=[]

api_id=9054139
api_hash='67016da318f1c1bf80454b8487678c77'
phone='+916306204612'
client=TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code : '))

#result
result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer = InputPeerEmpty(),
    limit=chunk_size,
    hash=0 
))

print(result)

#res = chats.extend(result.chats)
#print(res)