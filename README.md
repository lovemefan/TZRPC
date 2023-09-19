
<br/>
<h2 align="center">TZRPC</h2>
<h3 align="center">让深度学习调用： 简单！！！ 高效！！！</h3>
<br/>

[comment]: <> ([![pypi]&#40;https://img.shields.io/pypi/v/arq.svg&#41;]&#40;https://pypi.python.org/pypi/arq&#41;)
[![versions](https://img.shields.io/pypi/pyversions/arq.svg)](https://github.com/lovemefan/TZRPC)
![GitHub repo size](https://img.shields.io/github/repo-size/lovemefan/TZRPC)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/lovemefan/TZRPC/blob/main/README.md)
![GitHub forks](https://img.shields.io/github/forks/lovemefan/TZRPC)
![GitHub Repo stars](https://img.shields.io/github/stars/lovemefan/TZRPC)
[![license](https://img.shields.io/github/license/samuelcolvin/arq.svg)](https://github.com/lovemefan/TZRPC/blob/master/LICENSE)


> 深度学习模型在落地时需要提供高效快速交互接口，业务逻辑和深度模型解码通常运行在不同类型的机器上。
Http 并不适合大量数据的交互，而RPC (Remote Procedure Call) 远程过程调用, 而RPC在TCP层实现。提高了开发效率，算法工程师可以不必花费更多精力放在具体的接口实现上，而是专注于算法优化上。

tzrpc 框架基于google的 [grpc](https://github.com/grpc/) 实现，需要Python 3.7及以上， 支持流式传输！！！

目前支持以下基础类型：

| TZRPC 类型       | python 类型    | 是否支持 |
|----------------|--------------|-----|
| String         | str          | ✅   |
| Integer        | int          | ✅   |
| Float          | float        | ✅   |
| Double         | float        | ✅   |
| Boolean        | bool         | ✅   |
| Bytes          | bytes        | ✅   |
| Numpy          | numpy        | ✅   |
| Tensor         | torch.Tensor | ✅   |
| 使用pickle模块反序列化 | 任意python对象   | ✅    |


## 快速使用
### 安装
```bash
pip install tzrpc
```

或拉取最新代码，安装
```bash
git clone https://github.com/lovemefan/TZRPC.git
cd TZRPC
pip install -e .
```
### 服务端 Server.py

```python 
from tzrpc import TZRPC_Server
import numbers
server = TZRPC_Server(__name__)


@server.register
def say_hello(text):
    return "hello world " + text

@server.register
def send_numpy_obj(data):
    return data * 2 + 1

@server.register
def send_torch_tensor_obj(data):
    return data @ data.T

@server.register
def send_bytes(data: bytes):
    return data + data

@server.register
def send_number(data: numbers.Number):
    return data * 2


@server.register
def send_bool(_bool: bool):
    return not _bool


@server.register
def send_python_obj(data):
    return data

@server.register(stream=True)
def gumbel(num):
    if num % 3 == 0:
        yield f"number is {num}, you win"

if __name__ == '__main__':
    server.run("localhost", 8000)
```

### 客户端 Client.py
```python
from tzrpc import TZPRC_Client
import numpy as np
import torch
import numbers
SERVER_ADDRESS = "localhost:8000"
client = TZPRC_Client(SERVER_ADDRESS)


@client.register
def say_hello(text):
    return text

@client.register
def send_numpy_obj():
    data = np.array([[1, 2, 3], [4, 5, 6]])
    return data

@client.register
def send_torch_tensor_obj():
    data = torch.tensor([[1, 2, 3], [4, 5, 6]])
    return data

@client.register
def send_bytes():
    return b"just for test"

@client.register
def send_number(data: numbers.Number):
    return data


@client.register
def send_bool(_bool: bool):
    return _bool

@client.register
def send_python_obj(data):
    return data

@client.register(stream=True)
def gumbel(num):
    for i in range(num):
        yield i

if __name__ == '__main__':
    print(say_hello("lovemefan"))
    print(send_numpy_obj())
    print(send_torch_tensor_obj())
    print(send_bytes())
    print(send_number(2))
    print(send_number(1/3))
    print(send_bool(True))
    print(send_bool(False))
    
    class testOb:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    python_obj = testOb("test_name", 20)
    print(send_python_obj(python_obj).__dict__)
    
    # 流式demo
    for i in gumbel(10):
        print(i)
```

### 客户端输出
```
hello world lovemefan

[[ 3  5  7]
 [ 9 11 13]]
 
tensor([[14, 32],
        [32, 77]])
        
b'just for testjust for test'

4

0.6666666666666666

False

True

{'name': 'test_name', 'age': 20}

number is 0, you win
number is 3, you win
number is 6, you win
number is 9, you win
```