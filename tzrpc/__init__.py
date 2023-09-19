#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @FileName  :__init__.py
# @Time      :2022/9/4 18:11
# @Author    :lovemefan
# @email     :lovemefan@outlook.com
from .client.client import TZPRC_Client
from .server.server import TZRPC_Server

__all__ = ["TZRPC_Server", "TZPRC_Client"]
