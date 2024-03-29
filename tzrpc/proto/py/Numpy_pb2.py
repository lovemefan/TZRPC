# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Numpy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="Numpy.proto",
    package="tzrpc.proto",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x0bNumpy.proto\x12\x0btzrpc.proto"\xa8\x04\n\x05\x64type\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.tzrpc.proto.dtype.Type\x12\x30\n\nbyte_order\x18\x65 \x01(\x0e\x32\x1c.tzrpc.proto.dtype.ByteOrder\x12\x0e\n\x05names\x18\xc9\x01 \x03(\t\x12/\n\x06\x66ields\x18\xad\x02 \x03(\x0b\x32\x1e.tzrpc.proto.dtype.FieldsEntry\x12(\n\x08subdtype\x18\xe9\x07 \x01(\x0b\x32\x15.tzrpc.proto.subdtype\x1a\x41\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.tzrpc.proto.dtype:\x02\x38\x01"B\n\tByteOrder\x12\x11\n\rLITTLE_ENDIAN\x10\x00\x12\x0e\n\nBIG_ENDIAN\x10\x01\x12\n\n\x06NATIVE\x10\x02\x12\x06\n\x02NA\x10\x03"\xd3\x01\n\x04Type\x12\x0b\n\x07\x66loat64\x10\x00\x12\x0b\n\x07\x66loat32\x10\x01\x12\x0b\n\x07\x66loat16\x10\x02\x12\x0e\n\ncomplex128\x10\x03\x12\r\n\tcomplex64\x10\x04\x12\n\n\x06uint64\x10\x05\x12\n\n\x06uint32\x10\x06\x12\n\n\x06uint16\x10\x07\x12\t\n\x05uint8\x10\x08\x12\t\n\x05int64\x10\t\x12\t\n\x05int32\x10\n\x12\t\n\x05int16\x10\x0b\x12\x08\n\x04int8\x10\x0c\x12\x08\n\x04S128\x10\r\x12\x07\n\x03S64\x10\x0e\x12\x07\n\x03S32\x10\x0f\x12\x07\n\x03S16\x10\x10\x12\x06\n\x02S8\x10\x11"@\n\x08subdtype\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.tzrpc.proto.dtype.Type\x12\r\n\x05shape\x18\x65 \x03(\x03"\\\n\x07ndarray\x12\r\n\x05shape\x18\x01 \x03(\x03\x12!\n\x05\x64type\x18\x65 \x01(\x0b\x32\x12.tzrpc.proto.dtype\x12\r\n\x04\x64\x61ta\x18\xc9\x01 \x01(\x0c\x12\x10\n\x07strides\x18\xad\x02 \x03(\x03"1\n\x08ndarrays\x12%\n\x07ndarray\x18\x01 \x03(\x0b\x32\x14.tzrpc.proto.ndarrayb\x06proto3',
)


_DTYPE_BYTEORDER = _descriptor.EnumDescriptor(
    name="ByteOrder",
    full_name="tzrpc.proto.dtype.ByteOrder",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="LITTLE_ENDIAN",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BIG_ENDIAN",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NATIVE",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NA",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=301,
    serialized_end=367,
)
_sym_db.RegisterEnumDescriptor(_DTYPE_BYTEORDER)

_DTYPE_TYPE = _descriptor.EnumDescriptor(
    name="Type",
    full_name="tzrpc.proto.dtype.Type",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="float64",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="float32",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="float16",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="complex128",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="complex64",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="uint64",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="uint32",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="uint16",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="uint8",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="int64",
            index=9,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="int32",
            index=10,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="int16",
            index=11,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="int8",
            index=12,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="S128",
            index=13,
            number=13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="S64",
            index=14,
            number=14,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="S32",
            index=15,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="S16",
            index=16,
            number=16,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="S8",
            index=17,
            number=17,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=370,
    serialized_end=581,
)
_sym_db.RegisterEnumDescriptor(_DTYPE_TYPE)


_DTYPE_FIELDSENTRY = _descriptor.Descriptor(
    name="FieldsEntry",
    full_name="tzrpc.proto.dtype.FieldsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="tzrpc.proto.dtype.FieldsEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="tzrpc.proto.dtype.FieldsEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=234,
    serialized_end=299,
)

_DTYPE = _descriptor.Descriptor(
    name="dtype",
    full_name="tzrpc.proto.dtype",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="tzrpc.proto.dtype.type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
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
        _descriptor.FieldDescriptor(
            name="byte_order",
            full_name="tzrpc.proto.dtype.byte_order",
            index=1,
            number=101,
            type=14,
            cpp_type=8,
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
        _descriptor.FieldDescriptor(
            name="names",
            full_name="tzrpc.proto.dtype.names",
            index=2,
            number=201,
            type=9,
            cpp_type=9,
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
        _descriptor.FieldDescriptor(
            name="fields",
            full_name="tzrpc.proto.dtype.fields",
            index=3,
            number=301,
            type=11,
            cpp_type=10,
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
        _descriptor.FieldDescriptor(
            name="subdtype",
            full_name="tzrpc.proto.dtype.subdtype",
            index=4,
            number=1001,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    nested_types=[
        _DTYPE_FIELDSENTRY,
    ],
    enum_types=[
        _DTYPE_BYTEORDER,
        _DTYPE_TYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=29,
    serialized_end=581,
)


_SUBDTYPE = _descriptor.Descriptor(
    name="subdtype",
    full_name="tzrpc.proto.subdtype",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="tzrpc.proto.subdtype.type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
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
        _descriptor.FieldDescriptor(
            name="shape",
            full_name="tzrpc.proto.subdtype.shape",
            index=1,
            number=101,
            type=3,
            cpp_type=2,
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
    serialized_start=583,
    serialized_end=647,
)


_NDARRAY = _descriptor.Descriptor(
    name="ndarray",
    full_name="tzrpc.proto.ndarray",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="shape",
            full_name="tzrpc.proto.ndarray.shape",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
        _descriptor.FieldDescriptor(
            name="dtype",
            full_name="tzrpc.proto.ndarray.dtype",
            index=1,
            number=101,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="data",
            full_name="tzrpc.proto.ndarray.data",
            index=2,
            number=201,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="strides",
            full_name="tzrpc.proto.ndarray.strides",
            index=3,
            number=301,
            type=3,
            cpp_type=2,
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
    serialized_start=649,
    serialized_end=741,
)


_NDARRAYS = _descriptor.Descriptor(
    name="ndarrays",
    full_name="tzrpc.proto.ndarrays",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="ndarray",
            full_name="tzrpc.proto.ndarrays.ndarray",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
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
    serialized_start=743,
    serialized_end=792,
)

_DTYPE_FIELDSENTRY.fields_by_name["value"].message_type = _DTYPE
_DTYPE_FIELDSENTRY.containing_type = _DTYPE
_DTYPE.fields_by_name["type"].enum_type = _DTYPE_TYPE
_DTYPE.fields_by_name["byte_order"].enum_type = _DTYPE_BYTEORDER
_DTYPE.fields_by_name["fields"].message_type = _DTYPE_FIELDSENTRY
_DTYPE.fields_by_name["subdtype"].message_type = _SUBDTYPE
_DTYPE_BYTEORDER.containing_type = _DTYPE
_DTYPE_TYPE.containing_type = _DTYPE
_SUBDTYPE.fields_by_name["type"].enum_type = _DTYPE_TYPE
_NDARRAY.fields_by_name["dtype"].message_type = _DTYPE
_NDARRAYS.fields_by_name["ndarray"].message_type = _NDARRAY
DESCRIPTOR.message_types_by_name["dtype"] = _DTYPE
DESCRIPTOR.message_types_by_name["subdtype"] = _SUBDTYPE
DESCRIPTOR.message_types_by_name["ndarray"] = _NDARRAY
DESCRIPTOR.message_types_by_name["ndarrays"] = _NDARRAYS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

dtype = _reflection.GeneratedProtocolMessageType(
    "dtype",
    (_message.Message,),
    {
        "FieldsEntry": _reflection.GeneratedProtocolMessageType(
            "FieldsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _DTYPE_FIELDSENTRY,
                "__module__": "Numpy_pb2"
                # @@protoc_insertion_point(class_scope:tzrpc.proto.dtype.FieldsEntry)
            },
        ),
        "DESCRIPTOR": _DTYPE,
        "__module__": "Numpy_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.dtype)
    },
)
_sym_db.RegisterMessage(dtype)
_sym_db.RegisterMessage(dtype.FieldsEntry)

subdtype = _reflection.GeneratedProtocolMessageType(
    "subdtype",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUBDTYPE,
        "__module__": "Numpy_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.subdtype)
    },
)
_sym_db.RegisterMessage(subdtype)

ndarray = _reflection.GeneratedProtocolMessageType(
    "ndarray",
    (_message.Message,),
    {
        "DESCRIPTOR": _NDARRAY,
        "__module__": "Numpy_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.ndarray)
    },
)
_sym_db.RegisterMessage(ndarray)

ndarrays = _reflection.GeneratedProtocolMessageType(
    "ndarrays",
    (_message.Message,),
    {
        "DESCRIPTOR": _NDARRAYS,
        "__module__": "Numpy_pb2"
        # @@protoc_insertion_point(class_scope:tzrpc.proto.ndarrays)
    },
)
_sym_db.RegisterMessage(ndarrays)


_DTYPE_FIELDSENTRY._options = None
# @@protoc_insertion_point(module_scope)
