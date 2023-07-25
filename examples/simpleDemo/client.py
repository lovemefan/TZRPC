# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 19:57
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : client.py

from tzrpc import TZPRC_Client

SERVER_ADDRESS = "localhost:8000"
client = TZPRC_Client(SERVER_ADDRESS)


@client.register
def say_hello2(text):
    return text


@client.register
def say_hello3(text):
    return text


@client.register
def say_hello(text):
    return text


if __name__ == "__main__":
    print(say_hello(text="lovemefan 1"))
    print(say_hello(text="lovemefan 1"))
    print(say_hello2(text="lovemefan 2"))
    print(say_hello3(text="lovemefan 2"))
