# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 19:57
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : client.py

from tzrpc.client.client import TZPRC_Client
from tzrpc.proto.py.String_pb2 import String



SERVER_ADDRESS = "localhost:8000"
client = TZPRC_Client(SERVER_ADDRESS)


@client.register
def say_hello(stub, text):
    request = String(text=text)
    response = stub.toString(request)
    print(response.text)


if __name__ == '__main__':
    say_hello(text="lovemefan")