# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 9:47
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : rpc.py
import logging

from tzrpc.proto.py import Server_pb2
from tzrpc.proto.py.Server_pb2_grpc import toObjectServicer
from tzrpc.proto.py.String_pb2 import String

servicers = []
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]  - %(levelname)s - %(threadName)s - %(module)s.%(funcName)s - %(message)s')
logger = logging.getLogger(__name__)


class RpcServicer():

    def __init__(self):
        pass

    def register(self, task):
        self.task = task
        logger.info(f"Method {task.__name__}() registered.")
        servicers.append(self)

        def wrapper(*args, **kwargs):
            print(args, kwargs)
            self.args = args
            self.kwargs = kwargs
            task(*args, **kwargs)
        return wrapper

    def toString(self, request, context):
        result = self.task(request)
        response = String(text=result)
        return response


    def String(self, func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


    def toInteger(self, request, context):
        pass

    def toFloat(self, request, context):
        pass

    def toDouble(self, request, context):
        pass

    def toBoolean(self, request, context):
        pass

    def toBytes(self, request, context):
        pass

    def toNdarray(self, request, context):
        pass

    def toNdarrays(self, request, context):
        pass

    def toTensor(self, request, context):
        pass

    def toTensors(self, request, context):
        pass

    def toIntegerArrayList(self, request, context):
        pass

    def toFloatArrayList(self, request, context):
        pass

    def toDoubleArrayList(self, request, context):
        pass

    def toBooleanArrayList(self, request, context):

        pass
