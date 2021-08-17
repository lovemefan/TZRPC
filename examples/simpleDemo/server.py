# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 19:37
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : server.py
from tzrpc.TZRPC import TZRPC

rpc = TZRPC(__name__)


@rpc.register
def say_hello(response):
    print(response.text)
    return "hello world " + response.text


if __name__ == '__main__':
    rpc.run("localhost", 8000)