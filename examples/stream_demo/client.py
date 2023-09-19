# -*- coding:utf-8 -*-
# @FileName  :client.py
# @Time      :2023/9/18 18:11
# @Author    :lovemefan
# @Email     :lovemefan@outlook.com
from tzrpc.client.client import TZPRC_Client

SERVER_ADDRESS = "localhost:8000"
client = TZPRC_Client(SERVER_ADDRESS)


@client.register
def say_hello(text):
    return text


@client.register(stream=True)
def gumbel(num):
    for i in range(num):
        yield i


@client.register(stream=True)
def send_num(obj):
    yield obj


if __name__ == "__main__":
    # print(say_hello(text="lovemefan 1"))
    for i in send_num(5):
        print(i)

    for i in gumbel(10):
        print(i)
