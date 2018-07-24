# coding=utf-8
class ZhipaiCardUtils(object):
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
        return card % 100

    @staticmethod
    def get_card_color(card):
        """
        获取牌花色
        :param card:
        :return:
        """
        return card / 100

    @staticmethod
    def reversed_cmp(x, y):
        """
        :纸牌排序方法
        :param x:
        :param y:
        :return:
        """
        if ZhipaiCardUtils.get_card_value(x) > ZhipaiCardUtils.get_card_value(y):
            return 1
        if ZhipaiCardUtils.get_card_value(x) < ZhipaiCardUtils.get_card_value(y):
            return -1
        if x > y:
            return 1
        if x < y:
            return -1
        return 0
