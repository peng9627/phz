# coding=utf-8
class Pibanban(object):
    """
    :劈板板
    """

    @staticmethod
    def get_card_value(cardlist):
        """
        :获取牌值
        :param cardlist:
        :return:
        """
        if cardlist[0] % 100 == cardlist[1] % 100:
            if cardlist[0] % 100 == 14:
                return 20
            else:
                return (cardlist[0] % 100) * 10
        value = 0
        if cardlist[0] % 100 == 14:
            value += 1
        else:
            value += cardlist[0]
        if cardlist[1] % 100 == 14:
            value += 1
        else:
            value += cardlist[1]
        return value % 10
