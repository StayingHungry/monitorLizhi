#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 11:37
# @Author  : nanganglei
# @File    : testUpload.py
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
url = "http://pagetest.sogou-inc.com/index.php?m=case&a=view&q=SogouWireless&mod=bakupcase&caseid=137871"

dcap = dict(DesiredCapabilities.PHANTOMJS)

dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36  Safari/601.1")

dcap["phantomjs.page.customHeaders.Cookie"] = "gr_user_id=576a52b1-f320-4fa7-b21b-b061fb6c693c; SUID=4098810A6F36920A0000000059ED8AE4; UM_distinctid=162b2a63ad9793-016e817413a56c-1571466f-1fa400-162b2a63ada67c; _ga=GA1.2.55002029.1507626000; _gid=GA1.2.2137811080.1527832736; PHPSESSID=0mp1hm0rs56tboa1r9d370qci5"

urlDict = {
    "50022601":"http://pagetest.sogou-inc.com/index.php?m=case&a=view&q=SogouWireless&mod=lizhi_wuxian&caseid=137873",
    "50024701":"http://pagetest.sogou-inc.com/index.php?m=case&a=view&q=SogouWireless&mod=lizhi_wuxian&caseid=137874"

}


def modifyPagetest( ):

    driver = webdriver.PhantomJS(desired_capabilities=dcap)

    for item in urlDict:

        driver.get(urlDict[item])

        print urlDict[item]

        time.sleep(1)
        try:

            del_file = driver.find_element_by_id("deletecsv1_j0")

            del_file.click()

        except:

            pass

        file_input = driver.find_element_by_id("inputFile1_j0")

        file_name = "./" + item + ".csv"

        file_input.send_keys(file_name)

        time.sleep(1)

        driver.find_element_by_id("submit_btn").click()

        print driver.page_source

    driver.close()


if __name__ == "__main__":

    modifyPagetest()




