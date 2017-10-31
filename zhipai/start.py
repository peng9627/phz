# -*- encoding=utf-8 -*-
import random
import time

from concurrent import futures

import zhipai_pb2_grpc
from zhipai_pb2 import *


class Pibanban(object):
    """
    :劈板板
    """

    @staticmethod
    def get_card_value(cardlist):
        """
        :获取牌值
        :param cardlist:
        :return:
        """
        if cardlist[0] == cardlist[1]:
            return cardlist[0] * 10
        else:
            return (cardlist[0] + cardlist[1]) % 10


class Douniuniu(object):
    """
    :斗牛牛
    """

    @staticmethod
    def get_card_value(cardlist):
        """
        :获取牌值
        :param cardlist:牌
        :return:
        """
        temp = sorted(cardlist, cmp=Douniuniu.reversed_cmp)
        sum_val = sum(temp) % 100
        if temp[4] % 100 < 5 and sum_val < 11:
            return 13
        if temp[0] % 100 == temp[3] % 100 or temp[1] % 100 == temp[4] % 100:
            return 12
        if temp[0] % 100 > 10:
            return 11

        val = 0
        # 硬牛牛
        for i in range(0, 4):
            if val != 0:
                break
            for j in range(i + 1, 5):
                if (temp[i] + temp[j]) % 10 == sum_val % 10:
                    val = sum_val % 10 == 0 and 10 or sum_val % 10
                    break

        # 软牛牛
        if temp[0] % 100 == temp[1] % 100 - 1 == temp[2] % 100 - 2 and (temp[3] + temp[4]) % 100 > val:
            return (temp[3] + temp[4]) % 100
        if temp[1] % 100 == temp[2] % 100 - 1 == temp[3] % 100 - 2 and (temp[0] + temp[4]) % 100 > val:
            return (temp[0] + temp[4]) % 100
        if temp[2] % 100 == temp[3] % 100 - 1 == temp[4] % 100 - 2 and (temp[0] + temp[1]) % 100 > val:
            return (temp[0] + temp[1]) % 100

        return val

    @staticmethod
    def get_multiple(value):
        """
        :获取倍数
        :param value:牌值
        :return:
        """
        if 13 == value:
            return 8
        if 12 == value:
            return 6
        if 11 == value:
            return 5
        if 10 == value:
            return 3
        if 6 < value:
            return 2
        return 1

    @staticmethod
    def reversed_cmp(x, y):
        """
        :排序方法
        :param x:
        :param y:
        :return:
        """
        if x % 100 > y % 100:
            return 1
        if x % 100 < y % 100:
            return -1
        return x > y


class Performance(zhipai_pb2_grpc.ZhipaiServicer):
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
        if 1 == request.allocid:
            for b in request.userSettleData:
                if b.userId == request.banker:
                    banker_value = Pibanban.get_card_value(b.cardlist)
                    win = 0
                    for u in request.userSettleData:
                        if u.userId != request.banker:
                            userSettleResult = UserSettleResult
                            user_value = Pibanban.get_card_value(u.cardlist)
                            userSettleResult.userId = u.userId
                            userSettleResult.cardValue = user_value
                            if user_value > banker_value:
                                if user_value > 9:
                                    userSettleResult.win = 2 * u.score
                                    win -= 2 * u.score
                                else:
                                    userSettleResult.win = u.score
                                    win -= u.score
                            else:
                                userSettleResult.win = -u.score
                                win += u.score
                            settle.append(userSettleResult)
                    userSettleResult = UserSettleResult
                    userSettleResult.userId = b.userId
                    userSettleResult.cardValue = banker_value
                    userSettleResult.win = win
                    settle.append(userSettleResult)
                    break
        if 2 == request.allocid:
            for b in request.userSettleData:
                if b.userId == request.banker:
                    banker_value = Douniuniu.get_card_value(b.cardlist)
                    banker_multiple = Douniuniu.get_multiple(banker_value)
                    win = 0
                    banker_array_cards = sorted(b.cardlist, cmp=Douniuniu.reversed_cmp)
                    for u in request.userSettleData:
                        if u.userId != request.banker:
                            userSettleResult = UserSettleResult
                            user_value = Douniuniu.get_card_value(u.cardlist)
                            userSettleResult.userId = u.userId
                            userSettleResult.cardValue = user_value
                            user_multiple = Douniuniu.get_multiple(user_value)
                            if user_value < banker_value:
                                userSettleResult.win = -banker_multiple * u.score
                                win += banker_multiple * u.score
                            elif user_value > banker_value:
                                userSettleResult.win = user_multiple * u.score
                                win -= user_multiple * u.score
                            else:
                                user_array_cards = sorted(u.cardlist, cmp=Douniuniu.reversed_cmp)
                                if banker_array_cards[4] % 100 > user_array_cards[4] % 100:
                                    userSettleResult.win = -banker_multiple * u.score
                                    win += banker_multiple * u.score
                                elif banker_array_cards[4] % 100 < user_array_cards[4] % 100:
                                    userSettleResult.win = user_multiple * u.score
                                    win -= user_multiple * u.score
                                elif banker_array_cards[4] > user_array_cards[4]:
                                    userSettleResult.win = -banker_multiple * u.score
                                    win += banker_multiple * u.score
                                else:
                                    userSettleResult.win = user_multiple * u.score
                                    win -= user_multiple * u.score

                    userSettleResult = UserSettleResult
                    userSettleResult.userId = b.userId
                    userSettleResult.cardValue = banker_value
                    userSettleResult.win = win
                    settle.append(userSettleResult)
                    break
        return settle

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
            cardlist.extend([1, 101, 201, 301,
                             2, 102, 202, 302,
                             3, 103, 203, 303,
                             4, 104, 204, 304,
                             5, 105, 205, 305,
                             6, 106, 206, 306,
                             7, 107, 207, 307,
                             8, 108, 208, 308,
                             9, 109, 209, 309,
                             10, 110, 210, 310])
        if 2 == request.allocid:
            cardlist.extend([1, 101, 201, 301,
                             2, 102, 202, 302,
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
                             13, 113, 213, 313])
        random.shuffle(cardlist)
        shuffle.cardlist.extend(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    zhipai_pb2_grpc.add_ZhipaiServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50001')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    rpc_server()
