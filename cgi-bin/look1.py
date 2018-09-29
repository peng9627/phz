# -*- coding: utf-8 -*-
import grpc

import zhipai_pb2_grpc
from zhipai_pb2 import SettleData


def look(type):
    try:
        if "niuniu" == type:
            fname = '/home/game_logic/logs/bairen_niuniu.log'
            s = ""
            with open(fname, 'r') as f:  # 打开文件
                lines = f.readlines()  # 读取所有行
                last_line = lines[-1]  # 取最后一行
                cards = last_line.split(" [")
                s = cards[-1][:-2]
                cardslist = s.split(", ")
            cardslist = cardslist[:25]
        elif "tuitongzi" == type:
            fname = '/home/game_logic/logs/tuitongzi.log'
            s = ""
            with open(fname, 'r') as f:  # 打开文件
                lines = f.readlines()  # 读取所有行
                last_line = lines[-1]  # 取最后一行
                cards = last_line.split(" [")
                s = cards[-1][:-2]
                cardslist = s.split(", ")
            cardslist = cardslist[:8]
        elif "longhu" == type:
            fname = '/home/game_logic/logs/longhu.log'
            s = ""
            with open(fname, 'r') as f:  # 打开文件
                lines = f.readlines()  # 读取所有行
                last_line = lines[-1]  # 取最后一行
                cards = last_line.split(" [")
                s = cards[-1][:-2]
                cardslist = s.split(", ")
            cardslist = cardslist[:2]
        else:
            return ""
    except BaseException, e:
        print(e)
        return ""

    settleData = SettleData()
    settleData.banker = 1
    s = ""
    if "niuniu" == type:
        for i in range(0, 5):
            userSettleData = settleData.userSettleData.add()
            userSettleData.userId = i + 1
            userSettleData.cardlist.extend(
                [int(cardslist[i * 5]), int(cardslist[i * 5 + 1]), int(cardslist[i * 5 + 2]), int(cardslist[i * 5 + 3]),
                 int(cardslist[i * 5 + 4])])
            userSettleData.score = 1
            userSettleData.grab = 1
        conn = grpc.insecure_channel('127.0.0.1:50014')
        client = zhipai_pb2_grpc.ZhipaiStub(channel=conn)
        response = client.settle(settleData)
        for userSettleResule in response.userSettleResule:
            if userSettleResule.userId != 1:
                if userSettleResule.win > 0:
                    s += "赢%s\n" % str(userSettleResule.win)
                if userSettleResule.win < 0:
                    s += "输%s\n" % str(-userSettleResule.win)
    elif "tuitongzi" == type:
        for i in range(0, 4):
            userSettleData = settleData.userSettleData.add()
            userSettleData.userId = i + 1
            userSettleData.cardlist.extend([int(cardslist[i * 2]), int(cardslist[i * 2 + 1])])
            userSettleData.score = 1
            userSettleData.grab = 1
        conn = grpc.insecure_channel('127.0.0.1:50013')
        client = zhipai_pb2_grpc.ZhipaiStub(channel=conn)
        response = client.settle(settleData)
        for userSettleResule in response.userSettleResule:
            if userSettleResule.userId != 1:
                if userSettleResule.win > 0:
                    s += "赢\n"
                if userSettleResule.win < 0:
                    s += "输\n"
    elif "longhu" == type:
        for i in range(0, 2):
            userSettleData = settleData.userSettleData.add()
            userSettleData.userId = i + 1
            userSettleData.cardlist.extend([int(cardslist[i])])
            userSettleData.score = 1
            userSettleData.grab = 1
        conn = grpc.insecure_channel('127.0.0.1:50011')
        client = zhipai_pb2_grpc.ZhipaiStub(channel=conn)
        response = client.settle(settleData)
        for userSettleResule in response.userSettleResule:
            if userSettleResule.userId == 1:
                if userSettleResule.win > 0:
                    s += "龙\n"
                elif userSettleResule.win < 0:
                    s += "虎\n"
                else:
                    s += "和\n"
    return s
