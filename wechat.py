#!/usr/bin/env python
# -*-encoding:utf-8-*-

import itchat
from itchat.content import *
import requests
import const
import json

def play_account():
    recipents = ['chzipeng', 'jiankangkaixindyanzi', 'shenjianjun96993']
    key_list = list()
    for r in recipents:
        cur_key = itchat.search_friends(wechatAccount=r)[0]['UserName']
        key_list.append(cur_key)
    return key_list

def tuling_robot(msg):
    api_url = 'http://www.tuling123.com/openapi/api'
    data = {'key': const.API_KEY, 'info': msg, 'user_id': 'little-bug'}
    req = requests.post(api_url, data = data).json()
    reply = req.get('text')
    return reply

@itchat.msg_register([PICTURE, SHARING, VIDEO, MAP, CARD, RECORDING, ATTACHMENT, FRIENDS], isFriendChat = True)
def text_reply(msg):
    key_list = play_account()
    if msg['FromUserName'] in key_list:
        response = '[Grin][Grin][Grin][Grin][Grin]'
        itchat.send(response, msg['FromUserName'])

@itchat.msg_register(TEXT, isFriendChat = True)
def text_reply(msg):
    key_list = play_account()
    if msg['FromUserName'] in key_list:
        user_input = msg['Text']
        response = tuling_robot(user_input)
        itchat.send(response, msg['FromUserName'])

if __name__ == '__main__':
    itchat.auto_login(hotReload = True)
    #nick = itchat.loginInfo['User']['NickName']
    itchat.run()
