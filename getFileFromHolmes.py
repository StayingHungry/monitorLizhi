#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 12:07
# @Author  : nanganglei
# @File    : getFileFromHolmes.py
import sys
from getYesterdayDate import getYesterday, getToday
import requests
import json
from urllib import quote
reload(sys)
sys.setdefaultencoding('utf-8')
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'http://holmes.sogou-inc.com/sessionlog3/Controller_Wap_Web_Vr_Query?sc=w_sweb',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'gr_user_id=576a52b1-f320-4fa7-b21b-b061fb6c693c; SUID=4098810A6F36920A0000000059ED8AE4; UM_distinctid=162b2a63ad9793-016e817413a56c-1571466f-1fa400-162b2a63ada67c; _ga=GA1.2.55002029.1507626000; _gid=GA1.2.2137811080.1527832736; jpassport-sp={username:nanganglei@sogou-inc.com,timebefore:2018-06-01T06:51:13.614Z,notonorafter:2018-06-15T06:52:13.614Z,sign:eJwNjscNwEAIwFailydwsP9IydeSLYMVTlcFWqZGp061u/ADclJvGuyuxDbFc3DA4U6ENOshePqCf1+JN2F7gwANzSo5nOeiXnjEDYI0KFOIaAquOZla3RGzSolcb3s9Z1jdp2B/c2qabxLOFAb+E22Pgsg2AL/dZy5YBRJ/yTxUZajMmEA4STtjrxL4kV4rct2jnwleTN4H0s05pA==}; PHPSESSID=srm288nvc3tbobhd5sk7toult7'
    }

url = "http://holmes.sogou-inc.com/sessionlog3/Model_Wap_Web_Vr_Query?sc=w_sweb&"

def getFile(vrid):
    yesterday = getYesterday()
    toDate = getToday()

    params = "from=" + yesterday + "&to=" + toDate \
             + "&source_class=ch_source&channel%5B%5D=total&tar%5B%5D=pvnum&tar%5B%5D=clicknum&tar%5B%5D=posavg&tar%5B%5D=linkid&tar%5B%5D=ctr&pagetype%5B%5D=all&vrid=" +\
             vrid + "&mzid=&jzid=&isjzid=&queryword=&pvnumsift=0&lpvnum=&rpvnum=&clicknumsift=0&lclicknum=&rclicknum=&ctrsift=0&lctr=&rctr=&possift=0&lpos=&rpos="
    url_end = url + params

    response = requests.request("GET", url=url_end, headers=headers, verify=False)

    jsonObject = json.loads(str(response.text))

    rows = jsonObject["rows"]

    if len(rows) < 10:

        return

    fileName = "./" + vrid + ".csv"

    csvFile = open(fileName, "wb")

    csvFile.write("QUERY\n")

    for i, item in enumerate(rows):

        if i > 50:
            break

        query_tem = item["query"]

        print query_tem

        csvFile.write(quote(str(query_tem)))

        csvFile.write("\n")
    csvFile.close()

if __name__ == "__main__":
    getFile("50022601")