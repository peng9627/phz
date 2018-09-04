# -*- encoding=utf-8 -*-
import datetime
import logging
import random
import re
import time
from logging.handlers import TimedRotatingFileHandler

import grpc
from concurrent import futures

import paodekuai_pb2_grpc
from common import PaodekuaiType
from paodekuai_pb2 import *
from paodekuai_utils import PaodekuaiUtils

logging.basicConfig(level=logging.INFO)
thislog = logging.getLogger()


class Performance(paodekuai_pb2_grpc.PaodekuaiServicer):
    """
    :实现grpc
    """

    def playcard(self, request, context):
        """
        :出牌检测
        :param request:
        :param context:
        :return:
        """
        playResult = PlayResult()
        playResult.cardtype = request.cardtype

        last_card_type = PaodekuaiUtils.get_card_type(request.lastcards)
        if request.cardtype != last_card_type and 0 != request.cardtype:
            if last_card_type == PaodekuaiType.SANLIAN and request.cardtype == PaodekuaiType.FEIJI:
                last_card_type = PaodekuaiType.FEIJI
        last_value = PaodekuaiUtils.get_card_value(request.lastcards, last_card_type)

        # 上家没出牌
        if 0 == len(request.lastcards):
            if 0 == len(request.playcards):
                if request.baodan:
                    return PaodekuaiUtils.baodan(request, playResult)
                playResult.cardtype = PaodekuaiType.DANPAI
                playResult.result.append(request.handcards[0])
                return playResult
            else:
                my_card_type = PaodekuaiUtils.get_card_type(request.playcards)
                if request.baodan and my_card_type == PaodekuaiType.DANPAI:
                    return PaodekuaiUtils.maxdan(request, playResult)
                if my_card_type == PaodekuaiType.ERROR:
                    if request.baodan:
                        return PaodekuaiUtils.baodan(request, playResult)
                    playResult.cardtype = PaodekuaiType.DANPAI
                    playResult.result.append(request.handcards[0])
                    return playResult
                playResult.cardtype = my_card_type
        else:
            if last_card_type == PaodekuaiType.DANPAI and request.baodan:
                playResult1 = PlayResult()
                playResult1 = PaodekuaiUtils.maxdan(request, playResult1)
                if PaodekuaiUtils.get_card_value(playResult1.result, playResult1.cardtype) > last_value:
                    return playResult1
                else:
                    return playResult
            # 不出
            if 0 == len(request.playcards):
                autocard = PaodekuaiUtils.auto_play(request.handcards, last_card_type, last_value,
                                                    len(request.lastcards))
                if 0 != len(autocard):
                    playResult.result.extend(autocard)
                    cardtype = PaodekuaiUtils.get_card_type(autocard)
                    if 0 == request.cardtype:
                        playResult.cardtype = cardtype
                    elif cardtype != PaodekuaiType.ZHADAN:
                        playResult.cardtype = request.cardtype
                    else:
                        playResult.cardtype = PaodekuaiType.ZHADAN
                return playResult
            else:
                my_card_type = PaodekuaiUtils.get_card_type(request.playcards)
                if my_card_type == PaodekuaiType.ERROR:
                    autocard = PaodekuaiUtils.auto_play(request.handcards, last_card_type, last_value,
                                                        len(request.lastcards))
                    if 0 != len(autocard):
                        playResult.result.extend(autocard)
                        cardtype = PaodekuaiUtils.get_card_type(autocard)
                        if 0 == request.cardtype:
                            playResult.cardtype = cardtype
                        elif cardtype != PaodekuaiType.ZHADAN:
                            playResult.cardtype = request.cardtype
                        else:
                            playResult.cardtype = PaodekuaiType.ZHADAN
                    return playResult
                if request.cardtype != my_card_type and 0 != request.cardtype:
                    if my_card_type == PaodekuaiType.SANLIAN and request.cardtype == PaodekuaiType.FEIJI:
                        my_card_type = PaodekuaiType.FEIJI
                if my_card_type == request.cardtype or 0 == request.cardtype:
                    if len(request.playcards) == len(request.lastcards):
                        my_value = PaodekuaiUtils.get_card_value(request.playcards, my_card_type)
                        if my_value <= last_value:
                            thislog.warn("出牌错误:值小于")
                            autocard = PaodekuaiUtils.auto_play(request.handcards, last_card_type, last_value,
                                                                len(request.lastcards))
                            if 0 != len(autocard):
                                playResult.result.extend(autocard)
                                cardtype = PaodekuaiUtils.get_card_type(autocard)
                                if 0 == request.cardtype:
                                    playResult.cardtype = cardtype
                                elif cardtype != PaodekuaiType.ZHADAN:
                                    playResult.cardtype = request.cardtype
                                else:
                                    playResult.cardtype = PaodekuaiType.ZHADAN
                            return playResult
                    else:
                        thislog.warn("出牌错误:张数不同")
                        autocard = PaodekuaiUtils.auto_play(request.handcards, last_card_type, last_value,
                                                            len(request.lastcards))
                        if 0 != len(autocard):
                            playResult.result.extend(autocard)
                            cardtype = PaodekuaiUtils.get_card_type(autocard)
                            if 0 == request.cardtype:
                                playResult.cardtype = cardtype
                            elif cardtype != PaodekuaiType.ZHADAN:
                                playResult.cardtype = request.cardtype
                            else:
                                playResult.cardtype = PaodekuaiType.ZHADAN
                        return playResult
                elif my_card_type != PaodekuaiType.ZHADAN:
                    thislog.warn("出牌错误:牌型不同并且不是炸弹")
                    autocard = PaodekuaiUtils.auto_play(request.handcards, last_card_type, last_value,
                                                        len(request.lastcards))
                    if 0 != len(autocard):
                        playResult.result.extend(autocard)
                        cardtype = PaodekuaiUtils.get_card_type(autocard)
                        if 0 == request.cardtype:
                            playResult.cardtype = cardtype
                        elif cardtype != PaodekuaiType.ZHADAN:
                            playResult.cardtype = request.cardtype
                        else:
                            playResult.cardtype = PaodekuaiType.ZHADAN
                    return playResult
                if my_card_type == PaodekuaiType.ZHADAN:
                    playResult.cardtype = PaodekuaiType.ZHADAN
        playResult.result.extend(request.playcards)
        return playResult

    def shuffle(self, request, context):
        """
        :洗牌
        :param request:
        :param context:
        :return:
        """
        shuffle = ShuffleResult()
        cardlist = list()
        cardlist.extend([102,
                         103,
                         104,
                         105,
                         106,
                         107,
                         108,
                         109,
                         110,
                         111,
                         112,
                         113,
                         114, 202
                            , 203
                            , 204
                            , 205
                            , 206
                            , 207
                            , 208
                            , 209
                            , 210
                            , 211
                            , 212
                            , 213
                            , 214
                            , 302, 402
                            , 303, 403
                            , 304, 404
                            , 305, 405
                            , 306, 406
                            , 307, 407
                            , 308, 408
                            , 309, 409
                            , 310, 410
                            , 311, 411
                            , 312, 412
                            , 313, 413
                            , 314, 414])
        #random.shuffle(cardlist)
        first = 0
        mincard = 415
        for i in range(0, request.count):
            for j in range(i * 13, (i + 1) * 13):
                if 402 < cardlist[j] < mincard:
                    first = i
                    mincard = cardlist[j]

        if 415 == mincard:
            mincard = 315
            for i in range(0, request.count):
                for j in range(i * 13, (i + 1) * 13):
                    if 402 == cardlist[j]:
                        shuffle.first = i
                        shuffle.min = 402
                        shuffle.cardlist.extend(cardlist)
                        return shuffle
                    if 302 < cardlist[j] < mincard:
                        first = i
                        mincard = cardlist[j]
        if mincard == 315:
            mincard = 215
            for i in range(0, request.count):
                for j in range(i * 13, (i + 1) * 13):
                    if 302 == cardlist[j]:
                        shuffle.first = i
                        shuffle.min = 302
                        shuffle.cardlist.extend(cardlist)
                        return shuffle
                    if 202 < cardlist[j] < mincard:
                        first = i
                        mincard = cardlist[j]

        shuffle.first = first
        shuffle.min = mincard
        shuffle.cardlist.extend(cardlist)
        return shuffle


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    thislog.info("started!")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    paodekuai_pb2_grpc.add_PaodekuaiServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50009')
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
        filename='../logs/paodekuai/paodekuai-%s.log' % time.strftime("%Y-%m-%d"), when="H", interval=1,
        backupCount=7)
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.DEBUG)
    thislog.addHandler(log_file_handler)

    rpc_server()
    thislog.removeHandler(log_file_handler)()

    # print(CardUtils.get_dui([206, 306, 107, 207, 307, 108, 208, 308, 110, 210]))

    # print PaodekuaiUtils.get_card_type([108, 208, 308, 105, 207], 2)
    # print PaodekuaiUtils.get_card_type([103, 203, 303,104, 204, 304, 105, 207,105, 207], 2)


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
