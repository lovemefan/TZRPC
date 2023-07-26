
python -m grpc_tools.protoc -I=$PWD/tzrpc/proto Server.proto --python_out=$PWD/tzrpc/proto/py  --grpc_python_out=$PWD/tzrpc/proto/py
