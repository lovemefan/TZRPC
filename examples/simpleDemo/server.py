# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 19:37
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : server.py
from tzrpc.TZRPC import TZRPC

rpc = TZRPC(__name__)


@rpc.register
def say_hello2(text: str):
    print(text)
    return "hello world 2" + text


@rpc.register
def say_hello(text: str):
    print(text)
    return "hello world " + text




if __name__ == '__main__':
    rpc.run("localhost", 8000)
