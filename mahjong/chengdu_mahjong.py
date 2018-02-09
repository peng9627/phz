# coding=utf-8
from mahjong_cardtype import MahjongCardType


def getCardType(handlist, penglist, gangdata, rogue):
    """
    :获取牌型
    :return:
    """
    card_type = 0
    allcard = list()
    allcard.extend(handlist)
    allcard.extend(penglist)
    for gang in gangdata:
        allcard.append(gang.gangvalue)
    allcard = sorted(allcard)
    if MahjongCardType.big_double(handlist, rogue):
        card_type = 1
    if MahjongCardType.gold_hook(handlist):
        card_type = 2
    double7 = MahjongCardType.double7(handlist, rogue)
    if -1 != double7:
        card_type = double7 + 11
    if MahjongCardType.same_color(allcard, rogue):
        if 1 == card_type:
            card_type = 4
        elif 10 < card_type:
            card_type -= 6
        elif 2 == card_type:
            card_type = 10
        else:
            card_type = 3
    return card_type


def getScore(card_type):
    """
    :获取牌型分
    :return:
    """
    if 0 == card_type:
        return 1
    if 1 == card_type:
        return 2
    if 2 == card_type:
        return 4
    if 3 == card_type:
        return 4
    if 4 == card_type:
        return 8
    if 5 == card_type:
        return 4
    if 6 == card_type:
        return 8
    if 7 == card_type:
        return 8
    if 8 == card_type:
        return 8
    if 9 == card_type:
        return 8
    if 10 == card_type:
        return 8
    if 11 == card_type:
        return 4
    if 12 == card_type:
        return 8
    if 13 == card_type:
        return 8
    if 14 == card_type:
        return 8
    return 0
