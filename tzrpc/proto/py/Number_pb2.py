# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Number.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="Number.proto",
    package="tzrpc.proto",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0cNumber.proto\x12\x0btzrpc.proto"\x18\n\x07Integer\x12\r\n\x05value\x18\x01 \x01(\x03"\x16\n\x05\x46loat\x12\r\n\x05value\x18\x01 \x01(\x02"\x17\n\x06\x44ouble\x12\r\n\x05value\x18\x01 \x01(\x01"!\n\x10IntegerArrayList\x12\r\n\x05value\x18\x01 \x03(\x05"\x1f\n\x0e\x46loatArrayList\x12\r\n\x05value\x18\x01 \x03(\x02" \n\x0f\x44oubleArrayList\x12\r\n\x05value\x18\x01 \x03(\x01\x62\x06proto3',
)


_INTEGER = _descriptor.Descriptor(
    name="Integer",
    full_name="tzrpc.proto.Integer",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="tzrpc.proto.Integer.value",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=29,
    serialized_end=53,
)


_FLOAT = _descriptor.Descriptor(
    name="Float",
    full_name="tzrpc.proto.Float",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="tzrpc.proto.Float.value",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=55,
    serialized_end=77,
)


_DOUBLE = _descriptor.Descriptor(
    name="Double",
    full_name="tzrpc.proto.Double",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="tzrpc.proto.Double.value",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=79,
    serialized_end=102,
)


_INTEGERARRAYLIST = _descriptor.Descriptor(
    name="IntegerArrayList",
    full_name="tzrpc.proto.IntegerArrayList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="tzrpc.proto.IntegerArrayList.value",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=104,
    serialized_end=137,
)


_FLOATARRAYLIST = _descriptor.Descriptor(
    name="FloatArrayList",
    full_name="tzrpc.proto.FloatArrayList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="tzrpc.proto.FloatArrayList.value",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=139,
    serialized_end=170,
)


_DOUBLEARRAYLIST = _descriptor.Descriptor(
    name="DoubleArrayList",
    full_name="tzrpc.proto.DoubleArrayList",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="tzrpc.proto.DoubleArrayList.value",
            index=0,
            number=1,
            type=1,
            cpp_type=5,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=172,
    serialized_end=204,
)

DESCRIPTOR.message_types_by_name["Integer"] = _INTEGER
DESCRIPTOR.message_types_by_name["Float"] = _FLOAT
DESCRIPTOR.message_types_by_name["Double"] = _DOUBLE
DESCRIPTOR.message_types_by_name["IntegerArrayList"] = _INTEGERARRAYLIST
DESCRIPTOR.message_types_by_name["FloatArrayList"] = _FLOATARRAYLIST
DESCRIPTOR.message_types_by_name["DoubleArrayList"] = _DOUBLEARRAYLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Integer = _reflection.GeneratedProtocolMessageType(
    "Integer",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTEGER,
        "__module__": "Number_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.Integer)
    },
)
_sym_db.RegisterMessage(Integer)

Float = _reflection.GeneratedProtocolMessageType(
    "Float",
    (_message.Message,),
    {
        "DESCRIPTOR": _FLOAT,
        "__module__": "Number_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.Float)
    },
)
_sym_db.RegisterMessage(Float)

Double = _reflection.GeneratedProtocolMessageType(
    "Double",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOUBLE,
        "__module__": "Number_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.Double)
    },
)
_sym_db.RegisterMessage(Double)

IntegerArrayList = _reflection.GeneratedProtocolMessageType(
    "IntegerArrayList",
    (_message.Message,),
    {
        "DESCRIPTOR": _INTEGERARRAYLIST,
        "__module__": "Number_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.IntegerArrayList)
    },
)
_sym_db.RegisterMessage(IntegerArrayList)

FloatArrayList = _reflection.GeneratedProtocolMessageType(
    "FloatArrayList",
    (_message.Message,),
    {
        "DESCRIPTOR": _FLOATARRAYLIST,
        "__module__": "Number_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.FloatArrayList)
    },
)
_sym_db.RegisterMessage(FloatArrayList)

DoubleArrayList = _reflection.GeneratedProtocolMessageType(
    "DoubleArrayList",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOUBLEARRAYLIST,
        "__module__": "Number_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.DoubleArrayList)
    },
)
_sym_db.RegisterMessage(DoubleArrayList)


# @@protoc_insertion_point(module_scope)
