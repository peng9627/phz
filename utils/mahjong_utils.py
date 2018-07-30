# coding=utf-8
class MahjongUtils(object):
    """
    :纸牌工具类
    """

    @staticmethod
    def get_card_value(card):
        """
        获取牌值
        :param card:
        :return:
        """
        return card % 10

    @staticmethod
    def get_card_color(card):
        """
        获取牌花色
        :param card:
        :return:
        """
        return card / 10
