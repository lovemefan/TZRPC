# -*- coding:utf-8 -*-
# @FileName  :convert2numpy.py
# @Time      :2023/7/25 22:38
# @Author    :lovemefan
# @Email     :lovemefan@outlook.com
import numpy as np

from tzrpc.proto.py.Numpy_pb2 import dtype, ndarray

BYTE_ORDER_DICT = {
    "<": dtype.ByteOrder.LITTLE_ENDIAN,
    ">": dtype.ByteOrder.BIG_ENDIAN,
    "=": dtype.ByteOrder.NATIVE,
    "|": dtype.ByteOrder.NA,
}

BYTE_ORDER_DICT_REVERSE = {value: key for key, value in BYTE_ORDER_DICT.items()}

DATA_TYPE_DICT = {
    "float64": dtype.Type.float64,
    "float32": dtype.Type.float32,
    "float16": dtype.Type.float16,
    "complex128": dtype.Type.complex128,
    "complex64": dtype.Type.complex64,
    "uint64": dtype.Type.uint64,
    "uint32": dtype.Type.uint32,
    "uint16": dtype.Type.uint16,
    "uint8": dtype.Type.uint8,
    "int64": dtype.Type.int64,
    "int32": dtype.Type.int32,
    "int16": dtype.Type.int16,
    "int8": dtype.Type.int8,
    "S128": dtype.Type.S128,
    "S64": dtype.Type.S64,
    "S32": dtype.Type.S32,
    "S16": dtype.Type.S16,
    "S8": dtype.Type.S8,
}

DATA_TYPE_DICT_REVERSE = {value: key for key, value in DATA_TYPE_DICT.items()}


def numpy2protobuf(data: np.ndarray):
    def get_byteorder(_data: np.ndarray):
        order = _data.dtype.byteorder
        if order in BYTE_ORDER_DICT:
            return BYTE_ORDER_DICT[order]
        else:
            raise ValueError(f"byte order: {order} not support ")

    def get_ndarray_type(_data: np.ndarray):
        _type = _data.dtype.name
        if _type in DATA_TYPE_DICT:
            return DATA_TYPE_DICT[_type]
        else:
            raise ValueError(f"data type: {_type} not support ")

    buf = ndarray(
        shape=data.shape,
        dtype=dtype(byte_order=get_byteorder(data), type=get_ndarray_type(data)),
        data=data.data.tobytes(),
        strides=data.strides,
    )
    return buf


def protobuf2numpy(buf: ndarray):
    def get_ndarray_type(_data: ndarray):
        _type = _data.dtype.type
        if _type in DATA_TYPE_DICT_REVERSE:
            return DATA_TYPE_DICT_REVERSE[_type]
        else:
            raise ValueError(f"data type: {_type} not support ")

    return np.frombuffer(buf.data, dtype=get_ndarray_type(buf)).reshape(
        tuple(buf.shape)
    )


if __name__ == "__main__":
    import numpy as np

    np_obj = np.random.randn(2, 3, 4).view(np.int64)
    print(np_obj)
    a = numpy2protobuf(np_obj)
    print(a)
    b = protobuf2numpy(a)
    print(b)
