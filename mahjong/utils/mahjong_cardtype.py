# coding=utf-8
from mahjong.utils.mahjong_utils import MahjongUtils


class MahjongCardType(object):
    """
    :麻将算法
    """

    @staticmethod
    def same_color(allcards, rogue):
        """
        :清一色
        :param allcards:
        :return:
        """
        temp = list()
        temp.extend(allcards)
        rogueSize = MahjongUtils.containSize(allcards, rogue)
        for i in range(0, rogueSize):
            temp.remove(rogue)
        return temp[0] / 10 == temp[len(temp) - 1] / 10

    @staticmethod
    def gold_hook(handlist):
        """
        :金钩钓
        :param handlist:
        :return:
        """
        return 2 == len(handlist)

    @staticmethod
    def san_da(handlist, rogue):
        """
        :三搭
        :param handlist:
        :param rogue:
        :return:
        """
        return 5 == len(handlist) and MahjongCardType.big_double(handlist, rogue)

    @staticmethod
    def big_double(handlist, rogue):
        """
        :大对
        :param handlist:
        :param rogue:
        :return:
        """
        temp = list()
        temp.extend(handlist)
        san = MahjongUtils.get_san(temp)
        for i in range(0, 3):
            for s in san:
                temp.remove(s)
        rogueSize = MahjongUtils.containSize(handlist, rogue)
        if 0 == rogueSize and 2 == len(temp) and temp[0] == temp[1]:
            return True
        if rogue not in san:
            for i in range(0, rogueSize):
                temp.remove(rogue)
        if rogue in temp:
            temp.remove(rogue)
        dui = MahjongUtils.get_dui(temp)
        if 1 == rogueSize and ((2 == len(dui) and 4 == len(temp)) or 1 == len(temp)):
            return True
        if 2 == rogueSize and ((1 == len(dui) and 3 == len(temp)) or 0 == len(temp)):
            return True
        if 3 == rogueSize and ((4 == len(dui) and 8 == len(temp)) or (
                        2 == len(dui) and 5 == len(temp)) or 2 == len(temp)):
            return True
        if 4 == rogueSize and ((5 == len(dui) and 10 == len(temp)) or (3 == len(dui) and 7 == len(temp)) or (
                        0 < len(dui) and 4 == len(temp)) or 1 == len(temp)):
            return True

        return False

    @staticmethod
    def double7(handlist, rogue):
        """
        :七对
        :param handlist:
        :param rogue:
        :return:
        """
        temp = list()
        temp.extend(handlist)
        rogueSize = MahjongUtils.containSize(handlist, rogue)
        for i in range(0, rogueSize):
            temp.remove(rogue)
        si = MahjongUtils.get_si(temp)
        if 14 == len(handlist) and 14 - (2 * (len(MahjongUtils.get_dui(temp)) + len(si))) <= 2 * rogueSize:
            siCount = 0
            temp1 = list()
            temp1.extend(temp)
            for i in range(0, 4):
                for s in si:
                    temp1.remove(s)
            siCount += len(si)
            san = MahjongUtils.get_san(temp1)
            for i in range(0, 3):
                for s in san:
                    temp1.remove(s)
            siCount += len(san)
            rogueSize -= len(san)
            dui = MahjongUtils.get_dui(temp1)
            for i in range(0, 2):
                for s in dui:
                    temp1.remove(s)
            rogueSize -= len(dui)
            siCount += len(dui)
            return siCount
        return -1
