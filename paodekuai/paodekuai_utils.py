# coding=utf-8
from paodekuai.common import PaodekuaiType
from card_utils import CardUtils


class PaodekuaiUtils(object):
    """
    :跑得快
    """

    @staticmethod
    def get_card_type(cards, count):
        """
        :获取牌型 0错误 1单牌 2对子 3三张 4顺子 5连对 6三连 7飞机 8炸弹 9四张
        :param cards
        :param count 人数
        """
        temp = []
        for c in cards:
            if 2 == c % 100:
                temp.append(15)
            else:
                temp.append(c % 100)
        temp = sorted(temp)

        if 1 == len(temp):
            return PaodekuaiType.DANPAI
        elif 2 == len(temp) and temp[0] == temp[1]:
            return PaodekuaiType.DUIZI
        elif 3 == len(temp) and temp[0] == temp[2]:
            if 3 == count and 14 == temp[0]:
                return PaodekuaiType.ZHADAN
            return PaodekuaiType.SANZHANG
        elif 4 == len(temp):
            if temp[0] == temp[3]:
                return PaodekuaiType.ZHADAN
            elif temp[0] == temp[1] and temp[0] == temp[2] - 1 and temp[2] == temp[3]:
                return PaodekuaiType.LIANDUI
            elif temp[0] == temp[2] or temp[1] == temp[3]:
                return PaodekuaiType.SANZHANG
        elif 5 == len(temp):
            if temp[0] == temp[3] or temp[1] == temp[4]:
                return PaodekuaiType.SIZHANG
            if temp[0] == temp[2] or temp[1] == temp[3] or temp[2] == temp[4]:
                return PaodekuaiType.SANZHANG
            for c in range(0, len(temp) - 1):
                if temp[c] != temp[c + 1] - 1:
                    return PaodekuaiType.ERROR
            return PaodekuaiType.SHUNZI
        elif 6 == len(temp):
            if temp[0] == temp[2] and temp[3] == temp[5] and temp[0] == temp[3] - 1:
                return PaodekuaiType.SANLIAN
            elif temp[0] == temp[1] and temp[0] == temp[2] - 1 and temp[2] == temp[3] and temp[2] == temp[4] - 1 and \
                    temp[4] == temp[5]:
                return PaodekuaiType.LIANDUI
            elif temp[0] == temp[3] or temp[1] == temp[4] or temp[2] == temp[5]:
                return PaodekuaiType.SIZHANG
            for c in range(0, len(temp) - 1):
                if temp[c] != temp[c + 1] - 1:
                    return PaodekuaiType.ERROR
            return PaodekuaiType.SHUNZI
        if len(temp) > 6:
            istype = True
            for c in range(0, len(temp) - 1):
                if temp[c] != temp[c + 1] - 1:
                    istype = False
                    break
            if istype:
                return PaodekuaiType.SHUNZI
            istype = True
            for c in range(1, len(temp) - 2, 2):
                if temp[c] != temp[c + 1] - 1 or temp[c + 1] != temp[c + 2]:
                    istype = False
                    break
            if istype:
                return PaodekuaiType.LIANDUI
            istype = True
            san = CardUtils.get_san(temp)
            if len(san) > 1:
                if len(san) * 3 == len(temp):
                    for c in range(2, len(san) - 3, 3):
                        if san[c] != san[c + 1] - 1:
                            istype = False
                            break
                    if istype:
                        return PaodekuaiType.SANLIAN
                istype = True
                if 0 == len(temp) % 4:
                    if len(temp) / 4 <= len(san):
                        if san[0] != san[1] - 1:
                            san.remove(san[0])
                        else:
                            san.remove(san[len(san) - 1])
                        for c in range(3, len(san) - 1, 4):
                            if san[c] != san[c + 1] - 1:
                                istype = False
                                break
                    elif len(temp) / 3 > len(san):
                        istype = False
                elif 0 == len(temp) % 5:
                    if len(temp) / 5 <= len(san):
                        for c in range(2, len(san) - 1, 3):
                            if san[c] != san[c + 1] - 1:
                                istype = False
                    else:
                        istype = False
                else:
                    istype = False

                if istype:
                    return PaodekuaiType.FEIJI
        return PaodekuaiType.ERROR

    @staticmethod
    def get_card_value(cards, cardtype):
        """
        :获取牌值
        :param cards
        :param cardtype
        """
        temp = []
        for c in cards:
            if 2 == c % 100:
                temp.append(15)
            else:
                temp.append(c % 100)
        temp = sorted(temp)
        if cardtype == PaodekuaiType.DANPAI \
                or cardtype == PaodekuaiType.DUIZI \
                or cardtype == PaodekuaiType.LIANDUI \
                or cardtype == PaodekuaiType.SHUNZI \
                or cardtype == PaodekuaiType.ZHADAN \
                or cardtype == PaodekuaiType.SANLIAN:
            return temp[0]
        elif cardtype == PaodekuaiType.SANZHANG \
                or cardtype == PaodekuaiType.SIZHANG:
            return temp[2]
        elif cardtype == PaodekuaiType.FEIJI:
            for t in temp:
                if 3 <= temp.count(t) and temp.count(t + 1):
                    return t

    @staticmethod
    def reversed_cmp(x, y):
        """
        :排序方法
        :param x:
        :param y:
        :return:
        """
        if x % 100 == 2:
            x1 = x + 13
        else:
            x1 = x
        if y % 100 == 2:
            y1 = y + 13
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

    @staticmethod
    def get_zhadan(cardlist):
        """
        :获取炸弹
        :param cardlist
        """
        zhadan = list()
        if len(cardlist) > 3:
            for i in range(0, len(cardlist) - 3):
                if cardlist[i] % 100 == cardlist[i + 3] % 100:
                    zhadan.append(cardlist[i])
                    zhadan.append(cardlist[i + 1])
                    zhadan.append(cardlist[i + 2])
                    zhadan.append(cardlist[i + 3])
        return zhadan

    @staticmethod
    def get_san(cardlist):
        """
        :获取炸弹
        :param cardlist
        """
        san = list()
        if len(cardlist) >= 3:
            for i in range(0, len(cardlist) - 2):
                if cardlist[i] % 100 == cardlist[i + 2] % 100:
                    san.append(cardlist[i])
                    san.append(cardlist[i + 1])
                    san.append(cardlist[i + 2])
        return san

    @staticmethod
    def get_duizi(cardlist):
        """
        :获取对子
        :param cardlist
        """
        duizi = list()
        if len(cardlist) >= 2:
            for i in range(0, len(cardlist) - 1):
                if cardlist[i] % 100 == cardlist[i + 1] % 100:
                    duizi.append(cardlist[i])
                    duizi.append(cardlist[i + 1])
        return duizi

    @staticmethod
    def get_shunzi(cardlist, value, size):
        """
        :获取顺子
        :param cardlist
        :param value
        :param size
        """
        shunzi = list()
        dan = list()
        dan.extend(cardlist)
        removed = list()
        for d in dan:
            if d % 100 <= value:
                removed.append(d)
        for r in removed:
            dan.remove(r)
        if len(dan) >= size:
            for i in range(0, len(dan) - 4):
                shunzi = list()
                shunzi.append(dan[i])
                lastvalue = dan[i] % 100
                for j in range(i + 1, len(dan)):
                    if dan[j] % 100 == lastvalue + 1:
                        shunzi.append(dan[j])
                        lastvalue = dan[j] % 100
                        if len(shunzi) == size:
                            return shunzi
                    elif dan[j] % 100 > lastvalue:
                        break
        return shunzi

    @staticmethod
    def get_liandui(cardlist, value, size):
        """
        :获取连对
        :param cardlist
        :param value
        :param size
        """
        liandui = list()
        dui = PaodekuaiUtils.get_duizi(cardlist)
        removed = list()
        for d in dui:
            if d % 100 <= value:
                removed.append(d)
        for r in removed:
            dui.remove(r)
        if len(dui) >= size:
            for i in range(0, len(dui) - 3, 2):
                liandui = list()
                liandui.append(dui[i])
                liandui.append(dui[i + 1])
                lastvalue = dui[i] % 100
                for j in range(i + 2, len(dui) - 1, 2):
                    if dui[j] % 100 == lastvalue + 1:
                        liandui.append(dui[j])
                        liandui.append(dui[j + 1])
                        lastvalue = dui[j] % 100
                        if len(liandui) == size:
                            return liandui
                    elif dui[j] % 100 > lastvalue:
                        break
        return liandui

    @staticmethod
    def get_sanlian(cardlist, value, size):
        """
        :获取三连
        :param cardlist
        :param value
        :param size
        """
        sanlian = list()
        san = PaodekuaiUtils.get_san(cardlist)
        removed = list()
        for s in san:
            if s % 100 <= value:
                removed.append(s)
        for r in removed:
            san.remove(r)
        if len(san) >= size:
            for i in range(0, len(san) - 4, 2):
                sanlian = list()
                sanlian.append(san[i])
                sanlian.append(san[i + 1])
                sanlian.append(san[i + 2])
                lastvalue = san[i] % 100
                for j in range(i + 3, len(san) - 2, 3):
                    if san[j] % 100 == lastvalue + 1:
                        sanlian.append(san[j])
                        sanlian.append(san[j + 1])
                        sanlian.append(san[j + 2])
                        lastvalue = san[j] % 100
                        if len(sanlian) == size:
                            return sanlian
                    elif san[j] % 100 > lastvalue:
                        break
        return sanlian

    @staticmethod
    def auto_play(cardlist, cardtype, lastvalue, lastsize, count):
        """
        :自动出牌
        :param cardlist
        :param cardtype
        :param lastvalue
        :param lastsize
        :param count
        """
        playcards = list()
        if 3 == count and 114 in cardlist and 214 in cardlist and 314 in cardlist:
            playcards.append(114)
            playcards.append(214)
            playcards.append(314)
            return playcards
        cards = list()
        cards.extend(cardlist)
        cards.sort(cmp=PaodekuaiUtils.reversed_cmp)
        si = PaodekuaiUtils.get_zhadan(cards)
        if cardtype == PaodekuaiType.DANPAI:
            if cards[len(cards) - 1] % 100 > lastvalue or (cards[len(cards) - 1] % 100 == 2 and lastvalue != 15):
                playcards.append(cards[len(cards) - 1])
                return playcards
            if len(si) > 0:
                playcards.extend(si[0:4])
                return playcards
        elif cardtype == PaodekuaiType.DUIZI:
            dui = PaodekuaiUtils.get_duizi(cards)
            if len(dui) > 0 and (
                    dui[len(dui) - 1] % 100 > lastvalue or (dui[len(dui) - 1] % 100 == 2 and lastvalue != 15)):
                playcards.append(dui[len(dui) - 1])
                playcards.append(dui[len(dui) - 2])
                return playcards
            if len(si) > 0:
                playcards.extend(si[0:4])
                return playcards
        elif cardtype == PaodekuaiType.LIANDUI:
            liandui = PaodekuaiUtils.get_liandui(cards, lastvalue, lastsize)
            if len(liandui) == lastsize:
                playcards.extend(liandui)
                return playcards
            if len(si) > 0:
                playcards.extend(si[0:4])
                return playcards
        elif cardtype == PaodekuaiType.SHUNZI:
            shunzi = PaodekuaiUtils.get_shunzi(cards, lastvalue, lastsize)
            if len(shunzi) == lastsize:
                playcards.extend(shunzi)
                return playcards
            if len(si) > 0:
                playcards.extend(si[0:4])
                return playcards
        elif cardtype == PaodekuaiType.SANZHANG:
            if len(cards) < lastsize:
                return playcards
            san = PaodekuaiUtils.get_san(cards)
            if len(san) > 0 and (
                    san[len(san) - 1] % 100 > lastvalue or (san[len(san) - 1] % 100 == 2 and lastvalue != 15)):
                playcards.append(san[len(san) - 1])
                playcards.append(san[len(san) - 2])
                playcards.append(san[len(san) - 3])
                tempcards = list()
                tempcards.extend(cards)
                tempcards.remove(san[len(san) - 1])
                tempcards.remove(san[len(san) - 2])
                tempcards.remove(san[len(san) - 3])
                while len(playcards) < lastsize:
                    playcards.append(tempcards[0])
                    tempcards.remove(tempcards[0])
                return playcards
            if len(si) > 0:
                playcards.extend(si[0:4])
                return playcards
        elif cardtype == PaodekuaiType.SIZHANG:
            if len(si) > 0:
                playcards.extend(si[0:4])
                return playcards
        elif cardtype == PaodekuaiType.ZHADAN:
            if 0 < len(si) and (si[len(si) - 1] % 100 > lastvalue or (si[len(si) - 1] % 100 == 2 and lastvalue != 15)):
                playcards.append(si[len(si) - 1])
                playcards.append(si[len(si) - 2])
                playcards.append(si[len(si) - 3])
                playcards.append(si[len(si) - 4])
                return playcards
        elif cardtype == PaodekuaiType.SANLIAN:
            sanlian = PaodekuaiUtils.get_sanlian(cards, lastvalue, lastsize)
            if len(sanlian) == lastsize:
                playcards.extend(sanlian)
                return playcards
            if len(si) > 0:
                playcards.extend(si[0:4])
                return playcards
        elif cardtype == PaodekuaiType.FEIJI:
            sanlian = []
            if len(cards) < lastsize:
                return playcards
            if 0 == lastsize % 4:
                sanlian = PaodekuaiUtils.get_sanlian(cards, lastvalue, lastsize / 4)
            elif 0 == lastsize % 5:
                sanlian = PaodekuaiUtils.get_sanlian(cards, lastvalue, lastsize / 5)
            if len(sanlian) != 0:
                playcards.extend(sanlian)
                tempcards = list()
                tempcards.extend(cards)
                for s in sanlian:
                    tempcards.remove(s)
                if 0 == lastsize % 4 and len(tempcards) >= len(sanlian) / 3:
                    playcards.extend(tempcards[0:len(sanlian) / 3])
                    return playcards
                elif 0 == lastsize % 5 and len(tempcards) >= 2 * len(sanlian) / 3:
                    playcards.extend(tempcards[0:2 * len(sanlian) / 3])
                    return playcards
            if len(si) > 0:
                playcards.extend(si[0:4])
                return playcards
        return playcards
