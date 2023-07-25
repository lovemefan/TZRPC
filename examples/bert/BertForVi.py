# -*- coding: utf-8 -*-
# @Time  : 2021/7/25 13:28
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : BertForVi.py

import torch
from transformers import AutoModel, AutoTokenizer

from examples.bert.BertBase import BertBase
from tzrpc.decorator.singleton import singleton


@singleton
class BertForVietnamese(BertBase):
    def __init__(self):
        # super(self, 'BertForVietnamese')
        self.phobert = AutoModel.from_pretrained("vinai/phobert-base")

        # For transformers v4.x+:
        self.tokenizer = AutoTokenizer.from_pretrained(
            "vinai/phobert-base", use_fast=False
        )

    def output(self, input: str):
        input_ids = torch.tensor([self.tokenizer.encode(input)])

        with torch.no_grad():
            features = self.phobert(input_ids)  # Models outputs are now tuples
        return features


if __name__ == "__main__":
    line = "Tôi là sinh_viên trường đại_học Công_nghệ ."
    vi = BertForVietnamese()
    out = vi.output(line)
    123
