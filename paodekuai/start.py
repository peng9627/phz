# -*- encoding=utf-8 -*-
import datetime
import logging
import random
import time

import grpc
from concurrent import futures

import paodekuai_pb2_grpc
from common import PaodekuaiType
from paodekuai_pb2 import *
from paodekuai_utils import PaodekuaiUtils

thislog = logging


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

        last_card_type = PaodekuaiUtils.get_card_type(request.lastcards, request.count)
        last_value = PaodekuaiUtils.get_card_value(request.lastcards, last_card_type)

        # 上家没出牌
        if 0 == len(request.lastcards):
            if 0 == len(request.playcards):
                playResult.cardtype = PaodekuaiType.DANPAI
                playResult.result.append(request.handcards[0])
                return playResult
            else:
                my_card_type = PaodekuaiUtils.get_card_type(request.playcards, request.count)
                if my_card_type == PaodekuaiType.ERROR:
                    playResult.cardtype = PaodekuaiType.DANPAI
                    playResult.result.append(request.handcards[0])
                    return playResult
                playResult.cardtype = my_card_type
        else:
            # 不出
            if 0 == len(request.playcards):
                autocard = PaodekuaiUtils.auto_play(request.handcards, last_card_type, last_value,
                                                    len(request.lastcards), request.count)
                if 0 != len(autocard):
                    playResult.result.extend(autocard)
                    cardtype = PaodekuaiUtils.get_card_type(autocard, request.count)
                    if 0 == request.cardtype:
                        playResult.cardtype = cardtype
                    elif cardtype != PaodekuaiType.ZHADAN:
                        playResult.cardtype = request.cardtype
                    else:
                        playResult.cardtype = PaodekuaiType.ZHADAN
                return playResult
            else:
                my_card_type = PaodekuaiUtils.get_card_type(request.playcards, request.count)
                if my_card_type == PaodekuaiType.ERROR:
                    autocard = PaodekuaiUtils.auto_play(request.handcards, last_card_type, last_value,
                                                        len(request.lastcards), request.count)
                    if 0 != len(autocard):
                        playResult.result.extend(autocard)
                        cardtype = PaodekuaiUtils.get_card_type(autocard, request.count)
                        if 0 == request.cardtype:
                            playResult.cardtype = cardtype
                        elif cardtype != PaodekuaiType.ZHADAN:
                            playResult.cardtype = request.cardtype
                        else:
                            playResult.cardtype = PaodekuaiType.ZHADAN
                    return playResult
                if request.cardtype != my_card_type and 0 != request.cardtype:
                    if my_card_type == PaodekuaiType.SIZHANG and request.cardtype == PaodekuaiType.SANZHANG:
                        my_card_type = PaodekuaiType.SANZHANG
                    elif my_card_type == PaodekuaiType.SANLIAN and request.cardtype == PaodekuaiType.FEIJI:
                        my_card_type = PaodekuaiType.FEIJI
                if my_card_type == request.cardtype or 0 == request.cardtype:
                    if len(request.playcards) == len(request.lastcards):
                        my_value = PaodekuaiUtils.get_card_value(request.playcards, my_card_type)
                        if my_value <= last_value:
                            thislog.warn("出牌错误:值小于")
                            autocard = PaodekuaiUtils.auto_play(request.handcards, last_card_type, last_value,
                                                                len(request.lastcards), request.count)
                            if 0 != len(autocard):
                                playResult.result.extend(autocard)
                                cardtype = PaodekuaiUtils.get_card_type(autocard, request.count)
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
                                                            len(request.lastcards), request.count)
                        if 0 != len(autocard):
                            playResult.result.extend(autocard)
                            cardtype = PaodekuaiUtils.get_card_type(autocard, request.count)
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
                                                        len(request.lastcards), request.count)
                    if 0 != len(autocard):
                        playResult.result.extend(autocard)
                        cardtype = PaodekuaiUtils.get_card_type(autocard, request.count)
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
        #random.shuffle(cardlist)

        first = 0
        mincard = 415
        # 三人16张
        if 3 == request.count:
            cardlist.remove(102)
            cardlist.remove(202)
            cardlist.remove(302)
            cardlist.remove(414)
            for i in range(0, 3):
                for j in range(i * 16, (i + 1) * 16):
                    if 402 < cardlist[j] < mincard:
                        first = i
                        mincard = cardlist[j]
        else:
            for i in range(0, 4):
                for j in range(i * 13, (i + 1) * 13):
                    if 402 < cardlist[j] < mincard:
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
    server.add_insecure_port('[::]:50003')
    server.start()
    try:
        while True:
            time.sleep(60 * 60)
            thislog.root.handlers = []
            thislog.basicConfig(level=thislog.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt=None,
                                filename='../logs/paodekuai-%s.log' % time.strftime("%Y-%m-%d %H"),
                                filemode='w')
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    thislog.basicConfig(level=thislog.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt=None,
                        filename='../logs/paodekuai-%s.log' % time.strftime("%Y-%m-%d_%H"),
                        filemode='w')
    rpc_server()
    # print PaodekuaiUtils.get_card_type([406, 107, 108, 208, 308, 109, 209, 309], 3)


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
