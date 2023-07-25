# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 21:41
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : client.py
import logging
import grpc

from tzrpc.proto.py.Server_pb2_grpc import toObjectStub

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]  - %(levelname)s - %(threadName)s - %(module)s.%(funcName)s - %(message)s')
logger = logging.getLogger(__name__)


class TZPRC_Client:

    __type = ["String", "Integer", "Float", "Double", "Boolean", "Numpy", "Tensor"]

    def __init__(self, server_address: str):
        self.server_address = server_address
        self.channel = grpc.insecure_channel(server_address)

    def register(self, func):
        """
        :param return_type: type of return [String, ]
        :return:
        """
        # if return_type not in self.__type:
        #     raise ValueError(f"TZRPC return type only support {self.__type}")

        def wrapper(*args, **kwargs):
            stub = toObjectStub(self.channel, func.__name__)
            func(stub=stub, *args, **kwargs)
        return wrapper


class Listener:
    def __init__(self):
        pass


