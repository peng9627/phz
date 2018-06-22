# coding=utf-8
class MahjongUtils(object):
    """
    :麻将算法
    """

    @staticmethod
    def possible(handlist, degree):
        """
        :可能的牌
        :param handlist:
        :param degree:
        :return:
        """
        possible_list = set()
        for s in handlist:
            possible_list.add(s)
            for i in range(0, degree):
                if (s % 10) + i + 1 < 10:
                    possible_list.add(s + i + 1)
                if (s % 10) - i - 1 > 0:
                    possible_list.add(s - i - 1)
        return possible_list

    @staticmethod
    def get_dui(handlist):
        """
        :获取对子
        :param handlist:
        :return:
        """
        dui = set()
        temp = list()
        temp.extend(handlist)
        temp = sorted(temp)
        for i in range(0, len(temp) - 1):
            if temp[i] == temp[i + 1]:
                dui.add(temp[i])
                i += 1
        return dui

    @staticmethod
    def get_san(handlist):
        """
        :获取三个
        :param handlist:
        :return:
        """
        san = set()
        temp = list()
        temp.extend(handlist)
        temp = sorted(temp)
        for i in range(0, len(temp) - 2):
            if temp[i] == temp[i + 2]:
                san.add(temp[i])
                i += 2
        return san

    @staticmethod
    def get_si(handlist):
        """
        :获取四个
        :param handlist:
        :return:
        """
        si = set()
        temp = list()
        temp.extend(handlist)
        temp = sorted(temp)
        for i in range(0, len(temp) - 3):
            if temp[i] == temp[i + 3]:
                si.add(temp[i])
                i += 3
        return si

    @staticmethod
    def containSize(cardlist, card):
        """
        :包含数量
        :param cardlist:
        :param card:
        :return:
        """
        size = 0
        for c in cardlist:
            if c == card:
                size += 1
        return size

    @staticmethod
    def check_lug(handlist):
        """
        :胡牌规则
        :param handlist:
        :return:
        """
        if 0 == len(handlist):
            return True
        temp = list()
        temp.extend(handlist)
        md_val = temp[0]
        temp.remove(md_val)
        if 2 == MahjongUtils.containSize(temp, md_val):
            tempSame = list()
            tempSame.extend(temp)
            tempSame.remove(md_val)
            tempSame.remove(md_val)
            if MahjongUtils.check_lug(tempSame):
                return True
        if md_val + 1 in temp and md_val + 2 in temp:
            tempShun = list()
            tempShun.extend(temp)
            tempShun.remove(md_val + 1)
            tempShun.remove(md_val + 2)
            if MahjongUtils.check_lug(tempShun):
                return True
        return False

    @staticmethod
    def check_lug_rogue(handlist, rogue_count):
        """
        :胡牌规则
        :param handlist:
        :param rogue_count:
        :return:
        """
        if 0 == len(handlist):
            return True
        temp = list()
        temp.extend(handlist)
        md_val = temp[0]
        temp.remove(md_val)
        if 2 == MahjongUtils.containSize(temp, md_val):
            tempSame = list()
            tempSame.extend(temp)
            tempSame.remove(md_val)
            tempSame.remove(md_val)
            if MahjongUtils.check_lug_rogue(tempSame, rogue_count):
                return True
        if md_val + 1 in temp and md_val + 2 in temp:
            tempShun = list()
            tempShun.extend(temp)
            tempShun.remove(md_val + 1)
            tempShun.remove(md_val + 2)
            if MahjongUtils.check_lug_rogue(tempShun, rogue_count):
                return True
        if rogue_count > 0:
            if 1 == MahjongUtils.containSize(temp, md_val):
                tempSame = list()
                tempSame.extend(temp)
                tempSame.remove(md_val)
                if MahjongUtils.check_lug_rogue(tempSame, rogue_count - 1):
                    return True
            if md_val + 1 in temp:
                tempSame = list()
                tempSame.extend(temp)
                tempSame.remove(md_val + 1)
                if MahjongUtils.check_lug_rogue(tempSame, rogue_count - 1):
                    return True
            if md_val + 2 in temp and md_val % 10 != 9:
                tempSame = list()
                tempSame.extend(temp)
                tempSame.remove(md_val + 2)
                if MahjongUtils.check_lug_rogue(tempSame, rogue_count - 1):
                    return True
            if 1 < rogue_count:
                if MahjongUtils.check_lug_rogue(temp, rogue_count - 2):
                    return True
        return False

    @staticmethod
    def get_hu(handlist, rogue):
        """
        :胡牌规则
        :param handlist:
        :param rogue:
        :return:
        """
        hu = set()
        rogueSize = MahjongUtils.containSize(handlist, rogue)

        if rogueSize > 0:
            temp = list()
            temp.extend(handlist)
            temp.append(-1)
            if -1 != MahjongUtils.double7(temp, rogue):
                hu.add(-1)
                return hu
            temp.remove(-1)
            temp.remove(rogue)
            for i in range(0, rogueSize - 1):
                temp.remove(rogue)
            temp = sorted(temp)
            if MahjongUtils.check_lug_rogue(temp, rogueSize - 1):
                hu.add(-1)
                return hu
        possible = MahjongUtils.possible(handlist, rogueSize + 1)
        for p in possible:
            temp = list()
            temp.extend(handlist)
            temp.append(p)
            if -1 != MahjongUtils.double7(temp, rogue):
                hu.add(p)
            for i in range(0, rogueSize):
                temp.remove(rogue)
            tempset = set(temp)
            for s in tempset:
                if 1 != MahjongUtils.containSize(temp, s):
                    hutemp = list()
                    hutemp.extend(temp)
                    hutemp.remove(s)
                    hutemp.remove(s)
                    hutemp = sorted(hutemp)
                    if MahjongUtils.check_lug_rogue(hutemp, rogueSize):
                        hu.add(p)
                        break
                if rogueSize > 0:
                    hutemp = list()
                    hutemp.extend(temp)
                    hutemp.remove(s)
                    hutemp = sorted(hutemp)
                    if MahjongUtils.check_lug_rogue(hutemp, rogueSize - 1):
                        hu.add(p)
                        break
            temp.remove(p)
        return hu

    @staticmethod
    def double7(handlist, rogue):
        """
        :七对
        :param handlist:
        :param rogue:
        :return:
        """
        temp = list()
        temp.extend(handlist)
        rogueSize = MahjongUtils.containSize(handlist, rogue)
        for i in range(0, rogueSize):
            temp.remove(rogue)
        si = MahjongUtils.get_si(temp)
        if 14 == len(handlist) and 14 - (2 * (len(MahjongUtils.get_dui(temp)) + len(si))) <= 2 * rogueSize:
            siCount = 0
            temp1 = list()
            temp1.extend(temp)
            for i in range(0, 4):
                for s in si:
                    temp1.remove(s)
            siCount += len(si)
            san = MahjongUtils.get_san(temp1)
            for i in range(0, 3):
                for s in san:
                    temp1.remove(s)
            siCount += len(san)
            rogueSize -= len(san)
            dui = MahjongUtils.get_dui(temp1)
            for i in range(0, 2):
                for s in dui:
                    temp1.remove(s)
            rogueSize -= len(temp1)
            if rogueSize / 2 > len(dui):
                siCount += len(dui)
                rogueSize -= 2 * len(dui)
                siCount += rogueSize / 4
            else:
                siCount += rogueSize / 2
            return siCount
        return -1
