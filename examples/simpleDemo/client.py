# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 19:57
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : client.py
import numbers

import numpy as np
import torch

from tzrpc import TZPRC_Client

SERVER_ADDRESS = "localhost:8000"
client = TZPRC_Client(SERVER_ADDRESS)


@client.register
def say_hello2(text):
    return text


@client.register
def send_numpy_obj():
    data = np.random.randn(1, 2, 2, 4)
    return data


@client.register
def send_torch_tensor_obj():
    data = torch.tensor([[1, 2, 3], [4, 5, 6]])
    return data


@client.register
def say_hello(text):
    return text


@client.register
def send_bytes():
    return b"just for test"


@client.register
def send_number(data: numbers.Number):
    return data


@client.register
def send_bool(_bool: bool):
    return _bool


@client.register
def send_python_obj(obj):
    return obj


if __name__ == "__main__":
    print(say_hello(text="lovemefan 1"))
    print(say_hello(text="lovemefan 1"))
    print(say_hello2(text="lovemefan 2"))
    print(send_numpy_obj())
    print(send_torch_tensor_obj())
    print(send_bytes())
    print(send_number(2))
    print(send_number(1 / 3))
    print(send_bool(True))
    print(send_bool(False))

    print(send_python_obj({"audio": b"RIFF", "tran": 0}))
