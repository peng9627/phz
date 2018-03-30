# coding=utf-8
class CardUtils(object):
    """
    :牌工具类
    """

    @staticmethod
    def get_dui(handlist):
        """
        :获取对子
        :param handlist:
        :return:
        """
        dui = set()
        temp = list()
        temp.extend(handlist)
        temp = sorted(temp)
        for i in range(0, len(temp) - 1):
            if temp[i] == temp[i + 1]:
                dui.add(temp[i])
                i += 1
        duilist = []
        duilist.extend(dui)
        return duilist

    @staticmethod
    def get_san(cards):
        """
        :获取三个
        :param cards:
        :return:
        """
        san = set()
        temp = list()
        temp.extend(cards)
        temp = sorted(temp)
        for i in range(0, len(temp) - 2):
            if temp[i] == temp[i + 2]:
                san.add(temp[i])
                i += 2
        sanlist = []
        sanlist.extend(san)
        return sanlist

    @staticmethod
    def get_si(handlist):
        """
        :获取四个
        :param handlist:
        :return:
        """
        si = set()
        temp = list()
        temp.extend(handlist)
        temp = sorted(temp)
        for i in range(0, len(temp) - 3):
            if temp[i] == temp[i + 3]:
                si.add(temp[i])
                i += 3
        silist = []
        silist.extend(si)
        return silist
