# coding=utf-8
class Niuniu(object):
    """
    :牛牛
    """

    # 五小牛
    @staticmethod
    def isWuxiaoniu(cardlist):
        return cardlist[4] % 100 < 6 and sum(cardlist) % 100 < 11

    # 炸弹牛
    @staticmethod
    def isZhadanniu(cardlist):
        return cardlist[0] % 100 == cardlist[3] % 100 or cardlist[1] % 100 == cardlist[4] % 100

    # 五花牛
    @staticmethod
    def isWuhuaniu(cardlist):
        return cardlist[0] % 100 > 10 and cardlist[0] % 100 != 14

    # 葫芦牛
    @staticmethod
    def isHuluniu(cardlist):
        return ((cardlist[0] % 100 == cardlist[1] % 100 and cardlist[2] % 100 == cardlist[4] % 100) or (
                cardlist[0] % 100 == cardlist[2] % 100 and cardlist[3] % 100 == cardlist[4] % 100))

    # 顺子牛
    @staticmethod
    def isShunziniu(cardlist):
        return (cardlist[0] % 100 == (cardlist[1] % 100) - 1 or cardlist[0] % 100 == (cardlist[1] % 100) - 9) and \
               cardlist[1] % 100 == (cardlist[2] % 100) - 1 and \
               cardlist[2] % 100 == (cardlist[3] % 100) - 1 and cardlist[3] % 100 == (cardlist[4] % 100) - 1

    # 同花牛
    @staticmethod
    def sameColor(cardlist):
        sameColorTemp = list()
        sameColorTemp.extend(cardlist)
        sameColorTemp = sorted(sameColorTemp)
        return sameColorTemp[0] / 100 == sameColorTemp[4] / 100

    # 顺斗
    @staticmethod
    def getShunDouValue(cardlist):
        shunvalue = 0
        shundoutemp = list()
        for c in cardlist:
            if c % 100 == 14:
                shundoutemp.append((c - 13) % 100)
            else:
                shundoutemp.append(c % 100)
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
        if x % 100 == 14:
            x1 = x - 13
        else:
            x1 = x
        if y % 100 == 14:
            y1 = y - 13
        else:
            y1 = y
        if x1 % 100 > y1 % 100:
            return 1
        if x1 % 100 < y1 % 100:
            return -1
        if x > y:
            return 1
        if x < y:
            return -1
        return 0
