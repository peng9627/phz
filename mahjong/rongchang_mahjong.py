# coding=utf-8
from mahjong_utils import MahjongUtils
from mahjong_cardtype import MahjongCardType


def getCardType(handlist, penglist, gangdata, rogue, hucard):
    """
    :获取牌型
    :return:
    """
    print "计算牌型"
    print handlist
    print "计算牌型"
    print penglist
    card_type = list()
    allcard = list()
    allcard.extend(handlist)
    allcard.extend(penglist)
    for gang in gangdata:
        print gang.gangvalue
        allcard.append(gang.gangvalue)
    allcard = sorted(allcard)
    if MahjongCardType.gold_hook(handlist):
        card_type.append(11)
    elif MahjongCardType.big_double(handlist, rogue):
        card_type.append(7)
    if MahjongCardType.same_color(allcard, rogue):
        card_type.append(8)
    double7 = MahjongCardType.double7(handlist, rogue)
    if 0 <= double7:
        if 4 == MahjongUtils.containSize(handlist, hucard):
            card_type.append(10)
        else:
            card_type.append(9)
    print "结果"
    print card_type
    return card_type


def getScore(card_types):
    """
    :获取牌型分
    :return:
    """
    score = 0
    for card_type in card_types:
        if 0 == card_type:
            score = 1
        elif 1 == card_type:
            score += 1
        elif 2 == card_type:
            score += 4
        elif 3 == card_type:
            score += 6
        elif 4 == card_type:
            score += 10
        elif 5 == card_type:
            score += 4
        elif 6 == card_type:
            score += 6
        elif 7 == card_type:
            score += 4
        elif 8 == card_type:
            score += 6
        elif 9 == card_type:
            score += 6
        elif 10 == card_type:
            score += 10
        elif 11 == card_type:
            score += 10
        elif 12 == card_type:
            score += 4
        elif 13 == card_type:
            score += 4
        elif 14 == card_type:
            score += 4
    return score
