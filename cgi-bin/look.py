# -*- coding: utf-8 -*-
def look(type):
    try:
        if "niuniu" == type:
            fname = '/home/game_logic/logs/bairen_niuniu.log'
            s = ""
            with open(fname, 'r') as f:  # 打开文件
                lines = f.readlines()  # 读取所有行
                last_line = lines[-1]  # 取最后一行
                cards = last_line.split(" [")
                s = cards[-1][:-2]
                cardslist = s.split(", ")
            return cardslist[:25]
        if "tuitongzi" == type:
            fname = '/home/game_logic/logs/tuitongzi.log'
            s = ""
            with open(fname, 'r') as f:  # 打开文件
                lines = f.readlines()  # 读取所有行
                last_line = lines[-1]  # 取最后一行
                cards = last_line.split(" [")
                s = cards[-1][:-2]
                cardslist = s.split(", ")
            return cardslist[:8]
        if "longhu" == type:
            fname = '/home/game_logic/logs/longhu.log'
            s = ""
            with open(fname, 'r') as f:  # 打开文件
                lines = f.readlines()  # 读取所有行
                last_line = lines[-1]  # 取最后一行
                cards = last_line.split(" [")
                s = cards[-1][:-2]
                cardslist = s.split(", ")
            return cardslist[:2]
    except BaseException, e:
        print(e)
    return ""
