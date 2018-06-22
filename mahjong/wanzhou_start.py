# coding=utf-8
import datetime
import logging
import random
import re
import time
from logging.handlers import TimedRotatingFileHandler

import grpc
from concurrent import futures

import mahjong_pb2_grpc
import wanzhou_mahjong
from mahjong_pb2 import *
from mahjong_utils import MahjongUtils
from utils.card_utils import CardUtils

logging.basicConfig(level=logging.INFO)
thislog = logging.getLogger()


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
        cannothu_user = []
        for user in request.player:
            user_settle = settle.userSettleResule.add()
            user_settle.userId = user.player_id
            user_settles.setdefault(user.player_id, user_settle)
            users.setdefault(user.player_id, user)
            cannothu_user.append(user.player_id)

        for user in request.player:
            for g in user.gang:
                user_settles[user.player_id].gangScore += g.gangscore * len(g.fighter)
                for f in g.fighter:
                    user_settles[f].gangScore -= g.gangscore
        for hudata in request.hudata:
            if hudata.huUser in cannothu_user:
                cannothu_user.remove(hudata.huUser)
            tempcard = list()
            tempcard.extend(users[hudata.huUser].handlist)
            tempcard.append(hudata.majong)
            cardtype = wanzhou_mahjong.getCardType(tempcard, users[hudata.huUser].peng,
                                                   users[hudata.huUser].gang, request.rogue)
            score = wanzhou_mahjong.getScore(cardtype)
            if request.rogue != 0 and 21 in CardUtils.get_si(tempcard):
                cardtype = 25
                score = request.fengding
            for s in hudata.settle:
                if s != 0:
                    if 1 == score:
                        score = 12
                    else:
                        score *= 2
            if request.yinghu and request.rogue != 0:
                allcard = list()
                allcard.extend(users[hudata.huUser].handlist)
                allcard.extend(users[hudata.huUser].peng)
                allcard.append(hudata.majong)
                for gang in users[hudata.huUser].gang:
                    allcard.append(gang.gangvalue)
                if 21 not in allcard:
                    if 1 == score:
                        score = 12
                    else:
                        score *= 2
                    user_settles[hudata.huUser].settlePatterns.append(26)
            if 0 in hudata.settle and score == 1:
                score += 1
            if score > request.fengding:
                score = request.fengding
            if cardtype not in user_settles[hudata.huUser].settlePatterns:
                user_settles[hudata.huUser].settlePatterns.append(cardtype)
            for set in hudata.settle:
                if set not in user_settles[hudata.huUser].settlePatterns:
                    user_settles[hudata.huUser].settlePatterns.append(set)
            for u in hudata.loseUsers:
                user_settles[u].cardScore -= score
                user_settles[hudata.huUser].cardScore += score
        if request.peijiao:
            peijiao_users = list()
            user_score = {}
            if 1 < len(cannothu_user):
                for c in cannothu_user:
                    hucards = MahjongUtils.get_hu(users[c].handlist, request.rogue)
                    # 有叫
                    if 0 < len(hucards):
                        score = 0
                        for h in hucards:
                            tempcard = list()
                            tempcard.extend(users[c].handlist)
                            tempcard.append(h)
                            cardtype = wanzhou_mahjong.getCardType(tempcard, users[c].peng, users[c].gang,
                                                                   request.rogue)
                            cardscore = wanzhou_mahjong.getScore(cardtype)
                            if request.rogue != 0 and 21 in CardUtils.get_si(tempcard):
                                cardtype = 25
                                cardscore = request.fengding
                            if 1 == cardscore:
                                cardscore = 12
                            else:
                                cardscore *= 2
                            if request.yinghu and request.rogue != 0:
                                allcard = list()
                                allcard.extend(users[c].handlist)
                                allcard.extend(users[c].peng)
                                allcard.append(h)
                                for gang in users[c].gang:
                                    allcard.append(gang.gangvalue)
                                if 21 not in allcard:
                                    if 1 == cardscore:
                                        cardscore = 12
                                    else:
                                        cardscore *= 2
                            if cardscore > score:
                                score = cardscore
                            if score > request.fengding:
                                score = request.fengding
                        if score > 0:
                            user_score.setdefault(c, score)
                    else:
                        peijiao_users.append(c)
                if 0 < len(user_score) and 0 < len(peijiao_users):
                    for key, value in user_score.items():
                        for p in peijiao_users:
                            user_settles[p].cardScore -= value
                            user_settles[key].cardScore += value
        for sett in settle.userSettleResule:
            logging.info("userid")
            logging.info(sett.userId)
            logging.info("cardScore")
            logging.info(sett.cardScore)
            logging.info("gangScore")
            logging.info(sett.gangScore)
            logging.info("settlePatterns")
            logging.info(sett.settlePatterns)
        return settle

    def calculate(self, request, context):
        """
        :计算
        :param request:
        :param context:
        :return:
        """
        calculate = CalculateResult()
        san = MahjongUtils.get_san(request.player.handlist)
        if not request.player.baojiao:
            calculate.dui.extend(MahjongUtils.get_dui(request.player.handlist))
            calculate.san.extend(san)
            calculate.si.extend(MahjongUtils.get_si(request.player.handlist))
        else:
            gang = list()
            for s in san:
                temp = list()
                temp.extend(request.player.handlist)
                temp.remove(s)
                temp.remove(s)
                temp.remove(s)
                if 0 < len(MahjongUtils.get_hu(temp, 0)):
                    gang.append(s)
                temp.append(s)
                temp.append(s)
                temp.append(s)
            calculate.san.extend(gang)
        zimo = MahjongUtils.get_hu(request.player.handlist, request.rogue)
        calculate.zimo.extend(zimo)
        hu = list()
        if -1 in zimo:
            for z in [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28,
                      29]:
                handlist = list()
                handlist.extend(request.player.handlist)
                handlist.append(z)
                if 10 != wanzhou_mahjong.getCardType(handlist, request.player.peng, request.player.gang, request.rogue):
                    hu.append(z)
        else:
            for z in zimo:
                handlist = list()
                handlist.extend(request.player.handlist)
                handlist.append(z)
                if 10 != wanzhou_mahjong.getCardType(handlist, request.player.peng, request.player.gang, request.rogue):
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
        random.shuffle(cardlist)
        shuffle.cardlist.extend(cardlist)
        return shuffle

    def baojiaoGang(self, request, context):
        """
        :报叫杠
        :param request:
        :param context:
        :return:
        """
        gangs = Cards()
        # 暗杠 扒杠
        if len(request.player.handlist) % 3 == 2:
            temp = list()
            temp.extend(request.player.handlist)
            temp.remove(temp[len(temp) - 1])
            beforeHu = MahjongUtils.get_hu(temp, 0)
            si = MahjongUtils.get_si(request.player.handlist)
            for s in si:
                temp = list()
                temp.extend(request.player.handlist)
                temp.remove(s)
                temp.remove(s)
                temp.remove(s)
                temp.remove(s)
                afterHu = MahjongUtils.get_hu(temp, 0)
                if 0 == len(beforeHu - afterHu) and 0 == len(afterHu - beforeHu):
                    gangs.cards.append(s)
            for p in request.player.peng:
                temp = list()
                temp.extend(request.player.handlist)
                if p in temp:
                    temp.remove(p)
                    afterHu = MahjongUtils.get_hu(temp, 0)
                    if 0 == len(beforeHu - afterHu) and 0 == len(afterHu - beforeHu):
                        gangs.cards.append(p)
        else:  # 点杠
            temp = list()
            temp.extend(request.player.handlist)
            beforeHu = MahjongUtils.get_hu(temp, 0)
            san = MahjongUtils.get_san(request.player.handlist)
            for s in san:
                temp = list()
                temp.extend(request.player.handlist)
                temp.remove(s)
                temp.remove(s)
                temp.remove(s)
                afterHu = MahjongUtils.get_hu(temp, 0)
                if 0 == len(beforeHu - afterHu) and 0 == len(afterHu - beforeHu):
                    gangs.cards.append(s)
        return gangs


def rpc_server():
    """
    :启动grpc服务
    :return:
    """
    thislog.info("started!")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    mahjong_pb2_grpc.add_MajongCalculateServicer_to_server(Performance(), server)
    server.add_insecure_port('[::]:50008')
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
        filename='../logs/mahjong/mahjong.log', when="H", interval=1,
        backupCount=50)
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.DEBUG)
    thislog.addHandler(log_file_handler)

    rpc_server()
    thislog.removeHandler(log_file_handler)()
    # print wanzhou_mahjong.getCardType([1,1,1,1,22,22,22,22,3,3,4,4,5,5],[],[],21)
    # t = CardUtils.get_si([21, 21, 21, 21, 12, 12, 15, 15, 16, 16, 16])
    # score = wanzhou_mahjong.getScore(cardtype)
    # print(cardtype)
    # print(score)
    # print MahjongUtils.get_hu([4, 4, 6, 6, 11, 11, 15, 15, 16, 16, 24, 24, 21], 21)


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
