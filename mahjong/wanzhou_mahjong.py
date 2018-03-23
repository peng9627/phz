# coding=utf-8
from mahjong_cardtype import MahjongCardType


def getCardType(handlist, penglist, gangdata, rogue):
    """
    :获取牌型
    :return:
    """
    card_type = 10
    allcard = list()
    allcard.extend(handlist)
    allcard.extend(penglist)
    for gang in gangdata:
        allcard.append(gang.gangvalue)
    allcard = sorted(allcard)
    if MahjongCardType.big_double(handlist, rogue):
        card_type = 11
    if MahjongCardType.gold_hook(handlist):
        card_type = 12
    double7 = MahjongCardType.double7(handlist, rogue)
    if -1 != double7:
        card_type = double7 + 21
    if MahjongCardType.same_color(allcard, rogue):
        if 11 == card_type:
            if MahjongCardType.san_da(handlist):
                if MahjongCardType.big_double(handlist, rogue):
                    card_type = 15
                else:
                    card_type = 27
            else:
                card_type = 14
        elif 20 < card_type:
            card_type -= 5
        elif 12 == card_type:
            card_type = 20
        else:
            card_type = 13
    return card_type


def getScore(card_type):
    """
    :获取牌型分
    :return:
    """
    if 10 == card_type:
        return 1
    if 11 == card_type:
        return 12
    if 12 == card_type:
        return 24
    if 13 == card_type:
        return 12
    if 14 == card_type:
        return 24
    if 15 == card_type:
        return 48
    if 16 == card_type:
        return 24
    if 17 == card_type:
        return 48
    if 18 == card_type:
        return 96
    if 19 == card_type:
        return 96
    if 20 == card_type:
        return 96
    if 21 == card_type:
        return 12
    if 22 == card_type:
        return 24
    if 23 == card_type:
        return 48
    if 24 == card_type:
        return 96
    if 25 == card_type:
        return 48
    if 27 == card_type:
        return 24
    return 1
