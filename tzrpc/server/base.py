# -*- coding: utf-8 -*-
# @Time  : 2021/8/6 12:13
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : base.py
import re
from typing import Any
from warnings import warn

from tzrpc.decorator.rpc import RpcServicer
from tzrpc.exceptions.exceptions import TZRPCException

VALID_NAME = re.compile(r"^[a-zA-Z][a-zA-Z0-9_\-]*$")


class tzrpcBase(RpcServicer):
    def __init__(self, name) -> None:
        super().__init__()
        class_name = self.__class__.__name__

        if name is None:
            raise TZRPCException(
                f"{class_name} instance cannot be unnamed. "
                "Please use TZRPC(name='your_application_name') instead.",
            )

        if not VALID_NAME.match(name):
            warn(
                f"{class_name} instance named '{name}' uses a format that is"
                f"deprecated. Starting in version 21.12, {class_name} objects "
                "must be named only using alphanumeric characters, _, or -.",
                DeprecationWarning,
            )

        self.name = name

        # for base in TZRPCException.__bases__:
        #     base.__init__(self, *args, **kwargs)  # type: ignore

    def __str__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name="{self.name}")'

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)
