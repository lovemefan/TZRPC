# -*- coding:utf-8 -*-
# @FileName  :server.py
# @Time      :2023/9/18 18:11
# @Author    :lovemefan
# @Email     :lovemefan@outlook.com
from tzrpc import TZRPC_Server

server = TZRPC_Server(__name__, debug=False)


@server.register
def say_hello(text: str):
    return "hello world "


@server.register(stream=True)
def send_num(obj):
    for i in range(obj):
        yield i


@server.register(stream=True)
def gumbel(num):
    if num % 3 == 0:
        yield f"number is {num}, you win"


if __name__ == "__main__":
    server.run("localhost", 8000)
