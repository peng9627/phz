#!/usr/bin/env bash
 /usr/bin/python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=. ./zipai.proto