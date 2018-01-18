# coding=utf-8
class Zhajinhua(object):
    """
    :扎金花
    """

    @staticmethod
    def reversed_cmp(x, y):
        """
        :牛牛排序方法
        :param x:
        :param y:
        :return:
        """
        if x % 100 > y % 100:
            return 1
        if x % 100 < y % 100:
            return -1
        if x > y:
            return 1
        if x < y:
            return -1
        return 0

    @staticmethod
    def compare(cardlist, cards, isTuolaji):
        """
        :炸金花比牌
        :param cardlist:
        :param cards:
        :return:
        """
        cardlist_type = Zhajinhua.getCardType(cardlist, isTuolaji)
        cards_type = Zhajinhua.getCardType(cards, isTuolaji)
        if cardlist_type != cards_type:
            return cardlist_type > cards_type
        cardlist_values = [cardlist[0] % 100, cardlist[1] % 100, cardlist[2] % 100]
        cardlist_values = sorted(cardlist_values)
        cards_values = [cards[0] % 100, cards[1] % 100, cards[2] % 100]
        cards_values = sorted(cards_values)
        if cardlist_type == 1:
            if cardlist_values[1] != cards_values[1]:
                return 1 if cardlist_values[1] > cards_values[1] else -1
            if cardlist_values[0] != cardlist_values[1]:
                cardlist_value = cardlist_values[0]
            else:
                cardlist_value = cardlist_values[2]
            if cards_values[0] != cards_values[1]:
                cards_value = cards_values[0]
            else:
                cards_value = cards_values[2]
            if cardlist_value == cards_value:
                return 0
            return 1 if cardlist_value > cards_value else -1
        if cardlist_type == 2 or cardlist_type == 4:
            list123 = False
            card123 = False
            if cardlist_values[0] == 2 and cardlist_values[2] == 14:
                list123 = True
            if cards_values[0] == 2 and cards_values[2] == 14:
                card123 = True
            if list123 and card123:
                return 0
            elif list123 and not card123:
                return -1
            elif not list123 and card123:
                return 1
        for i in range(2, -1, -1):
            if cardlist_values[i] != cards_values[i]:
                return 1 if cardlist_values[i] > cards_values[i] else -1
        return 0

    @staticmethod
    def isSameThree(cardlist):
        """
        :豹子
        :param cardlist:
        """
        return cardlist[0] % 100 == cardlist[1] % 100 and cardlist[0] % 100 == cardlist[2] % 100

    @staticmethod
    def isSameColor(cardlist):
        """
        :金花
        :param cardlist:
        """
        return cardlist[0] / 100 == cardlist[1] / 100 and cardlist[0] / 100 == cardlist[2] / 100

    @staticmethod
    def isStraight(cardlist):
        """
        :顺子
        :param cardlist:
        """
        values = [cardlist[0] % 100, cardlist[1] % 100, cardlist[2] % 100]
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
        return cardlist[0] % 100 == cardlist[1] % 100 or cardlist[0] % 100 == cardlist[2] % 100 or (
                cardlist[1] % 100 == cardlist[2] % 100
        )

    @staticmethod
    def getCardType(cardlist, isTuolaji):
        """
        :金花牌型 0单牌 1对子 2顺子 3金花 4顺金 5豹子
        :拖拉机牌型 0单牌 1对子 2金花 3顺子 4顺金 5豹子
        :param cardlist:
        :param isTuolaji:
        """
        if Zhajinhua.isSameThree(cardlist):
            return 5
        if Zhajinhua.isSameColor(cardlist) and Zhajinhua.isStraight(cardlist):
            return 4
        if (not isTuolaji and Zhajinhua.isSameColor(cardlist)) or (isTuolaji and Zhajinhua.isStraight(cardlist)):
            return 3
        if (isTuolaji and Zhajinhua.isSameColor(cardlist)) or (not isTuolaji and Zhajinhua.isStraight(cardlist)):
            return 2
        if Zhajinhua.isDouble(cardlist):
            return 1
        return 0
