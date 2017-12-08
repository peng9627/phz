# coding=utf-8
from mahjong.utils.mahjong_cardtype import MahjongCardType


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
    if MahjongCardType.big_double(allcard, rogue):
        card_type = 1
    if MahjongCardType.gold_hook(allcard):
        card_type = 2
    double7 = MahjongCardType.double7(allcard, rogue)
    if -1 != double7:
        card_type = double7 + 11
    if MahjongCardType.same_color(allcard, rogue):
        if 1 == card_type:
            if MahjongCardType.san_da(allcard, rogue):
                card_type = 5
            else:
                card_type = 4
        if 10 < card_type:
            card_type -= 6
        if 2 == card_type:
            card_type = 10
    return card_type


def getScore(card_type):
    """
    :获取牌型分
    :return:
    """
    if 0 == card_type:
        return 1
    if 1 == card_type:
        return 12
    if 2 == card_type:
        return 24
    if 3 == card_type:
        return 12
    if 4 == card_type:
        return 24
    if 5 == card_type:
        return 48
    if 6 == card_type:
        return 24
    if 7 == card_type:
        return 48
    if 8 == card_type:
        return 96
    if 9 == card_type:
        return 96
    if 10 == card_type:
        return 96
    if 11 == card_type:
        return 12
    if 12 == card_type:
        return 24
    if 13 == card_type:
        return 48
    if 14 == card_type:
        return 96
    return 0
