# coding=utf-8
from utils.mahjong_utils import MahjongUtils


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
        :param cardtype:
        """
        cardvalue = 0
        if 0 == cardtype:
            if cardlist[0] != 31:
                cardvalue += (MahjongUtils.get_card_value(cardlist[0])) * 2
            # TODO 江湖　揽胜 半点
            else:
                cardvalue += 1
            if cardlist[1] != 31:
                cardvalue += (MahjongUtils.get_card_value(cardlist[1])) * 2
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

    @staticmethod
    def compare(cardlist, cards):
        """
        :推筒子比牌
        :param cardlist:
        :param cards:
        """
        cardlist_type = Tuitongzi.getCardType(cardlist)
        cards_type = Tuitongzi.getCardType(cards)
        if cardlist_type > cards_type:
            return 1
        elif cardlist_type < cards_type:
            return -1
        else:
            cardlist_value = Tuitongzi.get_card_value(cardlist, cardlist_type)
            cards_value = Tuitongzi.get_card_value(cards, cards_type)
            if cardlist_value > cards_value:
                return 1
            elif cardlist_value < cards_value:
                return -1
            else:
                if (cardlist[0] > cards[0] and cardlist[0] > cards[1]) or (
                        cardlist[1] > cards[0] and cardlist[1] > cards[1]):
                    return 1
                elif (cards[0] > cardlist[0] and cards[0] > cardlist[1]) or (
                        cards[1] > cardlist[0] and cards[1] > cardlist[1]):
                    return -1
        return 0

    @staticmethod
    def get_multiple(cardtype, value):

        """
        :获取倍数
        :param value:牌值
        :param gamerules
        :return:
        """
        multiple = 1
        if 0 == cardtype:
            if value > 15:
                multiple = 2
            if value > 17:
                multiple = 3
        elif 1 == cardtype or 2 == cardtype:
            multiple = 4
        elif 3 == cardtype:
            multiple = 5
        return multiple
