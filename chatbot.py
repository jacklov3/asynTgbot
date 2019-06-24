#!/usr/bin/env python3
# encoding: utf-8
'''
@author: JackyLove
@contact: asaltedfishz@gmail.com
@file: chatbot.py
@time: 2019-06-24 23:50
'''
import requests

def smartbot(msg):
    url='http://api.qingyunke.com/api.php?key=free&appid=0&msg='
    response = requests.get(url+str(msg))
    return response.text['content']

if __name__=='__main__':
    print(smartbot('赣州天气'))