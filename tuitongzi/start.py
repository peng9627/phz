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
from tuitongzi import Tuitongzi
from zhipai_pb2 import *

logging.basicConfig(level=logging.INFO)
thislog = logging.getLogger()


def cheat(cardlist, cheatData):
    """
    :实现cheat
    """
    cheat_index = 0
    cheat_probability = 0
    for c in range(0, len(cheatData)):
        if cheatData[c].level != 0:
            cheat_index = c
            cheat_probability = cheatData[c].level
            break
    if 0 != cheat_probability:
        if random.random() * 100 < cheat_probability:
            max_card = [cardlist[cheat_index * 2], cardlist[cheat_index * 2 + 1]]
            for i in range(0, len(cheatData)):
                if i != cheat_index:
                    if -1 == Tuitongzi.compare(max_card, [cardlist[i * 2], cardlist[i * 2 + 1]]):
                        cardlist[cheat_index * 2] = cardlist[i * 2]
                        cardlist[cheat_index * 2 + 1] = cardlist[i * 2 + 1]

                        cardlist[i * 2] = max_card[0]
                        cardlist[i * 2 + 1] = max_card[1]
                        max_card = [cardlist[cheat_index * 2], cardlist[cheat_index * 2 + 1]]
        else:
            max_card = [cardlist[cheat_index * 2], cardlist[cheat_index * 2 + 1]]
            for i in range(0, len(cheatData)):
                if i != cheat_index:
                    if 1 == Tuitongzi.compare(max_card, [cardlist[i * 2], cardlist[i * 2 + 1]]):
                        cardlist[cheat_index * 2] = cardlist[i * 2]
                        cardlist[cheat_index * 2 + 1] = cardlist[i * 2 + 1]

                        cardlist[i * 2] = max_card[0]
                        cardlist[i * 2 + 1] = max_card[1]
                        max_card = [cardlist[cheat_index * 2], cardlist[cheat_index * 2 + 1]]
    return cardlist


class Performance(zhipai_pb2_grpc.ZhipaiServicer):
    """
    :实现grpc
    """

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='tuitongzi.log',
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
                banker_type = Tuitongzi.getCardType(b.cardlist)
                banker_value = Tuitongzi.get_card_value(b.cardlist, banker_type)
                banker_multiple = Tuitongzi.get_multiple(banker_type, banker_value)
                win = 0
                banker_array_cards = sorted(b.cardlist)
                for u in request.userSettleData:
                    if u.userId != request.banker:
                        userSettleResult = settle.userSettleResule.add()
                        user_type = Tuitongzi.getCardType(u.cardlist)
                        user_value = Tuitongzi.get_card_value(u.cardlist, user_type)
                        userSettleResult.userId = u.userId
                        userSettleResult.cardValue = user_type
                        user_multiple = Tuitongzi.get_multiple(user_type, user_value)
                        # TODO
                        if user_type < banker_type or (user_type == banker_type and user_value < banker_value):
                            userSettleResult.win = -banker_multiple * u.score
                            win += banker_multiple * u.score
                        elif user_type > banker_type or (user_type == banker_type and user_value > banker_value):
                            userSettleResult.win = user_multiple * u.score
                            win -= user_multiple * u.score
                        else:
                            user_array_cards = sorted(u.cardlist)
                            # TODO 江湖
                            # if banker_array_cards[1] % 10 < user_array_cards[1] % 10:
                            #     userSettleResult.win = user_multiple * u.score
                            #     win -= user_multiple * u.score
                            # elif banker_array_cards[1] % 10 > user_array_cards[1] % 10:
                            #     userSettleResult.win = -banker_multiple * u.score
                            #     win += banker_multiple * u.score

                            # 其他
                            # if user_value != 0 and banker_array_cards[1] != 31 and (
                            #         banker_array_cards[1] % 10 < user_array_cards[1] % 10 or user_array_cards[1] == 31):
                            #     userSettleResult.win = user_multiple * u.score
                            #     win -= user_multiple * u.score
                            # else:
                            #     userSettleResult.win = -banker_multiple * u.score
                            #     win += banker_multiple * u.score

                            # 揽胜
                            if banker_array_cards[1] % 10 < user_array_cards[1] % 10:
                                userSettleResult.win = user_multiple * u.score
                                win -= user_multiple * u.score
                            else:
                                userSettleResult.win = -banker_multiple * u.score
                                win += banker_multiple * u.score
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
        cardlist = []
        cardlist.extend([11, 11, 11, 11,
                         12, 12, 12, 12,
                         13, 13, 13, 13,
                         14, 14, 14, 14,
                         15, 15, 15, 15,
                         16, 16, 16, 16,
                         17, 17, 17, 17,
                         18, 18, 18, 18,
                         19, 19, 19, 19,
                         31, 31, 31, 31])
        random.shuffle(cardlist)
        cardlist = cheat(cardlist, request.cheatData)
        shuffle.cardlist.extend(cardlist)
        thislog.info(cardlist)
        return shuffle

    def cheat(self, request, context):
        """
        :cheat
        :param request:
        :param context:
        :return:
        """
        shuffle = ShuffleResult()
        cheatCard = CheatCards()
        cheatCard.ParseFromString(request.extraData)
        cardlist = list()
        cardlist.extend(cheatCard.cardlist)
        cardlist = cheat(cardlist, request.cheatData)
        shuffle.cardlist.extend(cardlist)
        thislog.info(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    thislog.info("started!")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    zhipai_pb2_grpc.add_ZhipaiServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50013')
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
        filename='../logs/tuitongzi.log', when="H", interval=1,
        backupCount=200)
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.DEBUG)
    thislog.addHandler(log_file_handler)

    rpc_server()
    thislog.removeHandler(log_file_handler)()
    # print Zhajinhua.compare([203, 213, 206], [203, 414, 413], False)


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
