# -*- coding:utf-8 -*-
# @FileName  :constant.py
# @Time      :2023/7/25 17:29
# @Author    :lovemefan
# @Email     :lovemefan@outlook.com
from tzrpc.proto.py.Boolean_pb2 import Boolean
from tzrpc.proto.py.Bytes_pb2 import Bytes
from tzrpc.proto.py.Numpy_pb2 import ndarray
from tzrpc.proto.py.String_pb2 import String
from tzrpc.proto.py.Tensor_pb2 import Tensor

SUPPORT_TYPE = {
    "String": String,
    "Boolean": Boolean,
    "Bytes": Bytes,
    "Ndarray": ndarray,
    "Tensor": Tensor,
}

MAX_MESSAGE_LENGTH = 500 * 1024 * 1024

MAX_METADATA_SIZE = 1024 * 16
