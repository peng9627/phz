# coding=utf-8
import random
import time

import grpc
from concurrent import futures

from mahjong import mahjong_pb2_grpc
from mahjong.mahjong_pb2 import ShuffleResult, CalculateResult
from mahjong.utils import mahjong_utils


class Performance(mahjong_pb2_grpc.MajongCalculateServicer):
    """
    :实现grpc
    """

    def settle(self, request, context):
        pass

    def calculate(self, request, context):
        """
        :计算
        :param request:
        :param context:
        :return:
        """
        calculate = CalculateResult()
        calculate.dui.extend(mahjong_utils.MahjongUtils.get_dui(request.player.handlist))
        calculate.san.extend(mahjong_utils.MahjongUtils.get_san(request.player.handlist))
        calculate.si.extend(mahjong_utils.MahjongUtils.get_si(request.player.handlist))
        calculate.hu.extend(mahjong_utils.MahjongUtils.get_hu(request.player.handlist, request.rogue))
        return calculate

    def shuffle(self, request, context):
        """
        :洗牌
        :param request:
        :param context:
        :return:
        """
        shuffle = ShuffleResult()
        cardlist = list()
        if 1 == request.allocid:
            cardlist.extend([2, 102, 202, 302,
                             3, 103, 203, 303,
                             4, 104, 204, 304,
                             5, 105, 205, 305,
                             6, 106, 206, 306,
                             7, 107, 207, 307,
                             8, 108, 208, 308,
                             9, 109, 209, 309,
                             10, 110, 210, 310,
                             14, 114, 214, 314])
        if 2 == request.allocid or 3 == request.allocid or 4 == request.allocid or 5 == request.allocid:
            cardlist.extend([2, 102, 202, 302,
                             3, 103, 203, 303,
                             4, 104, 204, 304,
                             5, 105, 205, 305,
                             6, 106, 206, 306,
                             7, 107, 207, 307,
                             8, 108, 208, 308,
                             9, 109, 209, 309,
                             10, 110, 210, 310,
                             11, 111, 211, 311,
                             12, 112, 212, 312,
                             13, 113, 213, 313,
                             14, 114, 214, 314])
        random.shuffle(cardlist)
        shuffle.cardlist.extend(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mahjong_pb2_grpc.add_MajongCalculateServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50001')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    rpc_server()
