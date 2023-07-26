# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 19:37
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : server.py

from tzrpc import TZRPC_Server

server = TZRPC_Server(__name__)


@server.register
def send_numpy_obj(data):
    return data * 2 + 1


@server.register
def send_torch_tensor_obj(data):
    return data @ data.T


@server.register
def say_hello(text: str):
    return "hello world " + text


@server.register
def say_hello2(text: str):
    return "hello world 3 " + text


if __name__ == "__main__":
    server.run("localhost", 8000)
