# coding=utf-8
from utils.zhipai_card_utils import ZhipaiCardUtils


class Zhajinhua(object):
    """
    :扎金花
    """

    CARDTYPE_DANPAI = 0  # 单牌
    CARDTYPE_DUIZI = 1  # 对子
    CARDTYPE_SHUNZI = 2  # 顺子
    CARDTYPE_JINHUA = 3  # 金花
    CARDTYPE_SHUNJIN = 4  # 顺金
    CARDTYPE_BAOZI = 5  # 豹子

    @staticmethod
    def compare(cardlist, cards):
        """
        :炸金花比牌
        :param cardlist:
        :param cards:
        :return:
        """
        cardlist_type = Zhajinhua.getCardType(cardlist)
        cards_type = Zhajinhua.getCardType(cards)
        if cardlist_type != cards_type:
            return 1 if cardlist_type > cards_type else -1

        cardlist_value = Zhajinhua.getCardValue(cardlist, cardlist_type)
        cards_value = Zhajinhua.getCardValue(cards, cards_type)
        for i in range(0, len(cardlist_value) - 1, 1):
            if cardlist_value[i] > cards_value[i]:
                return 1
            elif cardlist_value[i] < cards_value[i]:
                return -1
        return 0

    @staticmethod
    def isSameThree(cardlist):
        """
        :豹子
        :param cardlist:
        """
        return ZhipaiCardUtils.get_card_value(cardlist[0]) == ZhipaiCardUtils.get_card_value(
            cardlist[1]) and ZhipaiCardUtils.get_card_value(cardlist[0]) == ZhipaiCardUtils.get_card_value(cardlist[2])

    @staticmethod
    def isSameColor(cardlist):
        """
        :金花
        :param cardlist:
        """
        return ZhipaiCardUtils.get_card_color(cardlist[0]) == ZhipaiCardUtils.get_card_color(
            cardlist[1]) and ZhipaiCardUtils.get_card_color(cardlist[0]) == ZhipaiCardUtils.get_card_color(cardlist[2])

    @staticmethod
    def isStraight(cardlist):
        """
        :顺子
        :param cardlist:
        """
        values = [ZhipaiCardUtils.get_card_value(cardlist[0]), ZhipaiCardUtils.get_card_value(cardlist[1]),
                  ZhipaiCardUtils.get_card_value(cardlist[2])]
        values = sorted(values)
        if values[0] == 2 and values[1] == 3 and values[2] == 14:
            return True
        return values[0] == values[1] - 1 and values[1] == values[2] - 1

    @staticmethod
    def isDouble(cardlist):
        """
        :对子
        :param cardlist:
        """
        return ZhipaiCardUtils.get_card_value(cardlist[0]) == ZhipaiCardUtils.get_card_value(
            cardlist[1]) or ZhipaiCardUtils.get_card_value(cardlist[0]) == ZhipaiCardUtils.get_card_value(
            cardlist[2]) or (
                       ZhipaiCardUtils.get_card_value(cardlist[1]) == ZhipaiCardUtils.get_card_value(cardlist[2])
               )

    @staticmethod
    def getCardType(cardlist):
        """
        :金花牌型 0单牌 1对子 2顺子 3金花 4顺金 5豹子
        :拖拉机牌型 0单牌 1对子 2金花 3顺子 4顺金 5豹子
        :param cardlist:
        """
        if Zhajinhua.isSameThree(cardlist):
            return Zhajinhua.CARDTYPE_BAOZI
        if Zhajinhua.isSameColor(cardlist) and Zhajinhua.isStraight(cardlist):
            return Zhajinhua.CARDTYPE_SHUNJIN
        if Zhajinhua.isSameColor(cardlist):
            return Zhajinhua.CARDTYPE_JINHUA
        if Zhajinhua.isStraight(cardlist):
            return Zhajinhua.CARDTYPE_SHUNZI
        if Zhajinhua.isDouble(cardlist):
            return Zhajinhua.CARDTYPE_DUIZI
        return Zhajinhua.CARDTYPE_DANPAI

    @staticmethod
    def getCardValue(cardlist, cardtype):
        """
        :param cardlist:
        :param cardtype:
        """
        cardlist_values = list()
        for card in cardlist:
            cardlist_values.append(ZhipaiCardUtils.get_card_value(card))
        cardlist_values = sorted(cardlist_values)
        if cardtype == Zhajinhua.CARDTYPE_SHUNJIN or cardtype == Zhajinhua.CARDTYPE_SHUNZI:
            if cardlist_values[0] == 2 and cardlist_values[2] == 14:
                return [3]
            else:
                return cardlist_values[3]
        elif cardtype == Zhajinhua.CARDTYPE_DUIZI:
            if cardlist_values[0] == cardlist_values[1]:
                return [cardlist_values[0], cardlist_values[2]]
            else:
                return [cardlist_values[2], cardlist_values[0]]
        else:
            return [cardlist_values[2], cardlist_values[1], cardlist_values[0]]
