# -*- coding:utf-8 -*-
# @FileName  :tensor_serialized.py
# @Time      :2023/7/26 13:19
# @Author    :lovemefan
# @Email     :lovemefan@outlook.com
from tzrpc.utils.logger import get_logger
from tzrpc.proto.py.Tensor_pb2 import data_type, Tensor
from tzrpc.utils.numpy_serialized import numpy2protobuf, protobuf2numpy

try:
    import torch
except ImportError:
    get_logger().error("""
    Please install torch use `pip install torch`
    """)


