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
        if cardlist[0] % 100 == cardlist[1] % 100:
            if cardlist[0] % 100 == 14:
                return 20
            else:
                return (cardlist[0] % 100) * 10
        value = 0
        if cardlist[0] % 100 == 14:
            value += 1
        else:
            value += cardlist[0]
        if cardlist[1] % 100 == 14:
            value += 1
        else:
            value += cardlist[1]
        return value % 10


class Douniuniu(object):
    """
    :斗牛牛
    """

    @staticmethod
    def get_card_value(cardlist, allocid, ruanniuniu, gameRules):
        """
        :获取牌值
        :param cardlist:牌
        :param allocid:
        :return:
        """
        sum_val = 0
        temp = list()
        for c in cardlist:
            if c % 100 == 14:
                temp.append(1)
                sum_val += 1
            else:
                temp.append(c)
                sum_val += c % 100 > 10 or 0 and c
        temp = sorted(temp, cmp=Douniuniu.reversed_cmp)

        # 贵阳斗牛牛
        if 2 == allocid:
            # 五小牛
            if (gameRules >> 2) % 2 == 1 and temp[4] % 100 < 5 and sum(temp) % 100 < 11:
                return 13
            # 炸弹牛
            if (gameRules >> 1) % 2 == 1 and temp[0] % 100 == temp[3] % 100 or temp[1] % 100 == temp[4] % 100:
                return 12
            # 五花牛
            if gameRules % 2 and temp[0] % 100 > 10:
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

            if ruanniuniu:
                # 软牛牛
                if temp[0] % 100 == temp[1] % 100 - 1 == temp[2] % 100 - 2 and (temp[3] + temp[4]) % 100 > val:
                    val = (temp[3] + temp[4]) % 100
                if temp[1] % 100 == temp[2] % 100 - 1 == temp[3] % 100 - 2 and (temp[0] + temp[4]) % 100 > val:
                    val = (temp[0] + temp[4]) % 100
                if temp[2] % 100 == temp[3] % 100 - 1 == temp[4] % 100 - 2 and (temp[0] + temp[1]) % 100 > val:
                    val = (temp[0] + temp[1]) % 100
                if temp[0] % 100 == temp[2] % 100 and (temp[3] + temp[4]) % 100 > val:
                    val = (temp[3] + temp[4]) % 100
                if temp[1] % 100 == temp[3] % 100 and (temp[0] + temp[4]) % 100 > val:
                    val = (temp[0] + temp[4]) % 100
                if temp[2] % 100 == temp[4] % 100 and (temp[0] + temp[1]) % 100 > val:
                    val = (temp[0] + temp[1]) % 100

            return val
        # 荣昌牛牛
        if 3 == allocid:
            # 五小牛
            if (gameRules >> 2) % 2 == 1 and temp[4] % 100 < 5 and sum(temp) % 100 < 11:
                return 14
            # 炸弹牛
            if (gameRules >> 1) % 2 == 1 and temp[0] % 100 == temp[3] % 100 or temp[1] % 100 == temp[4] % 100:
                return 13
            # 葫芦牛
            if (gameRules >> 5) % 2 == 1 and (temp[0] % 100 == temp[1] % 100 and temp[2] % 100 == temp[4] % 100) \
                    or (temp[0] % 100 == temp[2] % 100 and temp[3] % 100 == temp[4] % 100):
                return 12
            # 五花牛
            if gameRules % 2 == 1 and temp[0] % 100 > 10:
                return 11
            for i in range(0, 4):
                for j in range(i + 1, 5):
                    if (temp[i] + temp[j]) % 10 == sum_val % 10:
                        return sum_val % 10 == 0 and 10 or sum_val % 10

    @staticmethod
    def get_multiple(value, allocid, doubleRule):
        """
        :获取倍数
        :param value:牌值
        :return:
        """
        if 2 == allocid:
            if 13 == value:
                return 8
            if 12 == value:
                return 6
            if 11 == value:
                return 5
            if 10 == value:
                return 1 == doubleRule or 4 and 3
            if 9 == value:
                return 1 == doubleRule or 3 and 2
            if 6 < value:
                return 2
            return 1
        if 3 == allocid:
            if 14 == value:
                return 8
            if 13 == value:
                return 7
            if 12 == value:
                return 6
            if 11 == value:
                return 5
            if 10 == value:
                return 1 == doubleRule or 3 and 4
            if 9 == value:
                return 1 == doubleRule or 2 and 3
            if 8 == value:
                return 2
            if 6 < value and 2 == doubleRule:
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
            pd = PiBanBanSettleData()
            pd.ParseFromString(request.extraData)
            jackpot = pd.jackpot
            deskScore = pd.jackpot
            for b in request.userSettleData:
                if b.userId == request.banker:
                    banker_value = Pibanban.get_card_value(b.cardlist)
                    win = 0
                    for u in request.userSettleData:
                        if u.userId != request.banker:
                            playScore = u.score
                            if 2 == pd.playType:
                                if 1 == playScore:
                                    playScore = jackpot
                                    deskScore = 0
                                if 2 == playScore:
                                    playScore = jackpot / 2
                                    deskScore = jackpot / 2
                                if 3 == playScore:
                                    playScore = jackpot
                                    deskScore = 0
                                if 4 == playScore:
                                    playScore = deskScore
                                    deskScore = 0
                            elif playScore > jackpot:
                                playScore = jackpot
                            userSettleResult = settle.userSettleResule.add()
                            user_value = Pibanban.get_card_value(u.cardlist)
                            userSettleResult.userId = u.userId
                            userSettleResult.cardValue = user_value
                            if user_value > banker_value:
                                if user_value > 9:
                                    userSettleResult.win = 2 * playScore
                                    win -= 2 * playScore
                                else:
                                    userSettleResult.win = playScore
                                    win -= playScore
                            else:
                                userSettleResult.win = -playScore
                                win += playScore
                            jackpot + win
                    userSettleResult = settle.userSettleResule.add()
                    userSettleResult.userId = b.userId
                    userSettleResult.cardValue = banker_value
                    userSettleResult.win = win
                    break
        if 2 == request.allocid:
            data = GYNiuniuSettleData()
            data.ParseFromString(request.extraData)
            if 0 == request.banker:
                maxUser = request.userSettleData[0]
                max_value = Douniuniu.get_card_value(maxUser.cardlist, 2, data.playRule == 2, data.gameRules)
                for u in request.userSettleData:
                    user_value = Douniuniu.get_card_value(u.cardlist, 2, data.playRule == 2, data.gameRules)
                    if user_value > max_value:
                        max_value = user_value
                        maxUser = u
                    if user_value == max_value:
                        max_array_card = sorted(maxUser.cardlist, cmp=Douniuniu.reversed_cmp)
                        user_array_card = sorted(u.cardlist, cmp=Douniuniu.reversed_cmp)
                        if max_array_card[4] % 100 < user_array_card[4] % 100 \
                                or (max_array_card[4] % 100 == user_array_card[4] % 100
                                    and max_array_card[4] < user_array_card[4]):
                            max_value = user_value
                            maxUser = u

            for b in request.userSettleData:
                if b.userId == request.banker:
                    banker_value = Douniuniu.get_card_value(b.cardlist, 2, data.playRule == 2, data.gameRules)
                    banker_multiple = Douniuniu.get_multiple(banker_value, 2, data.doubleRule)
                    win = 0
                    banker_array_cards = sorted(b.cardlist, cmp=Douniuniu.reversed_cmp)
                    for u in request.userSettleData:
                        if u.userId != request.banker:
                            userSettleResult = settle.userSettleResule.add()
                            user_value = Douniuniu.get_card_value(u.cardlist, 2, data.playRule == 2, data.gameRules)
                            userSettleResult.userId = u.userId
                            userSettleResult.cardValue = user_value
                            user_multiple = Douniuniu.get_multiple(user_value, 2, data.doubleRule)
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

                    userSettleResult = settle.userSettleResule.add()
                    userSettleResult.userId = b.userId
                    userSettleResult.cardValue = banker_value
                    userSettleResult.win = win
                    break
        if 3 == request.allocid:
            data = RCNiuniuSettleData()
            data.ParseFromString(request.extraData)
            if 0 == request.banker:
                maxUser = request.userSettleData[0]
                max_value = Douniuniu.get_card_value(maxUser.cardlist, 3, False, data.gameRules)
                for u in request.userSettleData:
                    user_value = Douniuniu.get_card_value(u.cardlist, 3, False, data.gameRules)
                    if user_value > max_value:
                        max_value = user_value
                        maxUser = u
                    if user_value == max_value:
                        max_array_card = sorted(maxUser.cardlist, cmp=Douniuniu.reversed_cmp)
                        user_array_card = sorted(u.cardlist, cmp=Douniuniu.reversed_cmp)
                        if max_array_card[4] % 100 < user_array_card[4] % 100 \
                                or (max_array_card[4] % 100 == user_array_card[4] % 100
                                    and max_array_card[4] < user_array_card[4]):
                            max_value = user_value
                            maxUser = u

            for b in request.userSettleData:
                if b.userId == request.banker:
                    banker_value = Douniuniu.get_card_value(b.cardlist, 3, False, data.gameRules)
                    banker_multiple = Douniuniu.get_multiple(banker_value, 3, data.doubleRule)
                    win = 0
                    banker_array_cards = sorted(b.cardlist, cmp=Douniuniu.reversed_cmp)
                    for u in request.userSettleData:
                        if u.userId != request.banker:
                            userSettleResult = settle.userSettleResule.add()
                            user_value = Douniuniu.get_card_value(u.cardlist, 3, False, data.gameRules)
                            userSettleResult.userId = u.userId
                            userSettleResult.cardValue = user_value
                            user_multiple = Douniuniu.get_multiple(user_value, 3, data.doubleRule)
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

                    userSettleResult = settle.userSettleResule.add()
                    userSettleResult.userId = b.userId
                    userSettleResult.cardValue = banker_value
                    userSettleResult.win = win
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
        if 2 == request.allocid:
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
