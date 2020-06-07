from presuveres.presuve import move
from presuveres.color import color
from markdrawers.lister import *
from markdrawers.drawer import converttopng
from copy import deepcopy
import time
import os
from sets.func import *


def main():
    simyear = 2000  # year to simulate
    pixels = 5  # pixels to move
    queue = [(51, 153, 255), (0, 102, 204), (0, 0, 102), (0, 0, 204), (51, 51, 255),
             (102, 0, 204)]  # colors to consider while moving
    stfrom = 100  # starting lattitide
    narrowdate = False # if you want to start with exact date and date on exact date
    startdate = '08201985'  # if narrow = True - starting date
    enddate = '12011985'  # if narrow = True - ending date

    year = 1985
    godate = True
    tupstartdate = None
    tupenddate = None
    interupt = False
    dirbase = f"../../src/resources/img/base{year}/"
    dir = dirbase + "data/"
    dirarea = dirbase + "areadata/"
    dirtest = dirbase + "test/"
    dirsim = dirbase + f"{simyear}/"

    if os.path.exists(dirbase):
        if os.path.exists(dir) and os.path.exists(dirarea):
            if not os.path.exists(dirsim):
                os.mkdir(dirsim)

    if narrowdate:
        godate = False
        tupstartdate = datetoint(startdate)
        tupenddate = datetoint(enddate)

    start = time.time()
    for dirpath, dirnames, filenames in os.walk(dir):
        filenames.sort()
        for i in filenames:
            i = i[0:8]
            if narrowdate:
                tupi = datetoint(i)
                if not godate:
                    if tupi[0] >= tupstartdate[0] and tupi[1] >= tupstartdate[1]:
                        godate = True
                else:
                    if tupi[0] >= tupenddate[0] and tupi[1] >= tupenddate[1]:
                        interupt = True
            if godate:
                print(i)
                path = dir + i + '.txt'
                patharea = dirarea + i + '.txt'
                pathsim = dirsim + i + '.png'
                data = filetolist(path)
                pattern = deepcopy(data)
                arealist = filetolist(patharea)
                for cl in queue:
                    move(data, arealist, pattern.copy(), pixels, cl, stfrom=stfrom)
                color(data,3)
                color(data,3)
                converttopng(pathsim, listx=data)
                if interupt:
                    break

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
