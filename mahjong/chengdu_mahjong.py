# coding=utf-8
from mahjong_cardtype import MahjongCardType


def getCardType(handlist, penglist, gangdata, rogue):
    """
    :获取牌型
    :return:
    """
    card_type = []
    allcard = list()
    allcard.extend(handlist)
    allcard.extend(penglist)
    for gang in gangdata:
        allcard.append(gang.gangvalue)
    allcard = sorted(allcard)

    double7 = MahjongCardType.double7(handlist, rogue)
    if -1 != double7:
        card_type.append(10)
    elif MahjongCardType.gold_hook(handlist):
        card_type.append(8)
    elif MahjongCardType.big_double(handlist, rogue):
        card_type.append(7)
    if MahjongCardType.same_color(allcard, rogue):
        card_type.append(9)
    return card_type


def getScore(card_types):
    """
    :获取牌型分
    :return:
    """
    score = 1
    for card_type in card_types:
        if 1 == card_type:
            score *= 2
        if 2 == card_type:
            score *= 2
        if 3 == card_type:
            score *= 2
        if 4 == card_type:
            score *= 2
        if 5 == card_type:
            score *= 2
        if 7 == card_type:
            score *= 2
        if 8 == card_type:
            score *= 4
        if 9 == card_type:
            score *= 4
        if 10 == card_type:
            score *= 4
    if 0 in score:
        score += 1
    return score
