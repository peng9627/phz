# coding=utf-8
from mahjong.mahjong_utils import MahjongUtils
from mahjong_cardtype import MahjongCardType


def getCardType(handlist, penglist, gangdata, rogue, hucard):
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
        card_type.append(8)
    if MahjongCardType.same_color(allcard, rogue):
        card_type.append(7)
    if hucard % 10 == 2 or hucard % 10 == 5 or hucard % 10 == 8:
        card_type.append(9)

    # 将258
    withoutrogue = list()
    withoutrogue.extend(handlist)
    rogueSize = MahjongUtils.containSize(handlist, rogue)
    for i in range(0, rogueSize):
        withoutrogue.remove(rogue)
    if rogueSize > 1 and MahjongUtils.check_lug_rogue(withoutrogue, rogueSize - 2):
        card_type.append(10)
    else:
        jiang258s = [2, 5, 8, 12, 15, 18, 22, 25, 28]
        for j in jiang258s:
            jiang258size = MahjongUtils.containSize(handlist, j)
            jtemp = list()
            jtemp.extend(withoutrogue)
            if 1 == jiang258size and rogueSize > 0:
                jtemp.remove(j)
                if MahjongUtils.check_lug_rogue(jtemp, rogueSize - 1):
                    card_type.append(10)
                    break
            elif 2 == jiang258size:
                jtemp.remove(j)
                jtemp.remove(j)
                if MahjongUtils.check_lug_rogue(withoutrogue, rogueSize):
                    card_type.append(10)
                    break
    return card_type


def getScore(card_types):
    """
    :获取牌型分
    :return:
    """
    score = 1
    for card_type in card_types:
        if 0 == card_type:
            score *= 2
        if 7 == card_type:
            score *= 2
        if 8 == card_type:
            score *= 2
        if 9 == card_type:
            score *= 2
        if 10 == card_type:
            score *= 2
    return score
