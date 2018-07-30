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
from zhajinhua import Zhajinhua
from zhipai_pb2 import *

logging.basicConfig(level=logging.INFO)
thislog = logging.getLogger()


def changeCard(cardlist, cheat_index, max_card, i):
    """
    : 换牌
    :param cardlist:
    :param cheat_index:
    :param max_card:
    :param i:
    :return:
    """
    cardlist[cheat_index * 3] = cardlist[i * 3]
    cardlist[cheat_index * 3 + 1] = cardlist[i * 3 + 1]
    cardlist[cheat_index * 3 + 2] = cardlist[i * 3 + 2]
    cardlist[i * 3] = max_card[0]
    cardlist[i * 3 + 1] = max_card[1]
    cardlist[i * 3 + 2] = max_card[2]
    max_card[0] = cardlist[cheat_index * 5]
    max_card[1] = cardlist[cheat_index * 5 + 1]
    max_card[2] = cardlist[cheat_index * 5 + 2]


class Performance(zhipai_pb2_grpc.ZhipaiServicer):
    """
    :实现grpc
    """

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='jinhua.log',
                            filemode='w')

    def settle(self, request, context):
        """
        :结算
        :param request:
        :param context:
        :return:
        """
        settle = SettleResult()
        u1 = request.userSettleData[0]
        u2 = request.userSettleData[1]
        win = Zhajinhua.compare(u1.cardlist, u2.cardlist)
        userSettleResult = settle.userSettleResule.add()
        userSettleResult.userId = u1.userId
        userSettleResult.win = win
        userSettleResult.cardValue = Zhajinhua.getCardType(u1.cardlist)
        userSettleResult = settle.userSettleResule.add()
        userSettleResult.userId = u2.userId
        userSettleResult.cardValue = Zhajinhua.getCardType(u2.cardlist)
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
        cheat_index = 0
        cheat_probability = 0
        for c in range(0, len(request.cheatData)):
            if request.cheatData[c].level != 0:
                cheat_index = c
                cheat_probability = request.cheatData[c].level
                break
        if 0 != cheat_probability:
            if random.random() * 100 < cheat_probability:
                max_card = [cardlist[cheat_index * 3], cardlist[cheat_index * 3 + 1], cardlist[cheat_index * 3 + 2]]
                for i in range(0, len(request.cheatData)):
                    if i != cheat_index:
                        if -1 == Zhajinhua.compare(max_card,
                                                   [cardlist[i * 3], cardlist[i * 3 + 1], cardlist[i * 3 + 2]]):
                            changeCard(cardlist, cheat_index, max_card, i)
            else:
                max_card = [cardlist[cheat_index * 3], cardlist[cheat_index * 3 + 1], cardlist[cheat_index * 3 + 2]]
                for i in range(0, len(request.cheatData)):
                    if i != cheat_index:
                        if 1 == Zhajinhua.compare(max_card,
                                                  [cardlist[i * 3], cardlist[i * 3 + 1], cardlist[i * 3 + 2]]):
                            changeCard(cardlist, cheat_index, max_card, i)
        shuffle.cardlist.extend(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    logging.info("started!")
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
    log_fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(log_fmt)
    log_file_handler = TimedRotatingFileHandler(
        filename='../logs/jinhua-%s.log' % time.strftime("%Y-%m-%d"), when="H", interval=1,
        backupCount=7)
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
