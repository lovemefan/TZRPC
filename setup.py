# -*- coding: utf-8 -*-
# @Time  : 2021/8/6 11:20
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tzrpc",
    version="0.0.1",
    author="lovemefan",
    author_email="lovemefan@outlook.com",
    description="a rpc framework for python base on grpc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lovemefan/TZRPC",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License ::  MIT License",
        "Operating System :: OS Independent",
    ],
)
