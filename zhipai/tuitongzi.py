# coding=utf-8
class Tuitongzi(object):
    """
    :推筒子
    :param cardlist:
    """

    @staticmethod
    def get_card_value(cardlist, cardtype):
        """
        :推筒子牌值
        :param cardlist:
        """
        cardvalue = 0
        if 0 == cardtype:
            if cardlist[0] != 31:
                cardvalue += (cardlist[0] % 10) * 2
            else:
                cardvalue += 1
            if cardlist[1] != 31:
                cardvalue += (cardlist[1] % 10) * 2
            else:
                cardvalue += 1
            while cardvalue >= 20:
                cardvalue -= 20
            return cardvalue
        elif 1 == cardtype:
            return cardlist[0]
        else:
            return 0

    @staticmethod
    def getCardType(cardlist):
        """
        :推筒子牌型 0 单牌 1 豹子 2 二八杠 3 对红中
        :param cardlist:
        """
        if cardlist[0] == 31 and cardlist[1] == 31:
            return 3
        if (cardlist[0] == 12 and cardlist[1] == 18) or (cardlist[0] == 18 and cardlist[1] == 12):
            return 2
        if cardlist[0] == cardlist[1]:
            return 1
        return 0
