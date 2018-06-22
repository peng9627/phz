#!/usr/bin/env bash
 /usr/bin/python -m grpc_tools.protoc -I./ --python_out=../cishuipaodekuai/ --grpc_python_out=../cishuipaodekuai/ ./paodekuai.proto