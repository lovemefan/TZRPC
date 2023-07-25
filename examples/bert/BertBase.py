# -*- coding: utf-8 -*-
# @Time  : 2021/7/25 13:18
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : BertBase.py
from abc import ABCMeta, abstractmethod


class BertBase(metaclass=ABCMeta):
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"bert for {self.name}"

    @abstractmethod
    def output(self, input: str):
        pass
