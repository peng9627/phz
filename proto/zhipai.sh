#!/usr/bin/env bash
 /usr/bin/python -m grpc_tools.protoc -I./ --python_out=./zhipai/ --grpc_python_out=. ./zhipai.proto