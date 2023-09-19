# -*- coding: utf-8 -*-
# @Time  : 2021/8/6 11:20
# @Author : lovemefan
# @Email : lovemefan@outlook.com
# @File : setup.py
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = {"install": ["grpcio==1.40.0", "grpcio-tools==1.40.0", "numpy"]}

setuptools.setup(
    name="tzrpc",
    version="v0.0.4",
    author="Lovemefan, Yunnan Key Laboratory of Artificial Intelligence, "
    "Kunming University of Science and Technology, Kunming, Yunnan ",
    author_email="lovemefan@outlook.com",
    description="a rpc framework for python base on grpc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lovemefan/TZRPC",
    packages=setuptools.find_namespace_packages(),
    install_requires=requirements["install"],
    python_requires=">=3.7.0",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
