# -*- coding: utf-8 -*-
# @Time  : 2021/7/25 21:12
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : exceptions.py
from typing import Optional, Union


class TZRPCException(Exception):
    def __init__(
        self,
        message: Optional[Union[str, bytes]] = "",
    ) -> None:
        super().__init__(message)
