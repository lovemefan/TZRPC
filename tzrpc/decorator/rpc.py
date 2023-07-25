# -*- coding: utf-8 -*-
# @Time  : 2021/8/17 9:47
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : rpc.py
import logging

from tzrpc.proto.py.String_pb2 import String

servicers = []
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s]  - %(levelname)s - %(threadName)s - %(module)s.%(funcName)s - %(message)s",
)
logger = logging.getLogger(__name__)


class RpcServicer:
    def __init__(self):
        pass

    def register(self, task):
        _listener = Listener(task)
        # print(_listener)
        logger.info(f"Instance {_listener}  appended")
        logger.info(f"Instance's task  {_listener.task} ")
        servicers.append(_listener)

        def wrapper(*args, **kwargs):
            print(args, kwargs)
            print(f"{task.__name__}: text")
            self.args = args
            self.kwargs = kwargs
            return task(*args, **kwargs)

        return wrapper


class Listener:
    def __init__(self, task):
        logger.debug(f"Method {task} {task.__name__}() registered.")
        self.task = task
        logger.debug(f"self Method {self.task} {task.__name__}() registered.")

    def wrapper(self, *args, **kwargs):
        print(args, kwargs)
        print(f"{self.task.__name__}: text")
        return self.task(*args, **kwargs)

    def toString(self, request, context):
        logger.debug(f"Method {self.task} {self.task.__name__}() called.")
        result = self.task(request.text)
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
