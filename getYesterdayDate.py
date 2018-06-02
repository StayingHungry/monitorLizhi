#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 12:08
# @Author  : nanganglei
# @File    : getYesterdayDate.py
import datetime

def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=2)
    yesterday=today-oneday
    return str(yesterday)

def getToday():
    todayDate = datetime.date.today()
    return str(todayDate)

if __name__ == "__main__":
    print getYesterday()
    print getToday()