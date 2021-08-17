# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 9:47
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : rpc.py
from tzrpc.proto.py import Server_pb2
from tzrpc.proto.py.Server_pb2_grpc import toObjectServicer
from tzrpc.proto.py.String_pb2 import String


class RpcServicer(toObjectServicer):

    def __init__(self):
        pass

    def toString(self, request, context):
        pass

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
