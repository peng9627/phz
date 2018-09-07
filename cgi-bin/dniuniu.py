# -*- coding: utf-8 -*-

import urllib2

import grpc

import zhipai_pb2_grpc
from zhipai_pb2 import SettleData


def niuniu(type):
    url = "http://43.227.183.83:50020/cgi-bin/test.py?action=%s" % type

    req = urllib2.Request(url)
    print req

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    cards = res.split("[")
    cards = cards[-1][:-2]
    cards = cards.split("]")[0]
    cardslist = cards.replace("'", "").split(", ")
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
        conn = grpc.insecure_channel('207.148.17.107:50014')
        client = zhipai_pb2_grpc.ZhipaiStub(channel=conn)
        response = client.settle(settleData)
        for userSettleResule in response.userSettleResule:
            if userSettleResule.userId != 1:
                if userSettleResule.win > 0:
                    s += "第%s家赢%s\n" % (str(userSettleResule.userId - 1), str(userSettleResule.win))
                if userSettleResule.win < 0:
                    s += "第%s家输%s\n" % (str(userSettleResule.userId - 1), str(-userSettleResule.win))
    elif "tuitongzi" == type:
        for i in range(0, 4):
            userSettleData = settleData.userSettleData.add()
            userSettleData.userId = i + 1
            userSettleData.cardlist.extend(
                [int(cardslist[i * 2]), int(cardslist[i * 2 + 1])])
            userSettleData.score = 1
            userSettleData.grab = 1
        conn = grpc.insecure_channel('207.148.17.107:50013')
        client = zhipai_pb2_grpc.ZhipaiStub(channel=conn)
        response = client.settle(settleData)
        for userSettleResule in response.userSettleResule:
            if userSettleResule.userId != 1:
                if userSettleResule.win > 0:
                    s += "第%s家赢\n" % str(userSettleResule.userId - 1)
                if userSettleResule.win < 0:
                    s += "第%s家输\n" % str(userSettleResule.userId - 1)
    elif "longhu" == type:
        for i in range(0, 2):
            userSettleData = settleData.userSettleData.add()
            userSettleData.userId = i + 1
            userSettleData.cardlist.extend([int(cardslist[i])])
            userSettleData.score = 1
            userSettleData.grab = 1
        conn = grpc.insecure_channel('207.148.17.107:50011')
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


if __name__ == '__main__':
    print niuniu("tuitongzi")
