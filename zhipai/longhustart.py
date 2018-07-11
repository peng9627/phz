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
from zhipai_pb2 import *

logging.basicConfig(level=logging.INFO)
thislog = logging.getLogger()


class Performance(zhipai_pb2_grpc.ZhipaiServicer):
    """
    :实现grpc
    """

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='zhipai.log',
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
        if 499 < u1.cardlist[0]:
            u1_value = u1.cardlist[0] / 10
        else:
            u1_value = u1.cardlist[0] % 100
        if 14 == u1_value:
            u1_value = 1
        if 499 < u2.cardlist[0]:
            u2_value = u2.cardlist[0] / 10
        else:
            u2_value = u2.cardlist[0] % 100
        if 14 == u2_value:
            u2_value = 1
        if u1_value > u2_value:
            userSettleResult = settle.userSettleResule.add()
            userSettleResult.userId = u1.userId
            userSettleResult.win = 1

            userSettleResult = settle.userSettleResule.add()
            userSettleResult.userId = u2.userId
            userSettleResult.win = -1
        elif u1_value < u2_value:
            userSettleResult = settle.userSettleResule.add()
            userSettleResult.userId = u1.userId
            userSettleResult.win = -1

            userSettleResult = settle.userSettleResule.add()
            userSettleResult.userId = u2.userId
            userSettleResult.win = 1
        else:
            userSettleResult = settle.userSettleResule.add()
            userSettleResult.userId = u1.userId

            userSettleResult = settle.userSettleResule.add()
            userSettleResult.userId = u2.userId
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
    server.add_insecure_port('[::]:50011')
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
        filename='../logs/zhipai/longhu-%s.log', when="H", interval=1,
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
