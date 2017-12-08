# coding=utf-8
import random
import time

from concurrent import futures

from mahjong import mahjong_pb2_grpc, wanzhou_mahjong
from mahjong.mahjong_pb2 import *
from mahjong.utils import mahjong_utils


class Performance(mahjong_pb2_grpc.MajongCalculateServicer):
    """
    :实现grpc
    """

    def settle(self, request, context):
        """
        :结算
        :param request:
        :param context:
        :return:
        """
        settle = SettleResult()
        user_settles = {}
        users = {}
        for user in request.player:
            user_settles.setdefault(user.player_id, settle.userSettleResule.add())
            users.setdefault(user.player_id, user)
        for user in request.player:
            for g in user.gang:
                if g.type == BGANG:
                    user_settles[user.player_id].gangScore += len(g.fighter)
                    for f in g.fighter:
                        user_settles[f].gangScore -= 1
                if g.type == MGANG:
                    user_settles[user.player_id].gangScore += 3 * len(g.fighter)
                    for f in g.fighter:
                        user_settles[f].gangScore -= 3
                if g.type == AGANG:
                    user_settles[user.player_id].gangScore += 2 * len(g.fighter)
                    for f in g.fighter:
                        user_settles[f].gangScore -= 2
        for hudata in request.hudata:
            cardtype = wanzhou_mahjong.getCardType(users[hudata.huUser].handlist, users[hudata.huUser].peng,
                                                   users[hudata.huUser].gang, request.rogue)
            users[hudata.huUser].settlePatterns.add(SettlePatterns.items()[cardtype])
            score = wanzhou_mahjong.getScore(cardtype)
            for settle in hudata.settle:
                if settle != ZIMO:
                    score *= 2
            if ZIMO in hudata.settle:
                score += 1
            if score > request.fengding:
                score = request.fengding
            user_settles[hudata.huUser].cardScore += score * len(hudata.loseUsers)
            for u in hudata.loseUsers:
                user_settles[u].cardScore -= score

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
        zimo = mahjong_utils.MahjongUtils.get_hu(request.player.handlist, request.rogue)
        calculate.zimo.extend(zimo)
        hu = list()
        for z in zimo:
            handlist = list()
            handlist.extend(request.player.handlist)
            handlist.append(z)
            if 0 != wanzhou_mahjong.getCardType(handlist, request.player.peng, request.player.gang, request.rogue):
                hu.append(z)
        calculate.hu.extend(hu)
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
