#!/usr/bin/env bash
 /usr/bin/python -m grpc_tools.protoc -I./ --python_out=../mahjong/ --grpc_python_out=../mahjong/ ./mahjong.proto