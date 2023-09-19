# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 19:37
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : server.py
import numbers

from tzrpc import TZRPC_Server

server = TZRPC_Server(__name__, debug=False)


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


@server.register
def send_bytes(data: bytes):
    return data + data


@server.register
def send_number(data: numbers.Number):
    return data * 2


@server.register
def send_bool(_bool: bool):
    return not _bool


@server.register
def send_python_obj(data):
    print(data)
    return data


if __name__ == "__main__":
    server.run("localhost", 8000)
