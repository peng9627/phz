# -*- encoding=utf-8 -*-
import random
import time

import grpc
from concurrent import futures

import zhipai_pb2_grpc
from niuniu import Niuniu
from pibanban import Pibanban
from zhajinhua import Zhajinhua
from zhipai_pb2 import *


class Douniuniu(object):
    """
    :斗牛牛
    """

    @staticmethod
    def get_card_value(cardlist, allocid, ruanniuniu, gamerules):
        """
        :获取牌值
        :param cardlist:牌
        :param allocid:
        :param gamerules:
        :param ruanniuniu:
        :return:
        """
        sum_val = 0
        temp = list()
        for c in cardlist:
            if c % 100 == 14:
                temp.append(c - 13)
                sum_val += 1
            else:
                temp.append(c)
                sum_val += 0 if c % 100 > 10 else c
        temp = sorted(temp, cmp=Niuniu.reversed_cmp)

        # 贵阳斗牛牛
        if 2 == allocid:
            # 五小牛
            if (gamerules >> 2) % 2 == 1 and Niuniu.isWuxiaoniu(temp):
                return 13
            # 炸弹牛
            if (gamerules >> 1) % 2 == 1 and Niuniu.isZhadanniu(temp):
                return 12
            # 五花牛
            if gamerules % 2 == 1 and Niuniu.isWuhuaniu(temp):
                return 11

            val = 0
            # 硬牛牛
            for i in range(0, 4):
                if val != 0:
                    break
                for j in range(i + 1, 5):
                    temp1 = 0 if temp[i] % 100 > 10 else temp[i] % 100
                    temp2 = 0 if temp[j] % 100 > 10 else temp[j] % 100
                    if (temp1 % 100 + temp2 % 100) % 10 == sum_val % 10:
                        val = 10 if sum_val % 10 == 0 else sum_val % 10
                        if 0 == val:
                            val = 10
                        break

            valuetemp = list()
            for t in temp:
                valuetemp.append(10 if (t % 100) > 10 else (t % 100))

            if ruanniuniu:
                # 软牛牛
                shunvalue = Niuniu.getShunDouValue(cardlist)
                if val < shunvalue:
                    val = shunvalue
                if temp[0] % 100 == temp[2] % 100 and (valuetemp[3] + valuetemp[4]) % 10 > val:
                    val = (valuetemp[3] + valuetemp[4]) % 10
                    if 0 == val:
                        val = 10
                if temp[1] % 100 == temp[3] % 100 and (valuetemp[0] + valuetemp[4]) % 10 > val:
                    val = (valuetemp[0] + valuetemp[4]) % 10
                    if 0 == val:
                        val = 10
                if temp[2] % 100 == temp[4] % 100 and (valuetemp[0] + valuetemp[1]) % 10 > val:
                    val = (valuetemp[0] + valuetemp[1]) % 10
                    if 0 == val:
                        val = 10

            return val
        # 荣昌牛牛
        if 3 == allocid:
            # 同花顺
            if (gamerules >> 9) % 2 == 1 and Niuniu.sameColor(temp) and Niuniu.isShunziniu(temp):
                return 17
            # 炸弹牛
            if (gamerules >> 1) % 2 == 1 and Niuniu.isZhadanniu(temp):
                return 16
            # 五小牛
            if (gamerules >> 2) % 2 == 1 and Niuniu.isWuxiaoniu(temp):
                return 15
            # 五花牛
            if gamerules % 2 == 1 and Niuniu.isWuhuaniu(temp):
                return 14
            # 葫芦牛
            if (gamerules >> 5) % 2 == 1 and Niuniu.isHuluniu(temp):
                return 13
            # 同花牛
            if (gamerules >> 8) % 2 == 1 and Niuniu.sameColor(temp):
                return 12
            # 顺子牛
            if (gamerules >> 6) % 2 == 1 and Niuniu.isShunziniu(temp):
                return 11
            val1 = 0
            for i in range(0, 4):
                for j in range(i + 1, 5):
                    temp1 = 0 if temp[i] % 100 > 10 else temp[i] % 100
                    temp2 = 0 if temp[j] % 100 > 10 else temp[j] % 100
                    if (temp1 % 100 + temp2 % 100) % 10 == sum_val % 10:
                        val1 = (10 if sum_val % 10 == 0 else sum_val % 10)
                        break

            valuetemp = list()
            for t in temp:
                valuetemp.append(10 if (t % 100) > 10 else (t % 100))
            # 软牛牛
            if (gamerules >> 7) % 2 == 1:
                shunvalue = Niuniu.getShunDouValue(cardlist)
                if val1 < shunvalue:
                    val1 = shunvalue
                if temp[0] % 100 == temp[2] % 100 and (valuetemp[3] + valuetemp[4]) % 10 > val1:
                    val1 = (valuetemp[3] + valuetemp[4]) % 10
                    if 0 == val1:
                        val1 = 10
                if temp[1] % 100 == temp[3] % 100 and (valuetemp[0] + valuetemp[4]) % 10 > val1:
                    val1 = (valuetemp[0] + valuetemp[4]) % 10
                    if 0 == val1:
                        val1 = 10
                if temp[2] % 100 == temp[4] % 100 and (valuetemp[0] + valuetemp[1]) % 10 > val1:
                    val1 = (valuetemp[0] + valuetemp[1]) % 10
                    if 0 == val1:
                        val1 = 10
            return val1
        # 万州牛牛
        if 4 == allocid:
            # 五花牛
            if Niuniu.isWuhuaniu(temp):
                return 12
            # 炸弹牛
            if Niuniu.isZhadanniu(temp):
                return 11
            for i in range(0, 4):
                for j in range(i + 1, 5):
                    temp1 = 0 if temp[i] % 100 > 10 else temp[i] % 100
                    temp2 = 0 if temp[j] % 100 > 10 else temp[j] % 100
                    if (temp1 % 100 + temp2 % 100) % 10 == sum_val % 10:
                        return 10 if sum_val % 10 == 0 else sum_val % 10
            return 0

    @staticmethod
    def get_multiple(value, allocid, doubleRule):
        """
        :获取倍数
        :param value:牌值
        :param allocid
        :param doubleRule
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
                return 4 if 1 == doubleRule else 3
            if 9 == value:
                return 3 if 1 == doubleRule else 2
            if 6 < value:
                return 2
            return 1
        if 3 == allocid:
            if 17 == value:
                return 10
            if 16 == value:
                return 9
            if 15 == value:
                return 8
            if 14 == value:
                return 7
            if 13 == value:
                return 6
            if 12 == value:
                return 5
            if 11 == value:
                return 5
            if 10 == value:
                return 3 if 1 == doubleRule else 4
            if 9 == value:
                return 2 if 1 == doubleRule else 3
            if 8 == value:
                return 2
            if 6 < value and 2 == doubleRule:
                return 2
            return 1
        if 4 == allocid:
            if 12 == value:
                return 5
            if 11 == value:
                return 4
            if 10 == value:
                return 3
            if 6 < value:
                return 2
            return 1


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
        if 2 == request.allocid or 3 == request.allocid or 4 == request.allocid:
            data = NiuniuSettleData()
            data.ParseFromString(request.extraData)
            if 0 == request.banker:
                maxUser = request.userSettleData[0]
                max_value = Douniuniu.get_card_value(maxUser.cardlist, request.allocid, data.playRule == 2,
                                                     data.gameRules)
                for u in request.userSettleData:
                    user_value = Douniuniu.get_card_value(u.cardlist, request.allocid, data.playRule == 2,
                                                          data.gameRules)
                    if user_value > max_value:
                        max_value = user_value
                        maxUser = u
                    if user_value == max_value:
                        max_array_card = sorted(maxUser.cardlist, cmp=Niuniu.reversed_cmp)
                        user_array_card = sorted(u.cardlist, cmp=Niuniu.reversed_cmp)
                        if max_array_card[4] % 100 < user_array_card[4] % 100 \
                                or (max_array_card[4] % 100 == user_array_card[4] % 100
                                    and max_array_card[4] < user_array_card[4]):
                            max_value = user_value
                            maxUser = u

            for b in request.userSettleData:
                if b.userId == request.banker:
                    banker_value = Douniuniu.get_card_value(b.cardlist, request.allocid, data.playRule == 2,
                                                            data.gameRules)
                    banker_multiple = Douniuniu.get_multiple(banker_value, request.allocid, data.doubleRule)
                    banker_multiple *= b.grab
                    win = 0
                    banker_array_cards = sorted(b.cardlist, cmp=Niuniu.reversed_cmp)
                    for u in request.userSettleData:
                        if u.userId != request.banker:
                            userSettleResult = settle.userSettleResule.add()
                            user_value = Douniuniu.get_card_value(u.cardlist, request.allocid, data.playRule == 2,
                                                                  data.gameRules)
                            userSettleResult.userId = u.userId
                            userSettleResult.cardValue = user_value
                            user_multiple = Douniuniu.get_multiple(user_value, request.allocid, data.doubleRule)
                            user_multiple *= b.grab
                            if user_value < banker_value:
                                userSettleResult.win = -banker_multiple * u.score
                                win += banker_multiple * u.score
                            elif user_value > banker_value:
                                userSettleResult.win = user_multiple * u.score
                                win -= user_multiple * u.score
                            else:
                                user_array_cards = sorted(u.cardlist, cmp=Niuniu.reversed_cmp)
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
        if 5 == request.allocid:
            u1 = request.userSettleData[0]
            u2 = request.userSettleData[1]
            win = Zhajinhua.compare(u1.cardlist, u2.cardlist)
            userSettleResult = settle.userSettleResule.add()
            userSettleResult.userId = u1.userId
            userSettleResult.win = win
            userSettleResult = settle.userSettleResule.add()
            userSettleResult.userId = u2.userId
            userSettleResult.win = -win
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
        if 2 == request.allocid or 3 == request.allocid or 4 == request.allocid:
            cardlist.extend([102, 202, 302, 402,
                             103, 203, 303, 403,
                             104, 204, 304, 404,
                             105, 205, 305, 405,
                             106, 206, 306, 406,
                             107, 207, 307, 407,
                             108, 208, 308, 408,
                             109, 209, 309, 409,
                             110, 210, 310, 410,
                             111, 211, 311, 411,
                             112, 212, 312, 412,
                             113, 213, 313, 413,
                             114, 214, 314, 414])
        if 5 == request.allocid:
            jinhuaData = JinhuaData()
            jinhuaData.ParseFromString(request.extraData)
            if jinhuaData.gameType:
                cardlist.extend([102, 202, 302, 402,
                                 103, 203, 303, 403,
                                 104, 204, 304, 404,
                                 105, 205, 305, 405,
                                 106, 206, 306, 406,
                                 107, 207, 307, 407,
                                 108, 208, 308, 408,
                                 109, 209, 309, 409,
                                 110, 210, 310, 410,
                                 111, 211, 311, 411,
                                 112, 212, 312, 412,
                                 113, 213, 313, 413,
                                 114, 214, 314, 414])
            else:
                cardlist.extend([109, 209, 309, 409,
                                 110, 210, 310, 410,
                                 111, 211, 311, 411,
                                 112, 212, 312, 412,
                                 113, 213, 313, 413,
                                 114, 214, 314, 414])
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
    # temp = [111, 104, 211, 304, 411]
    # temp = sorted(temp, cmp=Niuniu.reversed_cmp)
    # print Niuniu.isHuluniu(temp)
