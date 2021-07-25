# TZRPC

[comment]: <> ([![pypi]&#40;https://img.shields.io/pypi/v/arq.svg&#41;]&#40;https://pypi.python.org/pypi/arq&#41;)
[![versions](https://img.shields.io/pypi/pyversions/arq.svg)](https://github.com/lovemefan/TZRPC)
[![license](https://img.shields.io/github/license/samuelcolvin/arq.svg)](https://github.com/samuelcolvin/arq/blob/master/LICENSE)

> 随着项目第三方服务调用需求，以及第三方环境的搭建对项目开发人员来说并不轻松。

> Http 并不适合大量数据的交互，而RPC (Remote Procedure Call) 远程过程调用, 而RPC在TCP层实现。提高了开发效率，开发人员可以把更多精力放在具体的接口实现，而不必考虑数据的底层传输问题。

rpc 框架采用采用google的 [grpc](https://github.com/grpc/) 实现，需要Python 3.6 or higher