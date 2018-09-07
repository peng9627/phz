# -*- encoding=utf-8 -*-
import datetime
import logging
import random
import re
import time
from logging.handlers import TimedRotatingFileHandler

import grpc
from concurrent import futures

import zhipai_pb2_grpc
from niuniu import Niuniu
from zhipai_pb2 import *

logging.basicConfig(level=logging.INFO)
thislog = logging.getLogger()


class Douniuniu(object):
    """
    :斗牛牛
    """

    @staticmethod
    def compare(cardlist, cards):
        """
        :斗牛牛比牌
        :param cardlist:
        :param cards:
        :return:
        """
        banker_value = Douniuniu.get_card_value(cardlist)
        banker_array_cards = sorted(cardlist, cmp=Niuniu.reversed_cmp)
        user_value = Douniuniu.get_card_value(cards)
        if user_value < banker_value:
            return 1
        elif user_value > banker_value:
            return -1
        else:
            user_array_cards = sorted(cards, cmp=Niuniu.reversed_cmp)
            if banker_array_cards[4] % 100 > user_array_cards[4] % 100:
                return 1
            elif banker_array_cards[4] % 100 < user_array_cards[4] % 100:
                return -1
            elif banker_array_cards[4] > user_array_cards[4]:
                return 1
            else:
                return -1

    @staticmethod
    def get_card_value(cardlist):
        """
        :获取牌值
        :param cardlist:牌
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

        val1 = 0
        for i in range(0, 4):
            for j in range(i + 1, 5):
                temp1 = 0 if temp[i] % 100 > 10 else temp[i] % 100
                temp2 = 0 if temp[j] % 100 > 10 else temp[j] % 100
                if (temp1 % 100 + temp2 % 100) % 10 == sum_val % 10:
                    val1 = (10 if sum_val % 10 == 0 else sum_val % 10)
        return val1

    @staticmethod
    def get_multiple(value):
        """
        :获取倍数
        :param value:牌值
        :return:
        """
        if 9 < value:
            return 3
        if 7 < value:
            return 2
        return 1


class Performance(zhipai_pb2_grpc.ZhipaiServicer):
    """
    :实现grpc
    """

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='bairen_niuniu.log',
                            filemode='w')

    def settle(self, request, context):
        """
        :结算
        :param request:
        :param context:
        :return:
        """
        settle = SettleResult()
        data = NiuniuSettleData()
        data.ParseFromString(request.extraData)
        for b in request.userSettleData:
            if b.userId == request.banker:
                banker_value = Douniuniu.get_card_value(b.cardlist)
                banker_multiple = Douniuniu.get_multiple(banker_value)
                banker_multiple *= b.grab
                win = 0
                banker_array_cards = sorted(b.cardlist, cmp=Niuniu.reversed_cmp)
                for u in request.userSettleData:
                    if u.userId != request.banker:
                        userSettleResult = settle.userSettleResule.add()
                        user_value = Douniuniu.get_card_value(u.cardlist)
                        userSettleResult.userId = u.userId
                        userSettleResult.cardValue = user_value
                        user_multiple = Douniuniu.get_multiple(user_value)
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
        random.shuffle(cardlist)
        cheat_index = 0
        cheat_probability = 0
        for c in range(0, len(request.cheatData)):
            if request.cheatData[c].level != 0:
                cheat_index = c
                cheat_probability = request.cheatData[c].level
                break
        if 0 != cheat_probability:
            data = NiuniuSettleData()
            data.ParseFromString(request.extraData)
            if random.random() * 100 < cheat_probability:
                max_card = [cardlist[cheat_index * 5], cardlist[cheat_index * 5 + 1], cardlist[cheat_index * 5 + 2],
                            cardlist[cheat_index * 5 + 3], cardlist[cheat_index * 5 + 4]]
                for i in range(0, len(request.cheatData)):
                    if i != cheat_index:
                        if -1 == Douniuniu.compare(max_card,
                                                   [cardlist[i * 5],
                                                    cardlist[i * 5 + 1],
                                                    cardlist[i * 5 + 2],
                                                    cardlist[i * 5 + 3],
                                                    cardlist[i * 5 + 4]]):
                            cardlist[cheat_index * 5] = cardlist[i * 5]
                            cardlist[cheat_index * 5 + 1] = cardlist[i * 5 + 1]
                            cardlist[cheat_index * 5 + 2] = cardlist[i * 5 + 2]
                            cardlist[cheat_index * 5 + 3] = cardlist[i * 5 + 3]
                            cardlist[cheat_index * 5 + 4] = cardlist[i * 5 + 4]
                            cardlist[i * 5] = max_card[0]
                            cardlist[i * 5 + 1] = max_card[1]
                            cardlist[i * 5 + 2] = max_card[2]
                            cardlist[i * 5 + 3] = max_card[3]
                            cardlist[i * 5 + 4] = max_card[4]
                            max_card = [cardlist[cheat_index * 5],
                                        cardlist[cheat_index * 5 + 1],
                                        cardlist[cheat_index * 5 + 2],
                                        cardlist[cheat_index * 5 + 3],
                                        cardlist[cheat_index * 5 + 4]]
            else:
                max_card = [cardlist[cheat_index * 5], cardlist[cheat_index * 5 + 1], cardlist[cheat_index * 5 + 2],
                            cardlist[cheat_index * 5 + 3], cardlist[cheat_index * 5 + 4]]
                for i in range(0, len(request.cheatData)):
                    if i != cheat_index:
                        if 1 == Douniuniu.compare(max_card,
                                                  [cardlist[i * 5],
                                                   cardlist[i * 5 + 1],
                                                   cardlist[i * 5 + 2],
                                                   cardlist[i * 5 + 3],
                                                   cardlist[i * 5 + 4]]):
                            cardlist[cheat_index * 5] = cardlist[i * 5]
                            cardlist[cheat_index * 5 + 1] = cardlist[i * 5 + 1]
                            cardlist[cheat_index * 5 + 2] = cardlist[i * 5 + 2]
                            cardlist[cheat_index * 5 + 3] = cardlist[i * 5 + 3]
                            cardlist[cheat_index * 5 + 4] = cardlist[i * 5 + 4]
                            cardlist[i * 5] = max_card[0]
                            cardlist[i * 5 + 1] = max_card[1]
                            cardlist[i * 5 + 2] = max_card[2]
                            cardlist[i * 5 + 3] = max_card[3]
                            cardlist[i * 5 + 4] = max_card[4]
                            max_card = [cardlist[cheat_index * 5],
                                        cardlist[cheat_index * 5 + 1],
                                        cardlist[cheat_index * 5 + 2],
                                        cardlist[cheat_index * 5 + 3],
                                        cardlist[cheat_index * 5 + 4]]
        shuffle.cardlist.extend(cardlist)
        thislog.info(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    logging.info("started!")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    zhipai_pb2_grpc.add_ZhipaiServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50014')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    log_fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(log_fmt)
    log_file_handler = TimedRotatingFileHandler(
        filename='../logs/bairen_niuniu.log', when="H", interval=1,
        backupCount=200)
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.DEBUG)
    thislog.addHandler(log_file_handler)

    rpc_server()
    thislog.removeHandler(log_file_handler)()


class Formatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        """
        Return the creation time of the specified LogRecord as formatted text.

        This method should be called from format() by a formatter which
        wants to make use of a formatted time. This method can be overridden
        in formatters to provide for any specific requirement, but the
        basic behaviour is as follows: if datefmt (a string) is specified,
        it is used with time.strftime() to format the creation time of the
        record. Otherwise, the ISO8601 format is used. The resulting
        string is returned. This function uses a user-configurable function
        to convert the creation time to a tuple. By default, time.localtime()
        is used; to change this for a particular formatter instance, set the
        'converter' attribute to a function with the same signature as
        time.localtime() or time.gmtime(). To change it for all formatters,
        for example if you want all logging times to be shown in GMT,
        set the 'converter' attribute in the Formatter class.
        """
        ct = self.converter(record.created)
        if datefmt:
            s = time.strftime(datefmt, ct)
        else:
            # t = time.strftime("%Y-%m-%d %H:%M:%S", ct)
            # s = "%s,%03d" % (t, record.msecs)
            s = str(datetime.datetime.now())
        return s
