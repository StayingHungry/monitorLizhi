from getFileFromHolmes import getFile
from  testUpload import modifyPagetest


vridList = ['50022601',
            '50024701']


def updateLizhiMonitor():

    for vrid in vridList:

        getFile(vrid)

    modifyPagetest()



if __name__ == "__main__":

    updateLizhiMonitor()