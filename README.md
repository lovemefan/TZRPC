# TZRPC

[comment]: <> ([![pypi]&#40;https://img.shields.io/pypi/v/arq.svg&#41;]&#40;https://pypi.python.org/pypi/arq&#41;)
[![versions](https://img.shields.io/pypi/pyversions/arq.svg)](https://github.com/lovemefan/TZRPC)
[![license](https://img.shields.io/github/license/samuelcolvin/arq.svg)](https://github.com/samuelcolvin/arq/blob/master/LICENSE)

> 随着项目第三方服务调用需求，以及第三方环境的搭建对项目开发人员来说并不轻松。

> Http 并不适合大量数据的交互，而RPC (Remote Procedure Call) 远程过程调用, 而RPC在TCP层实现。提高了开发效率，开发人员可以把更多精力放在具体的接口实现，而不必考虑数据的底层传输问题。

rpc 框架采用采用google的 [grpc](https://github.com/grpc/) 实现，需要Python 3.6 or higher

目前该项目还不够完善，输入只支持字符类型，输出支持一下类型

| TZRPC 类型|python 类型      |   方法 |
| ---- | ---- | ----|
|   String   |   str   | toString(text="") |
|  Integer    |   int   | toInteger(value=1) |
|    Float  |  float    |toFloat(value=1) |
|    Double  |  double    |toDouble(value=1) |
|    Boolean  |  bool    |toBoolean(value=1) |
|    Numpy  |  numpy    |toNumpy(shape: int, dtype: dtype, data: bytes, strides: int) |
|    Tensor  |  torch.Tensor   |toTensor(dims: int, data_type: Data_type, float_data: float, int32_data: int, byte_data:bytes, string_data:str, double_data: double, int64_data: int) |


## 快速实现TZRPC
### 安装
```bash
pip install -e .
```
### 服务端 Server.py

```python 
from tzrpc.server.server import TZRPC

rpc = TZRPC(__name__)


@rpc.register
def say_hello(text):
    print(text)
    return "hello world " + text


if __name__ == '__main__':
    rpc.run("localhost", 8000)
```
### 客户端 Client.py
```python
from tzrpc.client.client import TZPRC_Client
from tzrpc.proto.py.String_pb2 import String


SERVER_ADDRESS = "localhost:8000"
client = TZPRC_Client(SERVER_ADDRESS)


@client.register
def say_hello(stub, text):
    request = String(text=text)
    response = stub.toString(request)
    print(response.text)


if __name__ == '__main__':
    say_hello(text="lovemefan")
```

### 客户端输出
```
hello world lovemefan
```