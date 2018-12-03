# coding=utf-8
from utils.zhipai_card_utils import ZhipaiCardUtils


class Niuniu(object):
    """
    :牛牛
    """

    # 五小牛
    @staticmethod
    def isWuxiaoniu(cardlist):
        """
        : 无小牛
        :param cardlist:
        :return:
        """
        return ZhipaiCardUtils.get_card_value(cardlist[4]) < 6 and ZhipaiCardUtils.get_card_value(sum(cardlist)) < 11

    # 炸弹牛
    @staticmethod
    def isZhadanniu(cardlist):
        """
        : 炸弹牛
        :param cardlist:
        :return:
        """
        return (ZhipaiCardUtils.get_card_value(cardlist[0]) == ZhipaiCardUtils.get_card_value(cardlist[3])
                or ZhipaiCardUtils.get_card_value(cardlist[1]) == ZhipaiCardUtils.get_card_value(cardlist[4]))

    # 五花牛
    @staticmethod
    def isWuhuaniu(cardlist):
        """
        : 五花牛
        :param cardlist:
        :return:
        """
        return ZhipaiCardUtils.get_card_value(cardlist[0]) > 10 and ZhipaiCardUtils.get_card_value(cardlist[0]) != 14

    # 葫芦牛
    @staticmethod
    def isHuluniu(cardlist):
        """
        : 葫芦牛
        :param cardlist:
        :return:
        """
        return ((ZhipaiCardUtils.get_card_value(cardlist[0]) == ZhipaiCardUtils.get_card_value(cardlist[1])
                 and ZhipaiCardUtils.get_card_value(cardlist[2]) == ZhipaiCardUtils.get_card_value(cardlist[4]))
                or (ZhipaiCardUtils.get_card_value(cardlist[0]) == ZhipaiCardUtils.get_card_value(cardlist[2])
                    and ZhipaiCardUtils.get_card_value(cardlist[3]) == ZhipaiCardUtils.get_card_value(cardlist[4])))

    # 顺子牛
    @staticmethod
    def isShunziniu(cardlist):
        """
        : 顺子牛
        :param cardlist:
        :return:
        """
        return (ZhipaiCardUtils.get_card_value(cardlist[0]) == (ZhipaiCardUtils.get_card_value(cardlist[1])) - 1
                or ZhipaiCardUtils.get_card_value(cardlist[0]) == (ZhipaiCardUtils.get_card_value(cardlist[1])) - 9) and \
               ZhipaiCardUtils.get_card_value(cardlist[1]) == (ZhipaiCardUtils.get_card_value(cardlist[2])) - 1 and \
               ZhipaiCardUtils.get_card_value(cardlist[2]) == (
                   ZhipaiCardUtils.get_card_value(cardlist[3])) - 1 and ZhipaiCardUtils.get_card_value(cardlist[3]) == (
                   ZhipaiCardUtils.get_card_value(cardlist[4])) - 1

    # 同花牛
    @staticmethod
    def sameColor(cardlist):
        """
        : 同花牛
        :param cardlist:
        :return:
        """
        sameColorTemp = list()
        sameColorTemp.extend(cardlist)
        sameColorTemp = sorted(sameColorTemp)
        return ZhipaiCardUtils.get_card_color(sameColorTemp[0]) == ZhipaiCardUtils.get_card_color(sameColorTemp[4])

    # 顺斗
    @staticmethod
    def getShunDouValue(cardlist):
        """
        : 顺斗
        :param cardlist:
        :return:
        """
        shunvalue = 0
        shundoutemp = list()
        for c in cardlist:
            if ZhipaiCardUtils.get_card_value(c) == 14:
                shundoutemp.append(ZhipaiCardUtils.get_card_value(c - 13))
            else:
                shundoutemp.append(ZhipaiCardUtils.get_card_value(c))
        shundoutemp = sorted(shundoutemp, cmp=Niuniu.reversed_cmp)

        for i in range(0, 3):
            if shundoutemp[i] + 1 in shundoutemp and shundoutemp[i] + 2 in shundoutemp:
                shundouvtemp = list()
                shundouvtemp.extend(shundoutemp)
                shundouvtemp.remove(shundoutemp[i])
                shundouvtemp.remove(shundoutemp[i] + 1)
                shundouvtemp.remove(shundoutemp[i] + 2)
                value1 = 10 if shundouvtemp[0] > 10 else shundouvtemp[0]
                value2 = 10 if shundouvtemp[1] > 10 else shundouvtemp[1]
                tempvalue = value1 + value2
                if tempvalue > 10:
                    tempvalue -= 10
                if tempvalue > shunvalue:
                    shunvalue = tempvalue
        shundouvtemp = list()
        shundouvtemp.extend(shundoutemp)
        if 1 in shundouvtemp and 12 in shundouvtemp and 13 in shundouvtemp:
            shundouvtemp = list()
            shundouvtemp.extend(shundoutemp)
            shundouvtemp.remove(1)
            shundouvtemp.remove(12)
            shundouvtemp.remove(13)
            value1 = 10 if shundouvtemp[0] > 10 else shundouvtemp[0]
            value2 = 10 if shundouvtemp[1] > 10 else shundouvtemp[1]
            tempvalue = value1 + value2
            if tempvalue > 10:
                tempvalue -= 10
            if tempvalue > shunvalue:
                shunvalue = tempvalue
        return shunvalue

    @staticmethod
    def reversed_cmp(x, y):
        """
        :牛牛排序方法
        :param x:
        :param y:
        :return:
        """
        if ZhipaiCardUtils.get_card_value(x) == 14:
            x1 = x - 13
        else:
            x1 = x
        if ZhipaiCardUtils.get_card_value(y) == 14:
            y1 = y - 13
        else:
            y1 = y
        if ZhipaiCardUtils.get_card_value(x1) > ZhipaiCardUtils.get_card_value(y1):
            return 1
        if ZhipaiCardUtils.get_card_value(x1) < ZhipaiCardUtils.get_card_value(y1):
            return -1
        if x > y:
            return 1
        if x < y:
            return -1
        return 0

    @staticmethod
    def compare(cardlist, cards, gamerules):
        """
        :斗牛牛比牌
        :param cardlist:
        :param cards:
        :param gamerules:
        :return:
        """
        banker_value = Niuniu.get_card_value(cardlist, gamerules)
        banker_array_cards = sorted(cardlist, cmp=Niuniu.reversed_cmp)
        user_value = Niuniu.get_card_value(cards, gamerules)
        if user_value < banker_value:
            return 1
        elif user_value > banker_value:
            return -1
        else:
            user_array_cards = sorted(cards, cmp=Niuniu.reversed_cmp)
            if ZhipaiCardUtils.get_card_value(banker_array_cards[4]) > ZhipaiCardUtils.get_card_value(
                    user_array_cards[4]):
                return 1
            elif ZhipaiCardUtils.get_card_value(banker_array_cards[4]) < ZhipaiCardUtils.get_card_value(
                    user_array_cards[4]):
                return -1
            elif banker_array_cards[4] > user_array_cards[4]:
                return 1
            else:
                return -1

    @staticmethod
    def get_card_value(cardlist, gamerules):
        """
        :获取牌值
        :param cardlist:牌
        :param gamerules:
        :return:
        """
        sum_val = 0
        temp = list()
        for c in cardlist:
            if ZhipaiCardUtils.get_card_value(c) == 14:
                temp.append(c - 13)
                sum_val += 1
            else:
                temp.append(c)
                sum_val += 0 if ZhipaiCardUtils.get_card_value(c) > 10 else c
        temp = sorted(temp, cmp=Niuniu.reversed_cmp)

        # 心悦
        if (gamerules >> 3) % 2 == 1:
            # 同花顺
            if Niuniu.sameColor(temp) and Niuniu.isShunziniu(temp):
                return 17
            # 五小牛
            if Niuniu.isWuxiaoniu(temp):
                return 16
            # 炸弹牛
            if Niuniu.isZhadanniu(temp):
                return 15
            # 葫芦牛
            if Niuniu.isHuluniu(temp):
                return 14
            # 同花牛
            if Niuniu.sameColor(temp):
                return 13
            # 顺子牛
            if Niuniu.isShunziniu(temp):
                return 12
            # 五花牛
            if Niuniu.isWuhuaniu(temp):
                return 11
        else:
            # 五小牛
            if Niuniu.isWuxiaoniu(temp):
                return 16
            # 炸弹牛
            if Niuniu.isZhadanniu(temp):
                return 15
            # 五花牛
            if Niuniu.isWuhuaniu(temp):
                return 11
        val1 = 0
        for i in range(0, 4):
            for j in range(i + 1, 5):
                temp1 = 0 if ZhipaiCardUtils.get_card_value(temp[i]) > 10 else ZhipaiCardUtils.get_card_value(temp[i])
                temp2 = 0 if ZhipaiCardUtils.get_card_value(temp[j]) > 10 else ZhipaiCardUtils.get_card_value(temp[j])
                if (temp1 + temp2) % 10 == sum_val % 10:
                    val1 = (10 if sum_val % 10 == 0 else sum_val % 10)
        # 坎顺斗
        valuetemp = list()
        for t in temp:
            valuetemp.append(
                10 if (ZhipaiCardUtils.get_card_value(t)) > 10 else (ZhipaiCardUtils.get_card_value(t)))
        if gamerules % 2 == 1:
            shunvalue = Niuniu.getShunDouValue(cardlist)
            if val1 < shunvalue:
                val1 = shunvalue
            tempval = valuetemp[3] + valuetemp[4]
            if tempval % 10 == 0:
                tempval = 10
            else:
                tempval %= 10
            if ZhipaiCardUtils.get_card_value(temp[0]) == ZhipaiCardUtils.get_card_value(temp[2]) and tempval > val1:
                val1 = tempval
            tempval = valuetemp[0] + valuetemp[4]
            if tempval % 10 == 0:
                tempval = 10
            else:
                tempval %= 10
            if ZhipaiCardUtils.get_card_value(temp[1]) == ZhipaiCardUtils.get_card_value(temp[3]) and tempval > val1:
                val1 = tempval
            tempval = valuetemp[0] + valuetemp[1]
            if tempval % 10 == 0:
                tempval = 10
            else:
                tempval %= 10
            if ZhipaiCardUtils.get_card_value(temp[2]) == ZhipaiCardUtils.get_card_value(temp[4]) and tempval > val1:
                val1 = tempval
        return val1

    @staticmethod
    def get_multiple(value, gamerules):
        """
        :获取倍数
        :param value:牌值
        :param gamerules
        :return:
        """
        if 1 == (gamerules >> 1) % 2:
            if 17 == value:
                return 15
            if 16 == value:
                return 13
            if 15 == value:
                return 12
            if 14 == value:
                return 12
            if 13 == value:
                return 13
            if 12 == value:
                return 11
            if 11 == value:
                return 11
            if 0 < value:
                return value
        else:
            if 17 == value:
                return 5
            if 16 == value:
                return 5
            if 15 == value:
                return 5
            if 14 == value:
                return 5
            if 13 == value:
                return 5
            if 12 == value:
                return 5
            if 11 == value:
                return 5
            if 10 == value:
                return 4
            if 9 == value:
                return 3
            if 6 < value:
                return 2
        return 1
