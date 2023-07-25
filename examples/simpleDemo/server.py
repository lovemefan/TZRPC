# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 19:37
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : server.py
from tzrpc import TZRPC_Server

server = TZRPC_Server(__name__)


@server.register
def say_hello2(text: str):
    return "hello world 2 " + text


@server.register
def say_hello(text: str):
    return "hello world " + text


@server.register
def say_hello3(text: str):
    return "hello world 3 " + text


if __name__ == "__main__":
    server.run("localhost", 8000)
