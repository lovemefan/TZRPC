#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @FileName  :__init__.py
# @Time      :2022/9/4 18:11
# @Author    :lovemefan
# @email     :lovemefan@outlook.com
from .server.server import TZRPC_Server
from .client.client import TZPRC_Client

__all__ = ["TZRPC_Server", "TZPRC_Client"]
