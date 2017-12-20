# coding=utf-8
import random
import time

from concurrent import futures

from mahjong import mahjong_pb2_grpc, wanzhou_mahjong
from mahjong.mahjong_pb2 import *
from mahjong.utils import mahjong_utils
from zipai.zipai_pb2 import ZIMO


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
            user_settle = settle.userSettleResule.add()
            user_settle.userId = user.player_id
            user_settles.setdefault(user.player_id, user_settle)
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
            user_settles[hudata.huUser].settlePatterns.append(PIHU)
            score = wanzhou_mahjong.getScore(cardtype)
            for s in hudata.settle:
                if s != ZIMO:
                    score *= 2
            if ZIMO in hudata.settle:
                score += 1
            if score > request.fengding:
                score = request.fengding
            user_settles[hudata.huUser].cardScore += score * len(hudata.loseUsers)
            for u in hudata.loseUsers:
                user_settles[u].cardScore -= score
        return settle

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
        if 1 == request.alloc_id:
            cardlist.extend([1, 1, 1, 1,
                             2, 2, 2, 2,
                             3, 3, 3, 3,
                             4, 4, 4, 4,
                             5, 5, 5, 5,
                             6, 6, 6, 6,
                             7, 7, 7, 7,
                             8, 8, 8, 8,
                             9, 9, 9, 9,
                             11, 11, 11, 11,
                             12, 12, 12, 12,
                             13, 13, 13, 13,
                             14, 14, 14, 14,
                             15, 15, 15, 15,
                             16, 16, 16, 16,
                             17, 17, 17, 17,
                             18, 18, 18, 18,
                             19, 19, 19, 19,
                             21, 21, 21, 21,
                             22, 22, 22, 22,
                             23, 23, 23, 23,
                             24, 24, 24, 24,
                             25, 25, 25, 25,
                             26, 26, 26, 26,
                             27, 27, 27, 27,
                             28, 28, 28, 28,
                             29, 29, 29, 29])
        # random.shuffle(cardlist)
        shuffle.cardlist.extend(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mahjong_pb2_grpc.add_MajongCalculateServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50002')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    rpc_server()
